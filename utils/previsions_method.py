import pandas as pd

from utils.features import features_jour

HORIZONS = [15, 30, 45, 60, 75, 90, 105, 120]  # adapte à tes colonnes


def profil_mean(dataframe_support):
    dataframe_support_feature = features_jour(dataframe_support)
    return dataframe_support_feature.groupby(["station", "jour", "heure", "minute"])[
        "bikes"
    ].mean()


def mean_by_profil(prediction_o, dataframe_apprentissage):
    prediction = prediction_o.copy()
    stations = prediction.index.get_level_values("station")
    commit_at = prediction.index.get_level_values("commit_at")

    profil_moyen = profil_mean(dataframe_apprentissage)

    for h in HORIZONS:
        t = commit_at + pd.Timedelta(minutes=h)  # moment à prédire

        cle = pd.MultiIndex.from_arrays(
            [stations, t.dayofweek, t.hour, t.minute],
            names=["station", "jour", "heure", "minute"],  # mêmes noms que profil_moyen
        )

        prediction[f"bikes_+{h}min"] = profil_moyen.reindex(cle).to_numpy()
    return prediction

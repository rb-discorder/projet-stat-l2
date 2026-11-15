def features_jour(dataframe_support):
    dataframe_support_cpy = dataframe_support.copy()
    time = dataframe_support_cpy.index.get_level_values("commit_at")

    dataframe_support_cpy["jour"] = time.dayofweek
    dataframe_support_cpy["heure"] = time.hour
    dataframe_support_cpy["minute"] = time.minute

    return dataframe_support_cpy

def trier_top_joueurs(df, column='OVR', top_n=5):
    return df.sort_values(by=column, ascending=False).head(top_n)
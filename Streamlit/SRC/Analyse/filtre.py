def filtrer_donnees(df, league, position, gender, ovr_range, min_dri, min_pac):
    df_filtered = df.copy()
    
    if league != "Toutes":
        df_filtered = df_filtered[df_filtered['League'] == league]
        
    if position != "Tous":
        df_filtered = df_filtered[df_filtered['Position'] == position]
        
    if gender != "Tous":
        df_filtered = df_filtered[df_filtered['gender'] == gender]
        
    df_filtered = df_filtered[
        (df_filtered['OVR'] >= ovr_range[0]) & 
        (df_filtered['OVR'] <= ovr_range[1])
    ]
    
    df_filtered = df_filtered[df_filtered['DRI'] >= min_dri]
    
    col_vitesse = 'PAC' if 'PAC' in df_filtered.columns else 'PHY'
    df_filtered = df_filtered[df_filtered[col_vitesse] >= min_pac]
    
    return df_filtered
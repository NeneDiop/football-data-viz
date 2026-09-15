import streamlit as st

def afficher_filtres(df):
    st.sidebar.header("🔍 Filtres d'analyse")
    
    # Filtre Ligue
    leagues = ["Toutes"] + sorted(list(df['League'].dropna().unique()))
    selected_league = st.sidebar.selectbox("Sélectionner une Ligue :", leagues)
    
    # Filtre Poste
    positions = ["Tous"] + sorted(list(df['Position'].dropna().unique()))
    selected_position = st.sidebar.selectbox("Sélectionner un Poste :", positions)
    
    # Filtre Genre
    genders = ["Tous", "Masculin (M)", "Féminin (F)"]
    selected_gender_raw = st.sidebar.selectbox("Sélectionner le Genre :", genders)
    selected_gender = "M" if selected_gender_raw == "Masculin (M)" else ("F" if selected_gender_raw == "Féminin (F)" else "Tous")
        
    # Filtres Numériques
    min_ovr, max_ovr = int(df['OVR'].min()), int(df['OVR'].max())
    selected_ovr = st.sidebar.slider("Seuil note générale (OVR) :", min_ovr, max_ovr, (min_ovr, max_ovr))
    
    min_dri, max_dri = int(df['DRI'].min()), int(df['DRI'].max())
    selected_dri = st.sidebar.slider("Dribble minimum (DRI) :", min_dri, max_dri, min_dri)

    col_vitesse = 'PAC' if 'PAC' in df.columns else 'PHY'
    min_pac, max_pac = int(df[col_vitesse].min()), int(df[col_vitesse].max())
    selected_pac = st.sidebar.slider("Vitesse minimum (PAC) :", min_pac, max_pac, min_pac)
    
    return selected_league, selected_position, selected_gender, selected_ovr, selected_dri, selected_pac
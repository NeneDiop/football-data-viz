import streamlit as st
from constantes.input_data import load_data
from SRC.barre_filtre import afficher_filtres
from SRC.analyse import afficher_kpis
from SRC.Analyse.filtre import filtrer_donnees
from SRC.Analyse.tri import trier_top_joueurs
from SRC.Analyse.api import rechercher_valeur_joueur
from SRC.Graphique.scatter import plot_scatter_ovr_dri
from SRC.Graphique.lire import plot_distribution_ovr, plot_top_teams

st.set_page_config(page_title="Rapport Visuel Seaborn", layout="wide")

st.title("⚽ Tableau de Bord Interactif - EA Sports FC")

# 1. Chargement des données
df = load_data()

# 2. Barre de filtres
league, position, gender, ovr_range, min_dri, min_pac = afficher_filtres(df)

# 3. Recherche API PlayerElo
st.sidebar.divider()
st.sidebar.subheader("🌐 Recherche PlayerElo API")
nom_recherche = st.sidebar.text_input("Rechercher un joueur (Nom) :", "")
if nom_recherche:
    info_api = rechercher_valeur_joueur(nom_recherche)
    if info_api:
        st.sidebar.info(f"**Joueur :** {info_api['nom']}\n\n**ID API :** {info_api['id']}\n\n**Score Elo :** {info_api['valeur']}")

# 4. Filtrage dynamique
df_filtered = filtrer_donnees(df, league, position, gender, ovr_range, min_dri, min_pac)

# 5. Bandeau de chiffres clés
if len(df_filtered) == 0:
    st.error("⚠️ Aucun joueur ne correspond aux filtres sélectionnés.")
else:
    afficher_kpis(df_filtered)

st.divider()

# 6. Visualisations avec justifications
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Distribution des notes (Histogramme)")
    plot_distribution_ovr(df_filtered)

with col_right:
    st.subheader("📈 Relation Dribble / Note (Nuage de points)")
    plot_scatter_ovr_dri(df_filtered)

st.divider()

st.subheader("🏆 Comparaison par Club (Barplot)")
plot_top_teams(df_filtered)

st.divider()

# 7. Tableau du Top 5
st.subheader("📋 Top 5 des profils sélectionnés")
if len(df_filtered) > 0:
    top_joueurs = trier_top_joueurs(df_filtered, top_n=5)
    cols_to_show = ['Name', 'Position', 'Team', 'League', 'OVR', 'DRI']
    if 'PAC' in df_filtered.columns:
        cols_to_show.append('PAC')
    st.dataframe(top_joueurs[cols_to_show])
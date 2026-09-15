import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_distribution_ovr(df):
    if len(df) == 0:
        st.warning("Aucun joueur ne correspond aux filtres sélectionnés.")
        return
        
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df['OVR'], kde=True, color='skyblue', bins=20, ax=ax)
    ax.set_title("Distribution de la note générale (OVR)")
    ax.set_xlabel("Note OVR")
    ax.set_ylabel("Effectif")
    st.pyplot(fig)
    st.caption("💡 **Justification :** L'histogramme permet d'observer la rareté des joueurs à très forte note globale.")

def plot_top_teams(df):
    if len(df) == 0:
        st.warning("Aucun joueur ne correspond aux filtres sélectionnés.")
        return
        
    top_teams = df.groupby('Team')['OVR'].mean().sort_values(ascending=False).head(10).reset_index()
    fig, ax = plt.subplots(figsize=(9, 4.5))
    sns.barplot(data=top_teams, x='OVR', y='Team', palette='Blues_r', ax=ax)
    ax.set_title("Top 10 des clubs selon la moyenne OVR")
    ax.set_xlabel("Moyenne OVR")
    ax.set_ylabel("Club")
    ax.set_xlim(left=0)
    st.pyplot(fig)
    st.caption("💡 **Justification :** Le barplot compare la moyenne d'OVR par club pour cibler les effectifs les plus compétitifs.")
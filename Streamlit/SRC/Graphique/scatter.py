import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_scatter_ovr_dri(df):
    if len(df) == 0:
        st.warning("Aucun joueur ne correspond aux filtres sélectionnés.")
        return
        
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.regplot(
        data=df, 
        x='DRI', 
        y='OVR', 
        scatter_kws={'alpha': 0.3, 'color': '#2b5c8f'}, 
        line_kws={'color': '#e74c3c'},
        ax=ax
    )
    ax.set_title("Relation entre Dribble (DRI) et Note Générale (OVR)")
    ax.set_xlabel("Dribble (DRI)")
    ax.set_ylabel("Note Générale (OVR)")
    st.pyplot(fig)
    st.caption("💡 **Justification :** Le nuage de points montre la corrélation directe entre la maîtrise technique et la note globale.")
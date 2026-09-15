import streamlit as st

def afficher_kpis(df):
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre de Joueurs", f"{len(df):,}")
    col2.metric("Note Moyenne OVR", f"{df['OVR'].mean():.2f}" if len(df) > 0 else "N/A")
    col3.metric("Âge Moyen", f"{df['Age'].mean():.1f} ans" if len(df) > 0 else "N/A")
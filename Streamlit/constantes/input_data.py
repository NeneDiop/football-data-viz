import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    # Détermine le dossier actuel de ce fichier python
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Chemins possibles pour all_players_clean.csv
    possible_paths = [
        os.path.join(current_dir, "..", "all_players_clean.csv"), # Dans le dossier Streamlit/
        os.path.join(current_dir, "..", "..", "all_players_clean.csv"), # À la racine du projet
        "Streamlit/all_players_clean.csv",
        "all_players_clean.csv"
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return pd.read_csv(path)
            
    # Si non trouvé, tentative directe
    return pd.read_csv("Streamlit/all_players_clean.csv")
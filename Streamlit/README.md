# Application Streamlit — Analyse et Recrutement EA Sports FC

## Question métier
Comment identifier les meilleurs profils de joueurs selon des critères tactiques (poste, vitesse, dribble) pour optimiser le recrutement d'un club ?

## Choix des visualisations
- **Histogramme (Distribution)** : Analyse la répartition des notes globales (OVR) pour évaluer la rareté des profils d'élite dans le championnat sélectionné.
- **Barplot (Comparaison)** : Compare la moyenne OVR des 10 meilleurs clubs pour identifier les équipes dominantes du secteur.
- **Nuage de points (Relation)** : Évalue la corrélation entre le niveau de Dribble (DRI) et la Note Générale (OVR) avec une ligne de tendance.

## Limites du dataset
Le jeu de données se limite aux statistiques issues du jeu vidéo EA Sports FC et ne prend pas en compte les données médicales, le temps de jeu réel ou les valeurs marchandes financières réelles en temps réel.

## Lancement de l'application
`streamlit run main.py`
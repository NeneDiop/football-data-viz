import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration du style Seaborn
sns.set_theme(style="whitegrid")
df = pd.read_csv('all_players_clean.csv')

#==========================================
# 1. Compréhension du dataset
#==========================================

# Quelles sont les colonnes quantitatives ? Les colonnes qualitatives ?
# Variables quantitatives (46 au total) :
# Note globale et attributs principaux : OVR, PAC, SHO, PAS, DRI, DEF, PHY. 
# Attributs physiques et biométriques : Age, Height, Weight. 
# Attributs détaillés de jeu : Acceleration, Sprint.Speed, Finishing, Shot.Power, Dribbling, Agility, Stamina, Strength, etc. 
# Statistiques spécifiques aux gardiens (GK) : GK.Diving, GK.Handling, GK.Kicking, GK.Positioning, GK.Reflexes. 
# Variables qualitatives (9 au total) :
# Name, Position, Preferred.foot, Alternative.positions, Nation, League, Team, url, gender. 

# Quel est le joueur ayant la meilleure note OVR ?
# Le jeu possède 4 joueurs/joueuses à la note maximale de 91 OVR :
# 1.	Kylian Mbappé (Real Madrid / LALIGA EA SPORTS) 
# 2.	Rodri (Manchester City / Premier League) 
# 3.	Erling Haaland (Manchester City / Premier League) 
# 4.	Aitana Bonmatí (FC Barcelona / Liga F) 

# Quelles sont les 5 ligues les plus représentées ?
#1.	Sudamericana (826 joueurs) 
#2.	MLS (762 joueurs) 
#3.	EFL Championship (683 joueurs) 
#4.	EFL League One (615 joueurs) 
#5.	Premier League (597 joueurs) 

# ==========================================
# 2. VISUALISATIONS UNIVARIÉES
# ==========================================

# A. Variables quantitatives
# Distribution OVR
plt.figure(figsize=(8, 4))
sns.histplot(df['OVR'], kde=True, color='skyblue', bins=30)
plt.title("Distribution de la note générale (OVR)")
plt.show()

# Comparaison PAC et PHY côte à côte
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df['PAC'], ax=axes[0], color='lightgreen', kde=True)
axes[0].set_title("Distribution de PAC (Vitesse)")
sns.histplot(df['PHY'], ax=axes[1], color='salmon', kde=True)
axes[1].set_title("Distribution de PHY (Physique)")
plt.tight_layout()
plt.show()

# Densité KDE pour DRI
plt.figure(figsize=(8, 4))
sns.kdeplot(df['DRI'], fill=True, color='purple')
plt.title("Densité de probabilité pour la statistique DRI (Dribble)")
plt.show()

# B. Variables qualitatives
# Championnats les plus représentés
plt.figure(figsize=(10, 5))
top_leagues_order = df['League'].value_counts().head(10).index
sns.countplot(data=df, y='League', order=top_leagues_order, palette='viridis')
plt.title("Top 10 des ligues les plus représentées")
plt.show()

# Pays le plus présent : England (1590 joueurs)
plt.figure(figsize=(10, 5))
top_nations_order = df['Nation'].value_counts().head(10).index
sns.countplot(data=df, y='Nation', order=top_nations_order, palette='magma')
plt.title("Top 10 des pays les plus représentés")
plt.show()

# ==========================================
# 3. VISUALISATIONS BIVARIÉES
# ==========================================

# Relation PAC vs OVR
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='PAC', y='OVR', alpha=0.3, color='blue')
plt.title("Relation entre Vitesse (PAC) et Note Générale (OVR)")
plt.show()

# Régression linéaire DRI vs OVR
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='DRI', y='OVR', scatter_kws={'alpha':0.1}, line_kws={'color':'red'})
plt.title("Régression linéaire entre Dribble (DRI) et OVR")
plt.show()

# Jointplot PAS vs DRI
sns.jointplot(data=df, x='PAS', y='DRI', kind='scatter', alpha=0.2, color='teal')
plt.suptitle("Jointplot : Passe (PAS) vs Dribble (DRI)", y=1.02)
plt.show()

# Pairplot complet
cols_pairplot = ['OVR', 'PAC', 'SHO', 'PAS', 'DRI']
sns.pairplot(df[cols_pairplot].dropna(), diag_kind='kde', plot_kws={'alpha':0.2})
plt.show()

# Boxplot OVR par League (Top 5 ligues)
plt.figure(figsize=(10, 5))
top5_leagues = df['League'].value_counts().head(5).index
sns.boxplot(data=df[df['League'].isin(top5_leagues)], x='League', y='OVR', palette='Set2')
plt.title("Note OVR par Ligue (Top 5 ligues)")
plt.xticks(rotation=15)
plt.show()

# Comparer PAC, DRI, SHO entre 3 grands championnats
big3 = ['Premier League', 'LALIGA EA SPORTS', 'Bundesliga']
df_big3 = df[df['League'].isin(big3)].melt(id_vars=['League'], value_vars=['PAC', 'DRI', 'SHO'], var_name='Stat', value_name='Valeur')

plt.figure(figsize=(10, 5))
sns.boxplot(data=df_big3, x='Stat', y='Valeur', hue='League', palette='Set1')
plt.title("Comparaison de PAC, DRI, SHO entre 3 grands championnats")
plt.show()

# Violinplot DRI par Poste (ou par Ligue)
plt.figure(figsize=(12, 5))
top_positions = df['Position'].value_counts().head(8).index
sns.violinplot(data=df[df['Position'].isin(top_positions)], x='Position', y='DRI', inner="quartile")
plt.title("Distribution du Dribble (DRI) par Poste")
plt.show()

# Championnat avec la plus grande moyenne physique (PHY) -> Barplot
plt.figure(figsize=(10, 5))
phy_order = df.groupby('League')['PHY'].mean().sort_values(ascending=False).head(8).index
sns.barplot(data=df[df['League'].isin(phy_order)], x='PHY', y='League', order=phy_order, palette='crest')
plt.title("Championnats avec la plus grande moyenne en Physique (PHY)")
plt.show()

# ==========================================
# 4. VISUALISATIONS MULTIVARIÉES
# ==========================================

# Catplot OVR par League séparé par Nation (Top 5 nations)
top5_nations = df['Nation'].value_counts().head(5).index
df_cat = df[(df['League'].isin(top5_leagues)) & (df['Nation'].isin(top5_nations))]

sns.catplot(data=df_cat, x='League', y='OVR', hue='Nation', kind='box', height=5, aspect=2)
plt.title("OVR par Ligue et par Nation (Top 5)")
plt.xticks(rotation=20)
plt.show()

# Lmplot PAC vs SHO coloré par Ligue (Big 3)
sns.lmplot(data=df[df['League'].isin(big3)], x='PAC', y='SHO', hue='League', scatter_kws={'alpha':0.2}, height=6)
plt.title("PAC vs SHO par Ligue avec droite de régression")
plt.show()

# Heatmap de corrélation
plt.figure(figsize=(10, 8))
num_stats = ['OVR', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY', 'Age']
sns.heatmap(df[num_stats].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap des corrélations des statistiques numériques")
plt.show()

# FacetGrid : distribution OVR séparée par Ligue
g = sns.FacetGrid(df[df['League'].isin(top5_leagues)], col='League', col_wrap=3, height=3)
g.map(sns.histplot, 'OVR', kde=True, color='indigo')
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Distribution de l'OVR par Ligue")
plt.show()

# ==========================================
# 5. PERFORMANCE SPORTIVE
# ==========================================

# Ligue la plus explosive (Acceleration + Sprint.Speed)
df['Explosivity'] = df['Acceleration'] + df['Sprint.Speed']
plt.figure(figsize=(10, 5))
exp_order = df.groupby('League')['Explosivity'].mean().sort_values(ascending=False).head(8).index
sns.barplot(data=df[df['League'].isin(exp_order)], x='Explosivity', y='League', order=exp_order, palette='rocket')
plt.title("Ligues aux joueurs les plus explosifs (Moyenne Acceleration + Sprint Speed)")
plt.show()

# Équilibre Attaque vs Défense : Scatterplot (SHO + DRI) vs DEF
df['Attacking'] = df['SHO'] + df['DRI']
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Attacking', y='DEF', alpha=0.3, hue='Position', palette='tab10')
plt.title("Équilibre Attaque (SHO + DRI) vs Défense (DEF)")
plt.show()

# Radar Chart : Profil moyen par championnat (Bonus Matplotlib)
categories = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']
N = len(categories)

# Sélection de 3 championnats
leagues_radar = ['Premier League', 'LALIGA EA SPORTS', 'MLS']
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)

for league in leagues_radar:
    values = df[df['League'] == league][categories].mean().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=league)
    ax.fill(angles, values, alpha=0.1)

plt.xticks(angles[:-1], categories)
plt.title("Profil statistique moyen par Championnat")
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()

# ==========================================
# 6. EXERCICES AVANCÉS
# ==========================================

# 1. Top 10 clubs avec la meilleure moyenne d'OVR (au moins 15 joueurs)
top_clubs = df.groupby('Team').filter(lambda x: len(x) >= 15)
club_order = top_clubs.groupby('Team')['OVR'].mean().sort_values(ascending=False).head(10).index

plt.figure(figsize=(10, 5))
sns.barplot(data=top_clubs[top_clubs['Team'].isin(club_order)], x='OVR', y='Team', order=club_order, palette='Blues_r')
plt.title("Top 10 des clubs avec la meilleure moyenne d'OVR")
plt.show()

# 2. Distribution des gardiens de but (GK) vs Joueurs de champ
df['Type_Joueur'] = df['Position'].apply(lambda x: 'Gardien' if x == 'GK' else 'Joueur de champ')
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='OVR', hue='Type_Joueur', fill=True, common_norm=False, palette='Set1')
plt.title("Distribution de la note OVR : Gardiens vs Joueurs de champ")
plt.show()

# 3. Variance des statistiques par championnat (Boxplot global)
plt.figure(figsize=(12, 5))
sns.boxplot(data=df[df['League'].isin(top5_leagues)], x='League', y='OVR', palette='coolwarm')
plt.title("Variance de l'OVR par championnat (Top 5)")
plt.show()

# 4. Variation des stats physiques (PHY, DEF) par Nation
df_phys_nation = df[df['Nation'].isin(top5_nations)].melt(id_vars=['Nation'], value_vars=['PHY', 'DEF'], var_name='Stat_Physique', value_name='Valeur')
sns.catplot(data=df_phys_nation, x='Nation', y='Valeur', hue='Stat_Physique', kind='box', height=5, aspect=2)
plt.title("Variation des statistiques physiques (PHY, DEF) par Nation")
plt.show()
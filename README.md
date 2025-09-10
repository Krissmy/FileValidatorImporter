📂 File Validator & Importer

Un petit projet Python qui permet de :

Lire des fichiers CSV, Excel (.xls/.xlsx) et TXT

Vérifier les valeurs manquantes dans les données

Sauvegarder les données dans une base de données relationnelle SQLite

Utiliser soit une version console (CLI), soit une interface graphique (Tkinter)

🚀 Fonctionnalités
✅ Version Console (CLI)

Demande le chemin d’un fichier CSV, Excel ou TXT

Affiche un aperçu des données

Vérifie si des valeurs sont manquantes

Sauvegarde les données dans une base SQLite (fichiers.db)

🎨 Version Graphique (Tkinter)

Bouton pour charger un fichier depuis l’ordinateur

Affichage d’un aperçu des 10 premières lignes

Message si des valeurs sont manquantes

Bouton pour sauvegarder dans SQLite

🛠️ Installation

Clone le dépôt et installe les dépendances :

git clone https://github.com/ton-utilisateur/FileValidatorImporter.git
cd FileValidatorImporter
pip install pandas openpyxl


(⚠️ tkinter est inclus avec Python par défaut sur Windows/Mac. Sur Linux, installe python3-tk si nécessaire.)

-----------Utilisation------------
🔹Version Console
python cli_importer.py


Puis entrer le chemin du fichier (CSV, Excel, TXT).

🔹 Version Graphique
python gui_importer.py


Une fenêtre Tkinter s’ouvre avec deux boutons :

 Charger un fichier → choisir CSV/Excel/TXT

💾 Sauvegarder en DB → insérer les données dans SQLite


📦 Base de données

Les données sont stockées dans fichiers.db (SQLite).
Tu peux les explorer avec un outil comme DB Browser for SQLite ou avec Python :

import sqlite3
conn = sqlite3.connect("fichiers.db")
df = pd.read_sql("SELECT * FROM data", conn)
print(df.head())


👨‍💻 Auteur

Projet réalisé par K.A.TARNAGDA.
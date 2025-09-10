import pandas as pd
import sqlite3
import os

def lire_fichier(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(path)
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(path)
    elif ext == ".txt":
        df = pd.read_csv(path, delimiter="\t")
    else:
        raise ValueError("Format non supporté : " + ext)
    return df

def verifier_donnees(df):
    if df.isnull().values.any():
        print("Le fichier contient des valeurs manquantes.")
    else:
        print("Pas de données manquantes.")
    return df.isnull().sum()

def sauvegarder_db(df, table="data"):
    conn = sqlite3.connect("fichiers.db")
    df.to_sql(table, conn, if_exists="append", index=False)
    conn.close()
    print(f"Données sauvegardées dans la base SQLite (table {table})")

if __name__ == "__main__":
    fichier = input("Entrez le chemin du fichier (CSV, Excel, TXT): ")
    try:
        data = lire_fichier(fichier)
        print("Aperçu du fichier :")
        print(data.head())

        verifier_donnees(data)

        save = input("Voulez-vous sauvegarder dans la base ? (o/n): ").lower()
        if save == "o":
            sauvegarder_db(data)
    except Exception as e:
        print("Erreur :", e)

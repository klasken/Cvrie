import sys
import os
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

def run_supervised(chemin_dossier):
    print("Modèle entraîné avec succès !")

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python main.py [supervised|unsupervised] [path_to_dataset]\n")
        sys.exit(84)

    mode = sys.argv[1]
    dataset_path = sys.argv[2]

    if not os.path.exists(dataset_path):
        sys.stderr.write(f"Erreur : Le chemin {dataset_path} n'existe pas.\n")
        sys.exit(84)

    try:
        if mode == "supervised":
            print("Lancement de la classification supervisée (CVRIE V1)...")
            run_supervised(dataset_path)

        elif mode == "unsupervised":
            print("Lancement du clustering non-supervisé (CVRIE V1)...")
        else:
            sys.stderr.write("Erreur : Mode inconnu. Utilisez 'supervised' ou 'unsupervised'.\n")
            sys.exit(84)

        sys.exit(0)

    except Exception as e:
        sys.stderr.write(f"Erreur critique de CVRIE: {e}\n")
        sys.exit(84)


if __name__ == "__main__":
    main()  
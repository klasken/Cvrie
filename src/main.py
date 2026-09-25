import sys

def print_help():
    """
    Affiche l'aide sur la sortie d'erreur standard.
    """
    print("USAGE:", file=sys.stderr)
    print("    python3 main.py [filepath]", file=sys.stderr)
    print("DESCRIPTION:", file=sys.stderr)
    print("    filepath : chemin vers le jeu de données (CSV ou dossier d'images).", file=sys.stderr)

def main():
    try:
        if len(sys.argv) != 2:
            print("Erreur : Nombre d'arguments invalide.", file=sys.stderr)
            print_help()
            sys.exit(84)
        filepath = sys.argv[1]
        try:
            with open(filepath, 'r') as file:
                pass
        except FileNotFoundError:
            print(f"Erreur : Le fichier ou dossier '{filepath}' est introuvable.", file=sys.stderr)
            sys.exit(84)
        except PermissionError:
            print(f"Erreur : Permission refusée pour lire '{filepath}'.", file=sys.stderr)
            sys.exit(84)
        print("Programme CVRIE exécuté avec succès.")
        sys.exit(0)

    except Exception as e:
        print(f"Erreur inattendue du système : {e}", file=sys.stderr)
        sys.exit(84)

if __name__ == "__main__":
    main()
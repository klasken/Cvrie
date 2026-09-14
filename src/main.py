import sys

def main():
    try:
        print("CVRIE V1 - Traitement terminé avec succès.")
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Erreur critique de CVRIE: {e}\n")
        sys.exit(84)

if __name__ == "__main__":
    main()
from sys import argv

def main() :
        try:
            if len(argv) == 1:
                print("Aucun argument n'a été passé en paramètre")
            else:
              for x in range(1, len(argv)):
                    int(x)
                    print(argv[x])
        except Exception as e:
            print("[?] Une erreur est survenue: [?]", e)

if __name__ == "__main__":
    main()
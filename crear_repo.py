# para correr el codigo de .cmd pon en simbolo de sistema el nombre que le pongas a create_repo nombre_repo


import sys
import os


def create():
    nombre_repo = str(sys.argv[1])

    print(nombre_repo)


if __name__ == "__main__":
    create()

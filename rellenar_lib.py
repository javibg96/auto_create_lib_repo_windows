from shutil import copy
import sys
from crear_repo import get_cfg


def rellenar():
    nombre_repo = str(sys.argv[1])
    cfg = get_cfg()
    base_path = cfg["ruta_base"]
    git_ignore = base_path + nombre_repo + "\\.gitignore"
    setup = base_path + nombre_repo + "\\setup.py"
    mani = base_path + nombre_repo + "\\manifest.ini"

    print("rellenando libreria...")

    copy(".gitignore", git_ignore)
    copy("setup.py", setup)
    cambio = open(setup).read()
    cambio = cambio.replace("traductor_csv", nombre_repo)
    my_file = open(setup, "w")
    my_file.write(cambio)

    copy(".gitignore", git_ignore)
    copy("manifest.ini", mani)


if __name__ == "__main__":
    rellenar()

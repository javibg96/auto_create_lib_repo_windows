# para correr el codigo de .cmd pon en simbolo de sistema el nombre que le pongas a create_repo nombre_repo


import sys
import os
import errno
import gc
import re
from ruamel import yaml
import logging
from github import Github


def create():
    nombre_repo = str(sys.argv[1])
    print(nombre_repo)
    cfg = get_cfg()
    print(cfg)
    base_path = cfg["ruta_base"]
    username = cfg["username"]
    password = cfg["password"]
    user = Github(username, password).get_user()
    print(user)
    path = base_path + nombre_repo + "/src"

    try:  # si la carpeta existe almacena ahi, sino la crea, valido para almacenar en local
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    logging.error(
                        "specified path is not possible to be created")
                    raise
        gc.collect()
        logging.info("\nCreated " + path)
    except:  # try catch en caso de que no funcione el almacenamiento
        logging.error(f"Error creating repo in path {path}")
        raise


def get_cfg():
    """Parse the YAML config"""
    pattern = re.compile(r"\$\{(.*)\}(.*)$")
    yaml.add_implicit_resolver("!env", pattern)

    def env_constructor(loader, node):
        """Constructor for environment variables"""
        value = loader.construct_scalar(node)
        env_var, remaining_path = pattern.match(value).groups()
        return os.environ[env_var] + remaining_path

    yaml.add_constructor('!env', env_constructor)
    with open("git_creds.yml") as config:
        try:
            cfg = yaml.load(config, Loader=yaml.Loader)
        except yaml.YAMLError:
            logging.error("Error while loading config file.")
            raise
    return cfg


if __name__ == "__main__":
    create()



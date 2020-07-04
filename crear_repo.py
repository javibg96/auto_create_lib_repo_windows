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
    cfg = get_cfg()
    token = cfg["pers_token"]
    user = Github(token).get_user()
    user.create_repo(nombre_repo)


def get_cfg(ruta_base=""):
    """Parse the YAML config"""
    pattern = re.compile(r"\$\{(.*)\}(.*)$")
    yaml.add_implicit_resolver("!env", pattern)

    def env_constructor(loader, node):
        """Constructor for environment variables"""
        value = loader.construct_scalar(node)
        env_var, remaining_path = pattern.match(value).groups()
        return os.environ[env_var] + remaining_path

    yaml.add_constructor('!env', env_constructor)
    ruta_cfg = ruta_base + "git_creds.yml"
    with open(ruta_cfg) as config:
        try:
            cfg = yaml.load(config, Loader=yaml.Loader)
        except yaml.YAMLError:
            logging.error("Error while loading config file.")
            raise
    return cfg


if __name__ == "__main__":
    create()



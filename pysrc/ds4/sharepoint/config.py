import io
from os import environ

import yaml

# from hashids import Hashids

# import as
#   > from sharepoint import config
# use options
#   > config.c.XXX
#   > config.config.XXX
config = None
c = None


def init():
    global config
    global c
    data = _get_init_data_from_env("SHAREPOINT_CONFIG_PATH")
    config = c = Config(data)
    return config


def _get_init_data_from_env(env_keyname: str = "SHAREPOINT_CONFIG_PATH"):
    config_filepath = environ.get(env_keyname, "").strip()
    if not config_filepath:
        return {}
    with io.open(config_filepath, "r", encoding="utf-8") as fd:
        data = yaml.load(fd, Loader=yaml.FullLoader)
    return data


def _find(data, path, default=None):
    keys = path.split(".")
    rv = data
    for key in keys:
        rv = rv.get(key, {})
    return rv or default


class Config:
    def __init__(self, data={}):
        self.CLIENT_ID = _find(data, "client_id")
        self.CLIENT_SECRET = _find(data, "client_secret")

        # self.CORS_ORIGINS = _find(data, "cors_origins")

        # self.DS3_BACKEND = _find(data, "backends.ds3")
        # self.COOKIE_DOMAIN = _find(data, "cookie_domain")

        # self.ACCESS_TOKEN_SECRET = _find(data, "access_token_secret")
        # self.R_SALT = _find(data, "hashids.r_salt")
        # self.S_SALT = _find(data, "hashids.s_salt")
        # self.HASH_MIN_LEN = int(_find(data, "hashids.min_length"))
        # self.HASH_ALPHABET = _find(data, "hashids.alphabet")
        # self.TEMP_DIR = _find(data, "temp_dir")
        # self.R_HASHIDS = Hashids(
        #     salt=self.R_SALT,
        #     min_length=int(self.HASH_MIN_LEN),
        #     alphabet=self.HASH_ALPHABET,
        # )
        # self.S_HASHIDS = Hashids(
        #     salt=self.S_SALT,
        #     min_length=int(self.HASH_MIN_LEN),
        #     alphabet=self.HASH_ALPHABET,
        # )

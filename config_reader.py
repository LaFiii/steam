import json


class ConfigReader:
    DEFAULT_TIMEOUT = 10
    DEFAULT_BASE_URL = "https://store.steampowered.com/"
    CONFIG_PATH = "config.json"

    config = None

    @classmethod
    def load_config(cls):
        if cls.config is None:
            with open(cls.CONFIG_PATH, 'r') as f:
                cls.config = json.load(f)
        return cls.config

    @classmethod
    def get_timeout(cls):
        return cls.load_config()['default_timeout']

    @classmethod
    def get_base_url(cls):
        return cls.load_config()['base_url']

    @classmethod
    def get_expected_min_results(cls, game_name):
        mapping = cls.load_config()['expected_min_results']
        return mapping[game_name]

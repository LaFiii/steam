import json


class ConfigReader:
    config = None

    @classmethod
    def load_config(cls):
        if cls.config is None:
            with open('config.json', 'r') as f:
                cls.config = json.load(f)
        return cls.config

    @classmethod
    def get_timeout(cls):
        return cls.load_config().get('default_timeout', 10)

    @classmethod
    def get_base_url(cls) -> str:
        return cls.load_config().get('base_url', 'https://store.steampowered.com/')

    @classmethod
    def get_expected_min_results(cls, game_name):
        mapping = cls.load_config().get('expected_min_results', {})
        return mapping.get(game_name, 0)

import configparser
from pathlib import Path


def logs_path():
    """Path to the directory where are the files"""
    config = configparser.ConfigParser()
    config.read('././configuration.ini')
    if config:  # берем путь из конфига
        return config['aggregator']['directory']
    return Path(__file__).parent.parent.parent / 'logs'  # берем дефолтный путь до директории logs внутри проекта

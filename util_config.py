import configparser
import sys

CONFIG_FILE = 'dorg.config.ini'
config_parser = configparser.ConfigParser()

def initialize_config (LOGGER):
    LOGGER.info('reading config file...')

    config_parser.read(CONFIG_FILE)

    config = { "groups": {}, "exclusions": {} }
    exclusions = config_parser['EXCLUSIONS']
    config['exclusions']['folders'] = eval(exclusions['folders'])
    config['exclusions']['files'] = eval(exclusions['files'])
    config['exclusions']['extensions'] = eval(exclusions['extensions'])

    for section in config_parser:
        if section == 'DEFAULT' or section == 'EXCLUSIONS': continue

        group = config_parser[section]
        folder = group['folder']
        exts = eval(group['extensions'])

        for ext in exts:
            if ext in config:
                LOGGER.error('duplicate extension "' + ext + '" in another group, please check your config')
                sys.exit()
            config['groups'][ext] = folder

    LOGGER.info('config file loaded')
    return config

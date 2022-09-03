import configparser

class Read:
    def __init__(self, config_file = 'config/default.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_config(self, section, key):
        return self.config.get(section, key)
    
    def get_default(self, key):
        section = 'DEFAULT'
        return self.config.get(section, key)
    
    def get_colors(self, key):
        section = 'COLORS'
        return f'#{self.config.get(section, key)}'
    
class Write:
    def __init__(self, config_file = 'config/default.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
    
    def write_config(self, section, key, value):
        self.config.set(section, key, value)
        with open('config/default.ini', 'a+') as configfile:
            self.config.write(configfile)
            
import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")


class readconfig:

    @staticmethod
    def getapplicationURL():
        url = config.get('common info', 'baseURL')
        return url

import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class readconfig:


    @staticmethod
    def geturl():
        url=config.get('common info1','baseurl')
        return url
    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info1', 'password')
        return password







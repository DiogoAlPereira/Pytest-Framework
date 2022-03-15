import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUser():
        user=config.get('common info', 'user')
        return user

    @staticmethod
    def getPassword():
        password=config.get('common info', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstname = config.get('common info', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getZipCode():
        zipcode = config.get('common info', 'zipcode')
        return zipcode


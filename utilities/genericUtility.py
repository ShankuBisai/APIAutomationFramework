"""
@package utilities

This Python file will have a list of utilites that we would be using in our code

"""
import logging as logger
import random
import string
from datetime import datetime,timedelta

class GenericUtilities(object):
    def __init__(self):
        pass

    @staticmethod
    def generateRandomEmailAndPassword(domain = None,email_prefix=None):
        logger.debug("Generating Random email and password")

        if not domain:
            domain = "gmail.com"
        if not email_prefix:
            email_prefix = "testuser"

        randomEmailStringLength = 10
        randomString = "".join(random.choices(string.ascii_lowercase,k = randomEmailStringLength))
        email = email_prefix + "_" + randomString + "@" + domain

        passwordLength = 10
        password = "".join(random.choices(string.ascii_letters,k = randomEmailStringLength))

        randomInfo = {"email":email,"password":password}
        logger.debug("Random email and password generated")
        return randomInfo


    @staticmethod
    def searchValueinListOfDictionary(list,key,searchValue):
        for item in list:
            if item[key] == searchValue:
                return True
            else:
                return False


    @staticmethod
    def generateRandomString(length=10,prefix= None,suffix=None):
        randomString = "".join(random.choices(string.ascii_lowercase, k=length))
        if prefix:
            randomString = prefix + randomString
        if suffix:
            randomString = randomString + suffix
        return randomString


    @staticmethod
    def dateIsoFormat():
        daysFromToday = 30
        tmpDate = datetime.now() - timedelta(days=daysFromToday)
        afterCreatedDate = tmpDate.strftime("%Y-%m-%dT%H:%m:%S")
        return afterCreatedDate





from setuptools import setup
from typing import List

REQUIREMENTS_FILE_NAME ="requirements.txt"

def get_requirements_list():
    """
    Description : This function is going to return list of requiremetnt
    mention in requirements.txt file

    returns this function is going to return a list which will contain name 
    of libraries mention in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    



#Declaring variables for setup functions
PROJECT_NAME = "housing_predictor"
VERSION = '0.0.1'
AUTHOR = "Naresh_singh"
DESCRIPTION = "This is a first project of FSDS NOV batch"
setup(
name=PROJECT_NAME,
version =VERSION,
author = AUTHOR,
description= DESCRIPTION,
packages =["housing"],
install_requires = get_requirements_list()
)


from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requiremetns=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = "ML_Experiments",
    version = '0.0.1',
    author = 'Soma Sekhar Vuyyuru',
    author_email = 'vuyyurusomasekhar2004@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
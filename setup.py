from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(filepath:str)->List[str]:

    '''
    This function returns list of pachakes to install

    '''
    requirements = []
    with open(filepath) as fileobj:

        requirements = fileobj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name='mlproject_202303',
    version='0.0.1',
    author='Safil',
    author_email='safilpm@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')


)
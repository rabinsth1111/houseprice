from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip().replace('\n','') for req in requirements] 
        clean_requirements = []   
        for i in range(len(requirements)):
            if  requirements[i]!='':
                clean_requirements.append(requirements[i])
                

    return clean_requirements

setup(
    name = 'RegressorProject',
    version = '0.0.1',
    author = 'Rabin',
    author_email = 'rabinsth1111@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()

)

#print(range(5))
#print(get_requirements('requirements.txt'))
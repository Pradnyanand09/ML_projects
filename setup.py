from setuptools import find_packages,setup
from typing import List 

HYPEN_E_DOT="-e ."
def get_reuirements(file_path :str)->List[str]:
    """
    Function to read requirements from a file and return a list of requirements.
    """
    requirement=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="pradnyanand",
    author_email="pradnyanand09@gmail.com",
    install_requires= get_reuirements('requirements.txt'),


)
from setuptools import find_packages, setup # type: ignore
from typing import List

def get_requirements() -> List[str]:
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_lst

setup(
    name='Network-security',
    version='0.0.1',
    author="Adwait-Palsule",
    author_email='palsuleadwait@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

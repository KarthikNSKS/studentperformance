from setuptools import find_packages,setup
from typing import List

HYPEN_E="-e ."

def get_packages(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [items.replace("\n","") for items in file_obj]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements


setup(
    name="studentperformance",
    version="3.11.5",
    author="Karthik",
    author_email="karthikns.inbox@gmail.com",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt")
)
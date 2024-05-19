from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str) -> List[str]:
    """
    Args:
        filename: Path to requirements.txt.
    Returns:
        requirements: List of packages required by project.
    """

    with open(filepath) as f:
        requirements = f.read().splitlines()
    
    if "-e ." in requirements:
        requirements.remove("-e .")
    
    return requirements

setup(
    name="youtube-sentiment",
    version="0.0.1",
    author="jameszcliu",
    author_email="jameszcliu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
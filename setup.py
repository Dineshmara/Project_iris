from setuptools import find_packages, setup

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='project-iris',
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
)
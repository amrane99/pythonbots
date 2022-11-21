from setuptools import setup, find_packages

setup(
    name='pythonbots',
    version='0.1',
    description='A project boundling several Bots for Python.',
    url='https://github.com/amrane99/pythonbots',
    keywords='python setuptools',
    packages=find_packages(include=['bots', 'bots.*']),
)
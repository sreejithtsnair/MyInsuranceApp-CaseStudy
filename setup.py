
from setuptools import setup, find_packages

setup(
    name='myinsuranceapp',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/sreejithtsnair/MyInsuranceApp-CaseStudy.git',
    author='UnaxRincySree',
    author_email='team1@example.com'
)


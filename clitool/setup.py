from importlib_metadata import entry_points
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'clitool',
    version = '1.0.0',
    description = 'cli tool',
    long_description = readme,
    packages=find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [],
    entry_points={
        'console_scripts': 'clitool=clitool.cli:main'
    }
)
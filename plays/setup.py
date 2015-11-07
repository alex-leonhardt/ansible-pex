from setuptools import setup, find_packages
from glob import glob

setup(
  name='plays',
  author='ale',
  author_email='ale@somewhere.com',
  url='http://aaa.aa.com',
  version='0.0.1',
  include_package_data = True,
  packages=find_packages(),
  package_data={},
  install_requires=['ansible', 'argparse'],
)

from setuptools import setup, find_packages


setup(name='apitest',
      version='1.0',
      packages=find_packages(),
      install_requires=[
          "pytest==5.4.2",
          "pytest-html==2.1.1",
          "requests==2.23.0"
      ])
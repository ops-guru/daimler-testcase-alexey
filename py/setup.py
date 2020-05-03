# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Mercedes-Benz AG Programming Challenge",
    author_email="ezh@ezh.msk.ru",
    url="https://github.com/ezh/opsguru-ag-challenge",
    keywords=["Swagger", "Mercedes-Benz AG Programming Challenge"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    - Implement the specified REST Endpoint - Protect the API with BasicAuth - Use Docker to run your application - Use one of the following languages&amp;#58; Go, Java, Python, C++ - Automate the infrastructure rollout - Use an external service to determine the city name for depature and destination - Upload your solution to a private GitHub repository - Provide a link to the secured hosted instance of your solution - Provide the following files together with your code&amp;#58;   * Dockerfile   * Build-Script   * Deployment-Script   * Kubernetes deployment YAML (if Kubernetes is used)   * Infrastructure automation scripts   * README.md with documentation how to deploy the infrastructure and the application 
    """
)


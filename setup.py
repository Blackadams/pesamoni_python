# coding: utf-8

"""
    Pesaway Pesamoni API Documentation

"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pesamoni-pyapi"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Pesaway Pesamoni API Documentation",
    author_email="",
    url="https://github.com/Pesamoni/pesamoni_python",
    keywords=["Pesamoni", "Pesaway Pesamoni API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Automate mobile money payments, bank transfers and more..  # noqa: E501
    """
)

from setuptools import find_packages, setup

setup(
    name="ds4.sharepoint",
    version="0.0.7",
    packages=find_packages(),
    install_requires=[
        # internal
        # "ds4.auth",
        # external
        "O365",
    ],
)

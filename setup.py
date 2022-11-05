from distutils.core import setup


setup(

    # Application name:
    name="uvicorn_framework",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Maris Erts",
    author_email="mariserts84@gmail.com",

    # Packages
    packages=["uvicorn_framework"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "Jinja2==3.1.2",
        "pydantic==1.10.2",
        "SQLAlchemy==1.4.42",
        "uvicorn==0.19.0",
    ],

)

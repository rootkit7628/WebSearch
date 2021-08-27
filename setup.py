import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="websearch",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="iTeam-$ @iTeam-S",                     # Full name of the author
    description="Module python permettant de faire différente recherche de liens sur le Web.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6', 
    py_modules=["websearch"],              # Name of the python package
    install_requires=["BeautifulSoup4", "requests"]                     # Install other dependencies if any
)
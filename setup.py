from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Chi-Square Test for string columns'
LONG_DESCRIPTION = 'Pyspark has a function named ChiSquareTest which calculates the chi-square between two columns, but this function only accepts the numerical columns; by this package, a function named ChiSquareTestForString will be added to pyspark, which calculates the chi-square for string columns.'

setup(
        name="ChiSquareTestForString", 
        version=VERSION,
        author="Sasan Sharifipour",
        author_email="<sasansharifipour@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pyspark'],        
        keywords=['python', 'pyspark', 'ChiSquareTest', 'ChiSquareTestForString'],
        classifiers= [
            "Development Status :: Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
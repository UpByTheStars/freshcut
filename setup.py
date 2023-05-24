from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Freshcut
LONG_DESCRIPTION = 'Test'

# Setting up
setup(
        name="freshcut", 
        version=VERSION,
        author="UpByTheStars",
        author_email="admin@upbythestars.dev",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['freshcut', 'api', 'freshcut api']
)
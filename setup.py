from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Remove comments and empty lines
    requirements = [line.strip() for line in lines if line and not line.startswith('#')]
    return requirements

setup(
    name='covid19_detection',  
    version='0.1.0',  # Initial release version 
    author='johnrana02',  
    author_email='anujrana89114@gmail.com', 
    description='A project to detect COVID-19 from radiography images',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/johnrana02/Covid-19-Detection',  
    packages=find_packages(where='src'),  
    package_dir={'': 'src'},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License 2.0',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
     install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'covid19-detect=src.main:main',  
        ],
    },
)

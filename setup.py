from setuptools import setup, find_packages

# Function to read requirements.txt
def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name='orca-driver-mock',
    version='0.1.0', 
    description='A mock driver for the Orca Laboratory Automation Software',
    author='Cheshire Labs',
    author_email='michaeltsalmi@cheshirelabs.com',
    url='https://github.com/Cheshire-Labs/mock-driver',
    packages=find_packages(where='src'),
    install_requires=read_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU Affero General Public License v3 (AGPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)

from setuptools import setup, find_packages

setup(
    name='Project_Package',
    version='1.0.0',
    author='Cameron Preasmyer',
    author_email='spc6uz@virginia.edu',
    description='A Monte Carlo simulator with Die, Game, and Analyzer classes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://https://github.com/Preasmyer/Project_Package',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            # Example entry point for a command-line tool
            'montecarlo=montecarlo.__main__:main',
        ],
    },
)

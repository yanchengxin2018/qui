from setuptools import setup

setup(
    name='qui',
    version='2024.2.7.18',
    entry_points={
        'console_scripts': [
            'qui = qui.main:main',
        ],
    },
    packages=['qui'],
)

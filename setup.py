#!/usr/local/bin python3
from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Daria Litvintseva",
    author_email="litv.daria@gmail.com",
    url="https://github.com/litdarya/hangman-CI",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-pylint",
    ],
    tests_require=[
        "pytest",
        "pylint"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)

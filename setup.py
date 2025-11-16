from setuptools import setup, find_packages

setup(
    name="unimath",
    version="1.4.4",
    packages=find_packages(),
    install_requires=[
        "sympy","matplotlib"
    ],
    author="Poyraz Soylu",
    author_email="psoylu3467@gmail.com",
    description="Mathematical Environment Library in Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jolankaa/unimath",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
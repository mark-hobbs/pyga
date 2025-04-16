from setuptools import setup, find_packages

setup(
    name="pyga",
    version="0.0.1",
    description="A general-purpose genetic algorithm implemented in Python",
    author="Mark Hobbs",
    author_email="markhobbs91@gmail.com",
    url="https://github.com/mark-hobbs/pyga",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "tqdm",
        "matplotlib",
    ]
)
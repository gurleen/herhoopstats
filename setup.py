import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="herhoopstats",
    packages=find_packages(),
    version="0.0.1",
    description="Programmatic access to the Her Hoop Stats website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    author="Gurleen Singh",
    author_email="gs585@drexel.edu",
    url="https://github.com/gurleen/herhoopstats",
    download_url="https://github.com/gurleen/herhoopstats/archive/refs/heads/main.zip",
    keywords=["sports", "basketball", "stats"],
    install_requires=["requests", "bs4", "MechanicalSoup"],
    python_requires=">=3",
)

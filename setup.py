import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="youtube_easy_api",
    version="0.0.4",
    description="How to search among Youtube videos and extract their metadata using an easy interface.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pdrm83/youtube_api_wrapper",
    author="Pedram Ataee",
    author_email="pedram.ataee@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["youtube_easy_api"],
    include_package_data=True,
    install_requires=['urllib', 'google-api-python-client', 'google-auth-oauthlib', 'google'],
    entry_points={
        "console_scripts": [
            "pdrm83=youtube_easy_api.__main__:main",
        ]
    },
)
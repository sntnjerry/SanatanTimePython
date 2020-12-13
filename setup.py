from setuptools import setup

VERSION = "v1.0"

readme = open("readme.md", "r").read();

setup(
    name = "sanatantime",
    packages = ["sanatantime"],
    version = VERSION,
    license = "MIT",
    description = "Python module to convert christian system time to vedic sanatan time.",
    long_description = readme,
    long_description_content_type = "text/markdown",
    author = "Abhay Tripathi",
    author_email = "jerrymmm00@gmail.com",
    url = "https://github.com/sntnjerry/SanatanTimePython",
    download_url = "https://github.com/sntnjerry/SanatanTimePython/archive/" + VERSION + ".tar.gz",
    keywords = ["Sanatan Time", "Historic Time", "Vedic", "Sanatan", "Christian", "Christian Time"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)

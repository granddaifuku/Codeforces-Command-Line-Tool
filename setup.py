import setuptools
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

with open(os.path.join(root_dir, "src", "__init__.py")) as fi:
    init_text = fi.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    licenses = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    description = re.search(r'__description__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)



setuptools.setup(
    name="cft",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    packages=setuptools.find_packages(),
    package_data={
        "": ["main*"]
    },
    entry_points={
        "console_scripts": [
            "cft = src.cft:main"
        ]
    },
    install_requirements=[
        "shutil", "requests"
    ],
    platforms="any",
    license=licenses
)

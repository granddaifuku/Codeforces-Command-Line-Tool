import setuptools

setuptools.setup(
    name="cft",
    version="1.0.0",
    description="codeforces command line tool",
    author="granddaifuku",
    author_email="grandnadaifuku@gmail.com",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "cft = cf_cli:main"
        ]
    },
    install_requirements=[
        "shutil", "requests"
    ],
    license='MIT'
)

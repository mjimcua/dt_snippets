import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dt-snippets",
    version="1.0.0",
    author="Miguel Ángel Jiménez Cuadrillero",
    author_email="miguelangeljimenezcuadrillero@gmail.com",
    description="Datetime snippets for data scientist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Luce IT Copyright",
        "Operating System :: OS Independent",
    ),
    python_requires='~=3.6'
)
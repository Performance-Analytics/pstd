import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pstd",
    version="0.0.1",
    author="Carter Hinsley",
    author_email="carterhinsley@outlook.com",
    description="Procedural Strength Training Director",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Performance-Analytics/pstd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
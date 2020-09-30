import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyDSALib",
    version="0.01",
    author="Ian Wu",
    author_email="ianyhwu.97@gmail.com",
    description="A library of data structures, implemented in Python for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HerrHruby/PyDSL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
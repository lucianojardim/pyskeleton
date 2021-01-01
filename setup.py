""" setup for my_package """
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-package-lucianoj",
    version="0.0.9",
    author="lucianoj",
    author_email="author@example.com",
    description="Test publish python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github/lucianojardim/pyskeleton",
    packages=["my_package"],
    scripts=["bin/my_package"],
    install_requires=[
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

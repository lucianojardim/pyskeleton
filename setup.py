import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-package-lucianoj",
    version="0.0.8",
    author="lucianoj",
    author_email="author@example.com",
    description="Test publish python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://test.pypi.org/project/my-package-lucianoj",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

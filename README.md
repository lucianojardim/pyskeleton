# Example from VSCODE tutorial

Run ". ./setup.sh" -> select python intepreter installed locally

## Commands to setup everything

- python3 -m venv .venv # create virtual environment
- source .venv/bin/activate
- python -m pip install --upgrade pip
- python -m pip install pep8 # code formatter
- python -m pip install --upgrade autopep8 # code formatter
- python -m pip install pylint # linter. Can disable linter for a line using the following: # pylint: disable=wrong-import-position,unused-import
- pylint --generate-rcfile > .pylintrc
- make
- python -m pip install --upgrade setuptools wheel
- python setup.py sdist bdist_wheel
- python -m pip install --upgrade twine
- python -m twine upload --repository testpypi dist/* # Uploading distributions to <https://test.pypi.org/legacy/>
- python -m pip install --index-url <https://test.pypi.org/simple/> --no-deps my-package-lucianoj
- to test the package that was installed: run intepreter: python, then import my_package, and then my_package.execute()
- python -m pip uninstall my-package-lucianoj
- Use vscode to enable test framework pytest: > python configure tests (it also installs the pytest module)
- python -m pip install pytest-xdist # execute tests in parallel, remember to create associated pytest.ini
- python -m pip install jupyter # support for notebooks
- python -m pip install -e /Users/jardiml/development/python/temp # publish local packages using setup.py

## To execute the package (option #1: as a module)

- python -m my_package (__main__.py found in the my_package folder gets executed)

## To execute the package (option #2: as a package)

- Invoke the interactive interpreter: python
- Once inside, load the code: from my_package import execute
- Then run the function: execute()

default: installdev

#
# Cleanup
#
cleanup: cleanup-build cleanup-develop

cleanup-build:
	rm -fr build/
	rm -fr dist/

cleanup-develop:
	find . -name '*.egg-info' -exec rm -fr {} +

#
# Install and Freeze requirements
#
setup: install-basics install-reqs freeze

install-basics:
	python -m pip install --upgrade pip setuptools

install-reqs:
	python -m pip install -r requirements.txt

freeze:
	python -m pip freeze --all > requirements-freeze.txt

#
# Build and Publish
#
build: cleanup-build
	python setup.py sdist bdist_wheel
	ls -l dist

uploadtest: build
	python -m twine upload --repository testpypi dist/*

uploadprod: build
	python -m twine upload dist/*

#
# Install
#
installdev: cleanup
	python -m pip uninstall -y my-package-lucianoj
	python -m pip install -e .
	python -m pip list -e

installtest:
	python -m pip uninstall -y my-package-lucianoj
	python -m pip install --index-url https://test.pypi.org/simple/ my-package-lucianoj

installprod:
	python -m pip uninstall -y my-package-lucianoj
	python -m pip install my-package-lucianoj

#
# Others
#
.PHONY: init setup cleanup build freeze default
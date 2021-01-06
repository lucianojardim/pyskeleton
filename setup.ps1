python -m venv .venv

source .venv/Scrips/activate

python -m pip install --upgrade pip setuptools

python -m pip install -r requirements.txt

python -m pip freeze --all > requirements-freeze.txt

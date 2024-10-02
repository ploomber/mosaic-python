# Dash mosaic

Live demo: [dash-mosaic.ploomberapp.io](https://dash-mosaic.ploomberapp.io/)

## Installation

```sh
pip install dash-mosaic
```

## Run demo locally

```sh
cd demo
pip install -r requirements.txt
python app.py
```

Open: http://localhost:8050


## Documentation


## Setup

```sh
npm install
pip install -e .

pip install -r requirements.txt
pip install -r tests/requirements.txt
```

## Development

```sh
npm run build
python demo.py
```


## Release

```sh
# generate
npm run build
python setup.py sdist bdist_wheel
ls dist

# test artifact
pip install dash dist/dash_mosaic-0.0.1.tar.gz
python demo/app.py

# upload
pip install twine
twine upload dist/*

# clean up
rm -rf dist
```
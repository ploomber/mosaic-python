# streamlit-mosaic

## Development

```sh
# in one terminal
npm run start

# in another terminal
ST_MOSAIC_DEV=true && streamlit run demo/app.py
```

## Release

```sh
pip install build twine

cd streamlit-mosaic

cd streamlit_mosaic/frontend
npm run build
cd ../../

python -m build
twine upload dist/*
rm -rf dist
```

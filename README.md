<p align="center">
    <h1 align="center"><b>Mosaic Python</b></h1>
	<p align="center">
		Python bindings for <a href="https://github.com/uwdata/mosaic/" target="_blank">Mosaic</a>
    <br />
    <br />
    <br />
    <img width="100" height="100" src="https://avatars.githubusercontent.com/u/60114551?s=200&v=4" alt="Ploomber Logo">
    <br />
    <b>  Made by <a href="https://ploomber.io/?utm_source=mosaic-python&utm_medium=github">Ploomber</a> with ❤️</b>
    <br />
    <br />
    <i>Deploy Streamlit and Dash apps on <a href="https://www.platform.ploomber.io/register/?utm_source=mosaic-python&utm_medium=github">Ploomber.io</a> for free.</i>
    <br />
  </p>
</p>
<br/>


1. [Dash Mosaic](#dash-mosaic) (component for [Dash](https://github.com/plotly/dash))
2. [Streamlit Mosaic](#streamlit-mosaic) (component for [Streamlit](https://github.com/streamlit/streamlit))
3. Mosaic Spec: Python implementation of [Mosaic Spec](https://idl.uw.edu/mosaic/spec/) (coming soon!)

## Dash Mosaic

https://github.com/user-attachments/assets/dc4b9c4d-2381-4251-b926-cd9a6f4ad244

### Installation

```sh
pip install dash-mosaic-ploomber
```

<details>
<summary>Why?</summary>
dash-mosaic is already taken on PyPI.
</details>

### Usage

```python
from dash import Dash, html
import dash_mosaic

app = Dash(__name__)

# your mosaic spec as a python dictionary
spec = {...}

app.layout = html.Div(
    [
        dash_mosaic.DashMosaic(
            id="my-plot",
            spec=spec,
            # if None, it'll use DuckDB WASM. If a string, it'll use the
            # restConnector (if the url begins with "http") or the
            # socketConnector (if it begins with "ws")
            # **IMPORTANT** if you want to load a local file, you cannot pass
            # uri=None. See the latest section in the README.md
            uri=None,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
```


<details>
<summary>Click to expand full code example</summary>

```python
from dash import Dash, html
import dash_mosaic

app = Dash(__name__)

spec = {
    "meta": {
        "title": "Interactive Penguin Bill Measurements",
        "description": "Scatterplot of bill length vs depth with interactive selection",
    },
    "data": {
        "penguins": {
            "type": "parquet",
            "file": "https://raw.githubusercontent.com/uwdata/mosaic/refs/heads/main/data/penguins.parquet",
        }
    },
    "params": {
        "brush": {"select": "crossfilter"},
        "domain": ["Adelie", "Chinstrap", "Gentoo"],
        "colors": ["#1f77b4", "#ff7f0e", "#2ca02c"],
    },
    "vconcat": [
        {
            "name": "scatterplot",
            "width": 600,
            "height": 400,
            "xLabel": "Bill Length (mm) →",
            "yLabel": "↑ Bill Depth (mm)",
            "colorDomain": "$domain",
            "colorRange": "$colors",
            "plot": [
                {
                    "fill": "species",
                    "x": "bill_length",
                    "y": "bill_depth",
                    "data": {"from": "penguins", "filterBy": "$brush"},
                    "mark": "dot",
                },
                {"as": "$brush", "select": "intervalXY"},
            ],
        },
        {
            "name": "species_count",
            "width": 600,
            "height": 200,
            "xLabel": "Penguin Species →",
            "yLabel": "↑ Count",
            "colorDomain": "$domain",
            "colorRange": "$colors",
            "plot": [
                {
                    "fill": "species",
                    "y": {"count": None},
                    "x": "species",
                    "data": {"from": "penguins", "filterBy": "$brush"},
                    "mark": "barY",
                }
            ],
        },
    ],
}


app.layout = html.Div(
    [
        dash_mosaic.DashMosaic(
            id="penguin-plot",
            spec=spec,
            # **IMPORTANT** if you want to load a local file, you cannot pass
            # uri=None. See the latest section in the README.md
            uri=None,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
```

</details>

### Demo

```sh
cd dash-mosaic/demo
pip install -r requirements.txt
python app.py
```

Open: http://localhost:8050

## Streamlit Mosaic


https://github.com/user-attachments/assets/b018d900-7515-45ef-b708-8223d3f3df5c


### Installation

```sh
pip install streamlit-mosaic
```

### Usage

```python
import streamlit as st
from streamlit_mosaic import mosaic

# your mosaic spec as a dictionary
spec = {...}

mosaic(spec=spec,
       height=600,
        # if None, it'll use DuckDB WASM. If a string, it'll use the
        # restConnector (if the url begins with "http") or the
        # socketConnector (if it begins with "ws")
        # **IMPORTANT** if you want to load a local file, you cannot pass
        # uri=None. See the latest section in the README.md
       uri=None)
```



<details>
<summary>Click to expand full code example</summary>

```python
import streamlit as st
from streamlit_mosaic import mosaic

spec = {
    "meta": {
        "title": "Interactive Penguin Bill Measurements",
        "description": "Scatterplot of bill length vs depth with interactive selection",
    },
    "data": {
        "penguins": {
            "type": "parquet",
            "file": "https://raw.githubusercontent.com/uwdata/mosaic/refs/heads/main/data/penguins.parquet",
        }
    },
    "params": {
        "brush": {"select": "crossfilter"},
        "domain": ["Adelie", "Chinstrap", "Gentoo"],
        "colors": ["#1f77b4", "#ff7f0e", "#2ca02c"],
    },
    "vconcat": [
        {
            "name": "scatterplot",
            "width": 600,
            "height": 400,
            "xLabel": "Bill Length (mm) →",
            "yLabel": "↑ Bill Depth (mm)",
            "colorDomain": "$domain",
            "colorRange": "$colors",
            "plot": [
                {
                    "fill": "species",
                    "x": "bill_length",
                    "y": "bill_depth",
                    "data": {"from": "penguins", "filterBy": "$brush"},
                    "mark": "dot",
                },
                {"as": "$brush", "select": "intervalXY"},
            ],
        },
        {
            "name": "species_count",
            "width": 600,
            "height": 200,
            "xLabel": "Penguin Species →",
            "yLabel": "↑ Count",
            "colorDomain": "$domain",
            "colorRange": "$colors",
            "plot": [
                {
                    "fill": "species",
                    "y": {"count": None},
                    "x": "species",
                    "data": {"from": "penguins", "filterBy": "$brush"},
                    "mark": "barY",
                }
            ],
        },
    ],
}

# **IMPORTANT** if you want to load a local file, you cannot pass
# uri=None. See the latest section in the README.md
mosaic(spec=spec, height=600, uri=None)
```

</details>

### Demo

```sh
cd streamlit-mosaic/demo
pip install -r requirements.txt
streamlit run app.py
```


Open: http://localhost:8501

## Loading local files

If you want to visualize local files with `dash-mosaic` or `streamlit-mosaic`, passing
`uri=None` **won't work**. Instead, you can pass: `http://localhost:3000` and run
the `duckdb-server`:

```sh
pip install duckdb-server
duckdb-server
```

Read more in [Mosaic's documentation](https://idl.uw.edu/mosaic/server/).
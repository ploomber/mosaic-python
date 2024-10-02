# Mosaic Python

Python bindings for [Mosaic](https://github.com/uwdata/mosaic/)

1. [Dash Mosaic](#dash-mosaic) (component for [Dash](https://github.com/plotly/dash))
2. Streamlit Mosaic (coming soon!)
3. Mosaic Spec: Python implementation of [Mosaic Spec](https://idl.uw.edu/mosaic/spec/) (coming soon!)

## Dash Mosaic

https://github.com/user-attachments/assets/dc4b9c4d-2381-4251-b926-cd9a6f4ad244

```sh
pip install dash-mosaic-ploomber
```

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
            uri=None,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
```

</details>

### Demo

Run demo locally:

```sh
cd dash-mosaic/demo
pip install -r requirements.txt
python app.py
```

Open: http://localhost:8050

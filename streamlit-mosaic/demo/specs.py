basic = {
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

flights_10m = {
    "meta": {"title": "Cross-Filter Flights (10M)", "description": "description"},
    "data": {
        "flights10m": "SELECT GREATEST(-60, LEAST(ARR_DELAY, 180))::DOUBLE AS delay, DISTANCE AS distance, DEP_TIME AS time FROM 'https://idl.uw.edu/mosaic-datasets/data/flights-10m.parquet'"
    },
    "params": {"brush": {"select": "crossfilter"}},
    "vconcat": [
        {
            "plot": [
                {
                    "mark": "rectY",
                    "data": {"from": "flights10m", "filterBy": "$brush"},
                    "x": {"bin": "delay"},
                    "y": {"count": None},
                    "fill": "steelblue",
                    "inset": 0.5,
                },
                {"select": "intervalX", "as": "$brush"},
            ],
            "xDomain": "Fixed",
            "marginLeft": 75,
            "width": 600,
            "height": 200,
        },
        {
            "plot": [
                {
                    "mark": "rectY",
                    "data": {"from": "flights10m", "filterBy": "$brush"},
                    "x": {"bin": "time"},
                    "y": {"count": None},
                    "fill": "steelblue",
                    "inset": 0.5,
                },
                {"select": "intervalX", "as": "$brush"},
            ],
            "xDomain": "Fixed",
            "marginLeft": 75,
            "width": 600,
            "height": 200,
        },
        {
            "plot": [
                {
                    "mark": "rectY",
                    "data": {"from": "flights10m", "filterBy": "$brush"},
                    "x": {"bin": "distance"},
                    "y": {"count": None},
                    "fill": "steelblue",
                    "inset": 0.5,
                },
                {"select": "intervalX", "as": "$brush"},
            ],
            "xDomain": "Fixed",
            "marginLeft": 75,
            "width": 600,
            "height": 200,
        },
    ],
}


vonoroi = {
    "meta": {
        "title": "Voronoi Diagram",
        "description": "The `voronoi` mark shows the regions closest to each point. It is [constructed from its dual](https://observablehq.com/@mbostock/the-delaunays-dual), a Delaunay triangle mesh. Reveal triangulations or convex hulls using the dropdowns.\n",
        "credit": "Adapted from an [Observable Plot example](https://observablehq.com/@observablehq/plot-voronoi-scatterplot).",
    },
    "data": {
        "penguins": {
            "file": "https://raw.githubusercontent.com/uwdata/mosaic/refs/heads/main/data/penguins.parquet"
        }
    },
    "params": {"mesh": 0, "hull": 0},
    "vconcat": [
        {
            "plot": [
                {
                    "mark": "voronoi",
                    "data": {"from": "penguins"},
                    "x": "bill_length",
                    "y": "bill_depth",
                    "stroke": "white",
                    "strokeWidth": 1,
                    "strokeOpacity": 0.5,
                    "fill": "species",
                    "fillOpacity": 0.2,
                },
                {
                    "mark": "hull",
                    "data": {"from": "penguins"},
                    "x": "bill_length",
                    "y": "bill_depth",
                    "stroke": "species",
                    "strokeOpacity": "$hull",
                    "strokeWidth": 1.5,
                },
                {
                    "mark": "delaunayMesh",
                    "data": {"from": "penguins"},
                    "x": "bill_length",
                    "y": "bill_depth",
                    "z": "species",
                    "stroke": "species",
                    "strokeOpacity": "$mesh",
                    "strokeWidth": 1,
                },
                {
                    "mark": "dot",
                    "data": {"from": "penguins"},
                    "x": "bill_length",
                    "y": "bill_depth",
                    "fill": "species",
                    "r": 2,
                },
                {"mark": "frame"},
            ],
            "inset": 10,
            "width": 680,
        },
        {
            "hconcat": [
                {
                    "input": "menu",
                    "label": "Delaunay Mesh",
                    "options": [
                        {"value": 0, "label": "Hide"},
                        {"value": 0.5, "label": "Show"},
                    ],
                    "as": "$mesh",
                },
                {"hspace": 5},
                {
                    "input": "menu",
                    "label": "Convex Hull",
                    "options": [
                        {"value": 0, "label": "Hide"},
                        {"value": 1, "label": "Show"},
                    ],
                    "as": "$hull",
                },
            ]
        },
    ],
}


stock = {
    "meta": {
        "title": "Normalized Stock Prices",
        "description": "What is the return on investment for different days? Hover over the chart to normalize the stock prices for the percentage return on a given day. A `nearestX` interactor selects the nearest date, and parameterized expressions reactively update in response.\n",
    },
    "data": {
        "stocks": {
            "file": "https://raw.githubusercontent.com/uwdata/mosaic/refs/heads/main/data/stocks.parquet"
        },
        "labels": "SELECT MAX(Date) as Date, ARGMAX(Close, Date) AS Close, Symbol FROM stocks GROUP BY Symbol",
    },
    "params": {"point": {"date": "2013-05-13"}},
    "plot": [
        {"mark": "ruleX", "x": "$point"},
        {
            "mark": "textX",
            "x": "$point",
            "text": "$point",
            "frameAnchor": "top",
            "lineAnchor": "bottom",
            "dy": -7,
        },
        {
            "mark": "text",
            "data": {"from": "labels"},
            "x": "Date",
            "y": {
                "sql": "Close / (SELECT MAX(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
            },
            "dx": 2,
            "text": "Symbol",
            "fill": "Symbol",
            "textAnchor": "start",
        },
        {
            "mark": "lineY",
            "data": {"from": "stocks"},
            "x": "Date",
            "y": {
                "sql": "Close / (SELECT MAX(Close) FROM stocks WHERE Symbol = source.Symbol AND Date = $point)"
            },
            "stroke": "Symbol",
        },
        {"select": "nearestX", "as": "$point"},
    ],
    "yScale": "log",
    "yDomain": [0.2, 6],
    "yGrid": True,
    "xLabel": None,
    "yLabel": None,
    "yTickFormat": "%",
    "width": 680,
    "height": 400,
    "marginRight": 35,
}

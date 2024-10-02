import dash
from dash import Dash, html
import dash_material_ui as mui
import dash_mosaic
import specs
import util
from pathlib import Path

dash._dash_renderer._set_react_version("18.2.0")

app = Dash(__name__, use_pages=True, pages_folder="")
server = app.server

uri = None
# uri = "http://localhost:3000"

# Register the home page
dash.register_page(
    "home",
    path="/",
    layout=mui.App(
        mui.Grid(
            children=util.create_mosaic_item(
                title="Interactive Penguin Bill Measurements",
                description="This chart demonstrates a basic mosaic chart with interactive elements.",
                spec=specs.basic,
                uri=uri,
                id="penguin-plot",
            )
        )
    ),
)

dash.register_page(
    "flights",
    path="/flights",
    layout=mui.App(
        mui.Grid(
            children=util.create_mosaic_item(
                title="Cross-Filter Flights (10M)",
                description="Histograms showing arrival delay, departure time, and distance flown for 10 million flights. Once loaded, automatically-generated indexes enable efficient cross-filtered selections. You may need to wait a few seconds for the dataset to load.",
                spec=specs.flights_10m,
                uri=uri,
                id="flights-plot",
            )
        )
    ),
)

dash.register_page(
    "vonoroi",
    path="/vonoroi",
    title="Voronoi Diagram",
    layout=mui.App(
        mui.Grid(
            children=util.create_mosaic_item(
                title="Voronoi Diagram",
                description="This chart demonstrates a Voronoi diagram with interactive elements.",
                spec=specs.vonoroi,
                uri=uri,
                id="vonoroi-chart",
            )
        )
    ),
)

dash.register_page(
    "stocks",
    path="/stocks",
    title="Normalized Stock Prices",
    layout=mui.App(
        mui.Grid(
            children=util.create_mosaic_item(
                title="Normalized Stock Prices",
                description="What is the return on investment for different days? Hover over the chart to normalize the stock prices for the percentage return on a given day.",
                spec=specs.stock,
                uri=uri,
                id="stock-chart",
            )
        )
    ),
)

app.layout = mui.App(
    children=[
        mui.AppBar(
            title="Dash Mosaic",
            showMenuButton=True,
            id="app-bar",
            sections={
                **{
                    page["name"]: page["relative_path"]
                    for page in dash.page_registry.values()
                },
            },
        ),
        html.Div(
            children=[
                dash.page_container,
                # Add extra space to prevent content from being hidden by the footer
                html.Div(style={"height": "60px"}),
            ],
            style={
                "padding-left": "10px",
                "padding-right": "10px",
            },
        ),
        html.Footer(
            html.P(
                [
                    "Made with ❤️ by ",
                    html.A("Ploomber", href="https://ploomber.io", target="_blank"),
                ]
            ),
            style={
                "text-align": "center",
                "padding": "2px",
                "border-top": "1px solid #e0e0e0",
                "position": "fixed",
                "bottom": "0",
                "left": "0",
                "right": "0",
                "background-color": "white",
                "z-index": "1000",
            },
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)

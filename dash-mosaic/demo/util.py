import dash_material_ui as mui
from dash import html
import black
import dash_react_syntax_highlighter
import dash_mosaic


def create_mosaic_item(title, spec, uri, id, description=None):
    component = mui.Item(
        children=[
            dash_mosaic.DashMosaic(
                id=id,
                spec=spec,
                uri=uri,
            )
        ],
        size=6,
    )

    # Format the spec as a Python object
    formatted_spec = black.format_str(f"spec = {spec}", mode=black.Mode(line_length=88))

    component_code = f"""from dash import Dash, html
import dash_mosaic
import dash_material_ui as mui

app = Dash(__name__)

{formatted_spec}

app.layout = html.Div([
    mui.Item(
        children=[
            dash_mosaic.DashMosaic(
                id='{id}',
                spec=spec,
                uri={uri!r},
            )
        ],
        size=8,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
"""

    # Format the code using black
    formatted_code = black.format_str(component_code, mode=black.Mode(line_length=88))

    children = [
        mui.Item(html.H2(title), size=12),
    ]

    if description:
        children.append(mui.Item(html.P(description), size=12))

    children.extend(
        [
            component,
            mui.Item(
                children=[
                    dash_react_syntax_highlighter.DashReactSyntaxHighlighter(
                        code=formatted_code,
                        language="python",
                        styleName="okaidia",
                    ),
                ],
                size=6,
            ),
        ]
    )

    return children

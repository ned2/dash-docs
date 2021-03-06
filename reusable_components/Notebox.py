import dash
import dash_html_components as html
import dash_core_components as dcc
from tutorial import styles

def Notebox(content):
    return html.Div(
        children = [
            dcc.Markdown(content)
        ],
        style=styles.notebox
    )

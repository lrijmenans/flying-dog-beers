import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables

mytitle='Well...after Wizata...first IN HOUSE App!'
tabtitle='TFL'
myheading='First TFL Web App!'



########### Set up the chart





########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.Div(children='''
        Dash: Well...after Wizata...first IN HOUSE App!
    '''),
    dcc.Graph(
        id='AI Walls',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Kiln 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Kiln 2'},
            ],
            'layout': {
                'title': 'AI walls'
            }
        }
    ),
    
    ]
)

if __name__ == '__main__':
    app.run_server()

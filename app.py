import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables

mytitle='Well...after Wizata...first IN HOUSE App!'
tabtitle='TFL'
myheading='First TFL Web App!'

githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
df=pd.read_excel("https://github.com/lrijmenans/flying-dog-beers/AI analyse.xlsx", sheet_name="Tag data")
df=df.pivot(index="Timestamp",columns='Tag name', values='Value')
df=df.reset_index()
fig = px.scatter(df,color="Heat input - Setpoint (BEAI FM1 DB2 Cycle Based Calculation)",y="Wall temperature - Firing zone level 1 - Avg - S1 (BEAI FM1 DB2 Cycle Based Calculation)", x="Solid fuel - Fuel A - NCV (BEAI FM1 DB2 Cycle Based Calculation)", marginal_x="histogram", marginal_y="histogram")




########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='AI Walls',
        figure=fig
    ),
    
    ]
)

if __name__ == '__main__':
    app.run_server()

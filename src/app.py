import dash
from dash import html

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.Div([
        html.H1("الأسهم السعودية")
    ], style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.H3("الصف الثاني - العمود الأول")
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            html.H3("الصف الثاني - العمود الثاني")
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'margin': '20px 0'}),
    
    html.Div([
        html.Div([
            html.H3("الصف الثالث - العمود الأول")
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            html.H3("الصف الثالث - العمود الثاني")
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'margin': '20px 0'}),
    
    html.Div([
        html.Div([
            html.H3("الصف الرابع - العمود الأول")
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            html.H3("الصف الرابع - العمود الثاني")
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'margin': '20px 0'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)

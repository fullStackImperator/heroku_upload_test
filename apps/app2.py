# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
import pandas as pd
from datetime import datetime as dt
import base64
import dash_auth
import plotly
import plotly.figure_factory as ff
from app import app
import dash_table_experiments as dt
import json

####################################################################################

#Image
image_filename = 'bilder/AbsRepGross.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename2 = 'bilder/absrep.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

####################################################################################


DF_WALMART = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

DF_GAPMINDER = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
)
DF_GAPMINDER = DF_GAPMINDER[DF_GAPMINDER['year'] == 2007]
DF_GAPMINDER.loc[0:20]

DF_SIMPLE = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D', 'E', 'F'],
    'y': [4, 3, 1, 2, 3, 6],
    'z': ['a', 'b', 'c', 'a', 'b', 'c']
})

ROWS = [
    {'a': 'AA', 'b': 1},
    {'a': 'AB', 'b': 2},
    {'a': 'BB', 'b': 3},
    {'a': 'BC', 'b': 4},
    {'a': 'CC', 'b': 5},
    {'a': 'CD', 'b': 6}
]




layout = html.Div([
    
################ Header ###############
html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()) , className="brand-logo site-logo")
                #html.A(["Absolut Research"], className="brand-logo site-logo")
            ], id="header-logo"),

            ############### obere leiste ###############
            html.Div([
                html.A([
                    html.I([], className="fa fa-bars"),
                ], className="toggle-siteMenu"),
                html.A([
                    html.I([], className="fa fa-search"),
                ], className="toggle-siteSearchMobile"),
            ], className="meta-nav-mobile"),

            html.A([
                html.I([], className="fa fa-search"),
            ], className="toggle-siteSearch js_popup-init-search"),

            html.Div([
                html.Div([
                    html.A([
                        html.I([], className="fa fa-sign-in"),
                    ], className="js_popup-init-login account-info-login"),
                ], className="user-info-box"),

                html.Div([
                    html.Nav([
                        html.Ul([
                            html.Li([
                                html.A(["Newsletter"], className="first"),
                            ], className="first" ),
                            html.Li([
                                html.A(["Presse"]),
                            ],),
                            html.Li([
                                html.A(["Kontakt"], className="last"),
                            ], className="last" ),
                        ], className="nav meta-nav-menu" ),
                    ]),
                ], className="meta-nav-menu"),

                html.Div([
                    html.Ul([
                        html.Li([
                            html.A([
                                html.I([], className="fa fa-twitter"),
                            ], className="m-socialfollowing-link m-socialfollowing-link--twitter"),
                        ], className="m-socialfollowing-item" ),

                        html.Li([
                            html.A([
                                html.I([], className="fa fa-linkedin"),
                            ], className="m-socialfollowing-link m-socialfollowing-link--linkedin"),
                        ], className="m-socialfollowing-item m-socialfollowing-item--linkedin" ),

                        html.Li([
                            html.A([
                                html.I([], className="fa fa-xing"),
                            ], className="m-socialfollowing-link m-socialfollowing-link--xing"),
                        ], className="m-socialfollowing-item m-socialfollowing-item--xing" ),

                    ]),
                ], className="m-socialfollowing m-socialfollowing--header"),
                
            ], id="meta-nav", className="nav meta-nav"),

            ############### untere leiste ###############
            html.Div([
                html.Div([
                    html.Div([
                        html.Nav([
                            html.Ul([
                                html.Li([
                                    #html.A(["Home"], className="m-navigation-link"),
                                    #html.A([dcc.Link('Home', className="m-navigation-link", href='/apps/app2')], className="m-navigation-link"),
                                    dcc.Link('Report', className="m-navigation-link", href='/apps/app1'),
                                ], id="elem_49", className="m-navigation-item" ),
                                html.Li([
                                    #html.A(["Report"], className="m-navigation-link sf-with-ul"),
                                    dcc.Link('Ranking', className="m-navigation-link sf-with-ul", href='/apps/app2'),
                                ], id="elem_28", className="m-navigation-item m-navigation-item--parent" ),
                                html.Li([
                                    #html.A(["Ranking"], className="m-navigation-link"),
                                    dcc.Link('Optimierung', className="m-navigation-link", href='/apps/app3'),
                                ], id="elem_107", className="m-navigation-item" ),
                                html.Li([
                                    #html.A(["Monitor"], className="m-navigation-link sf-with-ul"),
                                    dcc.Link('Monitor', className="m-navigation-link sf-with-ul", href='/apps/app4'),
                                ], id="elem_31", className="m-navigation-item m-navigation-item--parent" ),
                                html.Li([
                                    #html.A(["Analyse"], className="m-navigation-link sf-with-ul"),
                                    dcc.Link('Analyse', className="m-navigation-link sf-with-ul", href='/apps/app5'),
                                ], id="elem_27", className="m-navigation-item m-navigation-item--parent" ),
                                html.Li([
                                    dcc.Link('Technische Analyse', className="m-navigation-link", href='/apps/app6'),
                                ], id="elem_49", className="m-navigation-item" ),
                            ], className="m-navigation-list sf-js-enabled sf-arrows"),
                        ], className="m-navigation"),
                    ], id="site-menu"),
                ], className="navigation-content"),
            ], className="site-navigation"),

            
        ], className="header-content"),
    ], className="site-wrapper"),
], className= "site-header"),


html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()) ),
                ], id="c1005", className= "csc-default"),
            ], id="c5339", className= "csc-default"),
        ], className= "site-teaser-container"),
    ], className= "site-wrapper"),
], className= "site-content"),
 
 
    ################### Calculations and Plotly ###################
#html.Div([
    html.Div([
    
    #html.H4('Gapminder DataTable'),
    html.H2('Interaktive Tabelle mit interaktiven Charts', style={'margin-bottom': '10px'}),
    dt.DataTable(
        rows=DF_GAPMINDER.to_dict('records'),

        # optional - sets the order of columns
        columns=sorted(DF_GAPMINDER.columns),

        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable-gapminder'
    ),
    html.Div(id='selected-indexes'),
    dcc.Graph(
        id='graph-gapminder'
    ),


    ], className= "site-wrapper", style={'margin-top': '30px', 'margin-bottom': '30px'}),
#], className= "site-content"),

    
], style={'marginBottom': 5, 'marginTop': 0, 'marginLeft': 0, 'marginRight': 0})


@app.callback(
    Output('datatable-gapminder', 'selected_row_indices'),
    [Input('graph-gapminder', 'clickData')],
    [State('datatable-gapminder', 'selected_row_indices')])
def update_selected_row_indices(clickData, selected_row_indices):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices


@app.callback(
    Output('graph-gapminder', 'figure'),
    [Input('datatable-gapminder', 'rows'),
     Input('datatable-gapminder', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Life Expectancy', 'GDP Per Capita', 'Population',),
        shared_xaxes=True)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_row_indices or []):
        marker['color'][i] = '#FF851B'
    fig.append_trace({
        'x': dff['country'],
        'y': dff['lifeExp'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['country'],
        'y': dff['gdpPercap'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['country'],
        'y': dff['pop'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 800
    fig['layout']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    fig['layout']['yaxis3']['type'] = 'log'
    return fig


#app.css.append_css({
#    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
#})

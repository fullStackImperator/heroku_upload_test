# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import colorlover as cl
from datetime import datetime as dt
import base64
import dash_auth
import plotly
import plotly.figure_factory as ff
import dash_table_experiments as dt
import cvxopt as opt
from cvxopt import blas, solvers
from app import app


# hide plotly bar -> does not work, input somewhere else!!
config={'displayModeBar': False}


####################################################################################
# Append an externally hosted CSS stylesheet
#my_css_url = "https://unpkg.com/normalize.css@5.0.0"
my_css_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
app.css.append_css({
    "external_url": my_css_url
})

####################################################################################

#Image
image_filename = 'bilder/AbsRepGross.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename2 = 'bilder/absrep.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

####################################################################################

np.random.seed(0)
df = pd.DataFrame({
    'Column {}'.format(i): np.random.rand(20) + i*10
    for i in range(6)})

####################################################################################



layout = html.Div([
#html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
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

    html.Div([
        html.Div(
            dcc.Graph(
                id='g1',
                # if selectedData is not specified then it is initialized as None
                selectedData={'points': [], 'range': None},
                #config={'displayModeBar': False}
            ), className="four columns"
        ),
        html.Div(
            dcc.Graph(
                id='g2',
                selectedData={'points': [], 'range': None},
                config={'displayModeBar': False}
            ), className="four columns"
        ),
        html.Div(
            dcc.Graph(
                id='g3',
                selectedData={'points': [], 'range': None},
                config={'displayModeBar': False}
            ), className="four columns"
        )
    ],  className="row" ),


    

    ], className= "site-wrapper", style={'margin-top': '30px', 'margin-bottom': '30px'}),
#], className= "site-content"),

    
], style={'marginBottom': 5, 'marginTop': 0, 'marginLeft': 0, 'marginRight': 0})



def highlight(x, y):
    def callback(*selectedDatas):
        index = df.index

        # filter the dataframe by the selected points
        for i, hover_data in enumerate(selectedDatas):
            selected_index = [
                p['customdata'] for p in selectedDatas[i]['points']
                # the first trace that includes all the data
                if p['curveNumber'] == 0
            ]
            if len(selected_index) > 0:
                index = np.intersect1d(index, selected_index)

        dff = df.iloc[index, :]

        color = '#002940' #'rgb(125, 58, 235)'

        trace_template = {
            'marker': {
                'color': color,
                'size': 12,
                'line': {'width': 0.5, 'color': 'white'}
            }
        }
        figure = {
            'data': [
                # the first trace displays all of the points
                # it is dimmed by setting opacity to 0.1
                dict({
                    'x': df[x], 'y': df[y], 'text': df.index,
                    'customdata': df.index,
                    'mode': 'markers', 'opacity': 0.1
                }, **trace_template),

                # the second trace is plotted on top of the first trace and
                # displays the filtered points
                dict({
                    'x': dff[x], 'y': dff[y], 'text': dff.index,
                    'mode': 'markers+text', 'textposition': 'top',
                }, **trace_template),
            ],
            'layout': {
                'margin': {'l': 15, 'r': 0, 'b': 15, 't': 5},
                'dragmode': 'select',
                'hovermode': 'closest',
                'showlegend': False
            }
        }

        # Display a rectangle to highlight the previously selected region
        shape = {
            'type': 'rect',
            'line': {
                'width': 1,
                'dash': 'dot',
                'color': 'darkgrey'
            }
        }
        if selectedDatas[0]['range']:
            figure['layout']['shapes'] = [dict({
                'x0': selectedDatas[0]['range']['x'][0],
                'x1': selectedDatas[0]['range']['x'][1],
                'y0': selectedDatas[0]['range']['y'][0],
                'y1': selectedDatas[0]['range']['y'][1]
            }, **shape)]
        else:
            figure['layout']['shapes'] = [dict({
                'type': 'rect',
                'x0': np.min(df[x]),
                'x1': np.max(df[x]),
                'y0': np.min(df[y]),
                'y1': np.max(df[y])
            }, **shape)]

        return figure

    return callback


#app.css.append_css({
#    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# app.callback is a decorator which means that it takes a function
# as its argument.
# highlight is a function "generator": it's a function that returns function
app.callback(
    Output('g1', 'figure'),
    [Input('g1', 'selectedData'),
     Input('g2', 'selectedData'),
     Input('g3', 'selectedData')]
)(highlight('Column 0', 'Column 1'))

app.callback(
    Output('g2', 'figure'),
    [Input('g2', 'selectedData'),
     Input('g1', 'selectedData'),
     Input('g3', 'selectedData')]
)(highlight('Column 2', 'Column 3'))

app.callback(
    Output('g3', 'figure'),
    [Input('g3', 'selectedData'),
     Input('g1', 'selectedData'),
     Input('g2', 'selectedData')]
)(highlight('Column 4', 'Column 5'))

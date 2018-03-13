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
import base64
import dash_auth
import quantmod as qm
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

df_symbol = pd.read_csv('data/dax_tickers.csv')
df_indikator = pd.read_csv('data/indikatoren2.csv')

functions = dir(qm.ta)[9:-4]
functions = [dict(label=str(function[4:]), value=str(function))
             for function in functions]
#print (functions)
#print (label)
#print (value)
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

        html.Label('Aktienauswahl', style={'width': '470px', 'display': 'inline-block', 'text-align': 'left', 'margin-left': '10px'}),
        html.Label('Indikatorauswahl', style={'width': '470px', 'display': 'inline-block', 'text-align': 'left', 'margin-left': '10px', 'padding-left': '10px'}),
        html.Span(
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': s[0], 'value': s[1]}
                    for s in zip(df_symbol.Company, df_symbol.Symbol)
            ], value='ADS' ),
            style={
                'width': '470px',
                'display': 'inline-block',
                'text-align': 'left',
                'margin-right': '10px'
            },
        ),
            
        # Dropdown for indicators
        html.Span(
            dcc.Dropdown(
                id='multi',
                #options= functions,
                options= [
                    {'label': s[0], 'value': s[1]}
                    for s in zip(df_indikator.Indikator, df_indikator.Symbol)
                #dict(label='EMA', value='EMA'),
                #dict(label='RSI', value='RSI'),
                #dict(label='MACD', value='MACD'),
                #dict(label='BBANDS', value='BBANDS'),
                ],
                multi=True, value=[] ),
            style={
                'width': '470px',
                'display': 'inline-block',
                'text-align': 'left',
                'margin-left': '10px'
            },
        ),

        html.Div([
            html.Label('Parameter für Indikatoren eingeben (optional):'),
            dcc.Input(id='arglist')
        ], id='arg-controls', style={'display': 'none', 'margin-bottom': '10px'}),
        # Graph output
        dcc.Graph(id='output', style={'margin-bottom': '10px', 'margin-top': '10px'}, config={'displayModeBar': False})

    ], className= "site-wrapper", style={'margin-top': '30px', 'margin-bottom': '30px'}),
#], className= "site-content"),

    
], style={'marginBottom': 5, 'marginTop': 0, 'marginLeft': 0, 'marginRight': 0})


# Setup callbacks

@app.callback(Output('arg-controls', 'style'), [Input('multi', 'value')])
def display_control(multi):
    if not multi:
        return {'display': 'none'}
    else:
        return {'display': 'inline-block'}

@app.callback(Output('output', 'figure'), [Input('dropdown', 'value'),
                                           Input('multi', 'value'),
                                           Input('arglist', 'value')])
# @cache.memoize(timeout=timeout)
def update_graph_from_dropdown(dropdown, multi, arglist):
    # Get Quantmod Chart
    ch = qm.get_symbol(dropdown, start='2016/01/01')
    # Get functions
    if arglist:
        arglist = arglist.replace('(', '').replace(')', '').split(';')
        arglist = [args.strip() for args in arglist]
        for function, args in zip(multi, arglist):
            if args:
                args = args.split(',')
                newargs = []
                for arg in args:
                    try:
                        arg = int(arg)
                    except:
                        try:
                            arg = float(arg)
                        except:
                            pass
                    newargs.append(arg)

                print(newargs)
                getattr(qm, function)(ch, *newargs)
            else:
                getattr(qm, function)(ch)
    else:
        for function in multi:
            getattr(qm, function)(ch)

    # Return plot as figure
    fig = ch.to_figure(width=960)
    return fig

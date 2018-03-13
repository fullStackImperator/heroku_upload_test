# -*- coding: utf-8 -*-
import pandas as pd
import dash
from dash import Dash
import plotly.plotly as py
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import colorlover as cl
import numpy as np
from flask import Flask
import base64
from app import app


#Image - Logo
image_filename = 'ttz.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())



#df = pd.read_csv('/Users/werkstudent/Desktop/BvS/BvS Digital/R&D/try/slide/data.csv', names=['Fonds', 'Kategorie', 'Datum', 'Periode', 'Return', 'Risiko'])
df = pd.read_csv('data.csv', names=['Fonds', 'Kategorie', 'Datum', 'Periode', 'Return', 'Risiko'])


min=df['Datum'].min()
max=df['Datum'].max()

marks={str(year): str(year) for year in df['Datum'].unique()}

#print (marks)
#print (min)
#print (max)

available_indicators = df['Periode'].unique()




layout = html.Div([


        # Header
        html.Header([       
            html.Div([
                    html.Img(
                        src='data:image/png;base64,{}'.format(encoded_image.decode()),
                        className='logo',
                        ),
                ], className='imgContainer' ),       
            html.Ul([
                html.Li(  dcc.Link('Digitales Family Office', href='https://digitalesfamilyoffice.de'),),
                html.Li(  dcc.Link('Breidenbach von Schlieffen', href='http://www.bvs-co.com'),),
                html.Li(  dcc.Link('Home', href='/apps/app1'),),
            ]),
        ],
            className='leiste',
        ),


        html.Div([       # Subheader       
            html.Ul([
                html.Li([
                    dcc.Link('Dropdown', href='javascript:void(0)', className='dropbtn2'),
                    html.Div([
                        dcc.Link('Hover', href='/apps/app6'),
                        dcc.Link('Selector', href='/apps/app7'),
                        dcc.Link('Langbericht', href='/apps/app8'),
                        dcc.Link('Optimierung', href='/apps/app9'),
                        dcc.Link('BvS Vergleich', href='/apps/app10'),
                        dcc.Link('Factsheet', href='/apps/app11')],
                    className='dropdown-content')],
                className="dropdown"),
                html.Li(  dcc.Link('Test', href='/apps/app5', className='subLink'), ),
                html.Li(  dcc.Link('Stresstest', href='/apps/app4', className='subLink'),),
                html.Li(  dcc.Link('Zinsen', href='/apps/app3', className='subLink'),),
                html.Li(  dcc.Link('Wertentwicklung', href='/apps/app2', className='subLink'),),
                html.Li(  dcc.Link('Cockpit', href='/apps/app1', className='subLink'),),
            ], className="subUL"),  #002940
        ],
            className='leiste2',
        ),





    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Periode'
            ),

        ],
        style={'width': '48%', 'display': 'inline-block'}),

    ]),

    dcc.Graph(id='graph-with-slider', animate=True, config={'displayModeBar': False}),
    dcc.Slider(
        id='year-slider',
        min=df['Datum'].min(),
        max=df['Datum'].max(),
        value=df['Datum'].min(),
        step=None,

        #min=0,
        #max=3,
        #step=1,
        #value=1,
        
        marks={str(year): str(year) for year in df['Datum'].unique()}
    )
])

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
     #dash.dependencies.Input('xaxis-column', 'value')])
#def update_figure(xaxis_column_name, selected_year):
def update_figure(selected_year):
    filtered_df = df[df.Datum == selected_year]
    print (selected_year)
    traces = []
    #dff = df[df['Year'] == year_value]
    for i in filtered_df.Kategorie.unique():
        df_by_kategorie = filtered_df[filtered_df['Kategorie'] == i]
        traces.append(go.Scatter(
            x=df_by_kategorie['Risiko'],
            #x=dff[dff['lifeExp'] == xaxis_column_name]['Value']
            y=df_by_kategorie['Return'],
            text=df_by_kategorie['Fonds'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Volatilität (%)'},
            yaxis={'title': 'Performance (%)', 'range': [-10, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()


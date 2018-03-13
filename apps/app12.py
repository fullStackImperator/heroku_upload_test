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

#Image - Logo
image_filename2 = 'elbphi.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())



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
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image2.decode()),
                className='elbphiBild',
            ),           
        ],  className='elbphiDiv' ),


])



if __name__ == '__main__':
    app.run_server()


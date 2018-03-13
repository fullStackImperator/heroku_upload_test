 # -*- coding: utf-8 -*-
import os

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State, Event
import dash
import dash_html_components as html
import dash_core_components as dcc
import base64
import colorlover as cl
import datetime as dt
import flask
import os
from pandas_datareader.data import DataReader
import time
import base64
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
from app import app


#Image - Logo
image_filename = 'ttz.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


np.random.seed(123)
# Turn off progress printing 
solvers.options['show_progress'] = False

## NUMBER OF ASSETS
n_assets = 4

## NUMBER OF OBSERVATIONS
n_obs = 1000

return_vec = np.random.randn(n_assets, n_obs)



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
                        dcc.Link('BvS Vergleich', href='/apps/app10')],
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
        



    html.Div(),
    html.Div(
        html.Button(id='submit-button', n_clicks=0, children='Berechne')
    ),
    dcc.Graph(id='scatter-plot',
              config={'displayModeBar': False}
    ),
])

#############################################################################

def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)

def random_portfolio(returns):
    ''' 
    Returns the mean and standard deviation of returns for a random portfolio
    '''

    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))
    
    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    
    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return random_portfolio(returns)
    return mu, sigma

#############################################################################

def optimal_portfolio(returns):
    n = len(returns)
    returns = np.asmatrix(returns)
    
    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]
    
    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))
    
    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    
    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] 
                  for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns, risks

#############################################################################
#############################################################################

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('submit-button', 'n_clicks')])
def update_graph(Manager):
    n_portfolios = 500
    means, stds = np.column_stack([
        random_portfolio(return_vec) 
        for _ in xrange(n_portfolios)
    ])

    weights, returns, risks = optimal_portfolio(return_vec)
    
    #listeM = []
    #listeS = []
    #for i in means:
    #    listeM.append(i)
    #for j in stds:
    #    listeS.append(j)
        
    N = 5
    
    #print (type(means))
    #print (type(np.random.randn(N)))
    #print ( '#####' )
    #print (means.reshape((5,)).shape)
    #print (listeM)
    #print (np.random.randn(N).shape)
    
    
    trace1 = go.Scatter(x=stds.reshape((n_portfolios,)), y=means.reshape((n_portfolios,)), mode = 'markers', name='Markers', marker = dict(
        size = 10,
        color = 'rgba(152, 0, 0, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
    )

    trace2 = go.Scatter(x=risks, y=returns, mode = 'lines+markers', name='Efficient Frontier',
        marker = dict(
            symbol = 'diamond',
            opacity = 1,
            size = 10,
            color = 'rgba(152, 0, 0, .8)',
            line = dict(
                width = 2,
                color = 'rgb(255, 255, 0)'
                )
        ), 
        line = dict(
            color = 'rgb(255, 232, 0)',
            width = 2,
            dash = 'dot',
            smoothing = 1,
            shape = 'spline',
        ), 

    )
    


    return {
        'data': [trace1, trace2], # trace2, trace3, trace4],
        'layout':
        go.Layout()
            #title='Customer Order Status for {}'.format(Manager),
            #barmode='stack')
    }



if __name__ == '__main__':
    app.run_server(debug=True)

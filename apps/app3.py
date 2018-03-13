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

np.random.seed(123)
# Turn off progress printing 
solvers.options['show_progress'] = False

## NUMBER OF ASSETS
n_assets = 4

## NUMBER OF OBSERVATIONS
n_obs = 1000

return_vec = np.random.randn(n_assets, n_obs)

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
            html.H2("Portfolio Optimierung")
        ),

        dcc.Graph(id='scatter-plot',
              config={'displayModeBar': False}
        ),

    ], className= "gi four-fifths desktop-one-whole"),

    html.Div([
        html.Div(
            html.H2("Eingabe")
        ),
        html.Div([
            html.Button(id='submit-button', n_clicks=0, children='Berechne')
        ], style={'margin-top': '10px', 'margin-bottom': '10px'}),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),
        dcc.Input( placeholder=' ISIN...', type='text', value=''),

    ], className= "gi one-fifth desktop-one-whole"),



    ], className= "site-wrapper", style={'margin-top': '30px', 'margin-bottom': '30px'}),
#], className= "site-content"),

    
], style={'marginBottom': 5, 'marginTop': 0, 'marginLeft': 0, 'marginRight': 0})





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
        go.Layout(
            #title='US Export of Plastic Scrap',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
        )
            #title='Customer Order Status for {}'.format(Manager),
            #barmode='stack')
    }

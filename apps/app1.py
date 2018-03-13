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
import dash_table_experiments as dt
import json
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
                dcc.Slider( min=0, max=5, value=0, marks={i: ''.format(i + 1) for i in range(6)}, id='slider'),
            ],className='slider_row',style={'margin-bottom': '10px'}),
            
            html.Div([
                
                html.Div([
                    html.Div([
                        html.Button('Back', id='back', style={'display': 'inline-block'}),
                        html.Button('Next', id='next', style={'display': 'inline-block'})
                    ], className='buttons', style={'justify-content': 'space-between'}),
                    html.Div([
                        """ """
                    ], className='ueber', style={'align-content': 'center', 'align-items': 'center', 'margin-right': '50px'}),
                ], className='one_line', style={'display':'flex', 'margin-bottom': '10px', 'justify-content': 'space-between' }),
                
                dcc.Markdown( id='text'),
                
            ], className='row 2', style={'margin-bottom': '10px'}),
            
           dcc.Graph( id='graph', style={'height': '60vh'}),

    ], className= "site-wrapper", style={'margin-top': '30px', 'margin-bottom': '30px'}),
#], className= "site-content"),

    
], style={'marginBottom': 5, 'marginTop': 0, 'marginLeft': 0, 'marginRight': 0})



#############
# Internal logic
last_back = 0
last_next = 0

df = pd.read_csv("data/yield_curve.csv")

xlist = list(df["x"].dropna())
ylist = list(df["y"].dropna())

del df["x"]
del df["y"]

zlist = []
for row in df.iterrows():
    index, data = row
    zlist.append(data.tolist())

UPS = {
    0: dict(x=0, y=0, z=1),
    1: dict(x=0, y=0, z=1),
    2: dict(x=0, y=0, z=1),
    3: dict(x=0, y=0, z=1),
    4: dict(x=0, y=0, z=1),
    5: dict(x=0, y=0, z=1),
}

CENTERS = {
    0: dict(x=0.3, y=0.8, z=-0.5),
    1: dict(x=0, y=0, z=-0.37),
    2: dict(x=0, y=1.1, z=-1.3),
    3: dict(x=0, y=-0.7, z=0),
    4: dict(x=0, y=-0.2, z=0),
    5: dict(x=-0.11, y=-0.5, z=0),
}

EYES = {
    0: dict(x=2.7, y=2.7, z=0.3),
    1: dict(x=0.01, y=3.8, z=-0.37),
    2: dict(x=1.3, y=3, z=0),
    3: dict(x=2.6, y=-1.6, z=0),
    4: dict(x=3, y=-0.2, z=0),
    5: dict(x=-0.1, y=-0.5, z=2.66)
}

TEXTS = {
    0: '''
    # Yield curve 101
    The yield curve shows how much it costs the federal government to borrow
    money for a given amount of time, revealing the relationship between long-
    and short-term interest rates.
    >>
    It is, inherently, a forecast for what the economy holds in the future —
    how much inflation there will be, for example, and how healthy growth will
    be over the years ahead — all embodied in the price of money today,
    tomorrow and many years from now.
    '''.replace('  ', ''),
    1: '''
    # Where we stand
    On Wednesday, both short-term and long-term rates were lower than they have
    been for most of history – a reflection of the continuing hangover
    from the financial crisis.
    >>
    The yield curve is fairly flat, which is a sign that investors expect
    mediocre growth in the years ahead.
    '''.replace('  ', ''),
    2: '''
    # Deep in the valley
    In response to the last recession, the Federal Reserve has kept short-term
    rates very low — near zero — since 2008. (Lower interest rates stimulate
    the economy, by making it cheaper for people to borrow money, but also
    spark inflation.)
    >>
    Now, the Fed is getting ready to raise rates again, possibly as early as
    June.
    '''.replace('  ', ''),
    3: '''
    # Last time, a puzzle
    The last time the Fed started raising rates was in 2004. From 2004 to 2006,
    short-term rates rose steadily.
    >>
    But long-term rates didn't rise very much.
    >>
    The Federal Reserve chairman called this phenomenon a “conundrum," and it
    raised questions about the ability of the Fed to guide the economy.
    Part of the reason long-term rates failed to rise was because of strong
    foreign demand.
    '''.replace('  ', ''),
    4: '''
    # Long-term rates are low now, too
    Foreign buyers have helped keep long-term rates low recently, too — as have
    new rules encouraging banks to hold government debt and expectations that
    economic growth could be weak for a long time.
    >>
    The 10-year Treasury yield was as low as it has ever been in July 2012 and
    has risen only modestly since.
    Some economists refer to the economic pessimism as “the new normal.”
    '''.replace('  ', ''),
    5: '''
    # Long-term rates are low now, too
    Here is the same chart viewed from above.
    '''.replace('  ', '')
}

ANNOTATIONS = {
    0: [],
    1: [dict(
        showarrow=False,
        x="1-month",
        y='2015-03-18',
        z=0.046,
        text="Short-term rates basically <br>follow the interest rates set <br>by the Federal Reserve.",
        xref='x',
        yref='y',
        zref='z',
        xanchor='left',
        yanchor='auto'
    )],
    2: [],
    3: [],
    4: [],
    5: [],
}
##################


@app.callback(
    Output('app-3-display-value', 'children'),
    [Input('app-3-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)



# Make 3d graph
@app.callback(Output('graph', 'figure'), [Input('slider', 'value')])
def make_graph(value):

    if value is None:
        value = 0

    if value in [0, 2, 3]:
        z_secondary_beginning = [z[1] for z in zlist if z[0] == 'None']
        z_secondary_end = [z[0] for z in zlist if z[0] != 'None']
        z_secondary = z_secondary_beginning + z_secondary_end
        x_secondary = [
            '3-month'] * len(z_secondary_beginning) + ['1-month'] * len(z_secondary_end)
        y_secondary = ylist
        opacity = 0.7

    elif value == 1:
        x_secondary = xlist
        y_secondary = [ylist[-1] for i in xlist]
        z_secondary = zlist[-1]
        opacity = 0.7

    elif value == 4:
        z_secondary = [z[8] for z in zlist]
        x_secondary = ['10-year' for i in z_secondary]
        y_secondary = ylist
        opacity = 0.25

    if value in range(0, 5):

        trace1 = dict(
            type="surface",
            x=xlist,
            y=ylist,
            z=zlist,
            hoverinfo='x+y+z',
            lighting={
                "ambient": 0.95,
                "diffuse": 0.99,
                "fresnel": 0.01,
                "roughness": 0.01,
                "specular": 0.01,
            },
            colorscale=[[0, "rgb(230,245,254)"], [0.4, "rgb(123,171,203)"], [
                0.8, "rgb(40,119,174)"], [1, "rgb(37,61,81)"]],
            opacity=opacity,
            showscale=False,
            zmax=9.18,
            zmin=0,
            scene="scene",
        )

        trace2 = dict(
            type='scatter3d',
            mode='lines',
            x=x_secondary,
            y=y_secondary,
            z=z_secondary,
            hoverinfo='x+y+z',
            line=dict(color='#444444')
        )

        data = [trace1, trace2]

    else:

        trace1 = dict(
            type="contour",
            x=ylist,
            y=xlist,
            z=np.array(zlist).T,
            colorscale=[[0, "rgb(230,245,254)"], [0.4, "rgb(123,171,203)"], [
                0.8, "rgb(40,119,174)"], [1, "rgb(37,61,81)"]],
            showscale=False,
            zmax=9.18,
            zmin=0,
            line=dict(smoothing=1, color='rgba(40,40,40,0.15)'),
            contours=dict(coloring='heatmap')
        )

        data = [trace1]

        # margin = dict(
        #     t=5,
        #     l=50,
        #     b=50,
        #     r=5,
        # ),

    layout = dict(
        autosize=True,
        font=dict(
            size=12,
            color="#CCCCCC",
        ),
        margin=dict(
            t=5,
            l=5,
            b=5,
            r=5,
        ),
        showlegend=False,
        hovermode='closest',
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=2, y=5, z=1.5),
            camera=dict(
                up=UPS[value],
                center=CENTERS[value],
                eye=EYES[value]
            ),
            annotations=[dict(
                showarrow=False,
                y="2015-03-18",
                x="1-month",
                z=0.046,
                text="Point 1",
                xanchor="left",
                xshift=10,
                opacity=0.7
            ), dict(
                y="2015-03-18",
                x="3-month",
                z=0.048,
                text="Point 2",
                textangle=0,
                ax=0,
                ay=-75,
                font=dict(
                    color="black",
                    size=12
                ),
                arrowcolor="black",
                arrowsize=3,
                arrowwidth=1,
                arrowhead=1
            )],
            xaxis={
                "showgrid": True,
                "title": "",
                "type": "category",
                "zeroline": False,
                "categoryorder": 'array',
                "categoryarray": list(reversed(xlist))
            },
            yaxis={
                "showgrid": True,
                "title": "",
                "type": "date",
                "zeroline": False,
            },
        )
    )

    figure = dict(data=data, layout=layout)
    # py.iplot(figure)
    return figure


# Make annotations
@app.callback(Output('text', 'children'), [Input('slider', 'value')])
def make_text(value):
    if value is None:
        value = 0

    return TEXTS[value]


# Button controls
@app.callback(Output('slider', 'value'),
              [Input('back', 'n_clicks'), Input('next', 'n_clicks')],
              [State('slider', 'value')])
def advance_slider(back, nxt, slider):

    if back is None:
        back = 0
    if nxt is None:
        nxt = 0
    if slider is None:
        slider = 0

    global last_back
    global last_next

    if back > last_back:
        last_back = back
        return max(0, slider - 1)
    if nxt > last_next:
        last_next = nxt
        return min(5, slider + 1)

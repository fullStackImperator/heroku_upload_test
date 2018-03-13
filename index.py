 # -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json

from app import app
#from apps import app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, app11, app12  #app1,
from apps import app1, app2, app3, app4, app5, app6 #, app7, app8, app9, app10, app11, app12  #app1,


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
    html.Div(id='page-content')
    
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    elif pathname == '/apps/app3':
         return app3.layout
    elif pathname == '/apps/app4':
         return app4.layout
    elif pathname == '/apps/app5':
         return app5.layout
    elif pathname == '/apps/app6':
         return app6.layout
    elif pathname == '/apps/app7':
         return app7.layout
    elif pathname == '/apps/app8':
         return app8.layout
    elif pathname == '/apps/app9':
         return app9.layout   
    elif pathname == '/apps/app10':
         return app10.layout
    elif pathname == '/apps/app11':
         return app11.layout
    elif pathname == '/apps/app12':
         return app12.layout 
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

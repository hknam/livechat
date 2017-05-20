import plotly
import plotly.graph_objs as go


drama_1 = [112,99,143,222,139,107,107,106,258,116,402,233,75,63,131,93,240,
            70,99,136,80,159,121,217,141,130,80,295,103,183,72,339,183,86,81,
            166,142,67,189,192,62,180,230,125,123,143,186,160,100,516,220,295,
            687,323,230,298,229,340]


# Create and style traces
trace0 = go.Scatter(
    #x = month,
    y = drama_1,
    name = 'drama 1',
    line = dict(
        color = ('#FF0000'),
        width = 4)
)

data = [trace0]
layout = dict(#title = 'Average High and Low Temperatures in New York',
                font=dict(
                family='sans-serif',
                size=24,
                color='#000'
                ),


              xaxis = dict(title = 'Play time', autorange=True,
                            showgrid=False,
                            zeroline=False,
                            showline=True,
                            autotick=True,
                            ticks='',
                            showticklabels=True),
              yaxis = dict(title = '# of posts',
                            autorange=True,
                            showgrid=False,
                            zeroline=True,
                            showline=True,
                            autotick=True,
                            ticks='',
                            showticklabels=True),
              )

fig = go.Figure(data=data,layout=layout)
plotly.offline.plot(
fig, filename='basic_bar_chart.html'
)

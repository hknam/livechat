import plotly
import plotly.graph_objs as go

x = ['Drama', 'Drama', 'Drama', 'Drama', 'Drama',
     'Entertainment', 'Entertainment', 'Entertainment', 'Entertainment',
     'Sports', 'Sports', 'Sports', 'Sports', 'Sports',
     'Online game', 'Online game', 'Online game', 'Online game', 'Online game']

title1 = go.Box(
    y=[ 4.09,2.91,3.36,3.55,2.45,
        2.73,3.55,3.00,3.64,3.09,
        2.82,2.82,2.55,3.45,2.91,
        2.91,2.45,2.45,2.27,3.18
    ],
    x=x,
    name='Title #1',
    marker=dict(
        color='#FF0000'
    )
)
title2 = go.Box(
    y=[ 3.45,3.18,2.36,3.09,2.64,
        2.73,2.55,5.09,3.09,3.64,
        2.45,2.27,2.64,3.82,3.73,
        3.73,3.36,3.09,2.82,3.55
    ],
    x=x,
    name='Title #2',
    marker=dict(
        color='#0100FF'
    )
)
title3 = go.Box(
    y=[ 1.73,1.91,2.73,1.64,2.91,
        3.18,3.27,2.36,4.55,2.27,
        2.82,2.36,2.18,3.55,4.27,
        4.27,1.91,2.09,2.09,2.27
    ],
    x=x,
    name='Title #3',
    marker=dict(
        color='#1DDB16'
    )
)
data = [title1, title2, title3]
layout = go.Layout(
    legend=dict(x=.85, y=1.0),
    font=dict(
            family='sans-serif',
            size=25,
            color='#000'
        ),
    xaxis=dict(
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=True,
        autotick=True,
        ticks='',
        showticklabels=True
    ),

    yaxis=dict(
        title='Ratings',
        #zeroline=False,
        autorange=True,
        showgrid=False,
        zeroline=True,
        showline=True,
        autotick=True,
        ticks='',
        showticklabels=True
    ),
    boxmode='group'
)

fig = go.Figure(data=data,layout=layout)
plotly.offline.plot(
fig, filename='basic_bar_chart.html'
)

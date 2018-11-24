#from bokeh.plotting import figure, output_file, show
#import bokeh.plotting as bk
#from bokeh.layouts import gridplot
#from bokeh.plotting import figure, show, output_file
#from bokeh.models import Range1d
#from bokeh.io import show
#from bokeh.models import LogColorMapper
#from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.resources import CDN
from bokeh.embed import file_html
#from bokeh.models import ColumnDataSource

def htmlbokehplot(df,mi,ma):

    df = df[(df['DEPT'] >= mi) & (df['DEPT'] <= ma)]

    x = df['GR']
    y = df['DEPT']

    # create a new plot with a title and axis labels
    p = figure(title="gamma ray", x_axis_label='x', y_axis_label='y', tools="pan,ywheel_zoom,lasso_select,box_select,hover,reset", tooltips=[("GR", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="GR", line_width=0.5, color='green')
    #new plot
    x2 = df['RHOB']
    p2 = figure(title="density", x_axis_label='x2', y_axis_label='y', tools="pan,ywheel_zoom,lasso_select,box_select,hover,reset", tooltips=[("RHOB", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    # add a line renderer with legend and line thickness
    p2.line(x2, y, legend="RHOB", line_width=0.5, color='blue')
    s = row(p,p2)
    return file_html(s, CDN, "my plot")

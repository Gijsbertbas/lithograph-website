#from bokeh.plotting import figure, output_file, show
#import bokeh.plotting as bk
#from bokeh.layouts import gridplot
#from bokeh.plotting import figure, show, output_file
#from bokeh.models import Range1d
#from bokeh.io import show
#from bokeh.models import LogColorMapper
#from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.layouts import row, gridplot
from bokeh.resources import CDN
from bokeh.embed import file_html
#from bokeh.models import ColumnDataSource

from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.glyphs import Patches
from bokeh.io import curdoc
from scipy import stats
import numpy as np


def lineplots(df):

    x = df['GR']
    y = df['DEPT']
    p = figure(title="gamma ray", x_axis_label='GR (API)', y_axis_label='depth(m)', y_range=(y.max(),y.min()), tools="pan, box_zoom,ywheel_zoom,hover,reset", tooltips=[("GR", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="GR", line_width=0.5, color='green')
    #new plot
    x2 = df['RHOB']
    p2 = figure(title="density", x_axis_label='density (kg/cc)', y_axis_label='depth (m)', y_range=p.y_range, tools="pan,box_zoom,ywheel_zoom,hover,reset", tooltips=[("RHOB", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    p2.line(x2, y, legend="RHOB", line_width=0.5, color='blue')

    x3 = df['NPHI']
    p3 = figure(x_axis_label='neutron porosity', y_axis_label='depth (m)', y_range=p.y_range, x_range=((0,1)), tools="pan,box_zoom,ywheel_zoom,hover,reset", tooltips=[("NPHI", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    p3.line(x3, y, legend="NPHI",line_width=0.5, color='red')

    return p, p2, p3

def lineplots2(df,tracks=['GR','RHOB']):
    x = df['GR']
    y = df['DEPT']

    # create a new plot with a title and axis labels
    p = figure(title="gamma ray", x_axis_label='GR', y_axis_label='depth(m)', y_range=(y.max(), y.min()),tools="pan,ywheel_zoom,lasso_select,box_select,hover,reset", tooltips=[("GR", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="GR", line_width=0.5, color='green')
    #new plot
    x2 = df['RHOB']
    p2 = figure(title="density", x_axis_label='RHOB', y_axis_label='depth(m)', y_range=p.y_range, tools="pan,ywheel_zoom,lasso_select,box_select,hover,reset", tooltips=[("RHOB", "@x"), ("depth", "@y")], plot_width=300, plot_height = 800)
    # add a line renderer with legend and line thickness
    p2.line(x2, y, legend="RHOB", line_width=0.5, color='blue')

    return p, p2


def htmlbokehplot(df):

    p, p2, p3 = lineplots(df)

    s = gridplot([[p,p2,p3]], sizing_mode="scale_width", plot_height=1500)
    #s = row(p,p2)
    return file_html(s, CDN, "my plot")

def htmlclassifiedplot(df,prediction):

    p, p2, p3 = lineplots(df)

    # need to be replaces with predicted lithologies
    #a = np.random.randint(1,9,len(df['DEPT']))
    a = prediction
    b = list(a[0:-1])

    dd = list(np.array(df['DEPT']))
    ddd = []
    c=[]
    #averaging
    sam = 67
    for i in range(round(len(a)/sam)):
        bb = b[i*sam:(i*sam+sam)]
        c.append(list(stats.mode(bb)[0])[0])
        ddd.append(dd[i*sam])

    d2 = [round(d,2) for d in ddd]

    values = c[0:-1]
    depths= d2

    #lithologies
    lithologies = ["sand","shale","siltstone", "Interbededd sand-shale", "limestone", "mudstone", "volcanic","dolomite"]
    thicks = [abs(depths[i+1]-depths[i]) for i in range((len(values)))]

    #initiation of variables
    y1 = []
    y2= []
    y3 = []
    y4=[]
    y5 = []
    y6=[]
    y7=[]
    y8=[]

    x1 = []
    x2 = []
    x3=[]
    x4=[]
    x5=[]
    x6=[]
    x7=[]
    x8=[]

    th = []
    th2 =[]
    th3=[]
    th4=[]
    th5=[]
    th6=[]
    th7=[]
    th8=[]

    lit = []
    lit2 =[]
    lit3 = []
    lit4=[]
    lit5=[]
    lit6=[]
    lit7=[]
    lit8=[]


    #classes
    for i in range((len(values))):
        if values[i] == 1:
            yy = depths[i]
            xx = 0*i
            ttt = thicks[i]
            th.append(ttt)
            x1.append(xx)
            y1.append(yy)
            l = lithologies[0]
            lit.append(l)

    for i in range((len(values))):
        if values[i] == 2:
            yy = depths[i]
            xx = 0*i
            ttt = thicks[i]
            th2.append(ttt)
            x2.append(xx)
            y2.append(yy)
            l = lithologies[1]
            lit2.append(l)

    for i in range((len(values))):
        if values[i] == 3:
            yy = depths[i]
            xx = 0*i
            x3.append(xx)
            y3.append(yy)
            ttt = thicks[i]
            th3.append(ttt)
            l = lithologies[2]
            lit3.append(l)

    for i in range((len(values))):
        if values[i] == 4:
            yy = depths[i]
            xx = 0*i
            x4.append(xx)
            y4.append(yy)
            ttt = thicks[i]
            th4.append(ttt)
            l = lithologies[3]
            lit4.append(l)

    for i in range((len(values))):
        if values[i] == 5:
            yy = depths[i]
            xx = 0*i
            x5.append(xx)
            y5.append(yy)
            ttt = thicks[i]
            th5.append(ttt)
            l = lithologies[4]
            lit5.append(l)

    for i in range((len(values))):
        if values[i] == 6:
            yy = depths[i]
            xx = 0*i
            x6.append(xx)
            y6.append(yy)
            ttt = thicks[i]
            th6.append(ttt)
            l = lithologies[5]
            lit6.append(l)

    for i in range((len(values))):
        if values[i] == 7:
            yy = depths[i]
            xx = 0*i
            x7.append(xx)
            y7.append(yy)
            ttt = thicks[i]
            th7.append(ttt)
            l = lithologies[6]
            lit7.append(l)

    for i in range((len(values))):
        if values[i] == 8:
            yy = depths[i]
            xx = 0*i
            x8.append(xx)
            y8.append(yy)
            ttt = thicks[i]
            th8.append(ttt)
            l = lithologies[7]
            lit8.append(l)


    # shape of the rectangle
    xpts = np.array([1, -1, -1, 1])
    ypts = np.array([0,0,1,1])


    # coordinates of all rectangles
    source3 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x3)],
            ys=[ypts*m+yy for m, yy in zip(th3,y3)],
            lith=[1*ll for ll in lit3]
        )
    )

    source1 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x1)],
            ys=[ypts*m+yy for m, yy in zip(th,y1)],
            lith=[1*ll for ll in lit]
        )
    )

    source2 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x2)],
            ys=[ypts*m+yy for m, yy in zip(th2,y2)],
            lith=[1*ll for ll in lit2]
        )
    )
    source4 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x4)],
            ys=[ypts*m+yy for m, yy in zip(th4,y4)],
            lith=[1*ll for ll in lit4]
        )
    )
    source5 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x5)],
            ys=[ypts*m+yy for m, yy in zip(th5,y5)],
            lith=[1*ll for ll in lit5]
        )
    )

    source6 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x6)],
            ys=[ypts*m+yy for m, yy in zip(th6,y6)],
            lith=[1*ll for ll in lit6]
        )
    )

    source7 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x7)],
            ys=[ypts*m+yy for m, yy in zip(th7,y7)],
            lith=[1*ll for ll in lit7]
        )
    )

    source8 = ColumnDataSource(dict(
            xs=[xpts+xx for i, xx in enumerate(x8)],
            ys=[ypts*m+yy for m, yy in zip(th8,y8)],
            lith=[1*ll for ll in lit8]
        )
    )


    # parameters of the figure
    plot = figure(
        title="Lithologies", x_axis_label='', y_axis_label='depth (m)', x_range=(-1,1),
        plot_width=300, plot_height=800, y_range=p.y_range,
        h_symmetry=False, v_symmetry=False, tools="pan,ywheel_zoom,lasso_select,box_zoom,hover,reset",
        tooltips=[("Lithology", "@lith")])#min_border=0,

    #plot.xaxis.visible = False

    glyph = Patches(xs="xs", ys="ys", fill_color="#F4D03F", line_color='blue', line_alpha=0)
    glyph2 = Patches(xs="xs", ys="ys", fill_color="#6E2C00", line_color='blue', line_alpha=0)
    glyph3 = Patches(xs="xs", ys="ys", fill_color="#DC7633", line_color='blue', line_alpha=0)
    glyph4 = Patches(xs="xs", ys="ys", fill_color="#F5B041", line_color='blue', line_alpha=0)
    glyph5 = Patches(xs="xs", ys="ys", fill_color="#AED6F1", line_color='blue', line_alpha=0)
    glyph6 = Patches(xs="xs", ys="ys", fill_color="#1B4F72", line_color='blue', line_alpha=0)
    glyph7 = Patches(xs="xs", ys="ys", fill_color="#196F3D", line_color='blue', line_alpha=0)
    glyph8 = Patches(xs="xs", ys="ys", fill_color="#A569BD", line_color='blue', line_alpha=0)
    #glyph9 = Patches(xs="xs", ys="ys", fill_color="#C41286", line_color='blue', line_alpha=0)
    plot.add_glyph(source3, glyph3)
    plot.add_glyph(source1, glyph)
    plot.add_glyph(source2, glyph2)
    plot.add_glyph(source4, glyph4)
    plot.add_glyph(source5, glyph5)
    plot.add_glyph(source6, glyph6)
    plot.add_glyph(source7, glyph7)
    plot.add_glyph(source8, glyph8)
    #plot.add_glyph(source9, glyph9)

    sss = gridplot([[p,p2,p3,plot]], sizing_mode="scale_width")

    return file_html(sss, CDN, "my plot")

import time
import numpy as np

# Visualization
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib

# Save Image
import platform
import os
from PIL import Image

matplotlib.use('Agg')


def parse_file(file, separator):
    usualDtypes = {
        'Timestamp': 'int64',
        'TID': 'int64',
        'PID': 'int64',
        'CMDLINE': 'object',
        'State': 'object',
        'CPU': 'int64',
        'Node': 'int64',
        'PrefNode': 'int64',
        'InPrefNode': 'int64',
        'Perf': 'object',
        'CPU%': 'int64',
        'RelPerf': 'float64',
        'Ops': 'int64',
        'OpIntensity': 'float64',
        'AvLat': 'int64',
    }
    distinto = False
    column = None
    try:
        file = pd.read_csv(file, sep=separator, dtype=usualDtypes)
    except ValueError:
        distinto = True
        file = pd.read_csv(file, sep=separator)
        for i in file.columns:
            if i in usualDtypes:
                if usualDtypes[i] != file.dtypes[file.columns.get_loc(i)]:
                    distinto = True
                    column = i
                    # print("disitnto, columna:", i, "index:", file.columns.get_loc(i))
    if column == None:
        return file if not distinto else None
    else:
        return file if not distinto else column


def remove_outliers(data, quantile_min=0.25, quantile_max=0.75):
    min_value = np.quantile(data, quantile_min)
    max_value = np.quantile(data, quantile_max)

    return data[(min_value <= data) & (data <= max_value)]


def compute_zs(data, x_index, y_index, xs, ys):
    columns = list(data.columns)

    zs = np.full((len(columns), len(ys), len(xs)), None, dtype=object)

    print(zs.shape)

    for row in data.itertuples(index=False):
        i = np.where(ys == row[y_index])
        j = np.where(xs == row[x_index])
        for z_index in range(len(row[:])):
            zs[z_index, i, j] = row[z_index]

    return zs


def numeric_heatmap(xs, ys, zs, colors):
    z_values = zs.astype(float)
    z_values = z_values[np.isfinite(z_values)]

    zmin = np.min(z_values)
    zmax = np.max(z_values)

    av = np.mean(z_values)
    median = np.median(z_values)
    stdev = np.std(z_values)

    print(f"\tAv.: {av}, Median: {median}, Std: {stdev}")

    # If zs are of float type
    if (z_values != z_values.astype(int)).any():
        # Use percentiles for computing zmin and zmax
        zs_no_outliers = remove_outliers(z_values, 0.15, 0.85)

        zmin = np.min(zs_no_outliers)
        zmax = np.max(zs_no_outliers)

        av = np.mean(zs_no_outliers)
        median = np.median(zs_no_outliers)
        stdev = np.std(zs_no_outliers)

        print(f"\tWithout outliers: Av.: {av}, Median: {median}, Std: {stdev}")

    print(f"\tColor range: ({zmin}, {zmax})")

    if colors == 'default':
        colors = None

    return go.Heatmap(z=zs, x=xs, y=ys, zmin=zmin, zmax=zmax, colorscale=colors)


def qualitative_heatmap(xs, ys, zs, zType) -> go.Heatmap:
    z_values = zs.copy()
    z_values = z_values.astype(zType).flatten()
    legend_entries = np.unique(z_values)
    value_to_int = {j: i for i, j in enumerate(legend_entries)}
    z_values = zs.copy()

    color_scheme = px.colors.qualitative.Plotly
    colors = []

    for string, val in value_to_int.items():
        # print(f"Value: {val}. String: {string}")
        z_values[z_values == string] = val
        colors.append([float(val) / len(legend_entries),
                      color_scheme[val % len(color_scheme)]])
        colors.append([float(val + 1) / len(legend_entries),
                      color_scheme[val % len(color_scheme)]])

    color_bar = dict(
        tickmode="array",
        tickvals=[i for i in range(len(legend_entries))],
        ticktext=legend_entries
    )

    '''if zType == bool:
        color_bar = dict(
            titleside="top",
            tickmode="array",
            tickvals=[0, 1],
            ticktext=["False", "True"],
            ticks="outside"
        )'''

    if not colors:
        colors = None

    return go.Heatmap(z=z_values, x=xs, y=ys, hovertemplate='x:%{x:d}<br>y:%{y:d}<br>z:%{text}', text=zs,
                      colorbar=color_bar, colorscale=colors)


def initial_chart(data):
    x_index = 0  # Timestamp
    y_index = 1  # TID or Address

    xs = np.unique(np.array(data.iloc[:, x_index]))
    ys = np.unique(np.array(data.iloc[:, y_index]))

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    fig = go.Figure()

    zs = compute_zs(data, x_index, y_index, xs, ys)

    xs = xs.astype(str)
    ys = ys.astype(str)

    for z_index, z_name in enumerate(columns):
        if z_name == "CPU%":
            print(f"Column {z_name}: ")
            try:
                hm = numeric_heatmap(xs, ys, zs[z_index], None)
                fig.add_trace(hm)
            except:
                print(f"\tNot numeric. Treating as qualitative.")
                hm = qualitative_heatmap(xs, ys, zs[z_index], str)
                fig.add_trace(hm)

    fig.write_image(
        file="assets/saida.png",
        format='png',
        width=1024.0,
        height=600.0
    )


def interactive_chart(data):
    x_index = 0  # Timestamp
    y_index = 1  # TID or Address

    xs = np.unique(np.array(data.iloc[:, x_index]))
    ys = np.unique(np.array(data.iloc[:, y_index]))

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    print(f"Preparing plots for: {columns}")

    fig = go.Figure()

    buttons = []

    start = time.time()

    zs = compute_zs(data, x_index, y_index, xs, ys)

    xs = xs.astype(str)
    ys = ys.astype(str)

    end = time.time()

    print(f"Zs computed in {end - start} seconds")

    for z_index, z_name in enumerate(columns):
        print(f"Column {z_name}: ")
        try:
            hm = numeric_heatmap(xs, ys, zs[z_index], None)
            fig.add_trace(hm)
        except:
            print(f"\tNot numeric. Treating as qualitative.")
            hm = qualitative_heatmap(xs, ys, zs[z_index], str)
            fig.add_trace(hm)

        visible = np.full(len(columns), False)
        visible[z_index] = True

        buttons.append(
            dict(
                method='update',
                label=z_name,
                args=[{'visible': visible}, {'title': z_name}]
            )
        )

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                buttons=buttons,
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.11,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name)
    )

    fig.show()


def interactive_chart_plot(index: tuple, plotName: str, data, save: dict, infoData: dict, colors: str):
    x_index, y_index, zName, zMin, zMax, zType, delOut = index

    dataType = [int, float, bool, str]

    data = data[data.TID.isin(getListOfTids(infoData))]
    if delOut:
        data = data[(data[zName] >= zMin) & (data[zName] <= zMax)]

    xs = np.unique(np.array(data.iloc[:, x_index]))
    ys = np.unique(np.array(data.iloc[:, y_index]))

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    print(f"Preparing plots for: {zName}")

    fig = go.Figure()

    buttons = []

    start = time.time()

    zs = compute_zs(data, x_index, y_index, xs, ys)
    z_index = columns.index(zName)

    xs = xs.astype(str)
    ys = ys.astype(str)

    end = time.time()

    print(f"Zs computed in {end - start} seconds")

    if colors == 'default':
        colors = None

    print(f"Column {zName}: ")

    if zType == 0:
        try:
            hm = qualitative_heatmap(xs, ys, zs[z_index], int)
            fig.add_trace(hm)
        except:
            return None

    elif zType == 1:
        try:
            hm = numeric_heatmap(
                xs, ys, zs[z_index], colors)
            fig.add_trace(hm)
        except:
            return None

    elif zType == 2 or zType == 3:
        try:
            hm = qualitative_heatmap(xs, ys, zs[z_index], dataType[zType])
            fig.add_trace(hm)
        except:
            return None

    visible = np.full(len(columns), False)
    visible[z_index] = True

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                buttons=buttons,
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.11,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name),
        title=plotName
    )

    if not save:
        fig.show()
    else:
        '''
        mySO = platform.system()
        if save['dir'] == '/':

            if mySO == 'Windows':
                save['dir'] = "C:" + \
                    os.path.join(os.environ["HOMEPATH"], "Desktop")
            elif mySO == 'Linux':
                save['dir'] = os.path.join(os.path.join(
                    os.path.expanduser('~')), 'Desktop')
            elif mySO == 'Darwin':
                save['dir'] = os.path.expanduser("~/Desktop")
            else:
                ""
        route = "" + save['dir'] + "/" + save['name'] + "." + save['format']
        route = route.replace(" ", "")
        print(route, save["format"], save['w'], save["h"])
        print(type(route), type(save["format"]),
              type(save['w']), type(save["h"]))
        '''
        save_image(fig, save)

    return True


def interactive_time_scatter(index: tuple, plotName: str, data, save: dict, infoData: dict):
    y_index, zName, zMin, zMax, delOut, varGraphs = index

    columns = list(data.columns)
    x_index = columns.index('Timestamp')

    x_name = columns[x_index]
    y_name = columns[y_index]

    fig = go.Figure()

    data = data[data.TID.isin(getListOfTids(infoData))]
    if delOut:
        data = data[(data[zName] >= zMin) & (data[zName] <= zMax)]
    data = data.sort_values(by=y_name)

    # Aqui é donde temos que facer o que nos manda oscar
    aux = []
    for pid in infoData:
        pid = int(pid)
        aux.append(pid)

    # print(auxData, type(auxData.PID))
    # figAux = px.line(auxData, x=x_name, y=y_name, color=zName, markers=False, color_discrete_sequence=colors)
    if varGraphs:
        zName = 'PID'
        y_name = 'TID'
    else:
        ''

    # print(x_name, y_name)
    # data.sort_values(by=y_name)
    auxData = data[data.PID.isin(aux)]
    auxData = auxData[[x_name, y_name, zName]]

    z_values = data[y_name].astype(float)
    z_values = z_values[np.isfinite(z_values)]

    zmin = np.min(z_values)
    zmax = np.max(z_values)
    if y_name == 'CPU':
        for i in range(int(zmin), int(zmax)):
            aux = pd.DataFrame({x_name: [0], y_name: i, zName: [0]})
            auxData = pd.concat([auxData, aux])

    auxData = auxData.sort_values(by=[y_name, x_name])

    try:

        fig = px.line(auxData, x=x_name, y=y_name, color=zName)
        fig.update_yaxes(range=[int(zmin), int(zmax)], autorange=False)

        z_values = data[x_name].astype(float)
        z_values = z_values[np.isfinite(z_values)]
        zmax = np.max(z_values)

        fig.update_xaxes(range=[100, int(zmax)], autorange=False)

    except:
        return None

    # px.colors.qualitative
    '''fig.add_trace(go.Scatter(
        x=df["Date"], y=df["Close"], name="Close", mode="lines"))
    fig.add_trace(go.Scatter(
        x=df["Date"], y=df["Open"], name="Open", mode="lines"))
    fig.update_layout(
        title="ICICI BANK stock prices", xaxis_title="Date", yaxis_title="Close"
    )
    fig.show()'''
    # fig.add_trace(figAux)

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name),
        title=plotName
    )

    if not save:
        # fig.for_each_trace(lambda trace: trace.update(visible="legendonly") if trace.name == '0' else ())
        fig.show()
    else:
        save_image(fig=fig, info=save)

    return True


def interactive_scatter(index: tuple, plotName: str, data, save: dict, lines: bool, infoData: dict, colors: str):
    x_index, y_index, zName, zMin, zMax, delOut = index

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    fig = go.Figure()

    # Esto é se o queremos facer por PIDs>
    # Pids = list(infoData.keys())
    # Pids = list(map(int, Pids))
    # data = data[data.PID.isin(Pids)]

    data = data[data.TID.isin(getListOfTids(infoData))]
    if delOut:
        data = data[(data[zName] >= zMin) & (data[zName] <= zMax)]
    data = data.sort_values(by=y_name)

    if colors == 'default':
        colors = None

    try:
        if lines:
            data = data.sort_values(by=x_name)
            try:
                fig = px.line(data, x=x_name, y=y_name, color=zName,
                              markers=False, color_continuous_scale=colors)
            except:
                fig = px.line(data, x=x_name, y=y_name, color=zName,
                              markers=False, color_discrete_sequence=colors)
        else:
            fig = px.scatter(data, x=x_name, y=y_name, color=zName,
                             color_continuous_scale=colors)
    except:
        return None

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name),
        title=plotName
    )

    if not save:
        fig.show()
    else:
        save_image(fig, save)

    return True


def getColorsContinuos():
    aux = px.colors.sequential.__all__
    aux.append('default')
    aux.sort()
    return aux


def getColorsLines():
    aux = px.colors.qualitative.__all__
    aux.append('default')
    aux.sort()
    return aux


def getColors():
    aux = px.colors.named_colorscales()
    aux.append('default')
    aux.sort()
    return aux


def getListOfTids(infoData: dict):
    '''
    Función que devolve unha lista de todos os TIDs que se atopan dentro do dicionario de entrada
    '''
    aux = []
    for listAux in infoData:
        aux.extend(infoData[listAux])
    return list(map(int, aux))


def roofline_model(data):
    ''
    x = [1, 4, None, 2, 3, None, 3, 4]
    y = [0, 0, None, 1, 1, None, 2, 2]
    # fig = px.scatter(data, x="gdpPercap", y="lifeExp",hover_name="country", log_x=True, log_y=False)
    # fig.add_trace(go.Scatter(x=x, y=y))
    # fig.show()


def calcularOutliers(data: pd.DataFrame, zName: str, values: dict):
    if not values:
        return (np.NaN, np.NaN)
    # print(data.dtypes[zName], type(data.dtypes[zName]))

    data = data[data.TID.isin(getListOfTids(values))]
    z_values = data[zName].astype(float)
    z_values = z_values[np.isfinite(z_values)]

    zmin = np.min(z_values)
    zmax = np.max(z_values)

    # Outliers valores máximos e mínimos da columna Z
    return (zmin, zmax)

    av = np.mean(z_values)
    median = np.median(z_values)
    stdev = np.std(z_values)

    print(f"\tAv.: {av}, Median: {median}, Std: {stdev}")
    first = av - 2 * stdev
    second = av + 2 * stdev
    return (first, second)
    # If zs are of float type
    if (z_values != z_values.astype(int)).any():
        # Use percentiles for computing zmin and zmax
        zs_no_outliers = remove_outliers(z_values, 0.15, 0.85)

        zmin = np.min(zs_no_outliers)
        zmax = np.max(zs_no_outliers)

        av = np.mean(zs_no_outliers)
        median = np.median(zs_no_outliers)
        stdev = np.std(zs_no_outliers)

        print(f"\tWithout outliers: Av.: {av}, Median: {median}, Std: {stdev}")


# Pensar de facelo doutro xeito, xa que gardalo de este tam e despois facer un resize quizáis non
# é a mellor idea, ainda que se a imaxe é moi pequena facéndoo directamente con write_image
# pérdese moita información, e ao facer o resize pérdese moita definición


def save_image(fig: go.Figure, info: dict):

    name = info['name'] + "." + info['format']
    name = name.replace(' ', '').replace(':', '_')
    name = info['dir'] + '/' + name
    fig.write_image(
        file=name,
        format=info['format'],
        width=float(info['wc']),
        height=float(info['hc'])
    )
    if info['wc'] != info['w'] or info['hc'] != info['h']:
        img = Image.open(name)
        aux = resize_with_pad(img, info['w'], info['h'])
        aux.save(name, format=info['format'])


def resize_with_pad(im, target_width, target_height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
    target_ratio = target_height / target_width
    im_ratio = im.height / im.width
    if target_ratio > im_ratio:
        # It must be fixed by width
        resize_width = target_width
        resize_height = round(resize_width * im_ratio)
    else:
        # Fixed by height
        resize_height = target_height
        resize_width = round(resize_height / im_ratio)

    image_resize = im.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new(
        'RGBA', (target_width, target_height), (255, 255, 255, 255))
    offset = (round((target_width - resize_width) / 2),
              round((target_height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')


if __name__ == '__main__':

    data = parse_file('thread_info_1.csv')
    # interactive_app_scatter_data(data)

    '''
    files = sys.argv[1:]

    print(f"Reading files: {files}")

    for file in files:
        print(f"Reading file: {file}")
        data = parse_file(file)
        interactive_chart(data)
    '''

'''
**************************************************************+

Mirar os seguintes links:
    - https://plotly.com/python/discrete-color/
    - https://plotly.com/python/line-and-scatter/
    - https://plotly.com/python/3d-scatter-plots/
    - https://plotly.com/python/plotly-express/

'''

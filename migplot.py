import sys
import time
import numpy as np

# Visualization
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Save Image
import platform
import os


def parse_file(file):
    return pd.read_csv(file, sep=';')


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


def numeric_heatmap(xs, ys, zs):
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

    return go.Heatmap(z=zs, x=xs, y=ys, zmin=zmin, zmax=zmax)


def qualitative_heatmap(xs, ys, zs):
    z_values = zs.copy()
    z_values = z_values.astype(str).flatten()
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
                hm = numeric_heatmap(xs, ys, zs[z_index])
                fig.add_trace(hm)
            except:
                print(f"\tNot numeric. Treating as qualitative.")
                hm = qualitative_heatmap(xs, ys, zs[z_index])
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
            hm = numeric_heatmap(xs, ys, zs[z_index])
            fig.add_trace(hm)
        except:
            print(f"\tNot numeric. Treating as qualitative.")
            hm = qualitative_heatmap(xs, ys, zs[z_index])
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


def interactive_chart_plot(x_index: int, y_index: int, zName: str, plotName: str, data, save: dict):
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
        if z_name == zName:
            print(f"Column {z_name}: ")
            try:
                hm = numeric_heatmap(xs, ys, zs[z_index])
                fig.add_trace(hm)
            except:
                print(f"\tNot numeric. Treating as qualitative.")
                hm = qualitative_heatmap(xs, ys, zs[z_index])
                fig.add_trace(hm)

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
        name = save['name'] + "." + save['format']
        name = name.replace(' ', '').replace(':', '_')
        fig.write_image(
            file=name,
            format=save['format'],
            width=float(save['w']),
            height=float(save['h'])
        )


def numeric_scatter(xs, ys, zs):
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

    return px.scatter(z=zs, x=xs, y=ys, zmin=zmin, zmax=zmax)


def qualitative_scatter(xs, ys, zs, data):
    return px.scatter(data_frame=data, x=xs, y=ys, text=zs)


def try_interactive_scatter(index: tuple, plotName: str, data, save: dict, lines: bool):
    x_index, y_index, zName = index

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    fig = go.Figure()

    data = data.query("PID == 1566542")
    #fig = px.line(data, x=x_name, y=y_name, color=zName, markers=False)
    fig = px.strip(data, x=x_name, y=y_name, color=zName)

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name),
        title=plotName
    )

    if not save:
        fig.show()


def interactive_scatter(x_index: int, y_index: int, zName: str, plotName: str, data, save: dict):
    # xs = np.unique(np.array(data.iloc[:, x_index]))
    # ys = np.unique(np.array(data.iloc[:, y_index]))

    columns = list(data.columns)

    x_name = columns[x_index]
    y_name = columns[y_index]

    print(f"Preparing plots for: {columns}")

    fig = go.Figure()

    data = data.query("PID == 1566542")
    fig = px.line(data, x=x_name, y=y_name, color=zName, markers=True)

    fig.update_layout(
        yaxis_type='category',
        xaxis=dict(title=x_name),
        yaxis=dict(title=y_name),
        title=plotName
    )

    if not save:
        fig.show()


if __name__ == '__main__':
    files = sys.argv[1:]

    print(f"Reading files: {files}")

    for file in files:
        print(f"Reading file: {file}")
        data = parse_file(file)
        interactive_chart(data)


'''
**************************************************************+

Mirar os seguintes links:
    - https://plotly.com/python/discrete-color/
    - https://plotly.com/python/line-and-scatter/
    - https://plotly.com/python/3d-scatter-plots/
    - https://plotly.com/python/plotly-express/

'''

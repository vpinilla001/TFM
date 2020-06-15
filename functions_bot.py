import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pathlib


def plot_serie(senal, start, end, name, mark):
    sns.set(rc={'figure.figsize': (13, 10)})
    data = pd.read_csv('datasets/cic.csv', index_col = 0)
    marker = {'si': '.', 'no': ''}
    dir_path = str(pathlib.Path().absolute()).replace('\\', '/')

    query = data.loc[start  : end ][senal]
    fig = plt.figure()
    ax = query.plot(color = 'blue', linewidth=1, linestyle='-', fontsize=20, marker = marker[mark])
    ax.set_ylabel('Valor', size=16)
    ax.set_xlabel('Fecha', size=16)
    ax.set_title(senal, size=20)
    plt.gcf().autofmt_xdate()
    path = dir_path + '/img/' + name + '.png'
    plt.savefig(path, dpi=fig.dpi)

def plot_serie2(senal, name, mark):
    sns.set(rc={'figure.figsize': (13, 10)})
    data = pd.read_csv('datasets/cic.csv', index_col = 0)
    marker = {'si': '.', 'no': ''}
    dir_path = str(pathlib.Path().absolute()).replace('\\', '/')

    query = data[senal]
    fig = plt.figure()
    ax = query.plot(color = 'blue', linewidth=1, linestyle='-', fontsize=20, marker = marker[mark])
    ax.set_ylabel('Valor', size=16)
    ax.set_xlabel('Fecha', size=16)
    ax.set_title(senal, size=20)
    plt.gcf().autofmt_xdate()
    path = dir_path + '/img/' + name + '.png'
    plt.savefig(path, dpi=fig.dpi)


def plot_hist(senal, start, end, name, color):
    sns.set(rc={'figure.figsize': (18, 10)})
    data = pd.read_csv('datasets/cic.csv', index_col = 0)
    colores = {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}
    dir_path = str(pathlib.Path().absolute()).replace('\\', '/')

    query = data.loc[start  : end ][senal]
    fig = plt.figure()
    ax = query.hist(bins = 30, color = colores[color], xlabelsize = 20, ylabelsize = 20)
    ax.set_ylabel('Frecuencia', size=16)
    ax.set_xlabel('Valor', size=16)
    ax.set_title(senal, size=20)
    path = dir_path + '/img/' + name + '.png'
    plt.savefig(path, dpi=fig.dpi)

def plot_hist2(senal, name, color):
    sns.set(rc={'figure.figsize': (18, 10)})
    data = pd.read_csv('datasets/cic.csv', index_col = 0)
    colores = {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}
    dir_path = str(pathlib.Path().absolute()).replace('\\', '/')

    query = data[senal]
    fig = plt.figure()
    ax = query.hist(bins = 30, color = colores[color], xlabelsize = 20, ylabelsize = 20)
    ax.set_ylabel('Frecuencia', size=16)
    ax.set_xlabel('Valor', size=16)
    ax.set_title(senal, size=20)
    path = dir_path + '/img/' + name + '.png'
    plt.savefig(path, dpi=fig.dpi)


def describe_information(senal, start, end):
    data = pd.read_csv('datasets/cic.csv', index_col=0)
    query = data.loc[start  : end ][senal]
    return query.describe().apply('{0:.2f}'.format)

def describe_information2(senal):
    data = pd.read_csv('datasets/cic.csv', index_col=0)
    query = data[senal]
    return query.describe().apply('{0:.2f}'.format)
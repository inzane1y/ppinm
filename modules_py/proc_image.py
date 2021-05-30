# proc_image.py

import numpy as np
import matplotlib.pyplot as plt
import modules_py.proc_data as pd
import modules_py.functions_vec as fv
import os

from matplotlib.colors import ListedColormap

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

cmap_pi_pnn = ListedColormap(['#ffffff00', '#a1ae25']) # Green
cmap_pi_pnd = ListedColormap(['#ffffff00', '#ec4f43']) # Red
cmap_pi_pnn_corr = ListedColormap(['#ffffff00', '#0960BD']) # Blue
cmap_pi_pnd_corr = ListedColormap(['#ffffff00', '#F6C90E']) # Yellow

color_red = '#F62A66'
color_red_light = '#F29696'
color_black = '#363636'
color_black_light = '#999999'
color_green = '#7DC383'
color_blue = '#148ACC'

def show(filename=None, png=False):
    plt.grid()
    plt.legend()
    plt.savefig(filename + '.pdf', dpi=300, format='PDF') \
        if filename is not None else plt.show()
    if png:
        plt.savefig(filename + '.png', dpi=300, format='PNG')
    plt.clf()

def plot(file_dir, label=None, ls=None, color=color_black):
    flag_label_present = False
    filenames = os.listdir(file_dir)
    for filename in filenames:
        x, Y = pd.gen_data(file_dir + '/' + filename)
        for y in Y:
            if flag_label_present:
                plt.plot(x, y, ls=ls, color=color)
            else:
                plt.plot(x, y, ls=ls, color=color, label=label)
                flag_label_present = True

def plot_2(file_dir, pf, condition_function, label_r=None,
    label_i=None, color_r=color_black, color_i=color_red):
    r_filenames = os.listdir(file_dir + '/' + pf)
    i_filenames = os.listdir(file_dir + '_i/' + pf)

    flag_label_present = False
    for r_filename in r_filenames:
        k, W = pd.gen_data(file_dir + '/' + pf + '/' + r_filename)
        for w in W:
            condition = np.abs(condition_function(k, w, float(pf)).imag) < 1e-5
            not_condition = np.invert(condition)
            if not flag_label_present:
                plt.plot(k[condition], w[condition] ** 2, label=label_r, color=color_r)
                plt.plot(k[not_condition], w[not_condition] ** 2, color=color_r, ls='dashed')
                flag_label_present = True
            else:
                plt.plot(k[condition], w[condition] ** 2 , color=color_r)
                plt.plot(k[not_condition], w[not_condition] ** 2 , color=color_r, ls='dashed')

    flag_label_present = False
    for i_filename in i_filenames:
        k, W = pd.gen_data(file_dir + '_i/' + pf + '/' + i_filename)
        for w in W:
            if not flag_label_present:
                plt.plot(k, -w * w, label=label_i, color=color_i)
                flag_label_present = True
            else:
                plt.plot(k, w ** 2, color=color_i)

def plot_2_as(file_dir, pf, label_r=None,
    label_i=None, color_r=color_black_light, color_i=color_red_light, ls='dotted'):
    r_filenames = os.listdir(file_dir + '/' + pf)
    i_filenames = os.listdir(file_dir + '_i/' + pf)

    flag_label_present = False
    for r_filename in r_filenames:
        k, W = pd.gen_data(file_dir + '/' + pf + '/' + r_filename)
        for w in W:
            if not flag_label_present:
                plt.plot(k, w ** 2, label=label_r, color=color_r, ls=ls)
                flag_label_present = True
            else:
                plt.plot(k, w ** 2, color=color_r, ls=ls)

    flag_label_present = False
    for i_filename in i_filenames:
        k, W = pd.gen_data(file_dir + '_i/' + pf + '/' + i_filename)
        for w in W:
            if not flag_label_present:
                plt.plot(k, -w ** 2, label=label_i, color=color_i, ls=ls)
                flag_label_present = True
            else:
                plt.plot(k, -w ** 2, color=color_i, ls=ls)

def contourf_imag(X, Y, func, *args, alpha=.2, cmap=cmap_pi_pnn, **kwargs):
    plt.contourf(X, Y * Y, np.abs(func(X, Y, *args, **kwargs).imag) > 1e-5,
        cmap=cmap, alpha=alpha)

def gen_title(func_name, pf):
    title = r'$\Re \left( \omega^2 - k^2 - 1'
    if 'pnn' in func_name:
        title += r'- \Pi_{\pi N N}'
        if 'corr' in func_name:
            title += r'^{(corr)}'
        if 'pnn_as' in func_name:
            title += r'(as)'
    if 'pnd' in func_name:
        title += r'- \Pi_{\pi N \Delta}'
        if 'corr' in func_name:
            title += r'^{(corr)}'
        if 'pnd_as' in func_name:
            title += r'(as)'
    title += r' = 0 \right)'
    # if 'as' in func_name:
    #     title += r'^{(as)}'
    title += r'$, $n = ' + str("%.2f" % (4 * float(pf) ** 3 / (6 * np.pi ** 2 * .47))) + r'n_0$'
    plt.title(title)

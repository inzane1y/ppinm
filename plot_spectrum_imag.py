import modules_py.proc_image as pi
import modules_py.proc_data as pd
import matplotlib.pyplot as plt
import numpy as np
import os

color_red = '#F62A66'
color_black = '#363636'

pf = '2.700'
func_name = 'eq_pnd_real'
r_filenames = os.listdir('graph_data/' + func_name + '/' + pf)
i_filenames = os.listdir('graph_data/' + func_name + '_i/' + pf)

r_label_done = False
for r_filename in r_filenames:
    k, W = pd.gen_data('graph_data/' + func_name + '/' + pf + '/' + r_filename)
    for w in W:
        if not r_label_done:
            plt.plot(k, w ** 2, label=r'$\omega^2(k)$', color=color_black)
            r_label_done = True
        else:
            plt.plot(k, w ** 2, color=color_black)

for i_filename in i_filenames:
    k, W = pd.gen_data('graph_data/' + func_name + '_i/' + pf + '/' + i_filename)
    for w in W:
        plt.plot(k, -w ** 2, color=color_red)

pi.show('figures/' + func_name + '_r_i_' + pf)

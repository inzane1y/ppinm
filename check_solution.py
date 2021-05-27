import modules_py.functions_vec as fv
import modules_py.proc_image as pi
import modules_py.proc_data as pd

import os
import matplotlib.pyplot as plt

pf = 2.7
dir_name = 'graph_data/eq_pnn_as/' + str(pf)
filenames = os.listdir(dir_name)

for filename in filenames:
    k, W = pd.gen_data(dir_name + '/' + filename)
    for w in W:
        plt.plot(k, fv.eq_pnn_as(k, w, pf))

plt.ylim(-.5, .5)
pi.show()

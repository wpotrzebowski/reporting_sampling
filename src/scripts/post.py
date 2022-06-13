import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from corner import corner
from bumps import dream

import paths
import utils
plt.style.use(paths.scripts / './matplotlibrc')

def latex_num(num):
    return f'{num:.3f}'

def latex_si(num, err, unit):
    return r'\SI{' + f'{num:.3f}' + r' \pm ' + f'{err:.3f}' + r'}{' + f'{unit}' + r'}'


state = dream.state.load_state(str(paths.data / './Practical6_Ni_simple'))

label_offset = [0, 1]
figsize = utils.set_size(246)
size_adapt = 1
label_offset[1] += label_offset[1] * 0.1 * size_adapt
figsize = (figsize[0], figsize[0] * size_adapt)
fig = plt.figure(figsize=figsize)

axes = []

p_chain = state.chains()[1].reshape(-1, 8)[:, -3:]

figure = corner(p_chain, fig=fig, 
                labels=[r'$\rho_{\mathrm{mag}}$/$10^{-6}$Å$^{-2}$', 
                        r'$\rho$/kgm$^{-3}$', 
                        '$d$/Å'],
                max_n_ticks=3)
axes = np.array(figure.axes).reshape((3, 3))

f_names = ['mag_sld', 'density', 'thick']
labels = [r'$\rho_{\mathrm{mag}}', r'$\rho_m', '$d'] 
units = [r'10^{-6}\angstrom^{-2}', r'\kilogram\meter^{-3}', r'\angstrom']
for ii, i in enumerate(p_chain.T):
    f_open = open(paths.tex / f'./output/{f_names[ii]}.txt', 'w')
    f_open.write(labels[ii] + r'=' + f'{latex_si(i.mean(), i.std(ddof=0), units[ii])}' + '$')
    f_open.close()

plt.savefig(paths.figures / "post.pdf", bbox_inches="tight")
plt.close()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from scipy.stats import norm

import paths
import utils
plt.style.use(paths.scripts / './matplotlibrc')

label_offset = [0, 1]
figsize = utils.set_size(246)
size_adapt = 0.5
label_offset[1] += label_offset[1] * 0.1 * size_adapt
figsize = (figsize[0], figsize[0] * size_adapt)
fig = plt.figure(figsize=figsize)
g = gs.GridSpec(1, 1, figure=fig)

axes = []

axes.append(fig.add_subplot(g[0, 0]))
u = norm(2.9, 0.1)
x = np.linspace(2.5, 3.3, 5000)
axes[-1].plot(x, u.pdf(x), c=utils.colors[0], label='Normal distribution')
axes[-1].set_xlabel(r'$\rho_m$/gcm$^{-3}$')
axes[-1].set_ylabel(r'$p(\rho_m)$/g$^{-1}$cm$^{3}$')
axes[-1].set_ylim(0, None)

plt.tight_layout()
plt.savefig(paths.figures / "prior.pdf", bbox_inches="tight")
plt.close()
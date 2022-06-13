import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from scipy.stats import norm, gaussian_kde

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
u = np.zeros((9000))
u[:3000] = norm(966.4, 5.4).rvs(3000)
u[3000:6000] = norm(829.0, 4.0).rvs(3000)
u[6000:] = norm(924.7, 17.6).rvs(3000)
kde = gaussian_kde(u, bw_method=0.05)
kde_x = np.linspace(800, 1000, 5000)
axes[-1].plot(kde_x, kde.pdf(kde_x), color=utils.colors[0], label='Gaussian KDE')
axes[-1].hist(u, bins=50, color=utils.colors[1], alpha=0.5, label='Sampling result', density=True)
axes[-1].set_xlabel('$V_t$/Å$^{3}$')
axes[-1].set_ylabel('$p(V_t)$/Å$^{-3}$')
axes[-1].set_ylim(0, None)
axes[-1].get_xaxis().get_major_formatter().set_scientific(False)

plt.figlegend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2)

plt.tight_layout()
plt.savefig(paths.figures / "samples.pdf", bbox_inches="tight")
plt.close()
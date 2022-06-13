colors = ["#0173B2", 
          "#DE8F05", 
          "#029E73", 
          "#D55E00", 
          "#CC78BC", 
          "#CA9161", 
          "#FBAFE4", 
          "#949494", 
          "#ECE133", 
          "#56B4E9"]

# 510.0pt. \textwidth
# 246.0pt. \columnwidth

def set_size(width: float, fraction: float=1, subplots: tuple=(1, 1), square: bool=False) -> tuple:
    """Set figure dimensions to avoid scaling in LaTeX.

    :param width: Document width in points, or string of predined document type
    :param fraction: Fraction of the width which you wish the figure to occupy, optional
    :param subplots: The number of rows and columns of subplots, optional
    :param square: Return a square dimension set
    :return: Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 426.79135
    elif width == 'beamer':
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / (4) 

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    if square:
        return (fig_width_in, fig_width_in)
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)
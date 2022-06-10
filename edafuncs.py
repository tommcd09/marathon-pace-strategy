"""Provides various functions for exploratory data analysis."""

import matplotlib.pyplot as plt
import seaborn as sns


def marathon_plot(df, labels, col=None, hue=None):
    """Takes DataFrame, list of title and x-label, column to plot,
    and column for hue, returns KDE plot.
    """
    fig, ax = plt.subplots(sharey=True, figsize=(15, 10))
    sns.kdeplot(data=df, x=col, hue=hue, ax=ax)
    ax.set_xlabel(labels[1], fontdict={'fontsize': 'x-large'})
    ax.set_ylabel('Density', fontdict={'fontsize': 'x-large'})
    ax.set_title(labels[0], fontdict={'fontsize': 'xx-large'})
    return fig, ax


def marathon_plot_axvline(df, labels, col=None, hue=None):
    """Takes DataFrame, list of title and x-label, column to plot,
    and column for hue, returns KDE plot plus an axvline at x = 0.
    """
    fig, ax = marathon_plot(df, labels, col=col, hue=hue)
    plt.axvline(linestyle = '--', color = 'g')
    plt.annotate('Perfectly Even Pace', xy=(0, 0.01), xytext=(2, 0.01),
                 arrowprops={'facecolor':'black', 'width': 3},
                 backgroundcolor = 'white', fontsize='x-large')
    return fig, ax


def marathon_facetgrid(g, col, labels):
    """Takes FacetGrid object g, column to plot, and list of title, subtitles and x-label,
    returns 2 KDE plots in a FacetGrid.
    """
    g.map(sns.kdeplot, col)
    g.fig.suptitle(labels[0], fontsize='xx-large', y=1)
    g.axes[0,0].set_title(labels[1], fontdict={'fontsize': 'xx-large'})
    g.axes[0,1].set_title(labels[2], fontdict={'fontsize': 'xx-large'})
    g.axes[0,0].set_xlabel(labels[3], fontdict={'fontsize': 'xx-large'})
    g.axes[0,1].set_xlabel(labels[3], fontdict={'fontsize': 'xx-large'})
    g.axes[0,0].set_ylabel('Density', fontdict={'fontsize': 'xx-large'})
    g.add_legend()
    plt.setp(g._legend.get_title(), fontsize='xx-large')
    plt.setp(g._legend.get_texts(), fontsize='xx-large')
    return g


def marathon_facetgrid_axvline(g, col, labels):
    """Takes FacetGrid object g, column to plot, and list of title, subtitles and x-label,
    returns 2 KDE plots in a FacetGrid plus axvlines at x = 0.
    """
    g = marathon_facetgrid(g, col, labels)
    g.axes[0,0].axvline(linestyle = '--', color = 'g')
    g.axes[0,1].axvline(linestyle = '--', color = 'g')
    g.axes[0,0].annotate('Perfectly Even Pace', xy=(0, 0.01), xytext=(2, 0.01),
                         arrowprops={'facecolor':'black', 'width': 3},
                         backgroundcolor = 'white', fontsize='xx-large')
    g.axes[0,1].annotate('Perfectly Even Pace', xy=(0, 0.01), xytext=(2, 0.01),
                         arrowprops={'facecolor':'black', 'width': 3},
                         backgroundcolor = 'white', fontsize='xx-large')
    return g


def marathon_scatter(df, x, y, labels, hue=None):
    """Takes DataFrame, columns to plot in x, y and hue,
    and list of title, x-label and y-label, returns scatterplot.
    """
    g = sns.lmplot(data=df, x=x, y=y, hue=hue, height=10, ci=None,
                   scatter_kws={'alpha': 0.15})
    g.fig.suptitle(labels[0], fontsize='xx-large', y=1)
    g.ax.set_xlabel(labels[1], fontdict={'fontsize': 'x-large'})
    g.ax.set_ylabel(labels[2], fontdict={'fontsize': 'x-large'})
    g.ax.set_xlim([2, 5])
    g.ax.set_ylim([-11, 32])
    return g


def print_corr(groups, corrs):
    """Takes lists of group labels and correlations,
    prints text with group labels and correlations.
    """
    for group, corr in zip(groups, corrs):
        print(f'Correlation of finish time and split difference (with p-value) ({group}): {corr}')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:43:07 2018

@author: prubbens
"""

''' IMPORT PACKAGES 
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

sns.set_style("ticks")

''' CUSTUM CODE TO MAKE A JOINTPLOT USING SEABORN
ORGINAL SOURCE: https://gist.github.com/ruxi/ff0e9255d74a3c187667627214e1f5fa
'''
def jointplot_w_hue(data, x, y, hue=None, colormap = None, 
                    figsize = None, fig = None, scatter_kws=None, legend=True, title=None):
    #defaults
    if colormap is None:
        colormap = sns.color_palette() #['blue','orange']
    if figsize is None:
        figsize = (5,5)
    if fig is None:
        fig  = plt.figure(figsize = figsize)
    if scatter_kws is None:
        scatter_kws = dict(alpha=0.4, lw=1)
        
    # derived variables
    if hue is None:
        return "use normal sns.jointplot"
    hue_groups = data[hue].unique()

    subdata = dict()
    colors = dict()
    
    active_colormap = colormap[0:len(hue_groups)]

    legend_mapping = []
    for hue_grp, color in zip(hue_groups, active_colormap):
        legend_entry = mpatches.Patch(color=color, label=hue_grp)
        legend_mapping.append(legend_entry)
        
        subdata[hue_grp] = data[data[hue]==hue_grp]
        colors[hue_grp] = color
        
    # canvas setup
    grid = gridspec.GridSpec(2, 2,
                           width_ratios=[4, 1],
                           height_ratios=[1, 4],
                           hspace = 0, wspace = 0
                           )
    ax_main    = plt.subplot(grid[1,0])
    ax_xhist   = plt.subplot(grid[0,0], sharex=ax_main)
    ax_yhist   = plt.subplot(grid[1,1])#, sharey=ax_main)
    
    ## plotting
    ax_main.set_xlabel('t-SNE 1', size=18)
    ax_main.set_ylabel('t-SNE 2', size=18)
    plt.setp(ax_main.get_xticklabels(), visible=True, size=14)
    plt.setp(ax_main.get_yticklabels(), visible=True, size=14)
    ax_xhist.set_xlabel('t-SNE 1', size=18)
    ax_yhist.set_ylabel('t-SNE 2', size=18)

    # histplot x-axis
    for hue_grp in hue_groups:
        sns.distplot(subdata[hue_grp][x], color = colors[hue_grp]
                     , ax = ax_xhist, hist=False)

    # histplot y-axis
    for hue_grp in hue_groups:
        sns.distplot(subdata[hue_grp][y], color = colors[hue_grp]
                     , ax = ax_yhist, vertical=True, hist=False) 

    # main scatterplot 
    # note: must be after the histplots else ax_yhist messes up
    for hue_grp in hue_groups:
        sns.regplot(data = subdata[hue_grp], fit_reg=False,
                    x = x, y = y, ax = ax_main, color = colors[hue_grp]
                    , scatter_kws=scatter_kws
                   )
        
    # despine
    for myax in [ax_yhist, ax_xhist]:
        sns.despine(ax = myax, bottom=False, top=True, left = False, right = True
                    , trim = False)
        plt.setp(myax.get_xticklabels(), visible=False)
        plt.setp(myax.get_yticklabels(), visible=False)
    
    
    # topright 
    if legend==True: 
        ax_legend = plt.subplot(grid[0,1])#, sharey=ax_main)
        plt.setp(ax_legend.get_xticklabels(), visible=False)
        plt.setp(ax_legend.get_yticklabels(), visible=False)
        ax_legend.legend(handles=legend_mapping)
    
    plt.savefig('TSNE_FCM_kde_new_gp_legend_'+title+'.png',bbox_inches='tight', dpi=500)
    #plt.show()
    plt.close()
    return dict(fig = fig, gridspec = grid)

''' READ IN RESULT OF PHENOGRAPH
DEPENDS ON k
'''
spectrum = pd.read_csv('Clustering_PhenoGraph_k/hsNorm_RamanSpectra_cluster_k=30.csv', index_col=0, header=0)
df = pd.read_csv('TSNE_all.csv', index_col=0)
df.sort_values('ID', inplace=True)


''' CREATE INDEX IN FUNCTION OF TREATMENT 
'''
bool_lag = df.loc[:,'ID'].str.startswith('lag ')
bool_log = df.loc[:,'ID'].str.startswith('log ')
bool_stat = df.loc[:,'ID'].str.startswith('stat ')

idx_lag = df.loc[bool_lag.values].index
idx_log = df.loc[bool_log.values].index
idx_stat = df.loc[bool_stat.values].index


''' VISUALIZE JOINTPLOT
'''
pal_lag = ("#c4f381","#a3ec3b","#7dc713")
pal_log = ("#a2b1fa","#5975f6","#1039f2")
pal_stat = ("#faa2b1","#f65975","#f21039")
pal = ("#c4f381","#a3ec3b","#7dc713","#a2b1fa","#5975f6","#1039f2","#faa2b1","#f65975","#f21039")
g = jointplot_w_hue(x='t-SNE 1', y='t-SNE 2', data=df.loc[idx_lag,['t-SNE 1','t-SNE 2','ID']], hue='ID', colormap=pal_lag, figsize=(6,6), legend=True, title='lag')#, col='Growth phase', fit_reg=False, aspect=1.2, palette=pal)
g = jointplot_w_hue(x='t-SNE 1', y='t-SNE 2', data=df.loc[idx_log,['t-SNE 1','t-SNE 2','ID']], hue='ID', colormap=pal_log, figsize=(6,6), legend=True, title='log')#, col='Growth phase', fit_reg=False, aspect=1.2, palette=pal)
g = jointplot_w_hue(x='t-SNE 1', y='t-SNE 2', data=df.loc[idx_stat,['t-SNE 1','t-SNE 2','ID']], hue='ID', colormap=pal_stat, figsize=(6,6), legend=True, title='stat')#, col='Growth phase', fit_reg=False, aspect=1.2, palette=pal)
df.sort_values('ID', inplace=True)
g = jointplot_w_hue(x='t-SNE 1', y='t-SNE 2', data=df.loc[:,['t-SNE 1','t-SNE 2','ID']], hue='ID', colormap=pal, figsize=(6,6), legend=False, title='all')#, col='Growth phase', fit_reg=False, aspect=1.2, palette=pal)
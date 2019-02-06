#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:49:12 2018

@author: prubbens
"""
''' IMPORT PACKAGES
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style("ticks")

''' DEFINE TREATMENT GROUPS AND SET OPTIMAL k
'''
groups = ['eth','but','cu','cr','kan','amp']
k_s = [24,16,24,32,48,16]
i=0

for group in groups: 
    df = pd.read_csv('TSNE_results/TSNE_all_perp=30_'+group+'.csv', index_col=0)
    clustering = pd.read_csv('Clustering_PhenoGraph_k/Clustering_PhenoGraph_k'+str(k_s[i])+'_group'+group+'.csv', index_col=0,header=None)
    groups = df.group.str.contains(group)

    df_group = df.loc[groups.values]
    df_group.rename(columns={'group.1':'Treatment'}, inplace=True)
    bool_rep1 = df.loc[:,'group'].str.endswith('1')
    bool_rep2 = df.loc[:,'group'].str.endswith('2')
    bool_rep3 = df.loc[:,'group'].str.endswith('3')

    idx_rep1 = df_group.loc[bool_rep1.values].index
    idx_rep2 = df_group.loc[bool_rep2.values].index
    idx_rep3 = df_group.loc[bool_rep3.values].index

    df_group.loc[idx_rep1,'Replicate'] = str(1)
    df_group.loc[idx_rep2,'Replicate'] = str(2)
    df_group.loc[idx_rep3,'Replicate'] = str(3)

    df_group.loc[clustering.index,'Cluster'] = clustering.values

    #PLOT T-SNE
    fig, ax = plt.subplots() 
    pal = sns.color_palette('colorblind',len(np.unique(df_group.loc[:,'Treatment'].values)))
    g = sns.scatterplot(x='t-SNE 1', y='t-SNE 2', data=df_group, hue='Treatment', palette=pal, style='Replicate', legend='brief', alpha=0.5, ax=ax)
    sns.despine()
    ax.set_xlabel("t-SNE 1", fontsize=18)
    ax.set_ylabel("t-SNE 2", fontsize=18)    
    plt.setp(g.get_xticklabels(), size=14)
    plt.setp(g.get_yticklabels(), size=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('Figures/TSNE_ramanome_group'+group+'.png',bbox_inches='tight', dpi=500)
    plt.show()
    
    #PLOT PHENOGRAPH CLUSTERING
    fig, ax = plt.subplots() 
    pal = sns.color_palette('colorblind',len(np.unique(df_group.loc[:,'Cluster'].values)))
    g = sns.scatterplot(x='t-SNE 1', y='t-SNE 2', data=df_group, hue='Cluster', palette=pal, legend='brief', alpha=0.5, ax=ax)
    sns.despine(ax=ax)
    ax.set_xlabel("t-SNE 1", fontsize=18)
    ax.set_ylabel("t-SNE 2", fontsize=18)    
    plt.setp(g.get_xticklabels(), size=14)
    plt.setp(g.get_yticklabels(), size=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('Figures/TSNE_ramanome_Clustering_k'+str(k_s[i])+'_group'+group+'.png',bbox_inches='tight', dpi=500)
    plt.show()
    
    i+=1
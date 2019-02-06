#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:54:59 2018

@author: prubbens
"""
import numpy as np
import pandas as pd
import phenograph
from sklearn.manifold import TSNE
from sklearn.metrics import v_measure_score, adjusted_rand_score

possible_k = np.arange(2,102,2)

groups = ['eth','but','cu','cr','kan','amp']
for group in groups: 
    ari = np.zeros(len(possible_k))
    v = np.zeros(len(possible_k))
    n_clusters = np.zeros(len(possible_k))
    df = pd.read_csv('dataRamanone.csv')
    FEATURES = list(df.columns[4:])
    groups = df.loc[:,'group.1'].str.startswith(group)
    df_group = df.loc[groups.values]

    tsne = TSNE(n_components=2, perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, metric='euclidean', init='pca', random_state=27, method='exact', angle=0.5)

    df_tsne = tsne.fit_transform(df_group.loc[:,FEATURES])
    df_tsne = pd.DataFrame(df_tsne, columns=['t-SNE 1', 't-SNE 2'], index=df_group.index)
    df_final = pd.concat([df.iloc[df_group.index,0:4],df_tsne], ignore_index=False, axis=1)
    df_final.to_csv('TSNE_all_perp=30_'+str(group)+'.csv')
    
    i=0
    for k_ in possible_k: 
        communities, graph, Q = phenograph.cluster(df_group.loc[:,FEATURES], k=k_, primary_metric='Euclidean')
        ari[i] = adjusted_rand_score(df_group.loc[:,'group'],communities)
        v[i] = v_measure_score(df_group.loc[:,'group'],communities)
        n_clusters[i] = len(np.unique(communities))
        communities = pd.Series(communities, index=df_group.index)
        communities.to_csv('Clustering_PhenoGraph_k'+str(k_) + '_group_rep' + group + '.csv')
        print(ari[i],v[i])
        i+=1
    ari = pd.DataFrame({'ARI':ari, 'k': possible_k})
    v = pd.DataFrame({'V-measure':v, 'k': possible_k})
    n_clusters = pd.DataFrame({'Clusters': n_clusters, 'k':possible_k})

    ari.to_csv('ARI_' + group + '_rep.csv')
    v.to_csv('V_' + group + '_rep.csv')
    n_clusters.to_csv('N_clusters_' + group + '_rep.csv')

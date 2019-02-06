#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' IMPORT PACKAGES
'''
import pandas as pd
import phenograph
from sklearn.manifold import TSNE
from sklearn.metrics import v_measure_score, adjusted_rand_score
import seaborn as sns
import matplotlib.pyplot as plt

''' READ IN PROCESSED RAMAN DATA
'''
df = pd.read_csv('hsNorm_RamanSpectra.csv', index_col=0, header=0).iloc[:,:-1]
features = list(df.columns)

''' FIX PARAMETER k FOR PHENOGRAPH AND RUN
'''
k_ = 100
communities, graph, Q = phenograph.cluster(df.loc[:,features], k=k_, primary_metric='Euclidean')

''' CALCULATE PERFORMANCE USING ADJUSTED RAND INDEX (ARI)
'''
ari = adjusted_rand_score(df.index,communities)
v = v_measure_score(df.index,communities)

''' PERFORM T-SNE
'''
tsne = TSNE(n_components=2, perplexity=30.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, metric='euclidean', init='pca', random_state=27, method='barnes_hut', angle=0.5)
df_tsne = tsne.fit_transform(df.loc[:,features])
df_tsne = pd.DataFrame(df_tsne, columns=['t-SNE 1', 't-SNE 2'])
df_tsne['ID'] = df.index
df_tsne['Cluster'] = communities

''' VISUALIZE T-SNE ACCORDING TO TREATMENT
'''
df_tsne.sort_values('ID', inplace=True)
plt.figure() 
pal = ("#c4f381","#a3ec3b","#7dc713","#a2b1fa","#5975f6","#1039f2","#faa2b1","#f65975","#f21039")
g = sns.lmplot(x='t-SNE 1', y='t-SNE 2', data=df_tsne, hue='ID', fit_reg=False, aspect=1.2, palette=pal)
g.set_titles(size=18)
g.set_xlabels(fontsize=20)
g.set_ylabels(fontsize=20)
g.set_xticklabels(fontsize=14)
g.set_yticklabels(fontsize=14)
plt.savefig('Figures/TSNE_RAMAN.png',bbox_inches='tight', dpi=500)
plt.show()

''' VISUALIZE CLUSTERING RESULTS OF PHENOGRAPH IN T-SNE PLOT
'''
plt.figure() 
pal = sns.color_palette('husl',10)
g = sns.lmplot(x='t-SNE 1', y='t-SNE 2', data=df_tsne, hue='Cluster', fit_reg=False, aspect=1.2, palette=pal)
g.set_titles(size=18)
g.set_xlabels(fontsize=20)
g.set_ylabels(fontsize=20)
g.set_xticklabels(fontsize=12)
g.set_yticklabels(fontsize=12)
plt.savefig('Figures/TSNE_Pheno_k'+str(k_)+'.png',bbox_inches='tight', dpi=500)
plt.show()

print('ARI: ' + str(ari))
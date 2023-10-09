import sys
import readline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

import matplotlib
matplotlib.use('TkAgg')

style.use('ggplot') # ggplot-hs 없으면 ggplot으로 바꾸세요

coverage = pd.read_table('test.out',
                         names=['chrom', 'start', 'end', 'count', 'nzpos', 'length', 'nzratio'])


chrom_human_order = lambda x: 'chr{:03d}'.format(int(x[3:])) if x[3:].isdigit() else x

binsize = coverage['length'].value_counts().index[0]

covs = coverage[(coverage['length'] == binsize) & (coverage['chrom'].apply(len) <= 6)].copy()
covs['chrom_sortkey'] = covs['chrom'].apply(chrom_human_order)
covs = covs.sort_values(by=['chrom_sortkey', 'start']).reset_index(drop=True)
covs.head()


plt.figure(figsize=(9, 3))#

#for chrom, bins in (covs.groupby('chrom')):
##print(chrom,": ",bins)
#   tmp = bins['count'] + 1
#   print(tmp)
#   #np.log2(bins['count'] + 1,dtype=object)
#   #np.log2(bins['count'] + 1,dtype='category')
#   np.array(bins['count'] + 1)

#vp = plt.violinplot([np.log2(bins['count'] + 1) for chrom, bins in covs.groupby('chrom')], showextrema=False, showmedians=True, widths=0.8)
vp = plt.violinplot([np.log2(np.array(bins['count'] + 1)) for chrom, bins in covs.groupby('chrom')], showextrema=False, showmedians=True, widths=0.8)
plt.setp(vp['bodies'], facecolor='k', alpha=.65)
plt.setp(vp['cmedians'], lw=2)

## chromosome 번호로 X 틱 레이블을 단다.
#chromosomes = np.sort(covs['chrom'].unique())
chromosomes = ['1', '2' ,'3' ,'4' ,'5', '6', '7' ,'8', '9' ,'10' ,'11', '12' ,'13' ,'14' ,'15', '16' ,'17' ,'18' ,'19', '20' ,'21' ,'22' , 'X' ,'Y']
#plt.xticks(np.arange(1, len(chromosomes) + 1),[c[3:] for c in chromosomes])

plt.xlabel('chromosome')
plt.ylabel('log2 read count/bin')

#plt.xticks(np.arange(1, len(chromosomes) + 1),[c[3:] for c in chromosomes])
plt.xticks(np.arange(1, len(chromosomes) + 1),[c for c in chromosomes])
plt.show()




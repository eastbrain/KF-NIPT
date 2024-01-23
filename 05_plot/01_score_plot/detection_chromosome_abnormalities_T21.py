import os
import sys
import argparse
import warnings
import scipy
import scipy.stats as ss
import pandas as pd
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('Agg')

#####################################################################################################
def plot_anomaly(df, threshold, title='KF-score'):
    #df = df.sort_index(ascending=True)
    df = df.sort_index(ascending=False)
    ranks = np.linspace(1, len(df), len(df))
    outliers = (df > threshold)
    t21 = df[df>3]

    for i in t21.index:
      score = round(t21[i],4)
      id = i.replace("s_","")
      print((id) + ": "+ str(score))

    plt.figure(dpi=150)
    plt.plot(ranks[outliers],  df[outliers],'o', color='r',label='trisomy 21')
    plt.plot(ranks[~outliers], df[~outliers],'o', color='b', label='normal')
    plt.axhline(threshold,color='r',label='threshold', alpha=0.5)
    plt.legend(loc = 'upper right')
    plt.title(title, fontweight='bold')
    plt.xlabel('Down Syndrome')
    plt.ylabel('KF-score')
    plt.xticks([])
    plt.show()

#####################################################################################################
def draw_chart(mat_file):
   df = pd.read_csv(mat_file, sep = "\t").set_index('chr').loc['chr21']
   plot_anomaly(df,3) 


#####################################################################################################
def main():
  warnings.filterwarnings('ignore')

  parser = argparse.ArgumentParser(description='Welcoming version (sckacker@ajou.ac.kr, gtphrase@eonelab.co.kr)')
  parser.add_argument('matrix' ,type=str,help='matrix.txt or table.txt')

  args = parser.parse_args(sys.argv[1:])
  mat_file = args.matrix
  draw_chart(mat_file)

if __name__ == '__main__':
  main()

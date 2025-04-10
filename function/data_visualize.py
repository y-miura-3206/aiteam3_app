import streamlit as st
import pandas as pd
from pycirclize import Circos

from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import os, tempfile

def reshape_df_2_radar(df):
    df = df[['スキルカテゴリ','スキルレベル','チェック項目.1']].astype({'スキルレベル': str})
    df_summary = df.groupby(['スキルカテゴリ','スキルレベル']).sum()
    df_summary = df_summary.reset_index()

    df_summary = df_summary.pivot(index='スキルカテゴリ',columns='スキルレベル',values='チェック項目.1')
    df_summary = df_summary.fillna(0)
    
    df_count = df.groupby(['スキルカテゴリ','スキルレベル']).count()
    df_count = df_count.reset_index()
    df_count = df_count.pivot(index='スキルカテゴリ',columns='スキルレベル',values='チェック項目.1')
    df_count = df_count.fillna(0)

    df_percentage = df_summary/df_count*100
    df_percentage.rename(columns={'1': 'レベル1','2': 'レベル2','3': 'レベル3'})
    df_percentage = pd.DataFrame(df_percentage)
    df_percentage = df_percentage.fillna(0).T
    return df_percentage

def df_2_radarchart(df,key):
    # max_value = df.max().max() + 2
    # max_value = int(max_value)
    circos = Circos.radar_chart(
        df,
        vmax=100,
        vmin=0,
        # fill=False,
        marker_size=6,
        grid_interval_ratio=0.2,
    )

    fig = circos.plotfig()
    _ = circos.ax.legend(loc="upper right", fontsize=10)
    fig.savefig(f"{key}.png")
    st.pyplot(fig)
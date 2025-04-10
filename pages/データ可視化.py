import streamlit as st
import pandas as pd
import numpy as np
from lib import _set_page_config, routing

from function import data_input,edit_df, data_visualize

import collections.abc # インポートしないとエラーが発生する
from pptx import Presentation # プレゼンテーションを作成
from pptx.util import Inches  # インチ
from pptx.enum.text import PP_ALIGN  # 中央揃えにする用
from pptx.util import Cm, Pt # センチ、ポイント

import matplotlib.pyplot as plt
import japanize_matplotlib

_set_page_config.set_page_config()

# if __name__ == "__main__":
#     routing.run_navi()

def create_metric_info(df):
    # レベルごと
    df_summary = df[['スキルレベル','チェック項目.1']]
    df_count = df_summary.groupby("スキルレベル").count().rename(columns={'チェック項目.1': '総合'})
    df_summary = df_summary.groupby("スキルレベル").sum().rename(columns={'チェック項目.1': '得点'})
    merged_df = pd.merge(df_count, df_summary, on='スキルレベル', how='left')
    merged_df["達成率"] = merged_df["得点"]/merged_df["総合"]*100
    merged_df = merged_df.round(2)

    # レベルごとかつ必須スキル
    df_necessary = df[['スキルレベル','チェック項目.1']][df['必須スキル']=='〇']
    df_necessary_count = df_necessary.groupby("スキルレベル").count().rename(columns={'チェック項目.1': '総合'})
    df_necessary_summary = df_necessary.groupby("スキルレベル").sum().rename(columns={'チェック項目.1': '得点'})
    merged_df_necessary = pd.merge(df_necessary_count, df_necessary_summary, on='スキルレベル', how='left')
    merged_df_necessary["達成率"] = merged_df_necessary["得点"]/merged_df_necessary["総合"]*100
    merged_df_necessary = merged_df_necessary.round(2)

    cols = st.columns(len(merged_df))
    for i in range(len(merged_df)):
        with cols[i]:
            try:
                whole_achive = merged_df["達成率"][i+1]
            except KeyError:
                whole_achive = '--該当なし--'
            try:
                nece_achive = merged_df_necessary["達成率"][i+1]
            except KeyError:
                nece_achive = '--該当なし--'
            cols[i].metric(f"levl{i+1}達成率", f"{whole_achive}%", f"{i*10}%") # もう一つ数値を入れることが可能（前回・平均との差分表示に利用可能）
            cols[i].metric(f"levl{i+1}必須項目達成率", f"{nece_achive}%", f"{i*10}%")

def display():
    sheet_dict = data_input.exlfile_upload("page1")
    if sheet_dict is not None:
        st.write(len(sheet_dict))
        sheet_name_list = list(sheet_dict.keys())

        # cols = st.columns(len(sheet_dict))

        for i in range(len(sheet_dict)):
            # with cols[i]:
            TF = False
            if i+1 == 1:
                TF = True
            with st.expander(f"tab{i+1}", expanded=TF):
                st.subheader(f"{sheet_name_list[i]}")
                # ここに各タブの内容を追加
                df = sheet_dict[sheet_name_list[i]]
                # st.dataframe(df)
                col1, col2 = st.columns(2)
                with col1:
                    df_for_radar = data_visualize.reshape_df_2_radar(df)
                    st.write(df_for_radar)
                    data_visualize.df_2_radarchart(df_for_radar, f'category{i}')

                with col2:
                    create_metric_info(df)

                    with st.container(border=True):

                        # You can call any Streamlit command, including custom components:
                        # st.bar_chart(np.random.randn(50, 3))
                        st.dataframe(df_for_radar)

                        prompt = st.chat_input("組織マネジメント力を上げるために必要なこととは？", key=f"chat{i}")
                        if prompt:
                            st.write(f"User has sent the following prompt: {prompt}")

   
# if __name__ == "__page__":
display()
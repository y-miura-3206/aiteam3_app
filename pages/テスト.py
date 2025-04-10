import streamlit as st
import pandas as pd
from lib import _set_page_config, routing

from function import data_input,edit_df, data_visualize

import collections.abc # インポートしないとエラーが発生する
from pptx import Presentation # プレゼンテーションを作成
from pptx.util import Inches  # インチ
from pptx.enum.text import PP_ALIGN  # 中央揃えにする用
from pptx.util import Cm, Pt # センチ、ポイント

_set_page_config.set_page_config()


# if __name__ == "__main__":
#     routing.run_navi()

def display():

    df = pd.DataFrame(
        data=[
            [80, 80, 80, 80, 80, 80, 80],
            [90, 20, 95, 95, 30, 30, 80],
            [60, 90, 20, 20, 100, 90, 50],
        ],
        index=["Hero", "Warrior", "Wizard"],
        columns=["HP", "MP", "ATK", "DEF", "SP.ATK", "SP.DEF", "SPD"],
    )
    st.dataframe(df)

# if __name__ == "__page__":
display()
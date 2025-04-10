import streamlit as st
import pandas as pd

def df_with_multiselect(df, column_name, list):
    selected_list = st.multiselct("項目選択",list)
    
def slider_with_info(info1,info2,key1):
    excel_file = pd.ExcelFile("function/考課評価基準.xlsx")
    sheet_dict = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
    col1,col2,col3 = st.columns([1,3,2])
    with col1:
        st.write(f"{info1}")
        st.write(f"{info2}")
    with col2:
        # デフォルト値は前年の数値
        number = st.slider("評価の記入", 0, 8, 2,key=f"{info1}{info2}")
    with col3:
        # 選択した数値による説明の表示
        df = sheet_dict[key1]
        df = df.query(f'分類 == "{info1}" and 評価項目 == "{info2}"')
        st.write(df.loc[:,[number]])
    st.divider

def annual_check_df(df,key,period):
    # 考課基準の詳細の表示用
    excel_file = pd.ExcelFile("function/考課評価基準.xlsx")
    sheet_dict = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
    info_df = sheet_dict[key]
    

    st.write(f"{key}自己評価の記入")

    lv_10_list = list(set(df["分類"]))
    display_lv10_columns = st.multiselect("表示分類選択",lv_10_list,lv_10_list,key=f"{key}分類")
    # 編集用dfの絞り込み
    df_ = df[df["分類"].isin(display_lv10_columns)]
    # 考課基準の絞り込み
    info_df = info_df[info_df["分類"].isin(display_lv10_columns)]

    lv_20_list = list(set(df_["評価項目"]))
    display_lv20_columns = st.multiselect("表示評価項目選択",lv_20_list,lv_20_list,key=f"{key}評価項目")
    # 編集用dfの絞り込み
    df_ = df_[df_["評価項目"].isin(display_lv20_columns)]
    # 考課基準の絞り込み
    info_df = info_df[info_df["評価項目"].isin(display_lv20_columns)]

    df_[period] = df_.iloc[:,-1]
    df_=df_[["分類","評価項目",period]]

    col1,col2 = st.columns([1,1])
    with col1:
        edited_df = st.data_editor(df_)
    with col2:
        with st.expander("See explanation"):
            info_df = info_df.set_index("評価項目")
            merged_info_df = pd.DataFrame()
            titles = []
            texts = []
            for i in range(len(edited_df)):
                set_column_num = edited_df.iat[i,-1]
                # st.write(edited_df.iat[i,0])
                set_row_name = edited_df.iat[i,1]
                # st.write(f"**{set_row_name}**")
                titles.append(set_row_name)

                # st.write(info_df.at[set_row_name,set_column_num])
                texts.append(info_df.at[set_row_name,set_column_num])

            all_markdown = ""
            for title, text in zip(titles, texts):
                all_markdown += f" \n\n**{title}**\n\n{text}"

            # st.write(all_markdown)
            with st.container():
                st.markdown(f"""
                    <div style="height: 300px; overflow: auto;">
                        {all_markdown}
                    </div>
                    """, unsafe_allow_html=True)

    df_columns = list(edited_df.columns)
    selected_columns_list = st.multiselect("表示カラム項目選択",df_columns,df_columns,key=f"{key}カラム")
    edited_df = edited_df[selected_columns_list]

    return edited_df

def annual_check_slider(df,key):
    st.write(f"{key}自己評価の記入")
    lv_10_list = list(set(df["分類"]))

    display_lv10_columns = st.multiselect("表示分類選択",lv_10_list,lv_10_list,key=f"{key}slider分類")
    df_ = df[df["分類"].isin(display_lv10_columns)]

    lv_20_list = list(set(df_["評価項目"]))

    display_lv20_columns = st.multiselect("表示評価項目選択",lv_20_list,lv_20_list,key=f"{key}slider評価項目")
    df_ = df_[df_["評価項目"].isin(display_lv20_columns)]
    st.write(df_)

    df_bunrui = df_["分類"]
    df_koumoku = df_["評価項目"]
    for i in range(len(df_)):
        slider_with_info(df_bunrui.iloc[i],df_koumoku.iloc[i],key)

    # df_columns = list(edited_df.columns)
    # selected_columns_list = st.multiselect("表示カラム項目選択",df_columns,df_columns,key=f"{key}カラム")
    # edited_df = edited_df[selected_columns_list]

    # return edited_df


def skill_check_visualize():

    st.title("スキルチェック可視化")

    # listの辞書
    # list_dict
    max_item = max(list_dict.items(), key=lambda x: len(x[1]))
    max_item_len = len(max_item[1])

    for key, value in list_dict.items():
        for i in range(max_item_len - len(value)):
            list_dict[key].append(float('nan'))

    list_dict_df = pd.DataFrame(list_dict)
    edited_list_dict_df = st.data_editor(list_dict_df,num_rows="dinamic")

    diff_df = edited_list_dict_df.copy()
    diff_df = diff_df.mask(list_dict_df.eq(edited_list_dict_df),None)

    not_null_df = diff_df.notnull()

    styled_df_1 = list_dict_df.style.apply(lambda x: ['background-color: lightpink' if v else '' for v in not_null_df[x.name]])
    styled_df_2 = edited_list_dict_df.style.apply(lambda x: ['background-color: lightgreen' if v else '' for v in not_null_df[x.name]])
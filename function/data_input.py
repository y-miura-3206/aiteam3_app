import streamlit as st
import pandas as pd
from openpyxl import Workbook

def exlfile_upload(txt):
    upload_file = st.file_uploader(label=f"{txt}",key=f"{txt}")

    if upload_file is not None:
        try:
            excel_file = pd.ExcelFile(upload_file)
            sheet_dict = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
            return sheet_dict
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("Excelファイルを選択してください")
        
def excel_form_local():
    try:
        excel_file = pd.ExcelFile("function/考課数値履歴.xlsx")
        sheet_dict = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}
        return sheet_dict
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
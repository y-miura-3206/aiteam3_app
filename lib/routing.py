import streamlit as st

def run_navi():
    pages = [
        st.Page("pages/データ可視化.py",title="データ可視化"),
        st.Page("pages/テスト.py",title="テスト")
    ]

    hierarchy_pages = {
        "可視化":[*pages[0:1]],
        # "テスト":[*pages[1:2]],
    }

    pg = st.navigation(hierarchy_pages)
    pg.run()

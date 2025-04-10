import streamlit as st

def set_page_config(page_title="title", layout="wide"):
    try:
        st.set_page_config(
            page_title="Ex-stream-ly Cool App",
            page_icon="🧊",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
        )
    except:
        pass

    st.markdown(
        """
        <style>
            [data-testid='StSidebarNav'] > ul {
            min-height: 28em;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
import streamlit as st
from lib import _set_page_config, routing

def main():
    # _set_page_config.set_page_config()
    routing.run_navi()

if __name__ == "__main__":
    main()


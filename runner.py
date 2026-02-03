import streamlit as st
import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "app.py"]
sys.exit(stcli.main())

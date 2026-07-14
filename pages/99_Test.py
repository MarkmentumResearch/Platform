
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Test")

CSV_PATH = Path("data") / "ticker_data.csv"

df = pd.read_csv(CSV_PATH)

st.write(df.shape)
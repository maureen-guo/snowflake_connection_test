import streamlit as st
from snowflake.snowpark.context import get_active_session
import pandas as pd

st.title("Sales & Quantity Metrics")

# Use current session to run queries
session = get_active_session()

# Query sample data directly
query = """
    SELECT L_PARTKEY, SUM(L_QUANTITY) AS TOTAL_QUANTITY
    FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM
    GROUP BY L_PARTKEY
    LIMIT 10
"""
df = session.sql(query).to_pandas()

# Display dynamic visual components
st.subheader("Top Parts by Quantity")
st.dataframe(df)
st.bar_chart(data=df, x="L_PARTKEY", y="TOTAL_QUANTITY")
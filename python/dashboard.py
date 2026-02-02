import streamlit as st
import pandas as pd
from db_connect import get_connection

st.set_page_config(page_title="F1 Analytics Dashboard", layout="wide")
st.title("🏎️ F1 Analytics Dashboard")

conn = get_connection()

drivers_df = pd.read_sql("""
    SELECT DISTINCT driver_name, wins, podiums
    FROM drivers
""", conn)



standings_df = pd.read_sql("""
    SELECT d.driver_name, SUM(r.points) AS total_points
    FROM race_results r
    JOIN drivers d ON r.driver_id = d.driver_id
    GROUP BY d.driver_id
    ORDER BY total_points DESC
""", conn)

conn.close()

st.subheader("Drivers Overview")
st.dataframe(drivers_df)

st.subheader("Driver Standings")
st.bar_chart(standings_df.set_index("driver_name"))
selected_driver = st.selectbox(
    "Select Driver",
    standings_df["driver_name"]
)

st.write(
    standings_df[standings_df["driver_name"] == selected_driver]
)

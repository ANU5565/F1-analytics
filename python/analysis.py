import pandas as pd
from db_connect import get_connection
def load_drivers():
    conn = get_connection()
    query = "SELECT driver_name, wins, podiums, championships FROM drivers"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

drivers_df = load_drivers()
print(drivers_df)


import pandas as pd
import matplotlib.pyplot as plt
from db_connect import get_connection

def tyre_usage():
    conn = get_connection()
    query = """SELECT driver_name, wins, podiums, championships FROM drivers"""
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = tyre_usage()

plt.figure()
plt.bar(df["wins"], df["podiums"])
plt.xlabel("Tyre Compound")
plt.ylabel("Usage Count")
plt.title("Tyre Compound Usage")
print(df)
plt.show()

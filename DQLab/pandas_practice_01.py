import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.columns)
order_df.rename(columns={"freight_value": "shipping cost"}, inplace=True)
print(order_df.columns)

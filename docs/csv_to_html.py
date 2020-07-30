import pandas as pd
df = pd.read_csv("Resources/cities.csv")
df.to_html('raw_data.html',classes=["table-bordered", "table-striped", "table-hover"])

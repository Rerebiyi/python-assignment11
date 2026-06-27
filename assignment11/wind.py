import plotly.express as px
import plotly.data as pldata

df = pldata.wind()

print(df.head(10))
print(df.tail(10))

# Data Cleaning

df["strength"] = df["strength"].str.replace("+", "", regex=False)
df["strength"] = df["strength"].str.replace(r"(\d+)-(\d+)", r"\1.5", regex=True)
df["strength"] = df["strength"].astype(float)

#  Interactive scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency"
)

# Save and open HTML file
fig.write_html("wind.html", auto_open=True)
import pandas as pd
import plotly.express as px
import csv
import numpy as np

# df = pd.read_csv('106data1.csv')
# fig = px.scatter(df,x='Temperature',y='Ice-cream Sales( ₹ )')

# fig.show()
def getDataSource(data_path):
    cold_drink_sales = []
    ice_cream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales( ₹ )"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :-  \n--->",correlation[0,1])
def setup():
    data_path  = "106data1.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
  #  plotFigure(data_path)
setup()
import pandas as pd
from datamallet.visualization import AutoPlot
df = pd.read_csv('data/tips.csv')

autoplot = AutoPlot(df=df, filename='basic',
                    include_scatter=True)

print(autoplot.chart_type())
list_of_figures = autoplot.show()



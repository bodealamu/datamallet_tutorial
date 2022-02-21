autoplot = AutoPlot(df=df,color='sex',
                    include_density_heatmap=True,
                    include_density_contour=True,
                    include_box=True,
                    include_correlation=True,include_pie=True,
                    include_histogram=True,
                    include_treemap=True,
                    include_sunburst=True,
                    include_violin=True,include_scatter=True,include_bar=True,
                    filename='plots')

list_of_figs = autoplot.show()

autoplot = AutoPlot(df=df,
                    filename='autoplot',
                    include_scatter=True,
                    include_violin=True,include_bar=True,
                    include_sunburst=True,include_treemap=True,
                    include_pie=True,
                    include_histogram=True,
                    include_correlation=True)

print(autoplot.chart_type())

autoplot.show()
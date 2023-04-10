import pandas as pd

y={'f(x)':[2,4,6,8],'g(x)':[4,2,-2,6]}
x=[1,2,3,4]

graph=pd.DataFrame(y,x)
graph.plot(kind='line',grid=True,title="My Graph",ylabel='f(x)',xlabel='x')

from google.colab import drive
drive.mount("/content/drive")

graph_plot=graph.plot(kind='line',grid=True,title="My Graph",ylabel='f(x)',xlabel='x',xlim=(1,4)).get_figure()
graph_plot.savefig('/content/drive/My Drive/mygraph.pdf')
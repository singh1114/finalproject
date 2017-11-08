import networkx as nx
import matplotlib.pyplot as plt
def pagerankalgo():

    G = nx.read_graphml("/home/sharan/Desktop/goa.graphml")

    results = nx.degree_centrality(G)

    results = sorted(results.items(), key=lambda x: x[1],reverse=True)
    x = []
    y = []

    top  = []
    top  = results[:10]
    for i in top:
        x.append(i[0])   #creating vertices for plotting
        y.append(i[1])

    y_pos = range(0,len(top))
    plt.bar(y_pos,y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.ylabel('Degree Centrality')
    plt.title('Analysis')
    plt.show()
    return "m"

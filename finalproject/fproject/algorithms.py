import networkx as nx
import matplotlib.pyplot as plt
def degreecentrality():

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
def pagerankalgo():
    import networkx as nx
    import time
    import matplotlib.pyplot as plt
    G = nx.read_graphml("/home/sharan/Desktop/punjab1.graphml")
    g = nx.Graph(G)
    id =[]
    value = []


    start_time = time.time()
    result = nx.pagerank(g)
    result = sorted(result.items(), key=lambda x: x[1],reverse=True)
    x = []
    y = []

    top  = []
    top  = result[:10]
    for i in top:
        x.append(i[0])   #creating vertices for plotting
        y.append(i[1])

    y_pos = range(0,len(top))
    plt.bar(y_pos,y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.ylabel('Pagerank')
    plt.title('Analysis')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))


class Node:
    def __init__(self,node):
        self.id = node
	#dictionary to store adjacent nodes
        self.adjacent = {}

    def add_neighbor(self,neighbor,weight = 1):
        self.adjacent[neighbor] = weight

    # Override the string function
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def get_id(self):
        return  self.id

    def get_weight(self,neighbor):
        return  self.adjacent[neighbor]

    def get_connections(self):
        return  self.adjacent.keys()


class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    def add_node(self,node):
        self.num_nodes += 1
        new_node = Node(node)
        self.node_dict[node] = new_node

    def add_edge(self,fromNode,toNode,costFrom = 1,costTo=0):
        if fromNode not in self.node_dict:
            self.add_node(fromNode)
        if toNode not in self.node_dict:
            self.add_node(toNode)

        self.node_dict[fromNode].add_neighbor(self.node_dict[toNode],costFrom)

        # if bidirectional
        # self.node_dict[toNode].add_neighbor(self.node_dict[fromNode], costTo)        

if __name__ == '__main__':
    g = Graph()

    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    for v in g:
        print( 'g.node_dict[%s]=%s' % (v.get_id(), g.node_dict[v.get_id()]) )

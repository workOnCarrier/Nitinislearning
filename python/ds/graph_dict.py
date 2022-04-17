
# baed on course by https://cglearning.udemy.com/user/elshad-karimov/


class GraphDict:
    def __init__(self, gdict: dict = None):
        if gdict is None:
            gdict = {}
        self.__gdict = gdict

    def addEdge(self, vertex, edge):
        self.__gdict[vertex].append(edge)

    def gdict(self):
        return self.__gdict

    def vertices(self):
        return self.__gdict.keys()

    def edges(self, vertex):
        if vertex not in self.__gdict.keys():
            raise Exception("vertex is not in graph")
        return self.__gdict[vertex]



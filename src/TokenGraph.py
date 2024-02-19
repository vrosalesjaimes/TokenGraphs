import sage.graphs.graph as graph
import networkx as nx
from itertools import combinations

class TokenGraph():
    """
    A class to represent a token graph.
    """
    
    def __init__(self, graph6_string: str, token_number: int) -> None:
        """
        Initializes the TokenGraph object with the given graph and token number.

        Args:
        graph (nx.Graph): The original graph.
        token_number (int): The number of tokens.
        """
        self.__graph = nx.Graph(graph6_string)
        self.__token_number = token_number

    @property
    def graph(self) -> nx.Graph:
        """
        Returns the original graph.
        """
        return self.__graph
    
    @graph.setter
    def graph(self, value: str) -> None:
        """
        Sets the original graph.
        """
        self.__graph = nx.Graph(value)
    
    @property
    def token_number(self) -> int:
        """
        Returns the number of tokens.
        """
        return self.__token_number
    
    @token_number.setter
    def token_number(self, value: int) -> None:
        """
        Sets the number of tokens.
        """
        assert value < self.graph.number_of_nodes(), "The number of tokens must be less than the number of nodes in the graph."
        self.__token_number = value
    

    def token_graph(self) -> nx.Graph:
        """
        Returns the token graph.
        """
        token_graph = nx.Graph()
        
        set = set(self.__graph.node_dict_factory().keys())
        nodes = set(combinations(set, self.token_number))
        
        graph.add_nodes_from(nodes)
        
        for A, B in combinations(nodes, 2):
            symetric_difference = A.symmetric_difference(B)
            
            if(len(symetric_difference) == 2):
                a,b = symetric_difference
                
                if ((a in A and b in B) or (a in B and b in A)) and (self.__graph.has_edge(a,b)):
                    graph.add_edge(A,B)
        
        return token_graph
from sage.graphs.graph import Graph
from itertools import combinations

class TokenGraph():
    """
    A class to represent a token graph.
    """
    
    def __init__(self, graph6_string: str, token_number: int) -> None:
        """
        Initializes the TokenGraph object with the given graph and token number.

        Args:
        graph (sage.Graph): The original graph.
        token_number (int): The number of tokens.
        """
        self.__graph = Graph(graph6_string)
        assert self.graph.num_verts() > token_number, "The number of tokens must be less than the number of nodes in the graph."
        self.__token_number = token_number

    @property
    def graph(self) -> Graph:
        """
        Returns the original graph.
        """
        return self.__graph
    
    @graph.setter
    def graph(self, value: str) -> None:
        """
        Sets the original graph.
        """
        self.__graph = Graph(value)
    
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
    
    def generate_toke_graph(self) -> Graph:
        """
        Generates the toekn graph.
        """
        token_graph = Graph()
        vertices = list(self.graph.get_vertices())
        
        for subset in combinations(vertices, self.token_number):
            token_graph.add_vertex(subset)
            
        for A, B in combinations(list(token_graph.get_vertices()), 2):
            symetric_difference = set(A).symmetric_difference(B)
            
            if len(symetric_difference) == 2:
                a, b = symetric_difference
                
                if ((a in A and b in B) or (a in B and b in A)) and (self.__graph.has_edge(a, b)):
                    token_graph.add_edge(A, B)

        return token_graph

# Implementation of Directed Graph

class Vertex:
  """
    This class represents each vertex in the graph. Every vertex has arcs to other vertices.

    Parameters:
    id (int): Int number to differentiate the new vertex

  """

  def __init__(self, id:int):
    self.id = id
    self.mark = False
    self.arcs = []
  
  def insertArc(self, target) -> bool:
    """
      Use this to connect the current vertex to other vertex 

      Parameters:
      target (Vertex): Vertex to create the new connection

      Returns:
      bool: return if insert was successful
    """

    for arc in self.arcs:
      if arc.target == target:
        return False

    newArc = Arc(target)
    self.arcs.append(newArc) 
    return True

  def __str__(self) -> str:
    """
      Convert Vertex class information to an easy-to-read format

      Returns:
      str: return easy-to-read string
    """

    vertexString = "Vertex {} Connected to: ".format(self.id)
    for arc in self.arcs:
      vertexString += "{}, ".format(arc.target.id)
    return vertexString


class Arc:
  """
    This class represents the connection between 2 vertices.

    Parameters:
    target (Vertex): vertex to generate the connection

  """

  def __init__(self, target:Vertex):
    self.target =target


class Graph:
  """
    This class contains all the methods to interact with the graph.
  """

  vertices = []

  def isConnected(self, origin:Vertex, target:Vertex) -> bool:
    """
      Check there is a coonection from origin vertex to target vertex

      Parameters:
        origin (Vertex): where the search begins
        target (Vertex): where the search ends
      
      Returns:
        bool: Returns if the origin vertex is connected to the target vertex
    """

    result = self.__isConnected(origin, target)
    self.clearMarks()
    return result

  def __isConnected(self, origin:Vertex, target:Vertex) -> bool:
    """
      Check there is a coonection from origin vertex to target vertex. This methods is called recursively.

      Parameters:
        origin (Vertex): where the search begins
        target (Vertex): where the search ends
      
      Returns:
        bool: Returns if the origin vertex is connected to the target vertex
    """

    if(origin.mark):
      return False

    origin.mark = True
    for arc in origin.arcs:
      if(arc.target == target):
        return True
      result = self.isConnected(arc.target, target)
      if result:
        return True
    return False

  def clearMarks(self):
    """
      Clear search marks that are generated when traversing the graph
    """
    for vertex in self.vertices:
      vertex.mark = False

  def insertVertex(self, vertex:Vertex) -> bool:
    """
      Inserts a new vertex in the graph.

      Parameters:
        vertex (Vertex): Vertex to insert

      Returns:
        bool: Return if the insert was successful.
    """
    if vertex in self.vertices:
      return False
    self.vertices.append(vertex)
    return True
  
  def __str__(self) -> str:
    """
      Convert Graph class information to an easy-to-read format

      Returns:
      str: return easy-to-read string
    """

    graphString = "-- Graph --\n"

    for vertex in self.vertices:
      graphString += str(vertex)+"\n"

    return graphString


# Example

# create grap
graph = Graph()

# create new vertices
vertex1 = Vertex(1)
vertex2 = Vertex(2)
vertex3 = Vertex(3)
vertex4 = Vertex(4)
vertex5 = Vertex(5)

# create connection between vertices
vertex1.insertArc(vertex2)
vertex2.insertArc(vertex3)
vertex3.insertArc(vertex4)
vertex4.insertArc(vertex1)
vertex4.insertArc(vertex5)

# Insert the vertices in the graph
graph.insertVertex(vertex1)
graph.insertVertex(vertex2)
graph.insertVertex(vertex3)
graph.insertVertex(vertex4)
graph.insertVertex(vertex5)

# check the vertices connections
print("1 to 5 is connected:",graph.isConnected(vertex1,vertex5))
print("5 to 1 is connected:",graph.isConnected(vertex5,vertex1))

print()

# Show the graph content
print(str(graph))


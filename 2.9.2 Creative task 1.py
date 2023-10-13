nodes = []
edges = []
app.index = 0
app.background = rgb(36, 39, 48)
selected_colour = rgb(169, 145, 241)
default_colour = rgb(98, 104, 110)


class Edge:
    def __init__(self, node1, node2, line):
        self.node1 = node1
        self.node2 = node2
        self.line = line


def add_edges(new_node):
    for i, node in enumerate(nodes):
        edge = Edge(
            i,
            app.index,
            Line(
                node.centerX,
                node.centerY,
                new_node.centerX,
                new_node.centerY,
                fill=default_colour,
            ),
        )
        edges.append(edge)


def add_node(x, y):
    app.index = len(nodes)
    node = Circle(x, y, 10, fill=default_colour)
    add_edges(node)
    nodes.append(node)


def update_colour():
    for edge in edges:
        if edge.node1 == app.index or edge.node2 == app.index:
            edge.line.toFront()
            edge.line.fill = selected_colour
            nodes[edge.node1].fill = selected_colour
            nodes[edge.node2].fill = selected_colour
            nodes[edge.node1].toFront()
            nodes[edge.node2].toFront()
        else:
            edge.line.fill = default_colour


def onMouseMove(x, y):
    nodes[app.index].centerX = x
    nodes[app.index].centerY = y
    for edge in edges:
        if edge.node1 == app.index:
            edge.line.x1 = x
            edge.line.y1 = y
        elif edge.node2 == app.index:
            edge.line.x2 = x
            edge.line.y2 = y


def onKeyPress(key):
    if key == "left":
        app.index -= 1
    elif key == "right":
        app.index += 1
    app.index %= len(nodes)
    update_colour()


def onMousePress(x, y):
    add_node(x, y)
    update_colour()


add_node(200, 200)

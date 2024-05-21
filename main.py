from ascii_graph import Pyasciigraph

graph = Pyasciigraph()

data = [
    ('January', 10),
    ('February', 20),
    ('March', 15),
    ('April', 30),
    ('May', 25),
    ('June', 35),
    ('July', 40),
    ('August', 45),
    ('September', 20),
    ('October', 15),
    ('November', 10),
    ('December', 5)
]

for line in graph.graph('Monthly Data', data):
    print(line)
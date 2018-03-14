import random


WEIGHT_MIN = 0
WEIGHT_MAX = 10**6

def generate_connected_graph(V):
	initialSet = set()
	visitedSet = set()
	vertices = set()
	edges = set()

	for i in range(V):
		initialSet.add(str(i))
		vertices.add(str(i))

	curVertex = random.sample(initialSet, 1).pop()
	initialSet.remove(curVertex)
	visitedSet.add(curVertex)

	while initialSet:
		adjVertex = random.sample(initialSet, 1).pop()
		edge = (random.randint(WEIGHT_MIN,WEIGHT_MAX), curVertex, adjVertex)
		edges.add(edge)
		initialSet.remove(adjVertex)
		visitedSet.add(adjVertex)
		curVertex = adjVertex
	return list(vertices), list(edges)


def main():
	vertices, edges = generate_connected_graph(10)
	print(vertices)
	print(edges)


if __name__ == '__main__':
	main()
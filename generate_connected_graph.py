import random


WEIGHT_MIN = 0
WEIGHT_MAX = 10**6

def generate_connected_graph(V):
	initialSet = set()
	visitedSet = set()
	vertices = list()
	edges = list()

	for i in range(V):
		initialSet.add(i)
		vertices.append(i)

	curVertex = random.sample(initialSet, 1).pop()
	initialSet.remove(curVertex)
	visitedSet.add(curVertex)

	while initialSet:
		adjVertex = random.sample(initialSet, 1).pop()
		edge = [random.randint(WEIGHT_MIN,WEIGHT_MAX), curVertex, adjVertex]
		edges.append(edge)
		initialSet.remove(adjVertex)
		visitedSet.add(adjVertex)
		curVertex = adjVertex
	return vertices, edges


def print_matrix(V, vertices, edges):
	#print(V)
	#print(edges)
	matrix = [['0']*V for y in range(V)]
	#print(matrix)
	for i in edges:
		# print(i)
		u = i[1]
		v = i[2]
		# print(str(i[1]) + ' ' + str(i[2]))
		#matrix[i[1]][i[2]] = matrix[i[2]][i[1]] = i[0]
		matrix[u][v] = str(i[0])
		matrix[v][u] = str(i[0])
		#print(matrix[i[1]][i[2]], i[1], i[2])
	for i in matrix:
		print(' '.join(i))


def main():
	V = 15 #input('Enter number of vertices: ')
	vertices, edges = generate_connected_graph(V)
	print_matrix(V, vertices, edges)


if __name__ == '__main__':
	main()
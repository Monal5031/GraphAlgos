#include "bits/stdc++.h"
#include <stdio.h>
#include <limits.h>

using namespace std;

#define ll long long
#define l long
#define ull unsigned long long
#define in(a) cin >> a
#define out(a) cout << a << "\n"
#define fast fin; fout; fio;
#define fin cin.tie(NULL)
#define fout cout.tie(NULL)
#define fio ios::sync_with_stdio(false)

#define V 15

int minKey(int key[], bool mstSet[]) {
	int min = INT_MAX, min_index;

	for (int v = 0; v < V; v++)
		if (mstSet[v] == false && key[v] < min)
				min = key[v], min_index = v;

	 return min_index;
}

int printMST(int parent[], int n, int graph[V][V]) {
	printf("Edge   Weight\n");
	for (int i = 1; i < V; i++)
			printf("%d - %d    %d \n", parent[i], i, graph[i][parent[i]]);
}


void primMST(int graph[V][V]) {
		int parent[V];
		int key[V];
		bool mstSet[V];

		for (int i = 0; i < V; i++)
				key[i] = INT_MAX, mstSet[i] = false;

		key[0] = 0;
		parent[0] = -1;

		for (int count = 0; count < V-1; count++) {
				int u = minKey(key, mstSet);

				mstSet[u] = true;
				for (int v = 0; v < V; v++)
					if (graph[u][v] && mstSet[v] == false && graph[u][v] <  key[v])
						 parent[v]  = u, key[v] = graph[u][v];
		}
		printMST(parent, V, graph);
}


int main() {
	fast
	l graph[V][V];

	for (int i = 0; i < V; ++i) {
		for (int j = 0; j < V; ++j) {
			in(graph[i][j])
		}
	}
	primMST(graph);

	return 0;
}
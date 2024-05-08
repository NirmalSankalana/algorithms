#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <limits>
#include <fstream>

using namespace std;

// Ford-Fulkerson with Edmonds-Karp (BFS-based) to find maximum flow
class MaxFlow {
public:
    MaxFlow(int n) : n(n), adj(n), capacity(n, vector<int>(n, 0)) {}

    void addEdge(int u, int v, int cap) {
        adj[u].push_back(v);
        adj[v].push_back(u);
        capacity[u][v] = cap;
    }

    int findMaxFlow(int source, int sink) {
        int totalFlow = 0;
        while (true) {
            vector<int> parent(n, -1);
            int flow = bfs(source, sink, parent);
            if (flow == 0) break;  // No augmenting path
            totalFlow += flow;

            // Update capacities along the augmenting path
            int curr = sink;
            while (curr != source) {
                int prev = parent[curr];
                capacity[prev][curr] -= flow;
                capacity[curr][prev] += flow;
                curr = prev;
            }
        }
        return totalFlow;
    }

private:
    int n;
    vector<vector<int>> adj;
    vector<vector<int>> capacity;

    int bfs(int source, int sink, vector<int>& parent) {
        fill(parent.begin(), parent.end(), -1);
        queue<pair<int, int>> q;
        q.push({source, numeric_limits<int>::max()});
        parent[source] = source;

        while (!q.empty()) {
            int curr = q.front().first;
            int flow = q.front().second;
            q.pop();

            for (int neighbor : adj[curr]) {
                if (parent[neighbor] == -1 && capacity[curr][neighbor] > 0) {
                    parent[neighbor] = curr;
                    int newFlow = min(flow, capacity[curr][neighbor]);
                    if (neighbor == sink) return newFlow;
                    q.push({neighbor, newFlow});
                }
            }
        }
        return 0;
    }
};

// Reading input graph from file
vector<pair<int, int>> readGraphFromFile(const string& filename) {
    vector<pair<int, int>> edges;
    ifstream infile(filename);
    if (!infile.is_open()) {
        cerr << "Error opening file." << endl;
        exit(1);
    }

    int n, m;
    infile >> n >> m;
    for (int i = 0; i < m; ++i) {
        int u, v;
        infile >> u >> v;
        edges.push_back({u - 1, v - 1});  // Using 0-based indexing
    }
    infile.close();
    return edges;
}

// Main function to calculate minimum cut between source and sink
int main() {
    string filename;
    cin >> filename;  // Read the filename from standard input
    vector<pair<int, int>> edges = readGraphFromFile(filename);

    int n = 0;  // Number of computers
    if (!edges.empty()) {
        n = edges.size() > 0 ? max(edges[0].first, edges[0].second) : 0;
        for (const auto& edge : edges) {
            n = max(n, max(edge.first, edge.second));
        }
        n++;  // Adjust for 0-based indexing
    }

    MaxFlow maxFlow(n);

    // Add edges to the MaxFlow object
    for (const auto& edge : edges) {
        maxFlow.addEdge(edge.first, edge.second, 1);  // Bidirectional edges with capacity 1
    }

    // Find the minimum cut between computer 1 and the central bank's server (computer n)
    int source = 0;  // Corresponds to computer 1 (0-based index)
    int sink = n - 1;  // Corresponds to central bank's server (last computer)

    int minCut = maxFlow.findMaxFlow(source, sink);

    cout << minCut << endl;  // Output the minimum number of connections to sever

    return 0;
}

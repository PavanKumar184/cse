import java.util.*;

// Class to represent a weighted edge in the graph
class Edge {
    int src, dest, weight;

    Edge() {
        src = dest = weight = 0;
    }
}

// Class to represent a graph with V vertices and E edges
class Graph {
    int V, E;
    Edge edge[];

    Graph(int v, int e) {
        V = v;
        E = e;
        edge = new Edge[e];
        for (int i = 0; i < e; ++i)
            edge[i] = new Edge();
    }

    // Bellman-Ford algorithm to find the shortest paths
    // from src to all other vertices
    void BellmanFord(int src) {
        int dist[] = new int[V];

        // Initialize distances from src to all other vertices as INFINITE
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        // Relax all edges |V| - 1 times. A simple shortest
        // path from src to any other vertex can have at-most |V| - 1 edges
        for (int i = 1; i < V; ++i) {
            for (int j = 0; j < E; ++j) {
                int u = edge[j].src;
                int v = edge[j].dest;
                int weight = edge[j].weight;
                if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v])
                    dist[v] = dist[u] + weight;
            }
        }

        // Check for negative-weight cycles.
        // The above step guarantees shortest distances if graph doesn't contain
        // negative weight cycle. If we get a shorter path, then there is a cycle.
        for (int j = 0; j < E; ++j) {
            int u = edge[j].src;
            int v = edge[j].dest;
            int weight = edge[j].weight;
            if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) {
                System.out.println("Graph contains negative weight cycle");
                return;
            }
        }

        // Print the distance array
        printSolution(dist);
    }

    // A utility function to print the constructed distance array
    void printSolution(int dist[]) {
        System.out.println("Vertex Distance from Source");
        for (int i = 0; i < V; ++i)
            System.out.println(i + "\t\t" + dist[i]);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of vertices: ");
        int V = scanner.nextInt();

        System.out.print("Enter the number of edges: ");
        int E = scanner.nextInt();

        Graph graph = new Graph(V, E);

        for (int i = 0; i < E; ++i) {
            System.out.println("Enter edge " + (i + 1) + " details (source destination weight): ");
            graph.edge[i].src = scanner.nextInt();
            graph.edge[i].dest = scanner.nextInt();
            graph.edge[i].weight = scanner.nextInt();
        }

        System.out.print("Enter the source vertex: ");
        int source = scanner.nextInt();

        scanner.close();

        graph.BellmanFord(source);
    }
}

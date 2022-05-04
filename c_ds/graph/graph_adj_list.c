#include <stdio.h>
#include <stdlib.h>
#define MAXV 1000

typedef struct edge_node_struct{
    int y;  // adjacency info
    int weight; // edge weight if any
    struct edge_node_struct* next; // next edge in the list
}edgenode;

typedef struct graph_struct{
    edgenode *edges[MAXV+1]; // adgacency info list
    int degree[MAXV+1];      // outdegree of each vertex
    int nvertices;           // number of vertices in graph
    int nedges;              // number of edges in graph
    bool directed;           // is graph directed
}graph;

void initialize_graph(graph* g, bool directed){
    int i;
    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;
    for (i=0; i < MAXV+1; i ++) g->edges[i] = NULL;
    for (i=0; i < MAXV+1; i ++) g->degree[i] = 0;
}

void insert_edge(graph* g, int x, int y, bool directed){
    edgenode* p;
    p = (edgenode*)malloc(sizeof(edgenode));
    p->weight = 0;
    p->y = y;
    p->next = g->edges[x];
    g->edges[x] = p;
    g->degree[x] ++;
    if (directed == false)
        insert_edge(g, y, x, true);
    else
        g->nedges ++;

}

void read_graph(graph* g, bool directed){
    int i, m, x, y;
    initialize_graph(g, directed);
    printf("enter number of vertices and edges");
    scanf("%d %d", &(g->nvertices), &m);

    for (i=1;i<=m;i++){
        scanf("%d %d", &x, &y);
        insert_edge(g, x, y, directed);
    }
}

void print_graph(graph* g){
    int i;
    edgenode* p;
    for(i=1; i <= g->nvertices;i++){
        printf("%d:", i);
        p = g->edges[i];
        while(p!= NULL){
            printf(" %d", p->y);
            p = p->next;
        }
        printf("\n");
    }
}

void try_graph_init_and_print(){
    graph test_graph;
    initialize_graph(&test_graph, false);
    read_graph(&test_graph, false);
}

bool processed[MAXV+1];
bool discovered[MAXV+1];
int parent[MAXV+1];

void initialize_search(graph *g){
    for (int i=1; i <= g->nvertices; i++){
        processed[i] = discovered[i] = false;
        parent[i] = -1;
    }
}

void bfs(graph* g, int start){
    queue q;
    int v;
    int y;
    edgenode* p;

    init_queue(&q);
    enqueue(&q, start);
    discovered[start] = true;
    while(empty_queue(&q) == false){
        v = dequeue(&q);
        process_vertex_early(v);
        processed[v] = True;
        p = g->edges[v];
        while(p!= NULL){
            y= p->y;
            if((processed[y] == false)||g->directed)
                process_edge(v,y);
            if(discovered[y] == false){
                enqueue(&q, y);
                discovered[y] = true;
                parent[y] = v;
            }
            p = p->next;
        }
        process_vertex_late(v);
    }
}

void find_path(int start, int end, int parents[]){
    if ((start == end) || (end== -1))
        printf("\n%d", start);
    else{
        find_path(start, parents[end], parents);
        printf(" %d", end);
    }
}

int main(){
    printf("hello world from graph of adj list implementation\n");
    fflush(stdout);
    try_graph_init_and_print();
    return 0;
}
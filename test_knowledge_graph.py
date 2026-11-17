
from modules.knowledge_graph import (
    create_knowledge_graph,
    get_crop_factors,
    get_crop_subgraph,
    compare_crop_conditions
)

# Test 1: Create the complete graph
graph = create_knowledge_graph()

print("===== KNOWLEDGE GRAPH TEST =====")
print("Total Nodes:", graph.number_of_nodes())
print("Total Edges:", graph.number_of_edges())


# Test 2: Retrieve Rice information
print("\n===== RICE KNOWLEDGE =====")

rice_factors = get_crop_factors("rice")

for factor in rice_factors:
    print(factor)


# Test 3: Create Rice visual subgraph
print("\n===== RICE VISUAL GRAPH =====")

rice_graph = get_crop_subgraph("rice")

print("Total Nodes:", rice_graph.number_of_nodes())
print("Total Edges:", rice_graph.number_of_edges())

print("Graph Nodes:", list(rice_graph.nodes()))
print("Graph Edges:", list(rice_graph.edges()))


# Test 4: Check unknown crop
print("\n===== UNKNOWN CROP TEST =====")

unknown_graph = get_crop_subgraph("unknown_crop")

print("Unknown crop nodes:", unknown_graph.number_of_nodes())

print("\nAll Knowledge Graph tests completed!")


import networkx as nx
import pandas as pd


# Create the Soil-Crop Knowledge Graph
def create_knowledge_graph():

    # Load crop recommendation dataset
    df = pd.read_csv("dataset/Crop_recommendation.csv")

    # Create directed graph
    graph = nx.DiGraph()

    # Soil and weather factors
    factors = {
        "N": "Nitrogen",
        "P": "Phosphorus",
        "K": "Potassium",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "ph": "Soil pH",
        "rainfall": "Rainfall"
    }

    # Add factor nodes
    for feature, name in factors.items():

        graph.add_node(
            name,
            node_type="factor",
            dataset_column=feature
        )

    # Add crop nodes and their relationships
    for crop in df["label"].unique():

        graph.add_node(
            crop,
            node_type="crop"
        )

        crop_data = df[df["label"] == crop]

        # Connect each factor with the crop
        for feature, name in factors.items():

            average_value = crop_data[feature].mean()
            minimum_value = crop_data[feature].min()
            maximum_value = crop_data[feature].max()

            graph.add_edge(
                name,
                crop,
                relation="observed dataset statistics",
                average=round(float(average_value), 2),
                minimum=round(float(minimum_value), 2),
                maximum=round(float(maximum_value), 2)
            )

    return graph


# Retrieve soil and weather information for a crop
def get_crop_factors(crop_name):

    graph = create_knowledge_graph()

    crop_name = crop_name.strip().lower()

    if crop_name not in graph:
        return []

    if graph.nodes[crop_name].get("node_type") != "crop":
        return []

    factors = []

    for node in graph.predecessors(crop_name):

        edge_data = graph[node][crop_name]

        factors.append({
            "Factor": node,
            "Relationship": edge_data["relation"],
            "Dataset Average": edge_data["average"],
            "Dataset Minimum": edge_data["minimum"],
            "Dataset Maximum": edge_data["maximum"]
        })

    return factors


# Create a smaller graph for a particular crop
def get_crop_subgraph(crop_name):

    graph = create_knowledge_graph()

    crop_name = crop_name.strip().lower()

    if crop_name not in graph:
        return nx.DiGraph()

    if graph.nodes[crop_name].get("node_type") != "crop":
        return nx.DiGraph()

    # Get all factors connected to the selected crop
    factors = list(graph.predecessors(crop_name))

    # Select crop and factor nodes
    selected_nodes = factors + [crop_name]

    # Create crop-specific subgraph
    crop_graph = graph.subgraph(selected_nodes).copy()

    return crop_graph

    
# Compare farmer inputs with observed crop dataset ranges
def compare_crop_conditions(crop_name, input_values):

    crop_factors = get_crop_factors(crop_name)

    if not crop_factors:
        return []

    factor_mapping = {
        "Nitrogen": "N",
        "Phosphorus": "P",
        "Potassium": "K",
        "Temperature": "temperature",
        "Humidity": "humidity",
        "Soil pH": "ph",
        "Rainfall": "rainfall"
    }

    comparison_results = []

    for factor in crop_factors:

        factor_name = factor["Factor"]

        input_key = factor_mapping[factor_name]

        farmer_value = input_values[input_key]

        minimum = factor["Dataset Minimum"]
        maximum = factor["Dataset Maximum"]

        if farmer_value < minimum:
            status = "Below observed range"

        elif farmer_value > maximum:
            status = "Above observed range"

        else:
            status = "Within observed range"

        comparison_results.append({
            "Factor": factor_name,
            "Farmer Value": round(farmer_value, 2),
            "Observed Minimum": minimum,
            "Observed Maximum": maximum,
            "Status": status
        })

    return comparison_results


from modules.knowledge_graph import compare_crop_conditions

# Sample farmer input values
input_values = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.87,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 150
}

# Compare farmer inputs with Rice dataset ranges
results = compare_crop_conditions(
    "rice",
    input_values
)

print("===== CROP CONDITION COMPARISON =====")

for result in results:
    print(result)

print("\nComparison test completed successfully!")

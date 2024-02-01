import pandas as pd
import numpy as np
import random
import json
# Set the scale for the demonstration
num_merchants = 10000000
num_pincodes = 30000

# Generate merchant IDs and pincodes
merchants = [f"Merchant_{i+1}" for i in range(num_merchants)]
unique_pincodes = set()
while len(unique_pincodes) < num_pincodes:
    unique_pincodes.add(str(random.randint(100000, 999999)))
pincodes = list(unique_pincodes)


relationship_dict = {}
# Randomly assign some pincodes to each merchant to simulate the sparse nature
for merchant in merchants:
    num_served_pincodes = random.randint(100, 1000)  # Each merchant serves between 1 to 10 pincodes for this demo
    served_pincodes = random.sample(pincodes, num_served_pincodes)
    relationship_dict[merchant] = served_pincodes
with open('relation.json', 'w') as f:
    json.dump(f, relationship_dict)

import pandas as pd
import numpy as np
import random
import json
from tqdm import tqdm
# Set the scale for the demonstration
num_merchants = 1000000
num_pincodes = 30000

# Generate merchant IDs and pincodes
merchants = [f"Merchant_{i+1}" for i in range(num_merchants)]
unique_pincodes = set()
while len(unique_pincodes) < num_pincodes:
    unique_pincodes.add(str(random.randint(100000, 999999)))
pincodes = list(unique_pincodes)



# Randomly assign some pincodes to each merchant to simulate the sparse nature
for merchant in tqdm(merchants):
    relationship_dict = {}
    num_served_pincodes = random.randint(1, 10)  
    served_pincodes = random.sample(pincodes, num_served_pincodes)
    relationship_dict[merchant] = served_pincodes
    with open('merchants/'+merchant+'.json', 'w') as f:
        json.dump(relationship_dict, f)
import pandas as pd
import numpy as np
import random
import json
from tqdm import tqdm
import pickle

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfPincode = False
        self.merchantIDs = set()  # Holds merchant IDs at the leaf node

class PincodeTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pincode, merchantID):
        if len(pincode) != 6:
            raise ValueError("Pincode must be exactly 6 digits long")
        node = self.root
        for digit in pincode:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.isEndOfPincode = True
        node.merchantIDs.add(merchantID)  # Add merchant ID only at the leaf node

    def search(self, pincode):
        if len(pincode) != 6:
            return False, 'Pincode is not 6 digits'
        node = self.root
        for digit in pincode:
            if digit not in node.children:
                return False, 'No Merchant'
            node = node.children[digit]
        # Return both the existence of the pincode and the set of merchants at the leaf node
        return node.isEndOfPincode, node.merchantIDs

# Example demonstrating differentiation
trie = PincodeTrie()





num_merchants = 10000000
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
    for pincode in served_pincodes:
        trie.insert(str(pincode), merchant)


with open('trie_data.pkl', 'wb') as file:
    pickle.dump(trie, file)
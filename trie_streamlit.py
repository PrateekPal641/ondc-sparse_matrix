import streamlit as st
import pandas as pd
import numpy as np
import random
import json
import logging
import pickle
from itertools import islice


logging.basicConfig(level=logging.INFO)

# Streamlit state to store data
@st.cache(allow_output_mutation=True)
def get_state():
    state = {}
    state['flag'] = False
    return state

state = get_state()

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

# Function to validate merchant format
def validate_merchant_format(merchant):
    return merchant.startswith("Merchant_") and merchant[9:].isdigit()

# Function to validate pincode format
def validate_pincode_format(pincode):
    return pincode.isdigit() and len(pincode) == 6

# Streamlit UI
st.title("Merchant-Pincodes Relationship and Search")

# Create tabs
tabs = st.tabs(["Relationships", "Search", "Insert"])
 
if 'trie' not in st.session_state:
    st.session_state.trie = PincodeTrie()

# First tab: Relationships
with tabs[0]:
    # Button to generate and save data
    if state['flag'] is False:
        print("here")
        state['flag'] = True

        num_merchants = 100
        num_pincodes = 300

        st.info("Generating sample data for 10 Million Merchants and 30 Thousand pincodes.")
        # Generate merchant IDs and pincodes
        merchants = [f"Merchant_{i+1}" for i in range(num_merchants)]
        unique_pincodes = set()
        while len(unique_pincodes) < num_pincodes:
            unique_pincodes.add(str(random.randint(100000, 999999)))
        pincodes = list(unique_pincodes)



        # Randomly assign some pincodes to each merchant to simulate the sparse nature
        for merchant in merchants:
            relationship_dict = {}
            num_served_pincodes = random.randint(1, 10)  
            served_pincodes = random.sample(pincodes, num_served_pincodes)
            for pincode in served_pincodes:
                st.session_state.trie.insert(str(pincode), merchant)


        with open('trie_data.pkl', 'wb') as file:
            pickle.dump(st.session_state.trie, file)
            
        
        st.info("Data representation done using linked lists with merchant Ids at leaf nodes and Pincode digits at different codes connected as per different combinations")
       
    st.success("DATA IS READY!! TRY SEARCH AND INSERT OPERATIONS")
        

   
# Second tab: Search
with tabs[1]:
    st.header("Search Pincode Serviceability")
    pincode_input = st.text_input("Enter Pincode to search:")
    if st.button("Search"):
        if validate_pincode_format(pincode=pincode_input) is True:
            exists, merchants = st.session_state.trie.search("pincode_input")
            if exists:
                st.success(f"Pincode {pincode_input} is servicable.")
                st.subheader("Merchants serving this pincode:")
                for merchant in merchants:
                    st.markdown(f"- {merchant}")
            else:
                st.warning(f"Pincode {pincode_input} is not servicable.")
        else:
            st.warning("Please enter correct Pincode.")

# Third tab: Insert
with tabs[2]:
    st.header("Insert Merchant-Pincode Pair")
    merchant_input = st.text_input("Enter Merchant:")
    pincode_input_insert = st.text_input("Enter servicable Pincode:")
    if st.button("Insert"):
        if validate_merchant_format(merchant=merchant_input) is False or validate_pincode_format(pincode=pincode_input_insert)is False:
            st.warning("Please enter correct MerchantId and Pincode.")
        else:
            if merchant_input and pincode_input_insert:
                st.session_state.trie.insert("234567", "Merchant2")
                st.success(f"Successfully added Pincode {pincode_input_insert} and Merchnat {merchant_input}.")
            else:
                st.warning("Please enter both Merchant and Pincode.")


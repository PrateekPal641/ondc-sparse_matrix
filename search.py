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
trie.insert("234566", "Merchant1")
trie.insert("234567", "Merchant2")

exists, merchants = trie.search("234566")
print(f"Exists: {exists}, Served by: {merchants}")  # True, {"Merchant1"}

exists, merchants = trie.search("234567")
print(f"Exists: {exists}, Served by: {merchants}")  # True, {"Merchant2"}

exists, merchants = trie.search("234569")
print(f"Exists: {exists}, Served by: {merchants}")  # True, {"Merchant2"}

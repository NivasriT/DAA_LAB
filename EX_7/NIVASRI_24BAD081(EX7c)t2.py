# Task 2: Build Huffman Tree and Generate Codes
print("NIVASRI T | 24BAD081")
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    heap = []
    for ch, freq in frequency.items():
        heapq.heappush(heap, Node(ch, freq))
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]
# Generate Huffman Codes
def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes

text = "BEEP BOOP BEER"

root = build_huffman_tree(text)
codes = generate_codes(root)
print("Huffman Codes:")
for ch in codes:
    print(f"{ch}: {codes[ch]}")

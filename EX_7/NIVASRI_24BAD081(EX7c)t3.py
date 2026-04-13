import heapq
print("NIVASRI T | 24BAD081")
text = "BEEP BOOP BEER"

# Count frequency
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

# Build heap (freq, count, node)
heap = []
count = 0

for ch, freq in frequency.items():
    heapq.heappush(heap, (freq, count, ch))
    count += 1

# Build Huffman Tree
while len(heap) > 1:
    f1, c1, left = heapq.heappop(heap)
    f2, c2, right = heapq.heappop(heap)

    heapq.heappush(heap, (f1 + f2, count, (left, right)))
    count += 1

# Generate codes
codes = {}

def generate(node, code=""):
    if isinstance(node, str):
        codes[node] = code
        return
    generate(node[0], code + "0")
    generate(node[1], code + "1")

generate(heap[0][2])

# ASCII bits
ascii_bits = len(text) * 8

# Huffman bits
huffman_bits = sum(len(codes[ch]) for ch in text)

# Space saved %
space_saved = ((ascii_bits - huffman_bits) / ascii_bits) * 100

print("ASCII Bits:", ascii_bits)
print("Huffman Bits:", huffman_bits)
print("Space Saved (%):", round(space_saved, 2))

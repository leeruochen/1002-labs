class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # flat array to store nodes
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, l, r):
        """Build tree[node] for range l to r"""
        if l == r:
            # Leaf node
            self.tree[node] = arr[l]
        else:
            mid = (l + r) // 2
            # Build left child
            self._build(arr, 2*node + 1, l, mid)
            # Build right child
            self._build(arr, 2*node + 2, mid + 1, r)
            # Internal node stores sum of children
            self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]

    def query_sum(self, ql, qr):
        return self._query_sum(0, 0, self.n - 1, ql, qr)

    def _query_sum(self, node, l, r, ql, qr):
        # No overlap
        if qr < l or ql > r:
            return 0
        # Total overlap
        if ql <= l and r <= qr:
            return self.tree[node]
        # Partial overlap
        mid = (l + r) // 2
        left_sum = self._query_sum(2*node + 1, l, mid, ql, qr)
        right_sum = self._query_sum(2*node + 2, mid + 1, r, ql, qr)
        return left_sum + right_sum
    
prices = [10, 20, 30, 40, 50]  # example stock close prices
st = SegmentTree(prices)

# Query sum from index 1 to 3 → 20+30+40 = 90
print(st.query_sum(1, 3))  # Output: 90
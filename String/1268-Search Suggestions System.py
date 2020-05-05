class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            ans.append(products[:3])
        
        return ans
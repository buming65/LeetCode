class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        result = []
        def track(now, next_number):
            if not next_number:
                result.append(now)
            else:
                for letter in number[next_number[0]]:
                    track(now + letter, next_number[1:])
        if digits:
            track("", digits)
        return result
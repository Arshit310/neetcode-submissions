class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(stri, opn, cls):
            if len(stri) == n*2:
                res.append(stri)
                return
            if opn<n:  
                backtrack(stri+"(", opn+1, cls)
            if cls<opn:
                backtrack(stri+")", opn, cls+1)
        if n == 0:
            return('[]')
        else:
            backtrack("", 0, 0)
            return res
        
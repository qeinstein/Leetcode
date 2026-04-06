class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        no_cols = n // rows
        
        res = []

        for start_col in range(no_cols):

            curr_idx = start_col
            

            while curr_idx < n:
                res.append(encodedText[curr_idx])
                
                curr_idx += (no_cols + 1)

                if len(res) % rows == 0: # Optional safety but while/rows is better
                    break

        return "".join(res).rstrip()

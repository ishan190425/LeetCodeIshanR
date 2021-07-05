class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = 0
        a = 0
        l = 0
        o = 0
        n = 0
        for c in text:
            if c == 'b':
                b += 1
            elif c == 'a':
                a += 1
            elif c == 'l':
                l += 1
            elif c == "o":
                o += 1
            elif c == "n":
                n += 1
                    
        count = 0

        while True:
            d = 0
            if b  >= 1:
                b -= 1
                d += 1
            if a >= 1:
                a -= 1
                d +=1
            if l >= 2:
                l -= 2
                d +=2
            if o >= 2:
                o -= 2
                d +=2
            if n >= 1:
                n -= 1
                d += 1
            if d == 7:
                count += 1
            else:
                break
        
        return count

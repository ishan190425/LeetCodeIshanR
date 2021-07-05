class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        count = 0
        for i in emails:
            z = i.index("@")
            l = list(i[0:z])
            while l.count(".") is not 0:
                l.remove(".")
            
            if "+" in l:
                pl = l.index("+")
                l = l[0:pl]
                
            final_email = str(l) + i[z:]
            
            if final_email not in d:
                d[final_email] = 0
                count += 1
        return count
        

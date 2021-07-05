class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        commands = []
        arguments = []
        for i in range(len(expression)):
            temp = expression[i]
            
            if temp == "!" or temp == "|" or temp == "&":
                commands.append(temp)
              
            elif temp == ')':
                c = commands.pop()
                su = False if arguments.pop() == "f" else True
                ctemp = arguments.pop()
                if ctemp == "(":
                    if c == "!":
                        su = not su
                while ctemp is not "(":
                    s = False if ctemp == "f" else True
                    if c == "|":
                        su = su or s
                    elif c == "&":
                        su = su and s
                    else:
                        su = not su
                    ctemp = arguments.pop()
                if su == True:
                    arguments.append("t")
                else:
                    arguments.append("f")
            elif temp == ",":
                    continue
            else: 
                arguments.append(temp)
                
        if arguments[0] == "f":
            return False
        else:
            return True

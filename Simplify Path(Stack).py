class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        organized = path.split("/")
        for i in organized:
            if i!="" and i!="." and i!="..":
                stack.append(i)
            elif stack!=[] and i== "..":
                stack.pop()
        print(stack)
        
        for i in range(1,len(stack)):
            stack[i]="/"+stack[i]
        return "/"+ "".join(stack)
            
        

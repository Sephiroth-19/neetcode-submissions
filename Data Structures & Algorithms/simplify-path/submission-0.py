class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        space = path.split('/')
        for i in space:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)
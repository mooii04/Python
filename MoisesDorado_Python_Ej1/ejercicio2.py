def check_balance(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

print(check_balance("{ [ a * ( c + d ) ] - 5 }"))  # True
print(check_balance("{ a * ( c + d ) ] - 5 }"))  # False
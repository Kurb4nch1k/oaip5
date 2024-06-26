def brackets(text):
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    for char in text:
        if char in brackets:
            stack.append(brackets[char])
        elif char in brackets.values():
            if stack and stack[-1] == char:
                stack.pop()
            else:
                return False
    return not stack

text = '([{}])()<{}>'
print(brackets(text))

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        item = self.stack.pop()
        if item == self.max_stack[-1]:
            self.max_stack.pop()
        return item

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]
    
#TASK 2:

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.isEmpty():
        reversed_string += stack.pop()
    
    return reversed_string

#TASK 3:

def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(int(operand1 / operand2))

    return stack.pop()


#TASK 4:
    

def is_balanced(expression):
    stack = Stack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.isEmpty() or stack.pop() != matching_brackets[char]:
                return False

    return stack.isEmpty()


#TASK 5:

def prefix_to_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/', '^'])

    # Split the expression into tokens and reverse it
    tokens = expression.split()[::-1]

    for token in tokens:
        if token not in operators:
            # If the token is an operand, push.
            stack.push(token)
        else:
            # If the token is an operator, pop two operands
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Combine the operands and operator in postfix form
            new_expr = operand1 + ' ' + operand2 + ' ' + token
            # Push the result back to the stack
            stack.push(new_expr)

    # The final element of the stack: postfix expression
    return stack.pop()


#TASK 6:

def sort_stack(original_stack):
    aux_stack = Stack()

    while not original_stack.isEmpty():
        # Pop the top element from the original stack
        temp = original_stack.pop()

        # While auxiliary stack is not empty and the top element of auxiliary stack is greater than temp
        while not aux_stack.isEmpty() and aux_stack.peek() > temp:
            # Pop from auxiliary stack and push it back to the original stack
            original_stack.push(aux_stack.pop())

        aux_stack.push(temp)

    # Transfer from auxiliary stack to original stack
    while not aux_stack.isEmpty():
        original_stack.push(aux_stack.pop())

    return original_stack


#TASK 7:

def infix_to_postfix(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    stack = Stack()
    output = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():  # If the token is an operand  
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop() # Pop the '(' from stack
        else:   # The token is an operator
            while (not stack.isEmpty() and precedence(stack.peek()) >= precedence(token)):
                output.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        output.append(stack.pop())

    return ' '.join(output)

#TASK 8:

def daily_temperatures(temperatures):
    # Initialize the result list with zeros
    result = [0] * len(temperatures)
    stack = []

    for i, current_temp in enumerate(temperatures):
        # While stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack
        while stack and current_temp > temperatures[stack[-1]]:
            # Pop the index from the stack
            previous_index = stack.pop()
            # Calculate the number of days until a warmer temperature
            result[previous_index] = i - previous_index
        # Push the current index onto the stack
        stack.append(i)

    return result



#TASK 9:

def longest_valid_parentheses(s):
    stack = [-1]  # Initialize stack with -1 to handle the base case
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push the index of the '(' onto the stack
        else:
            stack.pop()  # Pop the last index
            if not stack:
                stack.append(i)  # Push the current index as a base for the next valid substring
            else:
                max_length = max(max_length, i - stack[-1])  # Updating the max_length

    return max_length


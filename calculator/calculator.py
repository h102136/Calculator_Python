import re

class Calculator:
    
    # constructor, initialize the expression when an object is created
    def __init__(self):
        self.expression = "" # initialize the expression to an empty string

    # method to get the expression from the user
    def get_expression(self):
        # get the expression from the user with limited operators
        while True:
            self.expression = input("Enter an expression ex:(7+8.5)*5-9/3 (+, -, *, / only) or Q for quit: ")
            
            # check if the user wants to quit
            if self.expression.upper() == "Q":
                exit()
            if self.validate_expression():
                return self.expression

    # check if the expression is valid with limited operators
    def validate_expression(self):
        # define the valid characters (0-9, ., +, -, *, /, (, ))
        valid_chars = re.compile(r'^[\d\.\+\-\*\/\(\)]+$')
        # define the pattern for consecutive operators
        consecutive_operators = re.compile(r'[\+\-\*\/]{2,}')

        # if the expression contains invalid characters, will ask the user to re-enter the expression
        if not valid_chars.match(self.expression):
            print("The expression contains invalid characters")
            return False

        # if the expression contains consecutive operators, return False
        if consecutive_operators.search(self.expression):
            print("The expression contains consecutive operators")
            return False

        return True

    # the function is for re-initialize the expression and ask the user to re-enter the expression
    def reinitialize(self):
        self.expression = ""
        self.get_expression()

        # if the expression is still invalid, will ask the user to re-enter the expression
        if not self.validate_expression():
            self.reinitialize()

    # evaluate the expression
    def evaluate_expression(self):

        # parse the expression
        def parse_expression(expression):

            def apply_operator(operators, values):
                operator = operators.pop() # get the last operator in "operators" list
                right = values.pop() # get the last value in "values" list as "right"
                left = values.pop() # get the last value in "values" list as "left" after removing the last value as "right"
                
                # apply the operator to "left" and "right" and append the result to "values" list
                if operator == '+':
                    values.append(left + right)
                elif operator == '-':
                    values.append(left - right)
                elif operator == '*':
                    values.append(left * right)
                elif operator == '/':
                    values.append(left / right)

            operators = []
            values = []
            i = 0 # index of the expression

            while i < len(expression):
                # if the character is a digit or a dot, parse the number
                if expression[i].isdigit() or expression[i] == '.':
                    number = ''
                    while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                        number += expression[i]
                        i += 1
                    values.append(float(number))
                    i -= 1 # decrement the index by 1 to avoid skipping the next character after the number
                elif expression[i] in "+-*/":
                    # ensure that * and / are processed before + and -
                    while (operators and operators[-1] in "*/" and expression[i] in "+-") or (operators and operators[-1] in "*/" and expression[i] in "*/"):
                        apply_operator(operators, values)
                    operators.append(expression[i])
                # handling parentheses' precedence in expressions    
                elif expression[i] == '(':
                    operators.append(expression[i])
                elif expression[i] == ')':
                    while operators[-1] != '(':
                        apply_operator(operators, values)
                    operators.pop()
                i += 1

            while operators:
                apply_operator(operators, values)

            return values[0]

        return parse_expression(self.expression)

if __name__ == "__main__":
    calc = Calculator()
    while True:
        calc.get_expression()
        if not calc.validate_expression():
            calc.reinitialize()
        else:
            result = calc.evaluate_expression()
            print(f"The result of the expression is: {result}")
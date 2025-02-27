# Py2Js - Convert Python code to JavaScript code.
# Adolfo GM - 2025

import re

class Py2Js:
    def __init__(self, python_code):
        self.python_code = python_code
        self.js_code = []
        self.indent_stack = [0]

    def convert(self):
        '''
        ## Convert
          This method converts Python code to JavaScript code. 
        '''
        python_lines = self.python_code.split("\n")
        
        for line in python_lines:
            line = line.replace("math.pi", "3.14159")
            stripped_line = str(line.strip())
            indent_level = len(line) - len(stripped_line)

            while indent_level < self.indent_stack[-1]:
                self.js_code.append("}")
                self.indent_stack.pop()

            if not stripped_line:
                self.js_code.append("")
                continue

            elif "print(" in stripped_line:
                stripped_line = re.sub(r"\bprint\s*\(", "console.log(", stripped_line)

            elif re.match(r"^\w+\s*=\s*.*", stripped_line):
                stripped_line = "let " + stripped_line

            elif re.match(r"^for\s+\w+\s+in\s+range\(\d+\):", stripped_line):
                match = re.match(r"^for\s+(\w+)\s+in\s+range\((\d+)\):", stripped_line)
                var, limit = match.groups()
                stripped_line = f"for (let {var} = 0; {var} < {limit}; {var}++) {{"
                self.indent_stack.append(indent_level + 4)
            else:
                stripped_line = "// " + stripped_line

            self.js_code.append(stripped_line)

        while len(self.indent_stack) > 1:
            self.js_code.append("}")
            self.indent_stack.pop()

        return "\n".join(self.js_code)

if __name__ == "__main__":
    python_code = '''
import math 
print("hello")
x = 5
print(x)
b = 5
for b in range(5):
    print(b)
print(math.pi)
'''
    converter = Py2Js(python_code)
    js_output = converter.convert()
    
    with open("output.js", "w") as js_file:
        js_file.write(js_output)

    print(js_output)
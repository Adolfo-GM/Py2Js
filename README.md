# Py2Js - Convert Python to JavaScript  

Py2Js is a simple Python script that converts basic Python code to JavaScript, handling variable assignments, print statements, and basic loops. It replaces `print()` with `console.log()`, converts `for` loops using `range()`, and transforms `math.pi` into its numerical value. While not a full-fledged transpiler, it provides a quick and lightweight way to transition simple Python scripts to JavaScript.  

### Example usage

```python
from py2js import Py2Js

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
```

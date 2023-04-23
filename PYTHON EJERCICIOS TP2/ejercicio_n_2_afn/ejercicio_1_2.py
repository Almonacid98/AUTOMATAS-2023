import re

class Afn:
    def __init__(self, pattern):
        self.pattern = pattern
        
    def read_in(self, input_string):
        return bool(re.match(self.pattern, input_string))

pattern = r'^(aa|b)*(a|bb)*$'
in_str = str(input("Enter the corresponding character: "))
automation = Afn(pattern)
print(automation.read_in(in_str))
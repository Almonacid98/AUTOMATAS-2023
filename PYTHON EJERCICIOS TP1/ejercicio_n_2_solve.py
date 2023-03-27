def solve(operation):
    numbers = []
    operators = []
    current_number = ""
    out = []
    sum = 0
    for x in operation:
        if x.isdigit():
            current_number += x
        else:
            numbers.append(int(current_number))
            current_number = ""
            operators.append(x)
    numbers.append(int(current_number))
    result = numbers[0]
    print(numbers)
    print(operators)
    for i in range(1, len(numbers)):
        if operators[i-1] == "*":
            result = numbers[i-1] * numbers[i]
            numbers.pop(i)
            numbers.pop(i-1)
    operators.remove("*")
    out.append(result)

    for i in range(1, len(numbers)):
        if operators[i-1] == "+":
            sum = numbers[i-1] + numbers[i] + out[0]

    print(out)
 
    print(numbers)
    print(operators)
    return sum
                        
operation = input("Enter an operation with addition and multiplication: ")
print(solve(operation))
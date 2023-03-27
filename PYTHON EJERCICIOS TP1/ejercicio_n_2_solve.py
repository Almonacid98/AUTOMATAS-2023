def solve(operation):
    numbers = []
    operators = []
    current_number = ""
    for char in operation:
        if char.isdigit():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ""
            operators.append(char)
    numbers.append(int(current_number))
    result = numbers[0]
    print(numbers)
    print(operators)
    for i in range(1, len(numbers)):
            if operators[i-1] == "*":
                result *= numbers[i]
                print(result)
            if operators[i-1] == "+":
                result += numbers[i]
                print(result)
    return print(result)
                        
operation = input("Ingrese una operacion con sumas y multiplicacion: ")
solve(operation)
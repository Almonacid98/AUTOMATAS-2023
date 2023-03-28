def multiplication(multiplicator):
    mul = multiplicator
    l_mul = mul.split("*")
    l_mul = [int(x) for x in l_mul]
    mul_result = 1
    for element in l_mul:
        mul_result *= element
    return mul_result
def solve(operation):
    operation = operation.replace(" ","")
    op_list = operation.split("+")
    mult = 0
    for i in range(0, len(op_list)):
        elemnt = op_list[i]
        if "*" in elemnt:
            mult = elemnt
            result = multiplication(mult)
            op_list[i] = result
        else:
            pass
    op_list = [int(x) for x in op_list]
    final_result = sum(op_list)
    print("The final result is: ", final_result)
cad = str(input("..."))
solve(cad)
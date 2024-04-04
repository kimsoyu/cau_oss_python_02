# %% Homework #2

# 사용자에게 연산방법을 문자열로 입력을 받은 후
# 정수 2개를 입력받아 연산을 수행하는 프로그램

def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2
    

while True:
    op = input("input operation:")
    if op == "end":
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x, y: x*y)
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x, y: x/y)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x, y: x%y)
    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}")

print("Exit program")
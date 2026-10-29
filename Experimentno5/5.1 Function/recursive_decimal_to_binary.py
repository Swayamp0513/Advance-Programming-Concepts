def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)




num = int(input("Enter decimal number: "))
print("Binary representation:", decimal_to_binary(num))
 
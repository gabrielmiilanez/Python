num = int(input("Digite um numero: "))

if num % 2 != 0:
    print(f"O numero {num} é impar. Weird")
else:
    if 2 <= num <= 5:
        print(f"O numero {num} é par e entre 2 e 5. Not Weird")
    elif 6 <= num <= 20:
        print(f"O numero {num} é par e entre 6 e 20. Weird")
    else:
        print(f"O numero {num} é par e maior que 20. Not Weird")


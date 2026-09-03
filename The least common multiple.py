#Алгоритм Евклида для поиска НОД.
def gcd(a, b): 
    while b != 0:
        a, b = b, a % b
    return a

#Наименьшее общее кратное через НОД.
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

#Запрашивает число, пока не будет введено положительное.
def get_positive_number(prompt):
    """Запрашивает число, пока не будет введено положительное."""
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("Ошибка: число должно быть положительным. Попробуйте снова.")
                continue
            return num
        except ValueError:
            print("Ошибка: введите целое число.")

# Основная часть

num1 = get_positive_number("Введите первое число: ")
num2 = get_positive_number("Введите второе число: ")

result = lcm(num1, num2)
print(f"Наименьшее общее кратное чисел {num1} и {num2} равно {result}")

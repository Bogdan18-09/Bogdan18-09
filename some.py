# Функция для подсчёта количества цифр в строке
def count_digits(s):
    return sum(1 for char in s if char.isdigit())

# Ввод данных
N = int(input("Введите количество слов: "))
words = [input(f"Введите слово {i + 1}: ") for i in range(N)]

# Сортировка массива по количеству цифр в строке
sorted_words = sorted(words, key=count_digits)

# Вывод результата
print("Отсортированный массив:")
for word in sorted_words:
    print(word)
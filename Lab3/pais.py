def find_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                pairs.append((numbers[i], numbers[j]))
    return pairs

# Задана колекція чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Знаходження та друк пар чисел, сума яких дорівнює 10
result = find_pairs(numbers)
for pair in result:
    print(pair)

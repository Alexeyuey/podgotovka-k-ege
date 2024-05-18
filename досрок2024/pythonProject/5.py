def calculate_R(N):
    N_str = str(N)  # Преобразуем число в строку для удобства обработки

    triplets = []  # Список для хранения троек соседних цифр
    for i in range(len(N_str) - 2):
        # Получаем тройку соседних цифр и преобразуем в число
        triplet = int(N_str[i:i+3])
        # Добавляем тройку в список
        triplets.append(triplet)

    # Находим наибольшее и наименьшее число из списка троек
    max_triplet = max(triplets)
    min_triplet = min(triplets)

    R = max_triplet - min_triplet

    return R

def find_min_N_for_R(target_R):
    # Начинаем проверку с наименьшего N, равного 100
    N = 100
    while True:
        R = calculate_R(N)
        if R == target_R:
            return N
        N += 1

# Ищем наименьшее N для R = 415
min_N_for_R_415 = find_min_N_for_R(415)
print("Наименьшее значение N для R = 415:", min_N_for_R_415)

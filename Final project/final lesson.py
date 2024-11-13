import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  
    a = list(range(1, 101)) # создание списка
        
    # индексы первого элемента, последнего и среднего
    low = 0
    high = len(a) - 1
    mid = len(a) // 2
    
    while a[mid] != number:
        count += 1
        if number > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)    
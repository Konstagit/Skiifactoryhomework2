import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
   # Мы можем улучшить  метод, используя бинарный поиск, который делит диапазон возможных значений пополам на каждой итерации.
    count = 0
    low = 1
    high = 100
    predict = 0
    
    while predict != number:
        count += 1
        predict = (low + high) // 2  # Предсказываем середину диапазона
        if predict < number:
            low = predict + 1  # Сужаем диапазон, если предсказанное число меньше
        elif predict > number:
            high = predict - 1  # Сужаем диапазон, если предсказанное число больше

    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
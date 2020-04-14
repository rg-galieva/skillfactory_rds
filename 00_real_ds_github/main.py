import numpy as np

# VERSION ONE
def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали


# VERSION TWO
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали


# FINAL VERSION: Binary search
def game_core(randomNumber, predictionList = range(1, 101)):
    counter = 0
    first = predictionList[0]
    last = predictionList[-1]
    
    while first <= last:
        counter += 1
        midpoint = (first + last) // 2

        # Check if randomNumber is present at mid 
        if randomNumber == predictionList[midpoint]:        
            break 
        # If randomNumber is greater than mid value, ignore left half 
        elif randomNumber > predictionList[midpoint]:
            first = midpoint + 1
        # If randomNumber is greater, ignore right half 
        else:
            last = midpoint - 1

    return counter

# GAME
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# GAME TEST
score_game(game_core_v1) # => 101
score_game(game_core_v2) # => 33
score_game(game_core) # => 5
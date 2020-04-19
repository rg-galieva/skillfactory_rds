import numpy as np

# Game
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


# Example from the task: version one
def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали


# Example from the task: version two
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


# Solution
def game_core(targetValue, predictionList=range(1, 101)):
    '''Find targetValue in a given predictionList with minimum number of attempts.

        Divide and conquer by using binary search algorithm:
        - Create sorted predictionList with numbers from 1 to 100
        - Split predictionList into two halves
        - Compare the target value to the middle element of the predictionList
            If they are not equal, the half in which the target cannot lie is eliminated 
            and the search continues on the remaining half
        - After each iteration narrow down the predictionList by excluding already checked values
        - Repeat until the target value is found.

        Returns the number of iterations required to find targetValue.
    '''
    count = 0
    left_edge = predictionList[0]
    right_edge = predictionList[-1]
    
    while left_edge <= right_edge:
        count += 1
        midpoint = (left_edge+right_edge) // 2

        # Check if targetValue is present at mid 
        if targetValue == predictionList[midpoint]:        
            break
        # If targetValue is greater than mid value, ignore left half 
        elif targetValue > predictionList[midpoint]:
            left_edge = midpoint + 1
        # If targetValue is greater, ignore right half 
        else:
            right_edge = midpoint - 1

    return count

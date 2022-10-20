'''Game Guess the number'''

import numpy as np


def optimal_predict(number: int = 1) -> int:
    '''Game: the computer guesses the number in less than 20 attempts'''

    import numpy as np

    min = 1
    max = 101

    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
        mid = (min+max) // 2
    
        if mid > number:
          max = mid
    
        elif mid < number:
          min = mid

        else:
            print(f"he computer guessed the number in {count} attempts. this number {number}")
            break #end game exit loop
    return count
  
def score_game(random_predict) -> int:
    """For what number of attempts on average for 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average for:{score} attempts")
    return score
  
 
 

if __name__ == "__main__":
    # RUN
    score_game(optimal_predict)
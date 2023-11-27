import time  # Import the time module

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Introduce a delay of one second
        number -= 1
    print('HAPPY NEW YEAR!')

# Example usage:
# countdown(10)  # Will print without a delay
countdown_with_sleep(10)  # Will print with a delay of one second between each iteration

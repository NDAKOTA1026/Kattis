import math

def bank_robbery(file: str) -> int:
    """
    Solution to bank robbery
    """
    input_file = open(file, 'r')
    data = input_file.read().splitlines()
    first_line_data = data[0].split()
    low, high = first_line_data[1] , first_line_data[-1]
    
    count = 0
    for i in data[-1].split():
        if (i < high and i > low):
            count += 1
    return count

def cutting_carrot(n: int, h: int):
    """
    Solution to cutting carrot
    """
    for i in range(1, n):
        print(h * math.sqrt(i / n), end = ' ')


def naming_company(oleg_str: str, igor_str: str) -> str:
    result = ''
    oleg_list = sorted(i for i in oleg_str)
    igor_list = sorted((j for j in igor_str), reverse = True)
    
    for i in range(len(oleg_str)):
        if i % 2 == 0:
            result += oleg_list[int(i / 2)]
        else:
            result += igor_list[int((i - 1) /2)]
    return result
    
def labelling_cities():
    """
    Solution to labelling cities
    """
    pass







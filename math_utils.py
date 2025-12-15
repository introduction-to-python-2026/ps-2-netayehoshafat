def find_max_number(num1, num2, num3):
    max_num = None
    if num1 > num2:
        if num1 > num3:
            max_num = num1
        else:
            max_num = num3
    else:
        if num2 > num3:
            max_num = num2
        else:
            max_num = num3
    return max_num

def find_mean(num1, num2, num3):
    mean_num = (num1 + num2 + num3) / 3
    return mean_num

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = ((((num1 - mean) ** 2) + ((num2 - mean) ** 2) + ((num3 - mean) ** 2)) / 3) ** 0.5
    return mean, std


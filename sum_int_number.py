def sum_int_number(number):
    try:
        sum_result = sum(range(number + 1))
    except TypeError:
        sum_result = 0
    return sum_result

if __name__ == "__main__":
    print(sum_int_number(10))

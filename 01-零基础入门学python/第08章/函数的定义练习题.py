def sum_numbers(number):
    """
    实现1-number之间，所有数字的加和
    :param number:数字
    :return:加和结果
    """
    sum_value = 0
    for i in range(1,number+1):
        sum_value += i
    print(number,"加和的结果是：",sum_value)

sum_numbers(100)
sum_numbers(10)

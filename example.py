arr = [2, 4, 6, 8]
result_arr = []

def func1(a):
    print('I am A')
    
    add_first = a + 5
    multiply_second = add_first * 3
    
    return multiply_second

def func2(a):
    print('I am B')
    
    multiply_first = a * 3
    add_second = multiply_first + 5
    
    return add_second


for ele in arr:
    result_1 = func1(ele)
    result_2 = func2(ele)
    result_arr.append(result_1)
    result_arr.append(result_2)
    
print(sum(result_arr))
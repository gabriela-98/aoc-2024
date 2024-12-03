import re
from data import data

def find_mul(mul_data):
    pattern = r'mul\((\d+),\s*(\d+)\)'
    mul_list = []
    matches = re.findall(pattern, mul_data)
    for m in matches:
        num1, num2 = map(int, m)
        mul_list.append(num1 * num2)

    return mul_list

result = find_mul(data)
data_sum = sum(result)

print(data_sum)
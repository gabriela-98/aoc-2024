from data import data

data = data.split("\n")
result = [list(map(int, i.split())) for i in data]

count_a = 0
count = 0

def is_valid_report(res_data):
    level = None
    for i in range(len(res_data) - 1):
        diff = abs(res_data[i] - res_data[i + 1])
        current = ['increase' if res_data[i + 1] > res_data[i] else 'decrease' if res_data[i + 1] < res_data[i] else None]

        if level is None:
            level = current
        elif level != current:
            return False

        if diff == 0 or diff > 3:
            return False
    return True



def is_valid_after_removal(res_data):
    for i in range(len(res_data)):
        new_report = res_data[:i] + res_data[i + 1:]
        if is_valid_report(new_report):
            return True
    return False


for res in result:
    if is_valid_report(res):
        count_a += 1
    if is_valid_report(res) or is_valid_after_removal(res):
        count += 1

print("Safe reportsA:", count_a)
print("Safe reports:", count)

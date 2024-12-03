import re
from data import data


matches = re.findall(r"mul\((\d+),\s*(\d+)\)", data)
skip_mul = re.findall(
            r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data
        )

result_a = sum(int(x) * int(y) for x, y in matches)
print(result_a)

result_b = sum(int(x) * int(y)
               for match in skip_mul
               if (flag := (match == "do()") or (match != "don't()" and globals().get("flag", True))) and match.startswith("mul(")
               for x, y in [match[4:-1].split(",")])
print(result_b)
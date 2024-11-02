"""
Примитивный калькулятор.

У вас есть примитивный калькулятор, который умеет выполнять всего 3 операции с текущим числом x:
заменить x на 2x, 3x или x+1. По данному целому числу 1<=n<=10^5 определите минимальное число
операций k, необходимое, чтобы получить n из 1.
Выведите k и последовательных промежуточных чисел.
"""


def min_operations_calc(n):
    ops_count = [0, 0]
    prev_nums = [0, 1]
    for i in range(2, n + 1):
        prev_num1, prev_num2, prev_num3 = i // 2, i // 3, i - 1
        op1 = ((ops_count[prev_num1] + 1) if i % 2 == 0 else n, prev_num1)
        op2 = ((ops_count[prev_num2] + 1) if i % 3 == 0 else n, prev_num2)
        op3 = (ops_count[prev_num3] + 1, prev_num3)

        min_op = min(op1, op2, op3, key=lambda op: op[0])
        ops_count.append(min_op[0])
        prev_nums.append(min_op[1])

    nums = [n]
    num = n
    while num > 1:
        num = prev_nums[num]
        nums.append(num)

    return ops_count[-1], reversed(nums)


def run():
    n = int(input())
    ops_count, nums = min_operations_calc(n)
    print(ops_count)
    print(*nums)


if __name__ == "__main__":
    run()

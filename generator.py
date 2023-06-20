import random


# convert desimal to binary
def des_to_bin(des):
    return bin(int(des))[2:]


def des_to_bin_float(num: float, presision=10):
    des = ""
    f = num
    if num >= 1:
        w = int(num)
        des += des_to_bin(w)
        des += "."
        f = num - w

    for i in range(presision):
        if f == 0:
            break
        f *= 2
        if f >= 1:
            des += "1"
            f -= 1
        else:
            des += "0"

    return des


# des to binary problem
def des_to_bin_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nConvert these desimal to binary\n")
    solution.write("\nConvert these desimal to binary\n")
    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        problem.write(f"{i}. {rnd}\n")
        solution.write(f"{i}. {rnd} -> {des_to_bin(rnd)}\n")


# convert binary to desimal
def bin_to_des_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nConvert these binary to desimal\n")
    solution.write("\nConvert these binary to desimal\n")
    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        problem.write(f"{i}. {des_to_bin(rnd)}\n")
        solution.write(f"{i}. {des_to_bin(rnd)} -> {rnd}\n")


# binary sum problem
def bin_sum_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nAdd these binary numbers\n")
    solution.write("\nAdd these binary numbers\n")

    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        rnd2 = random.randint(range_start, range_end)
        problem.write(f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)}\n")

        sum = rnd + rnd2

        solution.write(
            f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)} = \
            {des_to_bin(sum)}\n"
        )


# binary sub problem
def bin_sub_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nSubtract these binary numbers\n")
    solution.write("\nSubtract these binary numbers\n")

    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        rnd2 = random.randint(range_start, range_end)

        while rnd == rnd2:
            rnd2 = random.randint(range_start, range_end)

        if rnd < rnd2:
            rnd, rnd2 = rnd2, rnd

        problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")

        sub = rnd - rnd2

        solution.write(
            f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
            {des_to_bin(sub)}\n"
        )


# binary mul problem
def bin_mul_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nMultiply these binary numbers\n")
    solution.write("\nMultiply these binary numbers\n")
    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        rnd2 = random.randint(5, 15)
        problem.write(f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)}\n")
        mul = rnd * rnd2
        solution.write(
            f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)} = \
            {des_to_bin(mul)}\n"
        )


def bin_div_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=20,
):
    problem.write("\nDivide these binary numbers\n")
    solution.write("\nDivide these binary numbers\n")
    for i in range(count + 1):
        rnd1 = random.randint(range_start, range_end)
        rnd2 = random.randint(5, 15)

        while rnd1 % rnd2 != 0:
            rnd1 = random.randint(range_start, range_end)

        problem.write(f"{i}. {des_to_bin(rnd1)} / {des_to_bin(rnd2)}\n")
        div = rnd1 / rnd2
        solution.write(
            f"{i}. {des_to_bin(rnd1)} / {des_to_bin(rnd2)} = {div}\n",
        )


def twos_complement(num):
    binary = des_to_bin(num)
    length = len(binary)
    comp = 2**length - num
    return des_to_bin(comp)


def ones_complement(num):
    binary = des_to_bin(num)
    length = len(binary)
    comp = 2**length - num - 1
    return des_to_bin(comp)


# ones complement problem
def ones_complement_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nFind the 1's complement of these binary numbers\n")
    solution.write("\nFind the 1's complement of these binary numbers\n")
    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        problem.write(f"{i}. {des_to_bin(rnd)}\n")
        solution.write(f"{i}. {des_to_bin(rnd)} = {ones_complement(rnd)}\n")


# 2's complement problem
def twos_complement_problem(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nFind the 2's complement of these binary numbers\n")
    solution.write("\nFind the 2's complement of these binary numbers\n")
    for i in range(1, count + 1):
        rnd = random.randint(range_start, range_end)
        problem.write(f"{i}. {des_to_bin(rnd)}\n")
        solution.write(f"{i}. {des_to_bin(rnd)} = {twos_complement(rnd)}\n")


# sub using 2's complement
def twos_complement_sub(
    problem,
    solution,
    count=10,
    range_end=500,
    range_start=10,
):
    problem.write("\nSubtract these binary numbers using 2's complement\n")
    solution.write("\nSubtract these binary numbers using 2's complement\n")
    for i in range(1, count + 1):
        rnd1 = random.randint(range_start, range_end)
        rnd2 = random.randint(range_start, range_end)

        while rnd1 == rnd2:
            rnd2 = random.randint(range_start, range_end)

        if rnd1 < rnd2:
            rnd1, rnd2 = rnd2, rnd1

        problem.write(f"{i}. {des_to_bin(rnd1)} - {des_to_bin(rnd2)}\n")

        sub = rnd1 - rnd2

        solution.write(
            f"{i}. {des_to_bin(rnd1)} - {des_to_bin(rnd2)} =\
            {des_to_bin(sub)}\n"
        )


# floating point decimal to binary
def float_to_bin_prob(
    problem,
    solution,
    count=10,
    range_end=10,
    range_start=1,
):
    problem.write("\nConvert these floating point decimal numbers to binary\n")
    solution.write("\nConvert these floating point decimal numbers to binary\n")
    for i in range(1, count + 1):
        rnd = round(random.uniform(range_start, range_end), 2)
        problem.write(f"{i}. {rnd}\n")
        solution.write(f"{i}. {rnd} = {des_to_bin_float(rnd)}\n")


if __name__ == "__main__":
    des = input("Enter a hexadecimal number: ")
    print(des_to_bin(des))

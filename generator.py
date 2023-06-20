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
        f = num - w
        if f == 0:
            return des
        des += "."

    else:
        des += "0."

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


class Problem:
    def __init__(self, count=10, range_end=500, range_start=20):
        self.count = count
        self.range_end = range_end
        self.range_start = range_start

    def generate(self, problem, solution):
        pass


class DesToBinProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nConvert these desimal to binary\n")
        solution.write("\nConvert these desimal to binary\n")
        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")
            solution.write(f"{i}. {rnd} -> {des_to_bin(rnd)}\n")


class BinToDesProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nConvert these binary to desimal\n")
        solution.write("\nConvert these binary to desimal\n")
        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {rnd}\n")


class BinSumProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nAdd these binary numbers\n")
        solution.write("\nAdd these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)}\n")

            sum = rnd + rnd2

            solution.write(
                f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)} = \
                {des_to_bin(sum)}\n"
            )


class BinSubProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nSubtract these binary numbers\n")
        solution.write("\nSubtract these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)

            while rnd == rnd2:
                rnd2 = random.randint(self.range_start, self.range_end)

            if rnd < rnd2:
                rnd, rnd2 = rnd2, rnd

            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")

            sub = rnd - rnd2

            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )


class BinMulProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nMultiply these binary numbers\n")
        solution.write("\nMultiply these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(4, 8)
            problem.write(f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)}\n")

            mul = rnd * rnd2

            solution.write(
                f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)} = \
                {des_to_bin(mul)}\n"
            )


class BinDivProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nDivide these binary numbers\n")
        solution.write("\nDivide these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(5, 15)

            while rnd % rnd2 != 0:
                for i in range(10):
                    rnd2 = random.randint(5, 15)
                    if rnd % rnd2 == 0:
                        break
                if rnd % rnd2 == 0:
                    break
                rnd = random.randint(self.range_start, self.range_end)

            problem.write(f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)}\n")

            div = rnd / rnd2

            solution.write(
                f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)} = \
                {des_to_bin_float(div)}\n"
            )


class OnesComplementProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nFind the ones complement of these binary numbers\n")
        solution.write("\nFind the ones complement of these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")

            ones = ones_complement(rnd)

            solution.write(f"{i}. {des_to_bin(rnd)} -> {ones}\n")


class TwosComplementProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nFind the twos complement of these binary numbers\n")
        solution.write("\nFind the twos complement of these binary numbers\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")

            twos = twos_complement(rnd)

            solution.write(f"{i}. {des_to_bin(rnd)} -> {twos}\n")


class TowsComplementSubProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nSubtract these binary numbers using twos complement\n")
        solution.write("\nSubtract these binary numbers using twos complement\n")

        for i in range(1, self.count + 1):
            rnd = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)

            while rnd == rnd2:
                rnd2 = random.randint(self.range_start, self.range_end)

            if rnd < rnd2:
                rnd, rnd2 = rnd2, rnd

            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")

            sub = rnd - rnd2

            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )


class FloatToBinProblem(Problem):
    def generate(self, problem, solution):
        problem.write("\nConvert these floating point numbers to binary\n")
        solution.write("\nConvert these floating point numbers to binary\n")

        for i in range(1, self.count + 1):
            rnd = random.uniform(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")

            bin = des_to_bin_float(rnd)

            solution.write(f"{i}. {rnd} -> {bin}\n")

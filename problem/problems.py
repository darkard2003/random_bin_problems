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


def des_to_oct(des):
    return oct(int(des))[2:]


def eights_complement(num):
    octal = des_to_oct(num)
    length = len(octal)
    comp = 8**length - num
    return des_to_oct(comp)


def sevens_complement(num):
    octal = des_to_oct(num)
    length = len(octal)
    comp = 8**length - num - 1
    return des_to_oct(comp)


def des_to_hex(des):
    return hex(int(des))[2:]

def sixteens_complement(num):
    hexa = des_to_hex(num)
    length = len(hexa)
    comp = 16**length - num
    return des_to_hex(comp)

def fifteens_complement(num):
    hexa = des_to_hex(num)
    length = len(hexa)
    comp = 16**length - num - 1
    return des_to_hex(comp)


class Problem:
    header = ""

    def __init__(self, count=5, range_end=500, range_start=20):
        self.count = count
        self.range_end = range_end
        self.range_start = range_start

    def write_text(self, problem, solution):
        pass

    def write_md(self, problem, solution, header_index=0):
        pass


class DesToBinProblem(Problem):
    header = "Convert these desimal to binary"

    def write_text(self, problem, solution):
        problem.write(self.header)
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")
            solution.write(f"{i}. {rnd} -> {des_to_bin(rnd)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")
            solution.write(f"{i}. {rnd} -> {des_to_bin(rnd)}\n")

        problem.write("\n\n")


class BinToDesProblem(Problem):
    header = "Convert these binary to desimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these binary to desimal\n")
        solution.write("\nConvert these binary to desimal\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {rnd}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {rnd}\n")

        problem.write("\n\n")


class BinSumProblem(Problem):
    header = "Add these binary numbers"

    def get_numbers(self):
        rnd = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(self.range_start, self.range_end)
        sum = rnd + rnd2
        return rnd, rnd2, sum

    def write_text(self, problem, solution):
        problem.write("\nAdd these binary numbers\n")
        solution.write("\nAdd these binary numbers\n")

        for i in range(self.count):
            rnd, rnd2, sum = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)} = \
                {des_to_bin(sum)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd, rnd2, sum = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} + {des_to_bin(rnd2)} = \
                {des_to_bin(sum)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class BinSubProblem(Problem):
    header = "Subtract these binary numbers"

    def get_numbers(self):
        rnd = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(self.range_start, self.range_end)

        while rnd == rnd2:
            rnd2 = random.randint(self.range_start, self.range_end)

        if rnd < rnd2:
            rnd, rnd2 = rnd2, rnd

        sub = rnd - rnd2
        return rnd, rnd2, sub

    def write_text(self, problem, solution):
        problem.write("\nSubtract these binary numbers\n")
        solution.write("\nSubtract these binary numbers\n")

        for i in range(self.count):
            rnd, rnd2, sub = self.get_numbers()

            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd, rnd2, sub = self.get_numbers()

            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class BinMulProblem(Problem):
    header = "Multiply these binary numbers"

    def get_numbers(self):
        rnd = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(4, 8)
        mul = rnd * rnd2
        return rnd, rnd2, mul

    def write_text(self, problem, solution):
        problem.write("\nMultiply these binary numbers\n")
        solution.write("\nMultiply these binary numbers\n")

        for i in range(self.count):
            rnd, rnd2, mul = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)} = \
                {des_to_bin(mul)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd, rnd2, mul = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} * {des_to_bin(rnd2)} = \
                {des_to_bin(mul)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class BinDivProblem(Problem):
    header = "Divide these binary numbers"

    def get_numbers(self):
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

        div = rnd / rnd2
        return rnd, rnd2, div

    def write_text(self, problem, solution):
        problem.write("\nDivide these binary numbers\n")
        solution.write("\nDivide these binary numbers\n")

        for i in range(self.count):
            rnd, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)} = \
                {des_to_bin_float(div)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} / {des_to_bin(rnd2)} = \
                {des_to_bin_float(div)}\n"
            )
        problem.write("\n\n")
        solution.write("\n\n")


class OnesComplementProblem(Problem):
    header = "Find the ones complement of these binary numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the ones complement of these binary numbers\n")
        solution.write("\nFind the ones complement of these binary numbers\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            ones = ones_complement(rnd)

            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {ones}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            ones = ones_complement(rnd)

            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {ones}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class TwosComplementProblem(Problem):
    header = "Find the twos complement of these binary numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the twos complement of these binary numbers\n")
        solution.write("\nFind the twos complement of these binary numbers\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")

            twos = twos_complement(rnd)

            solution.write(f"{i}. {des_to_bin(rnd)} -> {twos}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")

            twos = twos_complement(rnd)

            solution.write(f"{i}. {des_to_bin(rnd)} -> {twos}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class TowsComplementSubProblem(Problem):
    header = "Subtract these binary numbers using twos complement"

    def get_numbers(self):
        rnd = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(self.range_start, self.range_end)

        while rnd == rnd2:
            rnd2 = random.randint(self.range_start, self.range_end)

        if rnd < rnd2:
            rnd, rnd2 = rnd2, rnd

        sub = rnd - rnd2

        return rnd, rnd2, sub

    def write_text(self, problem, solution):
        problem.write("\nSubtract these binary numbers using twos complement\n")
        solution.write("\nSubtract these binary numbers using twos complement\n")

        for i in range(self.count):
            rnd, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_bin(rnd)} - {des_to_bin(rnd2)} = \
                {des_to_bin(sub)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class FloatToBinProblem(Problem):
    header = "Convert these floating point numbers to binary"

    def write_text(self, problem, solution):
        problem.write("\nConvert these floating point numbers to binary\n")
        solution.write("\nConvert these floating point numbers to binary\n")

        for i in range(self.count):
            rnd = random.uniform(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")

            bin = des_to_bin_float(rnd)

            solution.write(f"{i}. {rnd} -> {bin}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.uniform(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")

            bin = des_to_bin_float(rnd)

            solution.write(f"{i}. {rnd} -> {bin}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class DesToOctProblem(Problem):
    header = "Convert these decimal numbers to octal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these decimal numbers to octal\n")
        solution.write("\nConvert these decimal numbers to octal\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")

            oct = des_to_oct(rnd)

            solution.write(f"{i}. {rnd} -> {oct}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd}\n")

            oct = des_to_oct(rnd)

            solution.write(f"{i}. {rnd} -> {oct}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class OctToDesProblem(Problem):
    header = "Convert these octal numbers to decimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these octal numbers to decimal\n")
        solution.write("\nConvert these octal numbers to decimal\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd)}\n")
            solution.write(f"{i}. {des_to_oct(rnd)} -> {rnd}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd)}\n")
            solution.write(f"{i}. {des_to_oct(rnd)} -> {rnd}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class OctToBinProblem(Problem):
    header = "Convert these octal numbers to binary"

    def write_text(self, problem, solution):
        problem.write("\nConvert these octal numbers to binary\n")
        solution.write("\nConvert these octal numbers to binary\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd)}\n")
            solution.write(f"{i}. {des_to_oct(rnd)} -> {des_to_bin(rnd)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd)}\n")
            solution.write(f"{i}. {des_to_oct(rnd)} -> {des_to_bin(rnd)}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class BinToOctProblem(Problem):
    header = "Convert these binary numbers to octal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these binary numbers to octal\n")
        solution.write("\nConvert these binary numbers to octal\n")

        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {des_to_oct(rnd)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd)}\n")
            solution.write(f"{i}. {des_to_bin(rnd)} -> {des_to_oct(rnd)}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class OctSumProblem(Problem):
    header = "Find the sum of these octal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the sum of these octal numbers\n")
        solution.write("\nFind the sum of these octal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)} + {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} + {des_to_oct(rnd2)} = {des_to_oct(rnd1 + rnd2)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)} + {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} + {des_to_oct(rnd2)} = {des_to_oct(rnd1 + rnd2)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class OctSubProblem(Problem):
    header = "Find the difference of these octal numbers"

    def get_numbers(self):
        rnd1 = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(self.range_start, self.range_end)
        if rnd1 < rnd2:
            rnd1, rnd2 = rnd2, rnd1
        sub = rnd1 - rnd2
        return rnd1, rnd2, sub

    def write_text(self, problem, solution):
        problem.write("\nFind the difference of these octal numbers\n")
        solution.write("\nFind the difference of these octal numbers\n")

        for i in range(self.count):
            rnd1, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_oct(rnd1)} - {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} - {des_to_oct(rnd2)} = {des_to_oct(sub)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_oct(rnd1)} - {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} - {des_to_oct(rnd2)} = {des_to_oct(sub)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class OctMulProblem(Problem):
    header = "Find the product of these octal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the product of these octal numbers\n")
        solution.write("\nFind the product of these octal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)} * {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} * {des_to_oct(rnd2)} = {des_to_oct(rnd1 * rnd2)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)} * {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} * {des_to_oct(rnd2)} = {des_to_oct(rnd1 * rnd2)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class OctDivProblem(Problem):
    header = "Find the quotient of these octal numbers"

    def get_numbers(self):
        rnd1 = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(5, 15)

        while rnd1 % rnd2 != 0:
            rnd1 = random.randint(self.range_start, self.range_end)
            for i in range(5, 15):
                if rnd1 % i == 0:
                    rnd2 = i
                    break


        div = rnd1 // rnd2
        return rnd1, rnd2, div

    def write_text(self, problem, solution):
        problem.write("\nFind the quotient of these octal numbers\n")
        solution.write("\nFind the quotient of these octal numbers\n")

        for i in range(self.count):
            rnd1, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_oct(rnd1)} / {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} / {des_to_oct(rnd2)} = {des_to_oct(div)}\n"
            )

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_oct(rnd1)} / {des_to_oct(rnd2)}\n")
            solution.write(
                f"{i}. {des_to_oct(rnd1)} / {des_to_oct(rnd2)} = {des_to_oct(div)}\n"
            )

        problem.write("\n\n")
        solution.write("\n\n")


class EightsCompProblem(Problem):
    header = "Find the 8's complement of these octal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the 8's complement of these octal numbers\n")
        solution.write("\nFind the 8's complement of these octal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {eights_complement(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {eights_complement(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class SevensCompProblem(Problem):

    header = "Find the 7's complement of these octal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the 7's complement of these octal numbers\n")
        solution.write("\nFind the 7's complement of these octal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {sevens_complement(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {sevens_complement(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexToDesProblem(Problem):
    header = "Convert these hexadecimal numbers to decimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these hexadecimal numbers to decimal\n")
        solution.write("\nConvert these hexadecimal numbers to decimal\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {rnd1}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {rnd1}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class DesToHexProblem(Problem):
    header = "Convert these decimal numbers to hexadecimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these decimal numbers to hexadecimal\n")
        solution.write("\nConvert these decimal numbers to hexadecimal\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd1}\n")
            solution.write(f"{i}. {rnd1} = {des_to_hex(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {rnd1}\n")
            solution.write(f"{i}. {rnd1} = {des_to_hex(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexToOctProblem(Problem):
    header = "Convert these hexadecimal numbers to octal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these hexadecimal numbers to octal\n")
        solution.write("\nConvert these hexadecimal numbers to octal\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {des_to_oct(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {des_to_oct(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class OctToHexProblem(Problem):
    header = "Convert these octal numbers to hexadecimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these octal numbers to hexadecimal\n")
        solution.write("\nConvert these octal numbers to hexadecimal\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {des_to_hex(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_oct(rnd1)}\n")
            solution.write(f"{i}. {des_to_oct(rnd1)} = {des_to_hex(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexToBinProblem(Problem):
    header = "Convert these hexadecimal numbers to binary"

    def write_text(self, problem, solution):
        problem.write("\nConvert these hexadecimal numbers to binary\n")
        solution.write("\nConvert these hexadecimal numbers to binary\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {des_to_bin(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} = {des_to_bin(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class BinToHexProblem(Problem):
    header = "Convert these binary numbers to hexadecimal"

    def write_text(self, problem, solution):
        problem.write("\nConvert these binary numbers to hexadecimal\n")
        solution.write("\nConvert these binary numbers to hexadecimal\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd1)}\n")
            solution.write(f"{i}. {des_to_bin(rnd1)} = {des_to_hex(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_bin(rnd1)}\n")
            solution.write(f"{i}. {des_to_bin(rnd1)} = {des_to_hex(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")


class HexSumProblem(Problem):
    header = "Add these hexadecimal numbers"

    def write_text(self, problem, solution):
        problem.write("\nAdd these hexadecimal numbers\n")
        solution.write("\nAdd these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)} + {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} + {des_to_hex(rnd2)} = {des_to_hex(rnd1 + rnd2)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)} + {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} + {des_to_hex(rnd2)} = {des_to_hex(rnd1 + rnd2)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexSubProblem(Problem):
    header = "Subtract these hexadecimal numbers"

    def get_numbers(self):
        rnd1 = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(self.range_start, self.range_end)

        if rnd1 < rnd2:
            rnd1, rnd2 = rnd2, rnd1

        sub = rnd1 - rnd2

        return rnd1, rnd2, sub

    def write_text(self, problem, solution):
        problem.write("\nSubtract these hexadecimal numbers\n")
        solution.write("\nSubtract these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_hex(rnd1)} - {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} - {des_to_hex(rnd2)} = {des_to_hex(sub)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1, rnd2, sub = self.get_numbers()
            problem.write(f"{i}. {des_to_hex(rnd1)} - {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} - {des_to_hex(rnd2)} = {des_to_hex(sub)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexMulProblem(Problem):
    header = "Multiply these hexadecimal numbers"

    def write_text(self, problem, solution):
        problem.write("\nMultiply these hexadecimal numbers\n")
        solution.write("\nMultiply these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(5, 15)
            problem.write(f"{i}. {des_to_hex(rnd1)} * {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} * {des_to_hex(rnd2)} = {des_to_hex(rnd1 * rnd2)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            rnd2 = random.randint(5, 15)
            problem.write(f"{i}. {des_to_hex(rnd1)} * {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} * {des_to_hex(rnd2)} = {des_to_hex(rnd1 * rnd2)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class HexDivProblem(Problem):
    header = "Divide these hexadecimal numbers"

    def get_numbers(self):
        rnd1 = random.randint(self.range_start, self.range_end)
        rnd2 = random.randint(5, 15)

        while rnd1 % rnd2 != 0:
            rnd1 = random.randint(self.range_start, self.range_end)
            for i in range(5, 15):
                if rnd1 % i == 0:
                    rnd2 = i
                    break

        return rnd1, rnd2, rnd1 // rnd2

    def write_text(self, problem, solution):
        problem.write("\nDivide these hexadecimal numbers\n")
        solution.write("\nDivide these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_hex(rnd1)} / {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} / {des_to_hex(rnd2)} = {des_to_hex(div)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1, rnd2, div = self.get_numbers()
            problem.write(f"{i}. {des_to_hex(rnd1)} / {des_to_hex(rnd2)}\n")
            solution.write(f"{i}. {des_to_hex(rnd1)} / {des_to_hex(rnd2)} = {des_to_hex(div)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class SixteensComplementProblem(Problem):
    header = "Find the 16's complement of these hexadecimal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the 16's complement of these hexadecimal numbers\n")
        solution.write("\nFind the 16's complement of these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {sixteens_complement(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {sixteens_complement(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")

class FifteensComplementProblem(Problem):
    header = "Find the 15's complement of these hexadecimal numbers"

    def write_text(self, problem, solution):
        problem.write("\nFind the 15's complement of these hexadecimal numbers\n")
        solution.write("\nFind the 15's complement of these hexadecimal numbers\n")

        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {fifteens_complement(rnd1)}\n")

    def write_md(self, problem, solution, header_index=0):
        problem.write(f"### {header_index}. {self.header}\n")
        solution.write(f"### {header_index}. {self.header}\n")
        for i in range(self.count):
            rnd1 = random.randint(self.range_start, self.range_end)
            problem.write(f"{i}. {des_to_hex(rnd1)}\n")
            solution.write(f"{i}. {fifteens_complement(rnd1)}\n")

        problem.write("\n\n")
        solution.write("\n\n")


from generator_class import ProblemMaker
from generator import *


def generator_test():
    maker = ProblemMaker()
    maker.add_problems(
        [
            BinToDesProblem(),
            DesToBinProblem(),
            BinSubProblem(),
            BinSumProblem(),
            BinMulProblem(),
            BinDivProblem(),
            OnesComplementProblem(),
            TwosComplementProblem(),
            FloatToBinProblem(count=10),
        ]
    )
    maker.generate()


if __name__ == "__main__":
    generator_test()

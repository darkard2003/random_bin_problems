from problem.generator import *
from problem.generator_class import ProblemMaker

def main():
    maker = ProblemMaker()
    maker.add_problems(
        [
            BinToDesProblem(),
            DesToBinProblem(),
            BinSumProblem(),
            BinSubProblem(),
            BinMulProblem(),
            BinDivProblem(),
            OnesComplementProblem(),
            TwosComplementProblem(),
            FloatToBinProblem(),
        ]
    )
    maker.generate()


if __name__ == "__main__":
    main()

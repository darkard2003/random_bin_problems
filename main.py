from problem.problems import *
from problem.problem_maker import ProblemMaker

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

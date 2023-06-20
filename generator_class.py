from enum import Enum
import os
from generator import *


class ProblemMaker:
    def __init__(self):
        self.problem_filename = "problem.txt"
        self.solution_filename = "solution.txt"
        self.output_folder = "output"

        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

        self.problem_filepath = os.path.join(self.output_folder, self.problem_filename)
        self.solution_filepath = os.path.join(
            self.output_folder, self.solution_filename
        )

        self.problems: list[Problem] = []

    def add_problem(self, problem: Problem):
        self.problems.append(problem)

    def add_problems(self, problems: list[Problem]):
        self.problems.extend(problems)

    def generate(self):
        problem_file = open(self.problem_filepath, "w")
        solution_file = open(self.solution_filepath, "w")

        for problem in self.problems:
            problem.generate(problem_file, solution_file)

        problem_file.close()
        solution_file.close()

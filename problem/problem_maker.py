import os
from .problems import Problem


class ProblemMaker:
    def __init__(
        self,
        problem_filename="problem.txt",
        solution_filename="solution.txt",
        problem_md_filename="problem.md",
        solution_md_filename="solution.md",
    ):
        self.problem_filename = problem_filename
        self.solution_filename = solution_filename
        self.problem_md_filename = problem_md_filename
        self.solution_md_filename = solution_md_filename

        self.output_folder = "output"

        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

        self.problem_filepath = os.path.join(self.output_folder, self.problem_filename)
        self.solution_filepath = os.path.join(
            self.output_folder, self.solution_filename
        )

        self.problem_md_filepath = os.path.join(
            self.output_folder, self.problem_md_filename
        )
        self.solution_md_filepath = os.path.join(
            self.output_folder, self.solution_md_filename
        )

        self.problems: list[Problem] = []

    def add_problem(self, problem: Problem):
        self.problems.append(problem)

    def add_problems(self, problems: list[Problem]):
        self.problems.extend(problems)

    def generate_text(self):
        problem_file = open(self.problem_filepath, "w")
        solution_file = open(self.solution_filepath, "w")

        for problem in self.problems:
            problem.write_text(problem_file, solution_file)

        problem_file.close()
        solution_file.close()

    def generate_md(self):
        problem_file = open(self.problem_md_filepath, "w")
        solution_file = open(self.solution_md_filepath, "w")

        problem_file.write("# Problems\n\n")
        solution_file.write("# Solutions\n\n")

        for idx, problem in enumerate(self.problems):
            problem.write_md(problem_file, solution_file, idx)

        problem_file.close()
        solution_file.close()

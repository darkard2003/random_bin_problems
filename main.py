import generator

PROBLEM_FILE = "problem.txt"
SOLUTION_FILE = "solution.txt"


def main():
    with open(PROBLEM_FILE, "w") as prob, open(SOLUTION_FILE, "w") as sol:
        generator.des_to_bin_problem(prob, sol, count=5)
        generator.bin_to_des_problem(prob, sol, count=5)
        generator.bin_sum_problem(prob, sol, count=5)
        generator.bin_sub_problem(prob, sol, count=5)
        generator.bin_mul_problem(prob, sol, count=5)
        generator.bin_div_problem(prob, sol, count=5)
        # generator.ones_complement_problem(prob, sol, count=5)
        # generator.twos_complement_problem(prob, sol, count=5)
        # generator.twos_complement_sub(prob, sol, count=5)
        # generator.float_to_bin_prob(prob, sol)


if __name__ == "__main__":
    main()

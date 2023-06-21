import os
from problem.problems import *
from problem.problem_maker import ProblemMaker
import time
import txt2pdf


def make_md():
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    problem_md_name = f"problem_{time_str}.md"
    solution_md_name = f"solution_{time_str}.md"

    maker = ProblemMaker(
        problem_md_filename=problem_md_name,
        solution_md_filename=solution_md_name,
    )

    maker.add_problems(
        [
            # BinToDesProblem(),
            # DesToBinProblem(),
            # BinSumProblem(),
            # BinSubProblem(),
            # BinMulProblem(),
            # BinDivProblem(),
            # OnesComplementProblem(),
            # TwosComplementProblem(),
            # FloatToBinProblem(),
            OctToDesProblem(),
            DesToOctProblem(),
            EightsCompProblem(),
            SevensCompProblem(),
            OctToBinProblem(),
            BinToOctProblem(),
            HexToOctProblem(),
            OctToHexProblem(),
            SixteensComplementProblem(),
            FifteensComplementProblem(),
            HexToBinProblem(),
            BinToHexProblem(),
        ]
    )
    maker.generate_md()


def make_pdf():
    source_folder = "./output"
    target_folder = "./pdfs"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    made_md_files = os.listdir(target_folder)
    made_md_files = [filename.replace(".pdf", ".md") for filename in made_md_files]

    for filename in os.listdir(source_folder):
        if filename in made_md_files:
            continue

        if filename.endswith(".md"):
            txt2pdf.txt2pdf(
                md_file_path=os.path.join(source_folder, filename),
                pdf_file_path=os.path.join(
                    target_folder, filename.replace(".md", ".pdf")
                ),
            )


if __name__ == "__main__":
    make_md()
    make_pdf()

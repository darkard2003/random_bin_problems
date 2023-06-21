# Binary Problem Maker

## Why this code?
While teaching number system in computer science, i have to give so many problems to my students to practice. It's impractical to come up with random number when python can generate it for you. So i came up with this code to automaticly generate problems.

## How to use it?
1. Clone this repository
2. Install the requirements
3. Add or remove the problem classes in the add_problems() function in main.py
4. Run main.py
5. The problems will be generated in the output folder with the solution
5. And the pdf will be generated in the pdf folder

## How to add a new problem?
1. Create a new class in the problems folder
2. Inherit the Problem class
3. Implement the write_text() and write_md() function
4. Add the class in the add_problems() function in main.py

## warning
This code is not optimized for performance. It's just a quick and dirty solution to my problem. If you want to use it for a large number of problems, you should optimize it.

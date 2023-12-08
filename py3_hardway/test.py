def arithmetic_arranger(problems, show_answers=False):
 
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

for problem in problems:
    operands = problem.split()

    width = max(len(operands[0]), len(operands[2])) + 2
    line1 += operands[0].rjust(width) + "    "
    line2 += operands[1] + operands[2].rjust(width - 1) + "    "
    line3 += "-" * width + "    "
    if show_answers:
        answer = str(eval(problem))
        line4 += answer.rjust(width) + "    "

arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
if show_answers:
    arranged_problems += "\n" + line4.rstrip()


print(arithmetic_arranger(problems))
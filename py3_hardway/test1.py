def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

    for problem in problems:
        try:
            operand1, operator, operand2 = problem.split()
            operand1, operand2 = int(operand1), int(operand2)
        except ValueError:
            return "Error: Invalid input."

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        max_len = max(len(operand1), len(operand2))
        total = eval(f"{operand1} {operator} {operand2}")

        arranged_problems.append((
            operand1.rjust(max_len),
            operator,
            operand2.rjust(max_len),
            total,
        ))

    output = []
    for operand1, operator, operand2, total in arranged_problems:
        line1 = operand1 + operator + operand2
        line2 = str(total).rjust(len(line1))
        output.append(line1 + "\n" + line2 + "\n")

    if show_answers:
        return "".join(output)

    return "".join(line1 + "\n" for line1 in output)
    print(arranged_problems)
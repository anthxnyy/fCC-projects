def largest_num_length(problems, equation):
    return max(
        len(problems[equation].split()[0]), len(problems[equation].split()[2])
    )


def operator(problems, equation):
    return problems[equation].split()[1]


def arithmetic_arranger(problems, solutions=False):

    # Error checking
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        if problem.split()[1] not in ["-", "+"]:
            return "Error: Operator must be '+' or '-'."
        if (not problem.split()[0].isdigit()) or (
            not problem.split()[2].isdigit()
        ):
            return "Error: Numbers must only contain digits."
        if (len(problem.split()[0]) > 4) or (len(problem.split()[2]) > 4):
            return "Error: Numbers cannot be more than four digits."

    # Variables
    spacer = "    "
    num1_row = ""
    num2_row = ""
    dashes_row = ""
    solution_row = ""

    # Creates the first row
    for i in range(len(problems)):
        # Calculates the spaces needed to be aligned
        num1 = (
            "".join(
                " "
                for i in range(
                    len(problems[i].split()[0]),
                    largest_num_length(problems, i) + 2,
                )
            )
            + problems[i].split()[0]
        )

        # Adds the number to the row
        if i != 0:
            num1_row += spacer + num1
        else:
            num1_row += num1

    # Creates the second row
    for i in range(len(problems)):
        # Calculates the spaces needed to be aligned
        num2 = (
            operator(problems, i)
            + "".join(
                " "
                for i in range(
                    len(problems[i].split()[2]),
                    largest_num_length(problems, i) + 1,
                )
            )
            + problems[i].split()[2]
        )

        # Adds the operator with the number to the row
        if i != 0:
            num2_row += spacer + num2
        else:
            num2_row += num2

    # Creates the third row
    for i in range(len(problems)):
        # Calculates the spaces needed to be aligned
        dashes = "".join(
            "-" for i in range(largest_num_length(problems, i) + 2)
        )

        # Adds the dashes to the row
        if i != 0:
            dashes_row += spacer + dashes
        else:
            dashes_row += dashes

    # Combines each row
    if solutions:
        # Creates the fourth row
        for i in range(len(problems)):
            # Calculates the answer
            if operator(problems, i) == "+":
                answer = int(problems[i].split()[0]) + int(
                    problems[i].split()[2]
                )
            else:
                answer = int(problems[i].split()[0]) - int(
                    problems[i].split()[2]
                )

            # Calculates the spaces needed to be aligned
            solution = "".join(
                " "
                for i in range(
                    len(str(answer)), largest_num_length(problems, i) + 2
                )
            ) + str(answer)

            # Adds the solution to the row
            if i != 0:
                solution_row += spacer + solution
            else:
                solution_row += solution

        arranged_problems = (
            num1_row
            + "\n"
            + num2_row
            + "\n"
            + dashes_row
            + "\n"
            + solution_row
        )
    else:
        arranged_problems = num1_row + "\n" + num2_row + "\n" + dashes_row
    return arranged_problems

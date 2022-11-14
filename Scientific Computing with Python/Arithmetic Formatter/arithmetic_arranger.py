def arithmetic_arranger(problems, solutions=False) -> str:

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

    # Conversion
    # Each join method used is to create spaces and align each equation
    spacer = "    "
    num1_row = ""
    num2_row = ""
    dashes_row = ""
    solution_row = ""

    # Creates the first row
    for i in range(len(problems)):
        largest_num_length = max(
            len(problems[i].split()[0]), len(problems[i].split()[2])
        )

        # Calculates the spaces needed to be aligned
        num1 = (
            "".join(
                " "
                for i in range(
                    len(problems[i].split()[0]), largest_num_length + 2
                )
            )
            + problems[i].split()[0]
        )

        # Adds the number to the row
        if i == 0:
            num1_row += num1
        else:
            num1_row += spacer + num1

    # Creates the second row
    for i in range(len(problems)):
        largest_num_length = max(
            len(problems[i].split()[0]), len(problems[i].split()[2])
        )
        operator = problems[i].split()[1]

        # Calculates the spaces needed to be aligned
        num2 = (
            operator
            + "".join(
                " "
                for i in range(
                    len(problems[i].split()[2]), largest_num_length + 1
                )
            )
            + problems[i].split()[2]
        )
        # Adds the number with the operator to the row
        if i == 0:
            num2_row += num2
        else:
            num2_row += spacer + num2

    # Creates the third row
    for i in range(len(problems)):
        largest_num_length = max(
            len(problems[i].split()[0]), len(problems[i].split()[2])
        )

        # Calculates the spaces needed to be aligned
        dashes = "".join("-" for i in range(largest_num_length + 2))

        # Adds the dashes to the row
        if i == 0:
            dashes_row += dashes
        else:
            dashes_row += spacer + dashes

    # Creates the fourth row
    for i in range(len(problems)):
        largest_num_length = max(
            len(problems[i].split()[0]), len(problems[i].split()[2])
        )
        operator = problems[i].split()[1]

        # Calculates the answer
        if operator == "-":
            answer = int(problems[i].split()[0]) - int(problems[i].split()[2])
        elif operator == "+":
            answer = int(problems[i].split()[0]) + int(problems[i].split()[2])

        # Calculates the spaces needed to be aligned
        solution = "".join(
            " " for i in range(len(str(answer)), largest_num_length + 2)
        ) + str(answer)

        # Adds the solution to the row
        if i == 0:
            solution_row += solution
        else:
            solution_row += spacer + solution

    # Combines each row
    if solutions:
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

import json
import inquirer
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    questions = [
        inquirer.Text("xaxis", message="What do you want to name the xaxis?"),
        inquirer.Text("yaxis", message="What do you want to name the yaxis?"),
        inquirer.Text("title", message="What is the title of the graph?"),
        inquirer.List("type", message="What type of regression do you want to perform?", choices=["Linear", "Quadratic", "Cubic", "Quartic" , "Exponential", "Logarithmic", "Power Regression"])
    ]
    answers = inquirer.prompt(questions)
    xcoords, ycoords = [], []

    with open('settings.json', 'r') as file:
        data = json.load(file)

    for point in data["points"]:
        xcoords.append(point[0])
        ycoords.append(point[1])

    plt.scatter(xcoords, ycoords, color="red")
    plt.xlabel(answers["xaxis"])
    plt.ylabel(answers["yaxis"])
    plt.title(answers["title"])

    x = np.array(xcoords)
    y = np.array(ycoords)

    match answers["type"]:
        case "Linear":
            results = polyfit(x, y, 1)
            slope, intercept, r_squared = round(results[0][0],5), round(results[0][1],9), round(results[1],4)
            function = slope * x + intercept
            equation = f"Equation: y = {slope}x {sign_char(intercept)} {abs(intercept)}"
        case "Quadratic":
            results = polyfit(x, y, 2)
            leading, linear, constant, r_squared = round(results[0][0], 7), round(results[0][1], 6), round(results[0][2], 7), round(results[1], 4)
            function = leading * (x ** 2) + linear * x + constant
            equation = f"Equation: y = {leading}x\u00b2 {sign_char(linear)} {abs(linear)}x {sign_char(constant)} {abs(constant)}"
        case "Cubic":
            results = polyfit(x, y, 3)
            leading, quadratic, linear, constant, r_squared = round(results[0][0], 6), round(results[0][1], 5), round(results[0][2], 5), round(results[0][3], 6), round(results[1], 4)
            function = leading * (x ** 3) + quadratic * (x ** 2) + linear * x + constant
            equation = f"Equation: y = {leading}x\u00b3 {sign_char(quadratic)} {abs(quadratic)}x\u00b2 {sign_char(linear)} {abs(linear)}x {sign_char(constant)} {abs(constant)}"
        case "Quartic":
            results = polyfit(x, y, 4)
            leading, cubic, quadratic, linear, constant, r_squared = round(results[0][0], 5), round(results[0][1], 5), round(results[0][2], 5), round(results[0][3], 6), round(results[0][4],6), round(results[1], 4)
            function = leading * (x ** 4) + cubic * (x ** 3) + quadratic * (x ** 2) + linear * x + constant
            equation = f"Equation: y = {leading}x\u00b4 {sign_char(cubic)} {abs(cubic)}x\u00b3 {sign_char(quadratic)} {abs(quadratic)}x\u00b2 {sign_char(linear)} {abs(linear)}x {sign_char(constant)} {abs(constant)}"
        case "Exponential":
            results = polyfit(x, np.log(y), 1)
            base, initial, r_squared = round(math.exp(results[0][0]), 5), round(math.exp(results[0][1]), 5), round(results[1], 4)
            function = initial * base ** x
            equation = f"Equation: y = {initial} * {base}^x"
        case "Logarithmic":
            valid = True
            for xcoord in xcoords:
                if xcoord < 0:
                    valid = False
            if not valid:
                return "Invalid data for logarithmic regression (all x values must be positive)"
            results = polyfit(np.log(x), y, 1)
            constant, intercept, r_squared = round(results[0][0], 6), round(results[0][1], 5), round(results[1], 4)
            function = intercept + constant * np.log(x)
            equation = f"Equation: y = {intercept} + {constant}ln(x)"
        case "Power Regression":
            results = polyfit(np.log(x), np.log(y), 1)
            initial, power, r_squared = round(math.exp(results[0][1]), 6), round(results[0][0], 6), round(results[1], 4)
            function = initial * (x ** power)
            equation = f"Equation: y = {initial} * x^{power}"

    print(f"{equation}\nR\u00b2: {r_squared}")
    question = [
        inquirer.List("graph", message="Do you want to see the graph?", choices=["Yes", "No"])
    ]
    answers = inquirer.prompt(question)
    if answers["graph"] == "Yes":
        plt.plot(x,function)
        plt.show()

def sign_char(num):
    if num >= 0:
        sign = "+"
    else:
        sign = "-"
    return sign

# Polynomial Regression
def polyfit(x, y, degree):
    coeffs = np.polyfit(x, y, degree)

    # r-squared
    p = np.poly1d(coeffs)

    # fit values, and mean
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    r_squared = ssreg / sstot

    return coeffs, r_squared

if __name__ == '__main__':
    main()

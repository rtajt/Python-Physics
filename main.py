"""Module for a cleaner prompt + all scripts"""
import inquirer
from misc import conversions, regression

def main():
    """Based on user input, run corresponding script"""
    questions = [
        inquirer.List("script", message="Which type of script do you want to run?",
        choices=["Misc"])
    ]
    answers = inquirer.prompt(questions)
    match answers["script"]:
        case "Misc":
            questions = [
                inquirer.List("misc", message="Which misc script do you want to use?",
                choices=["Conversions", "Percent Error", "Regression"])
            ]
            answers = inquirer.prompt(questions)
            match answers["misc"]:
                case "Conversions":
                    conversions.main()
                case "Percent Error":
                    questions = [
                        inquirer.Text("observed", message="What is the observed value?"),
                        inquirer.Text("actual", message="What is the actual value?")
                    ]
                    answers = inquirer.prompt(questions)
                    observed = float(answers["observed"])
                    actual = float(answers["actual"])
                    error = (abs(observed - actual) / actual) * 100
                    print(f"There is an error of {error}%")
                case "Regression":
                    regression.main()
main()

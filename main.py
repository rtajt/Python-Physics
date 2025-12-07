"""Module for a cleaner prompt + all scripts"""
import inquirer
from misc import conversions


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
                choices=["Conversions"])
            ]
            answers = inquirer.prompt(questions)
            match answers["misc"]:
                case "Conversions":
                    conversions.main()
main()

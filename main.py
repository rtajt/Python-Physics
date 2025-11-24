"""Module for a cleaner prompt + all scripts"""
import inquirer
import conversions

def main():
    """Based on user input, run corresponding script"""
    questions = [
        inquirer.List("script", message="Which script do you want to run?",
        choices=["Unit Conversions"])
    ]
    answers = inquirer.prompt(questions)
    match answers["script"]:
        case "Unit Conversions":
            conversions.main()
main()

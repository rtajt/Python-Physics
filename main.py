import conversions
import inquirer

def main():
    questions = [
        inquirer.List("script", message="Which script do you want to run?", choices=["Unit Conversions"])
    ]
    answers = inquirer.prompt(questions)
    match answers["script"]:
        case "Unit Conversions":
            conversions.main()
main()
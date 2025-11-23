import inquirer
from pint import UnitRegistry

global old_unit, new_unit
ureg = UnitRegistry()


def main():
    questions = [
        inquirer.List("convert_type", message="What do you want to convert?", choices=["Length", "Area", "Volume", "Time", "Temperature", "Velocity", "Mass", "Force", "Pressure"])
    ]
    answers = inquirer.prompt(questions)
    selector(answers)

def selector(answers):
    choice = answers["convert_type"]
    match choice:
        case "Length":
            length_conversions()
def length_conversions():
    global old_unit, new_unit
    questions = [
        inquirer.Text("magnitude", message="What's the magnitude of the quantity you want to convert? (ex: 5, 41)"),
        inquirer.List("old_units", message="What are the units of it?", choices=["Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards", "Miles"]),
        inquirer.List("new_units", message="What units do you want to convert to?", choices=["Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards","Miles"])
    ]
    answers = inquirer.prompt(questions)

    # Find old unit and new unit and multiply by magnitude
    match answers["old_units"]:
        case "Millimeters":
            old_unit = ureg.millimeters
        case "Centimeters":
            old_unit = ureg.centimeters
        case "Meters":
            old_unit = ureg.meters
        case "Kilometers":
            old_unit = ureg.kilometers
        case "Inches":
            old_unit = ureg.inches
        case "Feet":
            old_unit = ureg.feet
        case "Yards":
            old_unit = ureg.yards
        case "Miles":
            old_unit = ureg.miles

    match answers["new_units"]:
        case "Millimeters":
            new_unit = ureg.millimeters
        case "Centimeters":
            new_unit = ureg.centimeters
        case "Meters":
            new_unit = ureg.meters
        case "Kilometers":
            new_unit = ureg.kilometers
        case "Inches":
            new_unit = ureg.inches
        case "Feet":
            new_unit = ureg.feet
        case "Yards":
            new_unit = ureg.yards
        case "Miles":
            new_unit = ureg.miles


    old_quantity = int(answers["magnitude"]) * old_unit
    new_quantity = old_quantity.to(new_unit)
    print(answers["magnitude"] + " " + answers["old_units"].lower() + " converts to " + str(new_quantity.magnitude) + " " + answers["new_units"].lower())

main()
import inquirer
from pint import UnitRegistry

ureg = UnitRegistry()

def main():
    questions = [
        inquirer.List("convert_type", message="What do you want to convert?",
                      choices=["Length", "Area", "Volume", "Time", "Temperature", "Velocity", "Mass", "Force",
                               "Pressure"])
    ]
    answers = inquirer.prompt(questions)
    selector(answers)


def selector(answers):
    choice = answers["convert_type"]

    # Every unit choice
    UNIT_OPTIONS = {
        "Length": ["Millimeters", "Centimeters", "Meters", "Kilometers",
                   "Inches", "Feet", "Yards", "Miles"],
        "Area": ["Centimeters Squared", "Meters Squared", "Kilometers Squared",
                 "Inches Squared", "Feet Squared", "Yards Squared",
                 "Acre", "Miles Squared"],
        "Volume": ["Centimeters Cubed", "Milliliters", "Liters", "Meters Cubed", "Teaspoons", "Tablespoons", "Inches Cubed", "Ounces", "Cups", "Pints", "Quarts", "Gallons", "Feet Cubed"]
    }

    # Every conversion function
    CONVERSION_FUNCS = {
        "Length": length_conversions,
        "Area": area_conversions,
        "Volume": volume_conversions
    }

    # Will be removed when conversions is done
    if choice not in UNIT_OPTIONS:
        print("Not yet implemented")
        return

    unit_choices = UNIT_OPTIONS[choice]

    # New questions
    questions = [
        inquirer.Text(
            "magnitude",
            message="What's the magnitude of the quantity you want to convert? (ex: 5, 41)"
        ),
        inquirer.List("old_units", message="What are the units of it?", choices=unit_choices),
        inquirer.List("new_units", message="What units do you want to convert to?", choices=unit_choices)
    ]

    # Ask user and dispatch to proper converter
    answers = inquirer.prompt(questions)
    old_unit, new_unit= CONVERSION_FUNCS[choice](answers)
    new_quantity = (float(answers["magnitude"]) * old_unit).to(new_unit)
    print(
        f'{answers["magnitude"]} {answers["old_units"].lower()} '
        f'converts to {new_quantity.magnitude} {answers["new_units"].lower()}'
    )

def length_conversions(answers):
    unit_map = {
        "Millimeters": ureg.millimeters,
        "Centimeters": ureg.centimeters,
        "Meters": ureg.meters,
        "Kilometers": ureg.kilometers,
        "Inches": ureg.inches,
        "Feet": ureg.feet,
        "Yards": ureg.yards,
        "Miles": ureg.miles
    }

    old_unit = unit_map[answers["old_units"]]
    new_unit = unit_map[answers["new_units"]]

    return old_unit, new_unit

def area_conversions(answers):
    unit_map = {
        "Centimeters Squared": ureg.centimeters ** 2,
        "Meters Squared": ureg.meters ** 2,
        "Kilometers Squared": ureg.kilometers ** 2,
        "Inches Squared": ureg.inches ** 2,
        "Feet Squared": ureg.feet ** 2,
        "Yards Squared": ureg.yards ** 2,
        "Acre": ureg.acre,
        "Miles Squared": ureg.miles ** 2
    }

    old_unit = unit_map[answers["old_units"]]
    new_unit = unit_map[answers["new_units"]]
    return old_unit, new_unit

def volume_conversions(answers):
    unit_map = {
        "Centimeters Cubed": ureg.centimeters ** 3,
        "Milliliters": ureg.milliliters,
        "Liters": ureg.liters,
        "Meters Cubed": ureg.meters ** 3,
        "Teaspoons": ureg.teaspoons,
        "Tablespoons Cubed": ureg.tablespoons,
        "Inches Cubed": ureg.inches ** 3,
        "Ounces": ureg.ounces,
        "Cups": ureg.cups,
        "Pints": ureg.pints,
        "Quarts": ureg.quarts,
        "Gallons": ureg.gallons,
        "Feet Cubed": ureg.feet ** 3
    }
    old_unit = unit_map[answers["old_units"]]
    new_unit = unit_map[answers["new_units"]]
    return old_unit, new_unit

if __name__ == "__main__":
    main()
"""Inquirer for prompting and pint for unit conversions"""
import inquirer
from pint import UnitRegistry
ureg = UnitRegistry()

def main():
    """Collects user input and passes data into the conversion type selector function"""
    questions = [
        inquirer.List("convert_type", message="What do you want to convert?",
        choices=["Length", "Area", "Volume", "Time", "Temperature", "Velocity", "Mass","Force",
        "Pressure"])
    ]
    answers = inquirer.prompt(questions)
    selector(answers)

def selector(answers):
    """Based on user input, run respective conversion function and return the new quantity"""
    choice = answers["convert_type"]

    # Every unit choice
    unit_options = {
        "Length": ["Millimeters", "Centimeters", "Meters", "Kilometers",
                   "Inches", "Feet", "Yards", "Miles"],
        "Area": ["Centimeters Squared", "Meters Squared", "Kilometers Squared",
                 "Inches Squared", "Feet Squared", "Yards Squared",
                 "Acre", "Miles Squared"],
        "Volume": ["Centimeters Cubed", "Milliliters", "Liters", "Meters Cubed", "Teaspoons",
        "Tablespoons", "Inches Cubed", "Ounces", "Cups", "Pints", "Quarts", "Gallons",
        "Feet Cubed"],
        "Time": ["Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"],
        "Temperature": ["Celsius", "Kelvin", "Fahrenheit"],
        "Velocity": ["Meters Per Second", "Kilometers Per Hour", "Feet Per Second",
                     "Miles Per Hour"],
        "Mass": ["Grams", "Kilograms", "Slugs", "Tons"],
        "Force": ["Newtons", "Kilogram Force", "Pound Force", "Ton Force"],
        "Pressure": ["Pascals", "Kilopascals", "Standard Atmosphere Units"]
    }

    # Every conversion function
    conversions_funcs = {
        "Length": length_conversions,
        "Area": area_conversions,
        "Volume": volume_conversions,
        "Time": time_conversions,
        "Temperature": temperature_conversions,
        "Velocity": velocity_conversions,
        "Mass": mass_conversions,
        "Force": force_conversions,
        "Pressure": pressure_conversions
    }

    unit_choices = unit_options[choice]

    # New questions
    questions = [
        inquirer.Text(
            "magnitude",
            message="What's the magnitude of the quantity you want to convert? (ex: 5, 41)"
        ),
        inquirer.List("old_units", message="What are the units of it?", choices=unit_choices),
        inquirer.List("new_units", message="What units do you want to convert to?",
        choices=unit_choices)
    ]

    # Run converter based on user input
    answers = inquirer.prompt(questions)
    old_unit, new_unit = conversions_funcs[choice](answers)

    # The actual conversion step
    q_ = ureg.Quantity
    old_quantity = q_(float(answers["magnitude"]), old_unit)
    new_quantity = old_quantity.to(new_unit)

    print(
        f'{answers["magnitude"]} {answers["old_units"].lower()} '
        f'converts to {new_quantity.magnitude} {answers["new_units"].lower()}'
    )

def length_conversions(answers):
    """Converts a given length quantity to a different unit type"""
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
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def area_conversions(answers):
    """Converts a given area quantity to a different unit type"""
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
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def volume_conversions(answers):
    """Converts a given volume quantity to a different unit type"""
    unit_map = {
        "Centimeters Cubed": ureg.cc,
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
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def time_conversions(answers):
    """Converts a given time quantity to a different unit type"""
    unit_map = {
        "Milliseconds": ureg.milliseconds,
        "Seconds": ureg.seconds,
        "Minutes": ureg.minutes,
        "Hours": ureg.hours,
        "Days": ureg.days,
        "Weeks": ureg.weeks,
        "Years": ureg.years
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def temperature_conversions(answers):
    """Converts a temperature quantity to a different unit type"""
    unit_map = {
        "Celsius": ureg.degC,
        "Kelvin": ureg.kelvin,
        "Fahrenheit": ureg.degF,
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def velocity_conversions(answers):
    """Converts a given velocity quantity to a different unit type"""
    unit_map = {
        "Meters Per Second": ureg.mps,
        "Kilometers Per Hour": ureg.kph,
        "Feet Per Second": ureg.fps,
        "Miles Per Hour": ureg.mph
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def mass_conversions(answers):
    """Converts a given mass quantity to a different unit type"""
    unit_map = {
        "Grams": ureg.gram,
        "Kilograms": ureg.kilograms,
        "Slugs": ureg.slug,
        "Tons": ureg.tons,
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def force_conversions(answers):
    """Converts a given force quantity to a different unit type"""
    unit_map = {
        "Newtons": ureg.newton,
        "Kilogram Force": ureg.kgf,
        "Pound Force": ureg.lbf,
        "Ton Force": ureg.ton_force
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

def pressure_conversions(answers):
    """Converts a given pressure quantity to a different unit type"""
    unit_map = {
        "Pascals": ureg.pascal,
        "Kilopascals": ureg.kilopascals,
        "Standard Atmosphere Units": ureg.atm,
    }
    return unit_map[answers["old_units"]], unit_map[answers["new_units"]]

if __name__ == "__main__":
    main()

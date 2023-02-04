import csv

from application.config.paths import FILES_OUTPUT_PATH


def average_params(name_file: str = "output") -> str:
    path_to_file = FILES_OUTPUT_PATH.joinpath("hw.csv")
    with open(path_to_file) as csv_file:
        height = 0
        weight = 0
        reader = csv.DictReader(csv_file)

        for row in reader:
            height += float(row["Height(Inches)"])
            weight += float(row["Weight(Pounds)"])

        avr_height = height / int(row["Index"])
        avr_weight = weight / int(row["Index"])
    return avr_height, avr_weight


def average_values():
    avr_height, avr_weight = average_params()
    cm_height = round(float(avr_height * 2.54), 3)  # cm
    kg_weight = round(float(avr_weight * 0.45), 3)  # kg
    print(f"Average height is: {cm_height} cm.\nAverage weight is: {kg_weight} kg.")

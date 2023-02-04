from application.astronauts.amount_of_astronauts import astronauts
from application.average.avarage_params import average_values
from application.logging.init_logging import init_logging
from application.users_generator.users_file import users_file


def main() -> None:
    # Astronauts names and amount
    astronauts()

    # Generate users
    users_file()

    # Get *.csv file from Google Drive and processing data
    average_values()


if __name__ == "__main__":
    init_logging()
    main()

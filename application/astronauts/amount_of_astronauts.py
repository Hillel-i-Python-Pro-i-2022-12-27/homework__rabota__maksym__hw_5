from application.astronauts.request_to_api import get_astronauts


def astronauts():
    response = get_astronauts()

    if isinstance(response, dict):
        names = []
        count_of_astronauts = response["number"]
        for astronaut in response["number"]:
            names.append(astronaut["name"])

        statistics = f"Currently astronauts: {count_of_astronauts}\n" + "\n".join(names)

        return statistics

    return response

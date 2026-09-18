import requests


def get_university_data(country="France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data


# name
# country
# alpha_two_code
# state-province
# domains (list)
# web_pages (list)

if __name__ == "__main__":
    state = []
    school_name = []

    uni_data = get_university_data("France")
    print(f"Numbers of schools : {len(uni_data)}\n\n")

    for university in (
        uni_data
    ):  # so for each uni_data[X], so uni_data[X] = university for each iteration
        statename = university["state-province"]

        if statename is not None and statename not in state:  # name is unidata[]
            state.append(statename)

    print(
        "French Universities by each region\n========================================================================="
    )
    for states in state:
        school_name = []

        for university in uni_data:
            if university["state-province"] == states:
                school_name.append(university["name"])

        if university == uni_data[len(university) - 1]:
            print(f"└─── {states} ({len(school_name)})")

        else:
            print(f"├── {states} ({len(school_name)})")

        for names in school_name:
            if names == school_name[len(school_name) - 1]:
                print(f"│   └── {names}")

            else:
                print(f"│   ├── {names}")

    count = sum(1 for u in uni_data if u["state-province"] is not None)
    print(f"Universities with region data: {count} / {len(uni_data)}")

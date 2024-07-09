import json


def employees_rewrite(sort_type: str):
    def convert_keys_to_lowercase(d):
        if isinstance(d, dict):
            return {k.lower(): convert_keys_to_lowercase(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [convert_keys_to_lowercase(i) for i in d]
        else:
            return d

    try:
        with open('employees.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception("employees.json file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding the JSON file.")

    data = convert_keys_to_lowercase(data)

    valid_keys = {"firstname", "lastname", "department", "salary"}
    sort_type_lower = sort_type.lower()
    if sort_type_lower not in valid_keys:
        raise ValueError('Bad key for sorting')

    employees = data["employees"]
    if sort_type_lower in {"firstname", "lastname", "department"}:
        employees_sorted = sorted(employees, key=lambda x: x[sort_type_lower])
    else:
        employees_sorted = sorted(employees, key=lambda x: x[sort_type_lower], reverse=True)

    sorted_data = {"employees": employees_sorted}
    output_filename = f'employees_{sort_type_lower}_sorted.json'
    with open(output_filename, 'w') as file:
        json.dump(sorted_data, file, indent=2)


if __name__ == "__main__":
    try:
        employees_rewrite('lastname')
        print("Employees sorted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


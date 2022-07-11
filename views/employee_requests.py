EMPLOYEES = [
    {
        "id": 1,
        "name": "Stan"},
    {
        "id": 2,
        "name": "Randy"},
    {
        "id": 3,
        "name": "Kenny"
    }
]


def get_all_employees():
    """This function gets all the employees"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """This function gets a single employee by id"""
    # Variable to hold the found employee. Very similar to the
    # for...of loop you used in JavaScript
    requested_employee = None
    # Iterate the EMPLOYEES list above
    for employee in EMPLOYEES:
        # Dictionaries in python use [] notation to find a key
        # Instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

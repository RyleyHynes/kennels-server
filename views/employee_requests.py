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


def create_employee(employee):
    """This function creates an employee"""
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever the number is
    new_id = max_id + 1

    # Add an 'id' property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with 'id' property added
    return employee


def delete_employee(id):
    """This function allows you to delete employees by their id
    """
    # Initial -1 value for employees index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """This function updates the employee
    """
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

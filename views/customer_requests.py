CUSTOMERS = [
    {
        "id": 1,
        "name": "Butters",
    },
    {
        "id": 2,
        "name": "Kyle",
    },
    {
        "id": 3,
        "name": "Mr. Mackey",
    }
]


def get_all_customers():
    """This function gets all the customers"""
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    """This function gets a single customer by id"""
    # Variable to hold the found customer. Very similar to the
    # for...of loop you used in JavaScript
    requested_customer = None
    # Iterate the CUSTOMERS list above
    for customer in CUSTOMERS:
        # Dictionaries in python use [] notation to find key
        # Instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

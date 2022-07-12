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


def create_customer(customer):
    """This function will create a customer"""
    # Get the id of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever number that is
    new_id = max_id + 1

    # Add an 'id' property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with 'id' property
    return customer


def delete_customer(id):
    """This function allows you to delete a specific animal based off the id
    """
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """This function updates the customer
    """
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

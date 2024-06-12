"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

In this section, we will discuss on
Case-1: How to access values outside the function
"""

print("Function with 1 return value")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return name

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In Tuple")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return name, company # it will return in tuple

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In List")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return [name, company]

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In Dictionary")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return {"name": name, "company": company}

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################


"""
Case-2: How to pass values to variables present inside the function

2 ways to pass values
1-way is we can pass only values
2-way is we can pass values using key=value format

In this section, we will discuss
1-way is we can pass only values
"""

print("Function with positional arguments")
print("-"*20)
# --------------


# name & company are called positional arguments
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1", "comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "comp-2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################


print("Function with variable positional arguments")
print("-"*20)
# --------------


# *prev_companies called variable positional arguments
# name & company are called positional arguments
def employee(name, company, *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("Prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1", "comp-1")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "comp-1")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "comp-2")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-4", "comp-2", "my_prev_comp_1")
# prev_companies = ("my_prev_comp_1", )
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-5", "comp-2", "my_prev_comp_1", "my_prev_comp_2")
# prev_companies = ("my_prev_comp_1", "my_prev_comp_2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################

"""
Here 2nd way to pass values

2-way is we can pass values using key=value format
"""

print("Function with keyword or named arguments")
print("-"*20)
# --------------


# name & company are called keyword or named arguments
# * is just syntax, It tells this is keyword/named argument function
# We are not passing any values to *
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee(company="comp-1", name="emp-2")
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="comp-2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################

print("Function with variable keyword or named arguments")
print("-"*20)
# --------------

# **prev_companies are variable keyword or named arguments
def employee(*, name, company, **prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("Prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee(name="emp-1", company="comp-1")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="comp-1")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="comp-2")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-4", company="comp-2", pc1="my_prev_comp_1")
# prev_companies = {pc1: "my_prev_comp_1"}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-5", company="comp-2", pc1="my_prev_comp_1", pc2="my_prev_comp_2")
# prev_companies = {pc1="my_prev_comp_1", pc2="my_prev_comp_2"}
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################
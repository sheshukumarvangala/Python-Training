1
new
message

Loading
history...

Prabhu
Trainer
3: 29
PM
print("Like if-else and for-else, we have 'while-else'")
print("-" * 20)
# ------------------

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)

index_no = 0
while index_no < len(my_list):
    print("Each Value:", my_list[index_no])
    index_no += 1
else:
    print("This is while-else block")
    print("After completing all the iteration, 'else' block will execute")
    print("after completing the for-loop if we want to do some cleanup activity")
    print("We can use this block to do some cleanup activity ")

# for i in my_list:
#     print("Each Value:", i)
# else:
#     print("This is for-else block")
#     print("After completing all the iteration, 'else' block will execute")
#     print("after completing the for-loop if we want to do some cleanup activity")
#     print("We can use this block to do some cleanup activity ")

print("#" * 40, end="\n\n")
########################################
:white_check_mark:
12

Prabhu
Trainer
4: 0
9
PM
15
_file_operations.py
New

Prabhu
Trainer
4: 22
PM
"""
Read/Write operations with text files like .txt
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps

Step-1: Connect to file
    - open() function

Step-2: Read/Write
    - For Writing: 1) write 2) writelines 3) print-function
    - For Reading: 1) read 2) readline 3) readlines

Step-3: Disconnect
    - close()
"""

print("All Write Operations")
print("-" * 20)
# ---------------

# Step-1: Connect to file
# ---------------

# my_file_handle = open("file name or file path here", "mode")
my_file_handle = open("my_out_file.txt", "w")
# mode "w": Write only mode
# mode "w": It will create new file
# mode "w": IMPORTANT: It will erase existing file content

# Step-2: Write
# ---------------
# For Writing: 1) write 2) writelines 3) print-function

# Our Data
x = 10
y = "Python"

# Convert other type of data to 'string' because 1) write 2) writelines
#   expects data in the form of string
x = str(x)

# 1) write: We can pass one string
my_file_handle.write(x + "\n")
my_file_handle.write(y + "\n")

# 2) writelines
my_data_in_list = [x + "\n", y + "\n"]
my_file_handle.writelines(my_data_in_list)

# 3) print-function
print(x, y, 20, "Java", sep="\n", file=my_file_handle)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("""
Created 'my_out_file.txt'. Please check
""")

print("#" * 40, end="\n\n")
#########################################

print("Read Operations: 1) read")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
file_content = my_file_handle.read()
# It will return complete file content in one string
print("file_content:", file_content, sep="\n", end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################
print("Read Operations: 1) read")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
file_content = my_file_handle.read()
# It will return complete file content in one string
print("file_content:", file_content, sep="\n", end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################
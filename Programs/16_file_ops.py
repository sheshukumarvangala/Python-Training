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
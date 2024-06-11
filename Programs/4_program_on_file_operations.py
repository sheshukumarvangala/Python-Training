"""
Read data from server_log.txt

then

extract
IP
PICS

then

Write extrated data to log_report.txt

Expected Output in log_report.txt:
--------------
    IP                  PICS
123.123.123.123     wpaper.gif
123.123.123.123     No Image
123.123.123.123     5star2000.gif
123.123.123.123     5star.gif
123.123.123.123     a2hlogo.jpg
123.123.123.123     No Image
--------------
"""

print("Read data from server_log.txt")
print("-"*20)
# ----------------

# Step-1: Connect to file
# ----------------
my_log_file_handle = open(r"../log/server_log.txt", "r")

# Step-2: Read
# ----------------
file_content_in_list = my_log_file_handle.readlines()
print(file_content_in_list)

# Step-3: Disconnect
# ----------------
my_log_file_handle.close()

print("#"*40, end="\n\n")
#########################################
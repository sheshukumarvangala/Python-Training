print("Extract Info and Write to file")
print("-"*20)
# ----------------

# Step-1: Connect to file
# ----------------
my_txt_file_handle = open("log_report.txt", "w")

# Step-2: Write
# ----------------
# Write Heading: For Writing: 1) write 2) writelines 3) print-function

# Write Heading 1) write
# my_txt_file_handle.write("IP\tPICS\n")

# Write Heading 2) writelines
heading_in_list = ["IP\t", "PICS\n"]
# my_txt_file_handle.writelines(heading_in_list)

# Write Heading 3) print-function
print("IP", "PICS", sep="\t", file=my_txt_file_handle)

for each_line in file_content_in_list:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        raw_img = sp[6] # /pics/wpaper.gif
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"
        print(ip, img, sep="\t", file=my_txt_file_handle)


# Step-3: Disconnect
# ----------------
my_txt_file_handle.close()

print("""
Created 'log_report.txt', Please Check
""")

print("#"*40, end="\n\n")
#########################################
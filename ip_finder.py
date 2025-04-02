import re
import os

# Function to find a unique filename by checking if the file already exists
def get_unique_filename(base_name):
    i = 1
    # Check if the file with the current number exists
    while os.path.exists(f"{base_name}_{i}.txt"):  
        i += 1  # Increment the number if the file exists
    return f"{base_name}_{i}.txt"  # Return the filename with the unique number

# Open and read the log file
with open("log.txt", "r") as file:  # log.txt = file containing log data
    logs = file.read()

# Regex to find IP addresses in the log data
ips = set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', logs))  # Using set to remove duplicates

# Get a unique filename for the output file
output_filename = get_unique_filename("ips_encontrados")

# Save the unique IPs into the output file
with open(output_filename, "w") as output:
    output.write("\n".join(sorted(ips)))  # Save the IPs in sorted order

print(f"{len(ips)} unique IPs found and saved in {output_filename}!")  # Inform the user about the number of IPs found


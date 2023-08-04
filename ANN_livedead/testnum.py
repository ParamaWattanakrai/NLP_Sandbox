import csv

def list_to_csv(data_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data_list)

# Example list
my_list = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "San Francisco"],
    ["Bob", 40, "Los Angeles"]
]

# Calling the function to convert and save the list to a CSV file
list_to_csv(my_list, "output.csv")
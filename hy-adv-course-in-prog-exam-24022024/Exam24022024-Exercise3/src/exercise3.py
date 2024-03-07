def save_data(string_list: list, file_name="shoppinglist.csv"):
    with open(file_name, "w", encoding="utf-8") as file:
        for string in string_list:
            # Split the string into its components
            components = string.split(", ")
            units_list = []
            for micro in components:
                micro = micro.split(": ")
                units_list.append(micro[1])
            
            formatted_string = ";".join(units_list)
            file.write(formatted_string + "\n")
    return

def load_data(filename="file.csv"):
    finished_list = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            components = line.strip().split(";")
            formatted_string = ""
            for i, component in enumerate(components):
                labels = ["name", "unit price", "quantity", "total price"]
                formatted_string += f"{labels[i]}: {component}, "
            # Remove the extra comma and space from the end
            formatted_string = formatted_string[:-2]
            finished_list.append(formatted_string)
    return finished_list


string_list2 = load_data(filename="file.csv")
string_list  = [
    "name: apple, unit price: 1.60€/kg, quantity: 2.2kg, total price: 3.52€",
    "name: potato, unit price: 1.30€/kg, quantity: 5.0kg, total price: 6.50€",
    "name: banana, unit price: 0.95€/kg, quantity: 1.2kg, total price: 1.14€",
    "name: milk, unit price: 1.25€/l, quantity: 2.0l, total price: 2.50€",
    "name: rye bread, unit price: 2.50€/piece, quantity: 3.0pieces, total price: 7.50€"
]



save_data(string_list)
string_list2 = load_data()
for i in range(len(string_list)):
    print(string_list[i] == string_list2[i])

string_list2 = load_data(filename="file.csv")
for i in range(len(string_list2)):
    print(string_list2[i])
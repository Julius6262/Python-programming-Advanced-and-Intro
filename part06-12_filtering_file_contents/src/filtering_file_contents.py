# Write your solution here

def filter_solutions():
    correct_line = []
    incorrect_line = []
    with open("solutions.csv", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(";")
            

            result = result = eval(line[1])  # Can evaluate string, so no need to convert to int.
            
            if result == int(line[2]):  
                correct_line.append(line)

            else:
                incorrect_line.append(line)

    with open("correct.csv", "w") as new_file:
        for line in correct_line:
            line = ";".join(line)
            new_file.write(line + "\n")
            
    
    with open("incorrect.csv", "w") as my_file:
        for line in incorrect_line:
            line = ";".join(line)
            my_file.write(line + "\n")
    


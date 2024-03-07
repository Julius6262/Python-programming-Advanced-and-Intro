# Write your solution here
def store_personal_data(person: tuple):
    with open ("people.csv", "a") as file:
        count = 0
        for val in person:
            val = str(val)
            file.write(val)
            count +=1
            if count == 3:
                break
            file.write(";")
        file.write("\n") 



# Write your solution here
def print_persons(filename: str):
    import json

    with open(filename) as json_file:
        data = json_file.read()
        
        informations = json.loads(data)

        
        for info in informations:
            
            name = info["name"]
            age = info["age"]
            hobbies = info["hobbies"]
            print(f"{name} {age} years", end=" ")  
            
            if len(hobbies) > 0:
                hobbies_string = "("
                for hobby in hobbies:
                    hobbies_string += hobby + ", "
                hobbies_string = hobbies_string[:-2]    
                print(f"{hobbies_string}", end= "")
                print(")")
            else:
                print("()")

# Write your solution here


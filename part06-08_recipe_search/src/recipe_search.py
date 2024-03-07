# Write your solution here

def search_by_name(filename: str, word: str) -> list:
    all_words = {}
    output_list = []
    w_title = None  # Initialize w_title outside the loop

    with open(filename) as file:
        for w in file:
            w = w.strip()

            # Check if the stripped string is not empty before further processing
            if w:
                if w[0].isupper():
                    w_title = w
                    all_words[w_title] = []
                elif w_title is not None:
                    all_words[w_title].append(w)

    print(all_words)
    for title in all_words:
        if word.lower() in title.lower():
            output_list.append(title)
    return output_list

def search_by_time(filename: str, prep_time: int):
    all_words = {}
    output_list = []
   
    with open(filename) as file:
        for w in file:
            w = w.strip()

            # Check if the stripped string is not empty before further processing
            if w:
                if w[0].isupper():  # The title/name of the recipe always start we an uppercase letter
                    w_title = w
                    all_words[w_title] = []
                elif w_title is not None:
                    all_words[w_title].append(w)
    
    
    for key,value in all_words.items():
        recipe_time = int(all_words[key][0])  # Time is always the first index in the value
        
        if recipe_time <= prep_time:
            output_list.append(f"{key}, preparation time {recipe_time} min")
        
        
    return output_list

def search_by_ingredient(filename: str, ingredient: str):

    all_words = {}
    output_list = []
   
    with open(filename) as file:
        for w in file:
            w = w.strip()

            # Check if the stripped string is not empty before further processing
            if w:
                if w[0].isupper():  # The title/name of the recipe always start we an uppercase letter
                    w_title = w
                    all_words[w_title] = []
                elif w_title is not None:
                    all_words[w_title].append(w)
    
    
    for key,value in all_words.items():
        if ingredient.lower() in all_words[key]:
            recipe_time = int(all_words[key][0])
            output_list.append(f"{key}, preparation time {recipe_time} min")
        
        
    return output_list

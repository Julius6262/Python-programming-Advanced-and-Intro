def retrieve_all():
    import urllib.request
    import json

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    try:
        list_tuples = []
        my_request = urllib.request.urlopen(url)
        
        data = json.loads(my_request.read().decode('utf-8'))
        
        for d in data:
            
            for key, value in d.items():
                if key == "enabled" and value != False:
                    tup = ()
                    tup += (d["fullName"], d["name"], d["year"], sum(d["exercises"]))
            
                    list_tuples.append(tup)
        # Build the formatted string
        result = "[\n"
        for t in list_tuples:
            result += f"    {t},\n"
        result = result[:-2] + "\n" + "]\n"

        return result
            
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return

    
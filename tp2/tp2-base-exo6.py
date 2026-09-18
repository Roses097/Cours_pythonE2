import requests 

def get_university_data(country = "France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data

#name
#country 
#alpha_two_code
# state-province
#domains (list)
#web_pages (list)

if __name__ == "__main__":
    state = []
    school_name = []
    
    uni_data = get_university_data("France")
    print(len(uni_data))
    
    
    for university in uni_data: #so for each uni_data[X], so uni_data[X] = university for each iteration
        statename = university["state-province"]
        if statename not in state: # name is unidata[]
            state.append(statename)
    
    for states in state:
        print(f"STATE : {states}")
        for university in uni_data:
            if university["state-province"] == states:
                school_name.append(university["name"])
                
                
    
    

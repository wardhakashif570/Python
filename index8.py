def check(abc):
    if len(abc) >= 2 and abc[:2] == "is":
        return abc
    
    return "is" + abc
        
print(check("warda"))        
print(check("issana"))
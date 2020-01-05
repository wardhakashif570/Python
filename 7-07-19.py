import csv


with open("index.csv") as f:
    contents_of_f = csv.reader(f)
    potter_competitions = []
    for each_line in contents_of_f:
        potter_competitions += each_line
# print(potter_competitions)


#to take input
def add_word():
    eng = raw_input("Enter the english word")
    urdu = raw_input("Enter the urdu word")
    with open("index.csv", "ab",) as f:
        data_handler = csv.writer(f, delimiter=",")
        data_handler.writerow([eng , urdu])
target = int(input('Enter your choice (press 1()  if you want the meaning  (press 2) if you want to add new word:'))
#target = target.lower()
if target == 1:
    word = input("Enter the word")
    if word in potter_competitions:
        print("item is present")
        index = potter_competitions.index(word)
        if potter_competitions.index(word) % 2 == 0:
            print("The meaning of " + potter_competitions[index] + " is " + potter_competitions[index +1])
        else:
            print("The meaning of " + potter_competitions[index] + " is " + potter_competitions[index - 1])    
     
    else:
        print("Item is not present")

elif target == 2:
    add_word()

# make a list to hold onto our items
shopping_list = []

# print out instuctions on how to use app
print("What should we pick up at the store?")
print("enter 'DONE' to stop adding items")



while True:
    # ask for new items
    new_item = input("> ")
    
    if new_item == 'DONE':
        break

    # add new items to our list
    shopping_list.append(new_item)
    

# be able to quit app


# print out list

print("Here's your list:" )

for item in shopping_list():
    print(item)

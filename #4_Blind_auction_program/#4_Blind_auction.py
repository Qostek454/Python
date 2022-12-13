
# Variables
bidders_list = [] 
other_bidders = 'yes'
name = ""
bid= 0
max_bid = 0
winners_name = ""

# function
def add_to_bidders_list(name_value,bid_value):
    bidders_list.append({"Name":name_value,"Bid": bid_value})
def clear():
    print('\n'*50)
    
# main code
while other_bidders != 'no':
    name = str(input("What is your name?: "))
    bid = int(input("What's your bid?: "))
    # check if max bid
    if bid > max_bid:
        max_bid = bid
        winners_name = name
        other_bidders = str(input("Are there any onther bidders Type 'yes' or 'no'"))
    else:
        other_bidders = str(input("Are there any onther bidders Type 'yes' or 'no'"))
    add_to_bidders_list(name,bid)
    clear()  

# Print result 
print(f"The winner is {winners_name} with a bid of ${max_bid}.")

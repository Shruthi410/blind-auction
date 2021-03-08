from replit import clear

from art import logo
print(logo)

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder] 
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with the bid of ${highest_bid}")


should_continue = True
while should_continue:
  name = input("Enter your name:")
  bid_amount = int(input("How much do you want to bid? $"))

  auction = {}
  auction[name] = bid_amount

  no_of_bidders = input("Are there any other users who want to bid?")
  if no_of_bidders == "yes":
    clear()
    should_continue = True

  elif no_of_bidders == "no":
    should_continue = False
    clear()
    highest_bidder(auction)


def find_hghst_bid(bidding_dict):
  hıghest_bid = 0
  for bidder in bidding_dict:
    bid_amount = bidding_dict[bidder]
    if(bid_amount >hıghest_bid):
      hıghest_bid = bid_amount
      winner =bidder
  print(f" The winner is {winner} with a bid of ${hıghest_bid}")

bids={}

continue_bidding = True

while continue_bidding:
  name = input ("What is your name ? : ")
  price = int(input("What is your bid ? :$ "))
  bids [name] = price
  should_continue = input(" Are there any other biders ? Type 'yes' or 'no' . \n").lower()  
  if should_continue ==   "no":
    continue_bidding = False
    find_hghst_bid(bids)
  elif should_continue == "yes":
    print("\n" *20)



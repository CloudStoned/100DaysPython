bidders = {}
auctionIsTrue = True

while  auctionIsTrue:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    choice = input("Are there any other biders? Yes or No: ").lower()
    bidders[name] = bid
    
    highest_bidder = max(bidders, key = lambda x: bidders[x])

    """
    high_amount = 0
    winner = ""
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > high_amount:
            high_amount = bid_amount
            winner = high_amount
    """

    print(f"Highest Bidder is {highest_bidder} amounting {bidders[highest_bidder]}")

    if choice == 'no':
        auctionIsTrue = False


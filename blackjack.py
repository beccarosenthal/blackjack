###
playing_game = True

from random import shuffle

def introductions():
    print "\nWelcome to Blackjack!\n"
    print "Do you need a refresher course on the rules?"
    print_rules = raw_input("> Y/N ")
    if print_rules.lower() == "y":
        prints_blackjack_rules()
    else:
        print "No need for rules. Let's see how good you are!"


def prints_blackjack_rules():
    """prints rules of blackjack"""
    print """
    When prompted, you will enter the amount of money you would like to gamble today and then told to enter your bet. You will then be dealt two cards. Your objective is to beat the dealer and get a hand value as close to 21 as possible without going over. Aces are worth 11 or 1, face cards are worth 10, and numbered cards are worth their value.

    Hit means 'take another card'; stay means keep your hand as is.

    If you win, you win the value of your bet. If your initial two card hand is valued at 21, you have a 'Blackjack', and you get back three times your bet. If you lose, you lose everything you bet.

    You'll get the hang of it!"""


def prints_sidebet_rules(): #I'm really proud of the rhyme scheme on this section
    """prints rules of sidebet in rhyme...because duh"""

    print """\nAhhh...so you want to hear about the sidebet.

    They say that sidebets are for suckers
    So like candy you may be.
    Sure the odds aren't in your favor,
    But no risk means no glory.

    If your first two cards are suited,
    You'll be paid back two to one.
    If the dealer wins the hand,
    sure, you will lose. But you'll have won.

    If your first two cards are suited
    AND are married, king and queen,
    Ten to one will be your fortune
    Bragging rights your currency.

    If you opt out on this hand,
    you may opt in next time around.
    But your odds will get no better.
    There's no use in waiting around.\n
    """


def guage_interest_in_sidebet(chips_remaining):
    """asks user if they want to play sidebet, lets them read rules if they want, returns T/F"""
    if chips_remaining == 0:
        return False
    valid_answer = False
    while valid_answer == False:

        print "\nWould you like to play the sidebet?\n"
        print "Enter Y/N"
        print "(Enter 'rules' to read the rules.)"
        play_sidebet = raw_input("> ")

        if play_sidebet.lower() == "y":
            valid_answer = True
            return True
        elif play_sidebet.lower() == "n":
            print "You will not play the sidebet"
            valid_answer = True
            return False
        elif play_sidebet.lower() == "rules" or play_sidebet.lower() == "r":
            prints_sidebet_rules()
        else:
            print "That is not a valid answer. Please try again"

def determine_sidebet_win(hand):
    """see if two card hand is suited, and if so, is it a married pair"""
    suit = []
    value = []
    for card in hand:
        suit.append(card[len(card)-2:])
        value.append(card[0])

    if suit[0] == suit[1]:
        if value[0] == "K" and value[1] == "Q":
            return "married suited pair"
        elif value[0] == "Q" and value[1] == "K":
            return "married suited pair"
        else:
            return "suited pair"

    return False


def chips_to_gamble():
    """asks user for $ value, verifies it, returns int"""
    print
    valid_chips_to_gamble = False
    while valid_chips_to_gamble == False:

        print "How many chips would you like to buy from the house today?\nRemember, it's fake money."

        chips = raw_input("$ ")
        if chips.isdigit() == False:
            print "That is not a valid amount. Try again."
        elif int(chips) > 0:
            valid_chips_to_gamble == True
            return int(chips)
        else:
            print "That is not a valid amount. Try again."


def place_your_bet():
    """asks user for bet, verifies it, returns bet as int"""
    print "\nYou have ${} worth of chips remaining.".format(chips_remaining)
    print

    valid_bet = False
    while valid_bet == False:

        print "How much would you like to bet?"
        bet = raw_input(" $ ")

        if bet.isdigit() == False:
            print "That is not a valid bet. Try again."
        elif int(bet) > 0 and chips_remaining - int(bet) > 0:
            valid_bet == True
            print "You bet ${}".format(bet)
            return int(bet)
        elif int(bet) > 0 and chips_remaining - int(bet) == 0:
            valid_bet == True
            print "You bet ${}".format(bet)
            print "\nYou're all in. Good luck!"
            return int(bet)
        else:
            print "That is not a valid bet. Try again"


def place_sidebet(chips_remaining):
    """gets user input for sidebet, verifies it, returns sidebet"""

    if chips_remaining == 0:
        print "You have no chips to bet on the sidebet. Hope your hand goes well."
        return 0

    valid_sidebet = False
    while valid_sidebet == False:
        print "\nHow much would you like to bet for the sidebet?"
        side_bet_amount = raw_input("$ ")

        if side_bet_amount.isdigit() == False:
            print "That is not a valid sidebet. Try again"
        elif int(side_bet_amount) > 0 and chips_remaining - int(side_bet_amount) > 0:
            valid_sidebet = True
            print "You bet ${} on the sidebet.".format(side_bet_amount)
            return int(side_bet_amount)
        elif int(side_bet_amount) > 0 and chips_remaining - int(side_bet_amount) >= 0:
            valid_sidebet = True
            print "You bet ${} on the sidebet.".format(side_bet_amount)
            print "\nYou're all in. Good luck!"
            return int(side_bet_amount)
        else:
            print "That is not a valid amount."

def hand_value(hand):
    """takes list, returns sum of card_values in the list"""

    sum_of_cards = 0
    for card in hand:
        if card[0].isdigit() == True:
            sum_of_cards = sum_of_cards + int(card[0])
        elif card[0] == "T" or card[0] == "J" or card[0] == "Q" or card[0] == "K":
            sum_of_cards = sum_of_cards + 10
        elif card[0] == "A": #card is Ace
            sum_of_cards = sum_of_cards + 11

    if sum_of_cards > 21:
        for card in hand:
            if card[0] == "A":
                sum_of_cards = sum_of_cards - 10
            if sum_of_cards < 21:
                return sum_of_cards

    return sum_of_cards


def build_full_shuffled_deck():
    """builds 52 card shuffled deck, returns as deck []"""

    numbers = range(2, 10)
    numbers.extend(['Ten', 'Jack', 'Queen', 'King', 'Ace'])
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    deck = []

    for suit in suits:
        for number in numbers:
            deck.append(str(number) + " of " + suit)

    shuffle(deck)
    return deck


def deal_two_cards(deck):
    """takes two cards from deck and puts them in hand"""

    hand = []
    while len(hand) < 2:
        hand.append(deck.pop())

    return hand


def is_it_blackjack(hand):
    """determines if two card hand is blackjack; returns booleon"""

    if hand_value(hand) == 21 and len(hand) == 2:
        is_blackjack = True
    else:
        is_blackjack = False
    return is_blackjack

def is_player_ready():
    """determines if player is ready, if they are, goes to hit or stay """
    player_turn = 0
    while player_turn != "y":
        player_turn = raw_input("Ready to play your hand? Y/N ").lower()

        if player_turn == "y":
            player_turn = True
            player_chooses_hit_or_stay()
            break
        elif player_turn == "n":
            print "The house gets your bet."
            print "You leave with ${} worth of chips.".format(chips_remaining)
            print "Have a nice life."
            end_game()
        else:
            print "There are no wrong answers...except for that one...try again"


def prints_dealer_card_showing():
    """prints first card in dealer's hand"""
    print "\nDealer has {} showing.".format(dealer_hand[0])


def dealer_turn():
    """plays out the dealer's turn, goes to who_wins function"""
    print "Dealer's turn\n"

    if hand_value(dealer_hand) >= 17 and len(dealer_hand) == 2:
        print "Dealer's hand:", dealer_hand
        print "\nThe dealer's hand value is set at {}.".format(hand_value(dealer_hand))
        print
        who_wins()
    elif hand_value(dealer_hand) < 21: #not sure why i put 21 not 17...
        print "Dealer's hand:", dealer_hand
        print "Dealer hand value:", hand_value(dealer_hand)
        print "The dealer must hit until the value is at least 17!"
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print "\nDealer's hand:", dealer_hand
        print "Dealer hand value:", hand_value(dealer_hand)
        print

        if hand_value(dealer_hand) > 21:
            print dealer_hand
            print "BUSTED"
            who_wins()
        elif 21 >= hand_value(dealer_hand) >= 17:
            print "The dealer's hand is set at {}.".format(hand_value(dealer_hand))
            print
            who_wins()

def who_wins(): #at each condition, make player wins, dealer wins, or push = true
    """returns player, dealer, or push"""

    if hand_value(player_hand) > 21:
        return 1
    elif hand_value(dealer_hand) > 21:
        return 0
    elif hand_value(player_hand) == 21 and len(player_hand) == 2:
        if hand_value(dealer_hand) == 21:
            return 3
        else:
            return "blackjack"
    elif hand_value(player_hand) > hand_value(dealer_hand):
        return 0
    elif hand_value(dealer_hand) > hand_value(player_hand):
        return 1
    else:
        return 3

def prints_sidebet_results():
    "Prints out the results of the sidebet"
    if determine_sidebet_win(player_hand) == "married suited pair":
        print "Congrats! It's a married suited pair!"
        print "You won the sidebet!"
        print "You win ${}!".format(sidebet * 10)
        print "\nNow onto the main hand.\n"
    elif determine_sidebet_win(player_hand) == "suited pair":
        print "Congrats! It's a suited pair!"
        print "You won the sidebet!"
        print "You win ${}!".format(sidebet * 3)
        print "\nNow onto the main hand, \n"
    else:
        print "Sorry. You lost the sidebet."
        print "The house keeps your ${} sidebet.".format(sidebet)
        print

def reconcile_sidebet():
    """returns the amount to be added to chips remaining due to sidebet"""
    winnings = 0

    if determine_sidebet_win(player_hand) == "married suited pair":
        winnings = sidebet * 10
    elif determine_sidebet_win(player_hand) == "suited pair":
        winnings = sidebet * 3
    else:
        winnings = 0

    return winnings

def reconcile_bet(): #now includes sidebet
    """returns new value of chips remaining"""

    if who_wins() == 0:
        print "Player wins!\n"
        print "You win ${}!".format(bet * 2)
        print
        return chips_remaining + bet * 2 + int(reconcile_sidebet())
    elif who_wins() == 1:
        print "Dealer wins!\n"
        print "The house keeps your ${} bet.".format(bet)
        print
        return chips_remaining + int(reconcile_sidebet())
    elif who_wins() == "blackjack": #is_it_blackjack(player_hand) == True:
        print
        return chips_remaining + bet * 3 + int(reconcile_sidebet())
    elif who_wins() == 3: #push
        print "It's a push. \n"
        print "The house returns your ${} bet.".format(bet)
        print
        return chips_remaining + bet + int(reconcile_sidebet())

def player_chooses_hit_or_stay():
    """asks if player wants to hit or stay, returns player_move"""

    print "\nPlayer hand: ", player_hand
    print "Hand value:", hand_value(player_hand)

    prints_dealer_card_showing()
    print

    if play_sidebet == True and len(player_hand) == 2:
        prints_sidebet_results()

    if play_sidebet == False and len(player_hand) == 2:
        if determine_sidebet_win(player_hand) == "married suited pair" or determine_sidebet_win(player_hand) ==  "suited pair":
            print "It's a shame you didn't play the sidebet..."
            print "You would have won a huge payout."
            print "\nJust saying\n"
            print "..."
            print
            print "Back to the main action:"


    print "Hit or Stay?"

    hit = ["hit", "Hit", "HIT", "h", "H"]
    stay = ["stay", "Stay", "STAY", "s", "S"]

    player_move = 0

    while player_move not in hit and player_move not in stay:

        player_move = raw_input("> ").lower()

        if player_move in hit:
            hit_me_baby_one_more_time(deck)
        elif player_move in stay:
            stay_with_me()
        else:
            "Try again"

def hit_me_baby_one_more_time(deck):
    """appends one card from deck into hand"""
    player_hand.append(deck.pop())

    if hand_value(player_hand) > 21:
        print player_hand
        print hand_value(player_hand)
        print "\nYou busted.\n"
        who_wins()
    else:
        player_chooses_hit_or_stay()

def stay_with_me():
    """prints player's final hand/value; goes on to dealer's turn"""

    print "\nYou chose to stay.\n"
    print "Your final hand is:", player_hand
    print "Your final hand value is:", hand_value(player_hand)
    print "\nAre you ready for the dealer's turn?"

    go = raw_input(" > Y/N ").lower() #Just to make the player have to do something
    if go == "n":
        print "Too bad"
    dealer_turn()

def end_game():
    exit()

def wanna_play_again():
    """if player wants to play again, return playing game == True"""
    print "Do you want to play again? "
    play_again = raw_input(" > Y/N ").lower()

    if play_again == "y":
        playing_game = True

        print "Great! Let's play again."
        return playing_game

    else:
        print "Thank you for playing blackjack. Have a nice life. "
        print "You leave the game with ${}.".format(chips_remaining)
        end_game()

##Welcome to game, generate how much player is gambling
introductions()

chips_remaining = chips_to_gamble()   #to start
###Make gameplay happen###
while playing_game == True:

    deck = build_full_shuffled_deck()
    player_hand = []
    dealer_hand = []

#dealing the initial two cards to player, two cards to dealer
    player_hand.extend(deal_two_cards(deck))
    dealer_hand.extend(deal_two_cards(deck))

    # place_your_bet()
    bet = place_your_bet()
    chips_remaining = chips_remaining - bet

        ###If they want to play sidebet, it will return as True; otherwise, False

    play_sidebet = guage_interest_in_sidebet(chips_remaining)
    if play_sidebet == True:
        sidebet = place_sidebet(chips_remaining)
    else:
        sidebet = 0

    chips_remaining = chips_remaining - sidebet
    print

    if chips_remaining > 0:
        print "Cards are dealt.\n"

#check for blackjacks; if none, play the game (is_player_ready()
    if is_it_blackjack(player_hand) == True and is_it_blackjack(dealer_hand) != True:
        print player_hand
        print dealer_hand
        if play_sidebet == True:
            print "You lost your ${} sidebet but...".format(sidebet)
            print 2 * "... \n"
        print "YOU GOT A BLACKJACK! CONGRATS"
        print "YOU WIN YOUR BET BACK PLUS ${}".format(str(bet*2))
        print
    elif is_it_blackjack(player_hand) == True and is_it_blackjack(dealer_hand) == True:
        print "YOU GOT A BLACKJACK! CONGRATS"
        print "Unfortunately, so did the dealer."
    elif is_it_blackjack(dealer_hand) == True:
        print "The dealer has a blackjack"
    else:
        is_player_ready()
#After the gameplay has happened, reconcile bet
    chips_remaining = reconcile_bet()

    if chips_remaining == 0:
        print "You ran out of chips. Come back again if you want to lose more money. \n \n"
        print "Remember, the house always wins."
        end_game()

    wanna_play_again()

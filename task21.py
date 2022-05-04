RANKS = "6789TJQKA"
COLOURS = "SCDH"


def check_same_colour(cards, card_to_beat):
    return [card for card in cards
            if card[1] == card_to_beat[1]
            and RANKS.index(card[0]) > RANKS.index(card_to_beat[0])]


def get_trump_cards(cards, trump_colour):
    return [card for card in cards
            if card[1] == trump_colour]


def get_beating_cards(my_cards, opponent_cards):
    beating_cards = []
    for op_card in opponent_cards:
        beating_cards += check_same_colour(my_cards, op_card)
    return list(set(beating_cards))


def can_beat_cards(trump_colour, my_cards, op_cards):
    my_trumps = get_trump_cards(my_cards, trump_colour)
    op_trumps = get_trump_cards(op_cards, trump_colour)

    my_cards = [card for card in my_cards if card not in my_trumps]
    op_cards = [card for card in op_cards if card not in op_trumps]

    beating_trumps = get_beating_cards(my_trumps, op_trumps)
    beating_cards = get_beating_cards(my_cards, op_cards)

    if len(beating_trumps) >= len(op_trumps):

        extra_trumps = beating_trumps[len(beating_trumps)-1:] \
            if len(beating_trumps) > len(op_trumps) \
            else []

        if len(beating_cards) >= len(op_cards):
            return "YES"
        else:
            my_trumps = [trump for trump in my_trumps if trump not in beating_trumps] + extra_trumps
            if len(beating_cards) + len(my_trumps) >= len(op_cards):
                return "YES"

    return "NO"


with open("input.txt", 'r') as f:
    datafile = f.readlines()

result = can_beat_cards(datafile[0].split()[2],
                        datafile[1].split(),
                        datafile[2].split())

with open("output.txt", 'w') as f:
    f.write(str(result))



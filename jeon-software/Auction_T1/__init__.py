from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Auction_T1'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    bid_1 = models.FloatField(label="",
                              max=20,
                              min=0)
    opponent_bid_1 = models.FloatField(label="",
                              max=20,
                              min=0)
    is_winner_1 = models.StringField(initial="None")

    entry_2 = models.StringField(initial="None")
    bid_2 = models.FloatField(label="",
                              max=20,
                              min=0,)
    is_winner_2 = models.StringField(initial="None")

    computer_3 = models.FloatField(label="",
                              max=20,
                              min=0)
    bid_3 = models.FloatField(label="",
                              max=20,
                              min=0)
    is_winner_3 = models.StringField(initial="None")

    entry_4 = models.StringField(initial="None")
    bid_4 = models.FloatField(label="",
                              max=20,
                              min=0)

    is_winner_4 = models.StringField(initial="None")


# def set_winner1(group: Group):
#     import random
#     players = group.get_players()
#     highest_bid = max([p.bid_1 for p in players])
#     players_with_highest_bid = [p for p in players if p.bid_1 == highest_bid]
#     winner = random.choice(players_with_highest_bid)  # if tie, winner is chosen at random
#     winner.is_winner_1 = "WON"
#     players_not_winner = [p for p in players if p is not winner]
#     for k in players_not_winner:
#         k.is_winner_1 = "LOSE"

def set_winner1(player: Player):
    import random
    opponent = player.get_others_in_group()[0]
    player.opponent_bid_1 = opponent.bid_1
    if player.bid_1 > player.opponent_bid_1:
        player.is_winner_1 = "WON"
    elif player.bid_1 == player.opponent_bid_1:
        player.is_winner_1 = random.choice(["WON","LOSE"])
    elif player.bid_1 < player.opponent_bid_1:
        player.is_winner_1 = "LOSE"

def set_winner2(player: Player):
    import random
    opponent = player.get_others_in_group()[0]
    if player.entry_2 == "EXIT":
        player.is_winner_2 = "EXITED"
    elif player.entry_2 == "ENTER":
        if player.bid_2 > opponent.bid_1:
            player.is_winner_2 = "WON"
        elif player.bid_2 == opponent.bid_1:
            player.is_winner_2 = random.choice(["WON","LOSE"])
        elif player.bid_2 < opponent.bid_1:
            player.is_winner_2 = "LOSE"


def set_winner3(player: Player):
    import random
    if player.bid_3 > player.computer_3:
        player.is_winner_3 = "WON"
    elif player.bid_3 == player.computer_3:
        player.is_winner_3 = random.choice(["WON","LOSE"])
    elif player.bid_3 < player.computer_3:
        player.is_winner_3 = "LOSE"

def set_winner4(player: Player):
    import random
    if player.entry_4 == "EXIT":
        player.is_winner_4 = "EXITED"
    elif player.entry_4 == "ENTER":
        if player.bid_4 > player.computer_3:
            player.is_winner_4 = "WON"
        elif player.bid_4 == player.computer_3:
            player.is_winner_4 = random.choice(["WON", "LOSE"])
        elif player.bid_4 < player.computer_3:
            player.is_winner_4 = "LOSE"

# PAGES


class Game1(Page):
    form_model = 'player'
    form_fields = ['bid_1']


class ResultsWaitPage1(WaitPage):
    # def after_all_players_arrive(group: Group):
    #     set_winner1(group)

    def after_all_players_arrive(group: Group):
        for p in group.get_players():
            set_winner1(p)

class Game2(Page):
    form_model = 'player'
    form_fields = ['entry_2','bid_2']

    def before_next_page(player, timeout_happened):
        import random
        player.computer_3 = round(random.uniform(0, 10.00), 2)

class ResultsWaitPage2(WaitPage):
    def after_all_players_arrive(group: Group):
        for p in group.get_players():
            set_winner2(p)

class Game3(Page):
    form_model = 'player'
    form_fields = ['bid_3']

    def before_next_page(player, timeout_happened):
        set_winner3(player)

class Game4(Page):
    form_model = 'player'
    form_fields = ['entry_4','bid_4']

    def before_next_page(player, timeout_happened):
        set_winner4(player)
        player.participant.is_winner_1 = player.is_winner_1
        player.participant.is_winner_2 = player.is_winner_2
        player.participant.is_winner_2 = player.is_winner_2
        player.participant.is_winner_3 = player.is_winner_3
        player.participant.is_winner_4 = player.is_winner_4
        player.participant.bid_1 = player.bid_1
        player.participant.bid_2 = player.bid_2
        player.participant.bid_3 = player.bid_3
        player.participant.bid_4 = player.bid_4
        player.participant.entry_2 = player.entry_2
        player.participant.entry_4 = player.entry_4
        player.participant.opponent_bid_1 = player.opponent_bid_1
        player.participant.computer_3 = player.computer_3

class MyWaitPage(WaitPage):
    template_name = 'Auction_T1/MyWaitPage.html'
    wait_for_all_groups = True

class Page5(Page):
    pass

class Wait(WaitPage):
    # def after_all_players_arrive(group: Group):
    #     set_winner1(group)

    # title_text = "Custom title text"
    body_text = "Please wait for your opponent to arrive."
    def after_all_players_arrive(group: Group):
        pass

page_sequence = [Page5,  Wait, Game1, ResultsWaitPage1, Game2, ResultsWaitPage2, Game3, Game4 ]

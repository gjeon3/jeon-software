from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Out'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part_selected = models.StringField(initial="N/A")
    event_selected = models.StringField(initial="N/A")
    task_selected = models.StringField(initial="N/A")

    spin_p = models.IntegerField(initial="N/A")
    spin_e = models.IntegerField(initial="N/A")
    spin_t = models.IntegerField(initial="N/A")

    pay_1 = models.FloatField()
    pay_2 = models.FloatField()
    pay_3 = models.FloatField()
    pay_4 = models.FloatField()

    pay_part = models.FloatField()
    pay_final = models.FloatField()

def set_pay_part1(player: Player):
    if player.event_selected == "A":
        if player.participant.own_risk == 1:
            risk = 16
        elif player.participant.own_risk == 2:
            risk = 24
        elif player.participant.own_risk == 3:
            risk = 32
        elif player.participant.own_risk == 4:
            risk = 40
        elif player.participant.own_risk == 5:
            risk = 48
        player.pay_final = 3 + risk + 2
        player.pay_part = risk
    elif player.event_selected == "B":
        if player.participant.own_risk == 1:
            risk = 16
        elif player.participant.own_risk == 2:
            risk = 12
        elif player.participant.own_risk == 3:
            risk = 8
        elif player.participant.own_risk == 4:
            risk = 4
        elif player.participant.own_risk == 5:
            risk = 0
        player.pay_final = 3 + risk + 2
        player.pay_part = risk

def set_pay_part2(player: Player):
    if player.task_selected == "1":
        task = player.pay_1
        player.pay_final = 3 + task + 2
        player.pay_part = task
    elif player.task_selected == "2":
        task = player.pay_2
        player.pay_final = 3 + task + 2
        player.pay_part = task
    elif player.task_selected == "3":
        task = player.pay_3
        player.pay_final = 3 + task + 2
        player.pay_part = task
    elif player.task_selected == "4":
        task = player.pay_4
        player.pay_final = 3 + task + 2
        player.pay_part = task
    else:
        pass

class Out1(Page):


    def before_next_page(player, timeout_happened ):
        is_winner_1 = player.participant.is_winner_1
        is_winner_2 = player.participant.is_winner_2
        is_winner_3 = player.participant.is_winner_3
        is_winner_4 = player.participant.is_winner_4
        bid_1 = player.participant.bid_1
        bid_2 = player.participant.bid_2
        bid_3 = player.participant.bid_3
        bid_4 = player.participant.bid_4

        if is_winner_1 == "WON":
            player.pay_1 = 20 - float(bid_1) + 10
        elif is_winner_1 == "LOSE":
            player.pay_1 = 20 - float(bid_1)

        if is_winner_2 == "WON":
            player.pay_2 = 20 - float(bid_2) + 10
        elif is_winner_2 == "LOSE":
            player.pay_2 = 20 - float(bid_2)
        elif is_winner_2 == "EXITED":
            player.pay_2 = 20

        if is_winner_3 == "WON":
            player.pay_3 = 20 - float(bid_3) + 10
        elif is_winner_3 == "LOSE":
            player.pay_3 = 20 - float(bid_3)

        if is_winner_4 == "WON":
            player.pay_4 = 20 - float(bid_4) + 10
        elif is_winner_4 == "LOSE":
            player.pay_4 = 20 - float(bid_4)
        elif is_winner_4 == "EXITED":
            player.pay_4 = 20

class ResultsWaitPage(WaitPage):
    pass


class Part(Page):
    form_model = 'player'
    form_fields = ['part_selected']

    # def vars_for_template(player: Player):
    #     rngp = player.rngp
    #     return dict(
    #         rng = rngp,
    #     )
    #
    # def before_next_page(player, timeout_happened ):
    #     import random
    #     rnge = random.randint(360, 720)
    #     player.rnge = rnge
    #     rngt = random.randint(360, 720)
    #     player.rngt = rngt
        # player.participant.task_selected = player.task_selected
        # player.participant.event_selected = player.event_selected

class Event(Page):
    form_model = 'player'
    form_fields = ['event_selected']
    def is_displayed(player: Player):
        return player.part_selected == "1"

    def before_next_page(player, timeout_happened ):
        set_pay_part1(player)
    #
    # def vars_for_template(player: Player):
    #     rnge = player.rnge
    #     return dict(
    #         rng = rnge,
    #     )

class Task(Page):
    form_model = 'player'
    form_fields = ['task_selected', ]
    def is_displayed(player: Player):
        return player.part_selected == "2"
    #
    # def vars_for_template(player: Player):
    #     rngt = player.rngt
    #     return dict(
    #         rng = rngt,
    #     )

    def before_next_page(player, timeout_happened ):
        set_pay_part2(player)





class Out2(Page):
    def vars_for_template(player: Player):
        return dict(
        )

class OutT(Page):

    def vars_for_template(player: Player):

        own_risk = player.participant.own_risk
        if own_risk == 1:
            part1_text = "Your selection: Gamble 1 (Event A,  $16; Event B, $16)"
        elif own_risk == 2:
            part1_text = "Your selection: Gamble 2 (Event A, $24; Event B, $16)"
        elif own_risk == 3:
            part1_text = "Your selection: Gamble 3 (Event A, $32; Event B, $8)"
        elif own_risk == 4:
            part1_text = "Your selection: Gamble 4 (Event A, $40; Event B, $4)"
        elif own_risk == 5:
            part1_text = "Your selection: Gamble 5 (Event A, $48; Event B, $0)"

        return dict(
            part_selected = player.part_selected,
            task_selected = player.task_selected,
            event_selected = player.event_selected,
            part1_text = part1_text,
            own_risk = player.participant.own_risk,
            bid_1 = player.participant.bid_1,
            is_winner_1 = player.participant.is_winner_1,
            entry_2 = player.participant.entry_2,
            bid_2 = player.participant.bid_2,
            is_winner_2 = player.participant.is_winner_2,
            computer_3 = player.participant.computer_3,
            bid_3 = player.participant.bid_3,
            is_winner_3 = player.participant.is_winner_3,
            entry_4 = player.participant.entry_4,
            bid_4 = player.participant.bid_4,
            is_winner_4 = player.participant.is_winner_4,
            opponent_bid_1 =player.participant.opponent_bid_1,
        )

class OutE(Page):
    def vars_for_template(player: Player):
        return dict(
        )
page_sequence = [Out1, Part, Task, Event, OutT, OutE]

from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Practice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bid_0 = models.StringField(blank=True, initial=999)
    computer_0 = models.StringField(blank=True, initial=999)


# PAGES


class Page4(Page):
    form_model = 'player'
    form_fields = ['bid_0','computer_0']
    timeout_seconds = 10

class Page5(Page):
    pass






page_sequence = [Page4]

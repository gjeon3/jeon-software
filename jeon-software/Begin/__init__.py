from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Begin'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Page00(Page):
    pass

class Page0(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page00, Page0]

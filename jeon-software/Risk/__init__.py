from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Risk'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    own_risk = models.IntegerField(initial=None,
                                   widget=widgets.RadioSelect,
                                   choices=[1,2,3,4,5])



# PAGES
class Risk(Page):
    form_model = 'player'
    form_fields = ['own_risk']
    def vars_for_template(player: Player):
        import random

        l = [1, 2, 3, 4, 5]
        k = random.choice(l)

        return dict(
            k = k
        )
    def before_next_page(player, timeout_happened):
        player.participant.own_risk = player.own_risk


class ResultsWaitPage(WaitPage):
    pass


class Page2(Page):
    pass


page_sequence = [Risk, Page2]

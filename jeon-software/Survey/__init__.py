from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(initial=None,blank=True)
    gender_other = models.StringField(initial=None,blank=True)
    relation = models.StringField(initial=None,blank=True)
    relation_other= models.StringField(initial=None,blank=True)
    age = models.StringField(initial="",blank=True)
    ethnicity = models.StringField(initial=None,blank=True)
    ethnicity_other = models.StringField(initial=None, blank=True)
    state = models.StringField(initial=None,blank=True)
    state_other = models.StringField(initial=None, blank=True)
    grade = models.StringField(initial=None,blank=True)
    grade_other = models.StringField(initial=None, blank=True)
    major = models.StringField(initial=None,blank=True)

    own_salary_1 = models.StringField(initial=None,blank=True)
    own_hour_1 = models.StringField(initial=None,blank=True)
    married_1 = models.StringField(initial=None,blank=True)
    spouse_salary_1 = models.StringField(initial=None,blank=True)
    spouse_hour_1 = models.StringField(initial=None,blank=True)
    nochild_1 = models.StringField(initial=None,blank=True)
    onechild_1 = models.StringField(initial=None,blank=True)
    twochild_1 = models.StringField(initial=None,blank=True)

    own_salary_2 = models.StringField(initial=None,blank=True)
    own_hour_2 = models.StringField(initial=None,blank=True)
    married_2 = models.StringField(initial=None,blank=True)
    spouse_salary_2 = models.StringField(initial=None,blank=True)
    spouse_hour_2 = models.StringField(initial=None,blank=True)
    nochild_2 = models.StringField(initial=None,blank=True)
    onechild_2 = models.StringField(initial=None,blank=True)
    twochild_2 = models.StringField(initial=None,blank=True)

    own_salary_3 = models.StringField(initial=None,blank=True)
    own_hour_3 = models.StringField(initial=None,blank=True)
    married_3 = models.StringField(initial=None,blank=True)
    spouse_salary_3 = models.StringField(initial=None,blank=True)
    spouse_hour_3 = models.StringField(initial=None,blank=True)
    nochild_3 = models.StringField(initial=None,blank=True)
    onechild_3 = models.StringField(initial=None,blank=True)
    twochild_3 = models.StringField(initial=None,blank=True)

    bno_1 = models.StringField(initial=None,blank=True)
    bno_2 = models.StringField(initial=None,blank=True)
    bno_3 = models.StringField(initial=None,blank=True)
    bno_4 = models.StringField(initial=None,blank=True)

    opp_risk = models.IntegerField(initial=None,
                                   widget=widgets.RadioSelect,
                                   choices=[1,2,3,4,5])


    gi_1 = models.StringField(initial=None,blank=True)
    gi_2 = models.StringField(initial=None,blank=True)
    gi_3 = models.StringField(initial=None,blank=True)
    gi_4 = models.StringField(initial=None,blank=True)
    gi_5 = models.StringField(initial=None,blank=True)
    gi_6 = models.StringField(initial=None,blank=True)


class Page6(Page):
    pass
class Survey0(Page):
    pass
class Survey2(Page):
    form_model = 'player'
    form_fields = ['gender','gender_other',
                   'relation','relation_other',
                   'age',
                   'ethnicity','ethnicity_other',
                   'state','state_other',
                   'grade','grade_other',
                   'major']

class Survey3(Page):
    form_model = 'player'
    form_fields = ['bno_1','bno_2','bno_3','bno_4']

class Survey1(Page):
    form_model = 'player'
    form_fields = ['opp_risk']

    def vars_for_template(player: Player):
        import random

        l = [1, 2, 3, 4, 5]
        k = random.choice(l)

        return dict(
            k = k
        )

class Survey4_25(Page):
    form_model = 'player'
    form_fields = ['own_salary_1','own_hour_1','married_1','spouse_salary_1','spouse_hour_1',
                   'nochild_1','onechild_1','twochild_1',
                   'own_salary_2', 'own_hour_2', 'married_2', 'spouse_salary_2', 'spouse_hour_2',
                   'nochild_2', 'onechild_2', 'twochild_2',
                   'own_salary_3', 'own_hour_3', 'married_3', 'spouse_salary_3', 'spouse_hour_3',
                   'nochild_3', 'onechild_3', 'twochild_3'
                   ]

    def is_displayed(player: Player):
        age = int(player.age or 20)
        return age < 25

class Survey4_30(Page):
    form_model = 'player'
    form_fields = [
                   'own_salary_2', 'own_hour_2', 'married_2', 'spouse_salary_2', 'spouse_hour_2',
                   'nochild_2', 'onechild_2', 'twochild_2',
                   'own_salary_3', 'own_hour_3', 'married_3', 'spouse_salary_3', 'spouse_hour_3',
                   'nochild_3', 'onechild_3', 'twochild_3'
                   ]

    def is_displayed(player: Player):
        age = int(player.age or 20)
        return age > 25

class Survey4(Page):
    form_model = 'player'
    form_fields = ['own_salary_1','own_hour_1','married_1','spouse_salary_1','spouse_hour_1',
                   'nochild_1','onechild_1','twochild_1',
                   'own_salary_2', 'own_hour_2', 'married_2', 'spouse_salary_2', 'spouse_hour_2',
                   'nochild_2', 'onechild_2', 'twochild_2',
                   'own_salary_3', 'own_hour_3', 'married_3', 'spouse_salary_3', 'spouse_hour_3',
                   'nochild_3', 'onechild_3', 'twochild_3'
                   ]

class Survey5(Page):
    form_model = 'player'
    form_fields = ['gi_1', 'gi_2', 'gi_3', 'gi_4','gi_5', 'gi_6']


class ResultsWaitPage(WaitPage):
    pass




# page_sequence = [Page6, Survey0, Survey2,Survey3,]

page_sequence = [Page6, Survey2,Survey3, Survey1, Survey4_25, Survey4_30, Survey5 ]

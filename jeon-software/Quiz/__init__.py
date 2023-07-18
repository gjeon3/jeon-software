from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    qset_1 = models.StringField(
    )
    qset_2 = models.StringField(
    )
    qset_3 = models.StringField(
    )
    qset_4 = models.StringField(
    )
    qset_5 = models.StringField(
    )

    aset_1 = models.StringField(
    )
    aset_2 = models.StringField(
    )
    aset_3 = models.StringField(
    )
    aset_4 = models.StringField(
    )
    aset_5 = models.StringField(
    )

    answer_1 = models.StringField(blank=False
    )
    answer_2 = models.StringField(blank=False
    )
    answer_3 = models.StringField(blank=False
    )
    answer_4 = models.StringField(blank=False
    )
    answer_5 = models.StringField(blank=False
    )

    pass_1 = models.StringField(initial="None")
    pass_2 = models.StringField(initial="None")
    pass_3 = models.StringField(initial="None")
    pass_4 = models.StringField(initial="None")
    pass_5 = models.StringField(initial="None")

    pass_key = models.StringField(initial="No")




# PAGES
class Page3(Page):

    def before_next_page(player, timeout_happened):
        import random
        qsets = []
        asets = []
        for s in range(5):
            k1 = round(random.uniform(0, 10.00), 2)
            k2 = round(random.uniform(0, 20.00), 2)
            q1 = "Suppose you bid <b>${}</b> and you <b>WIN</b>. What is your earnings?".format(k1)
            q2 = "Suppose you bid <b>$0.00</b> and you <b>WIN</b>. What is your earnings?"
            q3 = "Suppose you bid <b>$0.00</b> and you <b>LOSE</b>. What is your earnings?"
            q4 = "Suppose you bid <b>${}</b> and you <b>LOSE</b>. What is your earnings?".format(k2)
            q5 = "Suppose you bid <b>$10.00</b> and you <b>WIN</b>. What is your earnings?"
            q6 = "Suppose you bid <b>$10.00</b> and you <b>LOSE</b>. What is your earnings?"

            question1 = random.choice([q1])
            question2 = random.choice([q2, q3])
            question3 = random.choice([q4])
            question4 = random.choice([q5, q6])

            qset = [question1, question2, question3, question4]
            qset_combined = ', '.join(qset)
            qsets.append(qset_combined)

            # Determine the corresponding answers
            answer1 = round(20 - k1 + 10, 2)
            if 'WIN' in question2:
                answer2 = round(20 + 10, 2)
            else:
                answer2 = round(20, 2)
            answer3 = round(20 - k2, 2)
            if 'WIN' in question4:
                answer4 = round(20, 2)
            else:
                answer4 = round(20 - 10, 2)

            answer1 = "{:.2f}".format(answer1)
            answer2 = "{:.2f}".format(answer2)
            answer3 = "{:.2f}".format(answer3)
            answer4 = "{:.2f}".format(answer4)

            aset = [str(answer1), str(answer2), str(answer3), str(answer4)]
            aset_combined = ', '.join(aset)
            asets.append(aset_combined)

        player.qset_1 = str(qsets[0])
        player.qset_2 = str(qsets[1])
        player.qset_3 = str(qsets[2])
        player.qset_4 = str(qsets[3])
        player.qset_5 = str(qsets[4])

        player.aset_1 = str(asets[0])
        player.aset_2 = str(asets[1])
        player.aset_3 = str(asets[2])
        player.aset_4 = str(asets[3])
        player.aset_5 = str(asets[4])

class ResultsWaitPage(WaitPage):
    pass

class Check1(Page):
    form_model = 'player'
    form_fields = ['answer_1','pass_1','pass_key']

    def vars_for_template(player: Player):

        q_set_1 = player.qset_1
        q_set1 = q_set_1.split(", ")

        a_set_1 = player.aset_1
        a_set1 = a_set_1.split(", ")


        return dict(
            q_set = q_set1,
            a_set=a_set1,
        )


class Check2(Page):
    form_model = 'player'
    form_fields = ['answer_2','pass_2','pass_key']

    def is_displayed(player: Player):
        return player.pass_key == "No"

    def vars_for_template(player: Player):

        q_set_2 = player.qset_2
        q_set2 = q_set_2.split(", ")

        a_set_2 = player.aset_2
        a_set2 = a_set_2.split(", ")


        return dict(
            q_set = q_set2,
            a_set=a_set2,
        )

class Check3(Page):
    form_model = 'player'
    form_fields = ['answer_3','pass_3','pass_key']

    def is_displayed(player: Player):
        return player.pass_key == "No"

    def vars_for_template(player: Player):

        q_set_3 = player.qset_3
        q_set3 = q_set_3.split(", ")

        a_set_3 = player.aset_3
        a_set3 = a_set_3.split(", ")


        return dict(
            q_set = q_set3,
            a_set=a_set3,
        )


class Check4(Page):
    form_model = 'player'
    form_fields = ['answer_4','pass_4','pass_key']

    def is_displayed(player: Player):
        return player.pass_key == "No"

    def vars_for_template(player: Player):

        q_set_4 = player.qset_4
        q_set4 = q_set_4.split(", ")

        a_set_4 = player.aset_4
        a_set4 = a_set_4.split(", ")


        return dict(
            q_set = q_set4,
            a_set=a_set4,
        )

class Check5(Page):
    form_model = 'player'
    form_fields = ['answer_5','pass_5','pass_key']

    def is_displayed(player: Player):
        return player.pass_key == "No"

    def vars_for_template(player: Player):

        q_set_5 = player.qset_5
        q_set5 = q_set_5.split(", ")

        a_set_5 = player.aset_5
        a_set5 = a_set_5.split(", ")

        return dict(
            q_set = q_set5,
            a_set=a_set5,
        )


page_sequence = [Page3, Check1, Check2, Check3, Check4, Check5]

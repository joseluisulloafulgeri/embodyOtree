from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'embody'
    PLAYERS_PER_GROUP = None
    NUM_FIELDS =14
    TASKS = ["pyField" + str(i+1) for i in range(NUM_FIELDS)]
    #print(TASKS)
    NUM_ROUNDS = len(TASKS)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pyField1 =  models.LongStringField(blank=True)
    pyField2 = models.LongStringField(blank=True)
    pyField3 =  models.LongStringField(blank=True)
    pyField4 = models.LongStringField(blank=True)
    pyField5 =  models.LongStringField(blank=True)
    pyField6 = models.LongStringField(blank=True)
    pyField7 =  models.LongStringField(blank=True)
    pyField8 = models.LongStringField(blank=True)
    pyField9 =  models.LongStringField(blank=True)
    pyField10 = models.LongStringField(blank=True)
    pyField11 =  models.LongStringField(blank=True)
    pyField12 = models.LongStringField(blank=True)
    pyField13 =  models.LongStringField(blank=True)
    pyField14 = models.LongStringField(blank=True)
    rand_page_sequence = models.StringField()
# FUNCTIONS

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.TASKS, round_numbers))
            print('player', p.id_in_subsession)
            print('task_rounds is', task_rounds)
            p.participant.task_rounds = task_rounds
            p.rand_page_sequence = str(list(task_rounds.values())).strip('[]')



# PAGES
class Field1(Page):
    form_model = 'player'
    form_fields = ['pyField1']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField1']

class Field2(Page):
    form_model = 'player'
    form_fields = ['pyField2']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField2']
class Field3(Page):
    form_model = 'player'
    form_fields = ['pyField3']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField3']

class Field4(Page):
    form_model = 'player'
    form_fields = ['pyField4']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField4']
class Field5(Page):
    form_model = 'player'
    form_fields = ['pyField5']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField5']
class Field6(Page):
    form_model = 'player'
    form_fields = ['pyField6']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField6']
class Field7(Page):
    form_model = 'player'
    form_fields = ['pyField7']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField7']
class Field8(Page):
    form_model = 'player'
    form_fields = ['pyField8']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField8']

class Field9(Page):
    form_model = 'player'
    form_fields = ['pyField9']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField9']

class Field10(Page):
    form_model = 'player'
    form_fields = ['pyField10']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField10']

class Field11(Page):
    form_model = 'player'
    form_fields = ['pyField11']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField11']
class Field12(Page):
    form_model = 'player'
    form_fields = ['pyField12']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField12']

class Field13(Page):
    form_model = 'player'
    form_fields = ['pyField13']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField13']

class Field14(Page):
    form_model = 'player'
    form_fields = ['pyField14']
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['pyField14']

page_sequence = [Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,Field11,Field12,Field13,Field14]


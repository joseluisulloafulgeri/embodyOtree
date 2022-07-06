from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


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
# FUNCTIONS

# PAGES
class Field1(Page):
    form_model = 'player'
    form_fields = ['pyField1']


class Field2(Page):
    form_model = 'player'
    form_fields = ['pyField2']

class Field3(Page):
    form_model = 'player'
    form_fields = ['pyField3']


class Field4(Page):
    form_model = 'player'
    form_fields = ['pyField4']

class Field5(Page):
    form_model = 'player'
    form_fields = ['pyField5']

class Field6(Page):
    form_model = 'player'
    form_fields = ['pyField6']

class Field7(Page):
    form_model = 'player'
    form_fields = ['pyField7']

class Field8(Page):
    form_model = 'player'
    form_fields = ['pyField8']


class Field9(Page):
    form_model = 'player'
    form_fields = ['pyField9']


class Field10(Page):
    form_model = 'player'
    form_fields = ['pyField10']


class Field11(Page):
    form_model = 'player'
    form_fields = ['pyField11']

class Field12(Page):
    form_model = 'player'
    form_fields = ['pyField12']

class Field13(Page):
    form_model = 'player'
    form_fields = ['pyField13']


class Field14(Page):
    form_model = 'player'
    form_fields = ['pyField14']
page_sequence = [Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,Field11,Field12,Field13,Field14]

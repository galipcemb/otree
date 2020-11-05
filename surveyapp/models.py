from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'surveyapp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="Lütfen yaşınızı girin.")
    gender = models.StringField(label="Lütfen cinsiyetinizi seçin.",
                                choices=["Kadın","Erkek","Belirtmek istemiyorum"]
                                )
    courses = models.BooleanField(label="Daha önce Oyun Teorisi, Davranışsal İktisat ya da Deneysel İktisat derslerinden birini aldınız mı?",
                                  choices=[
                                      [True,"Evet"],
                                      [False, "Hayır"],
                                  ])

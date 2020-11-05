from otree.api import models
from ._builtin import Page, WaitPage
from .models import Constants

class choicepassive(Page):

    form_model = 'player'
    form_fields = ['offer_accepted']
    def is_displayed(self):
        return self.player.id_in_group == 2

    offer_accepted = models.BooleanField(label="dddd",
                                         choices=[
                                      [True,"Evet"],
                                      [False, "Hayır"],
                                  ])



    def vars_for_template(self):
        return dict(
            contribution_label='How much of your {} do you want to contribute?'.format(self.player.endowment)
        )

class Introduction(Page):
    form_model = 'group'

    def is_displayed(self):
        return self.player.id_in_group == 1

class Offer(Page):
    form_model = 'group'
    form_fields = ['sent']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.group.sent)


page_sequence = [choicepassive, Introduction, Offer, ResultsWaitPage, Results]

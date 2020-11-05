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


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = 2
    num_rounds = 1

    instructions_template1 = 'dictator/instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(10) #20


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    sent = models.CurrencyField(
        doc="""Amount dictator decided to transfer""",
        min=0,
        max=Constants.endowment,
        label="Göndermek istediğim miktar",
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent
        p2.payoff = self.sent


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return "dictator"
        else:
            return "receiver"


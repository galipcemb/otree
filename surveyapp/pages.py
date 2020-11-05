from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["age","gender","courses"]





page_sequence = [SurveyQuestions]

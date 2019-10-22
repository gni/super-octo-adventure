from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day, CustomBusinessDay
class JoursFeries(AbstractHolidayCalendar):
    """ Custom Holiday calendar for France based on
        https://en.wikipedia.org/wiki/Public_holidays_in_France
      - 1 January: Nouvel an
      - Bouge: Lundi pâques
      - Fête du travail
      - Armistice 1945
      - Bouge: Fête de l‘Ascension 39 jours après pâques
      - Fête Nationale
      - Assomption
      - Toussaint
      - Armistice 1918
      - Noël
    """
    rules = [
        Holiday('Nouvel an', month=1, day=1),
        EasterMonday,
        Holiday('Fête du travail', month=5, day=1),
        Holiday('Armistice 1945', month=5, day=8),
        Holiday('Fête de l‘Ascension', month=1, day=1, offset=[Easter(), Day(39)]),
        Holiday('Fête Nationale', month=7, day=14),
        Holiday('Assomption', month=8, day=15),
        Holiday('Toussaint', month=11, day=1),
        Holiday('Armistice 1918', month=11, day=11),
        Holiday('Noël', month=12, day=25)
    ]
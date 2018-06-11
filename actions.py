from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    """docstring for ActionWeather."""
    def __init__(self):
        super(ActionWeather, self).__init__()

    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        response =  "weather for location {loc} is awesome today tomorrow and dayafter".format(loc=loc)
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

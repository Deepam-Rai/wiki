import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, Restarted
from rasa_sdk.executor import CollectingDispatcher


logger = logging.getLogger(__name__)


class ActionRestart(Action):
    """
    name: action_restart
    description: Displays the restarted messages to indicate to the user.
    """
    def name(self) -> Text:
        return "action_restart"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Restarted...")
        return [AllSlotsReset(), Restarted()]

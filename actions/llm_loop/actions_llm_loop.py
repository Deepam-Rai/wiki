from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import logging
from actions.utils import *
from actions.constants import *


logger = logging.getLogger(__name__)


class ActionSubmitLlmLoop(Action):
    """
    name: action_submit_llm_loop
    description:
    """

    def name(self) -> Text:
        return 'action_submit_llm_loop'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []



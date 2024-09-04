import logging
from typing import List, Text, Dict, Any
from rasa_sdk import FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .constants import *


logger = logging.getLogger(__name__)


class ValidateLlmLoop(FormValidationAction):
    def name(self) -> Text:
        return "validate_llm_loop"

    async def extract_user_dialogue(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict
    ) -> Dict[Text, Any]:
        if tracker.get_slot(REQUESTED_SLOT) == USER_DIALOGUE:
            text = tracker.latest_message.get("text")
            return {USER_DIALOGUE: text}
        return {USER_DIALOGUE: tracker.get_slot(USER_DIALOGUE)}

    def validate_user_dialogue(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        if tracker.get_slot(REQUESTED_SLOT) == USER_DIALOGUE:
            dispatcher.utter_message(text="regarding this ...")
            return {
                USER_DIALOGUE: slot_value
            }
        return {USER_DIALOGUE: tracker.get_slot(USER_DIALOGUE)}

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        slots = domain_slots.copy()
        return slots

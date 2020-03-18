import IntentInterface as intent

class UnknownQnaIntent(intent.IntentInterface):
    def __init__(self):
        print('Constructor.')

    def process_intent_as_raw_string(self, bot_services, entities, user_activity):
        """Should be overridden."""
        print('Called process_intent_as_raw_string')

    def process_intent_as_slack_formatted_string(self, bot_services, entities, user_activity):
        """Should be overridden."""
        print('Called process_intent_as_slack_formatted_string')
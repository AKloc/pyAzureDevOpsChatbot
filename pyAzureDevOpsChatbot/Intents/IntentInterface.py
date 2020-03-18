class IntentInterface():

    IntentName = 'Undefined'

    def process_intent_as_raw_string(self, bot_services, entities, user_activity):
        """Should be overridden."""
        raise NotImplementedError

    def process_intent_as_slack_formatted_string(self, bot_services, entities, user_activity):
        """Should be overridden."""
        raise NotImplementedError


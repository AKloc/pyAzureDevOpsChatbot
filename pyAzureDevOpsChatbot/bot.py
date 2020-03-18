# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    # Parse the actual message and take action.
    async def on_message_activity(self, turn_context: TurnContext):
        activity = turn_context.activity

        # Python libraries don't have native mention support?
        # https://docs.microsoft.com/en-us/microsoftteams/platform/bots/how-to/conversations/channel-and-group-conversations?tabs=python
        
        # if activity.channel_id == 'slack' and activity.conversation.is_group is None:
        #     if not activity.

        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    # This gets called when someone joins the chatroom?
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

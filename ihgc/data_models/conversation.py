from datetime import datetime


class Message:
    def __init__(
        self,
        message: str,
        author: str,
        is_me: bool,
        message_id: int,
        created_at: datetime,
    ):
        """Class object to hold message data

        Args:
            message (str): Text message
            author (str): Name of author, or string-id
            is_me (bool): Was you you that sent this message?
            message_id (int): id of message
            created_at (datetime): when was the message sent?
        """

        assert isinstance(message, str)
        self.message = message

        assert isinstance(author, str)
        self.author = author

        assert isinstance(is_me, bool)
        self.is_me = is_me

        assert isinstance(message_id, int)
        self.message_id = message_id

        assert isinstance(created_at, datetime)
        self.created_at = created_at

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "author": self.author,
            "message": self.message,
            "created_at": self.created_at,
            "is_me": self.is_me,
        }


class Conversation:
    def __init__(self, messages: list, conversation_id: int):
        """Class object to hold conversation data, which is a sequence of messages

        Args:
            messages (list[Message]): List if messages.
            conversation_id (int): Id of conversation,
                where a conversation is a sequence of messages that
                "makes sence" to group together. For instance, one
                "chat" can hold many conversations over time.
        """
        assert isinstance(messages, list)
        self.messages = messages

        assert isinstance(conversation_id, int)
        self.conversation_id = conversation_id

    def to_dict(self):
        return {
            "conversation_id": self.conversation_id,
            "messages": [m.to_dict() for m in self.messages],
        }


class Channel:
    def __init__(self, conversations: list, channel_id: int):
        """A channel is a place where we have conversations.
            This can be both 1-on-1 chats and groupchats.

        Args:
            conversations (list[Conversation]): List of conversations
            channel_id (int): Id of channel
        """
        assert isinstance(conversations, list)
        self.conversations = conversations

        assert isinstance(channel_id, int)
        self.channel_id = channel_id

    def to_dict(self):
        return {
            "channel_id": self.channel_id,
            "conversations": [c.to_dict() for c in self.conversations],
        }
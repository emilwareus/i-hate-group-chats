from datetime import datetime, date
import json
import re


def default_serializer(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()


def datetime_parser(dct):
    for (key, value) in dct.items():
        try:
            dct[key] = datetime.fromisoformat(value)
        except Exception as e:
            pass
    return dct


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
    def __init__(self, conversation_id: int, messages: list = []):
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
    def __init__(
        self,
        channel_id: int,
        conversations: list = [],
        is_group: bool = False,
        name: str = "",
        info: dict = {},
    ):
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

        assert isinstance(is_group, bool)
        self.is_group = is_group

        assert isinstance(name, str)
        self.name = name

        assert isinstance(info, dict)
        self.info = info

    def to_dict(self):
        return {
            "name": self.name,
            "channel_id": self.channel_id,
            "is_group": self.is_group,
            "conversations": [c.to_dict() for c in self.conversations],
            "info": self.info,
        }

    def from_dict(self, data):
        self = Channel.from_dict(data)
        return self

    def from_dict(data):

        assert isinstance(data["channel_id"], int)

        assert isinstance(data["is_group"], bool)

        assert isinstance(data["name"], str)

        assert isinstance(data["info"], dict)

        channel = Channel(
            channel_id=data["channel_id"],
            is_group=data["is_group"],
            name=data["name"],
            info=data["info"],
        )

        channel.conversations = [
            Conversation(
                conversation_id=conv["conversation_id"],
                messages=[Message(**message) for message in conv["messages"]],
            )
            for conv in data["conversations"]
        ]
        return channel

    def write_json(self, filename):
        data = self.to_dict()

        assert ".json" in filename

        with open(filename, "w") as fp:
            json.dump(data, fp, default=default_serializer)

    def read_json(self, filename):
        self = Channel.read_json(filename)
        return self

    def read_json(filename):

        with open(filename, "r") as fp:
            data = json.load(fp, object_hook=datetime_parser)

        print(data)
        channel = Channel.from_dict(data)
        return channel

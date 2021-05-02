from ihgc.data_models.conversation import Message, Conversation, Channel
from datetime import datetime


def test_models():
    messages = [
        Message(
            message="How are you?",
            author="Jocke",
            is_me=False,
            message_id=1,
            created_at=datetime(2021, 1, 1, 1, 1, 1),
        ),
        Message(
            message="I'm fine!",
            author="Carl",
            is_me=True,
            message_id=2,
            created_at=datetime(2021, 1, 1, 1, 1, 2),
        ),
        Message(
            message="Ok...",
            author="Jocke",
            is_me=False,
            message_id=3,
            created_at=datetime(2021, 1, 1, 1, 1, 3),
        ),
    ]

    assert len(messages) == 3
    assert messages[0].to_dict() == {
        "message_id": 1,
        "author": "Jocke",
        "message": "How are you?",
        "created_at": datetime(2021, 1, 1, 1, 1, 1),
        "is_me": False,
    }

    conversation = Conversation(messages=messages, conversation_id=1)

    assert conversation.conversation_id == 1
    assert len(conversation.messages) == 3
    assert conversation.messages == messages
    assert isinstance(conversation.to_dict(), dict)

    channel = Channel(conversations=[conversation], channel_id=1)

    assert channel.channel_id == 1
    assert len(channel.conversations[0].messages) == 3
    assert conversation.messages == messages
    assert isinstance(channel.to_dict(), dict)

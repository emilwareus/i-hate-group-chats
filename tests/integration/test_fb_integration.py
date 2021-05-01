from ihgc.integrations.fb_integration import FBIntegration
import os
from dotenv import load_dotenv
from pprint import pprint
import pytest

load_dotenv()


@pytest.mark.integtest
def test_integration():

    fbi = FBIntegration(os.getenv("FB_USERNAME"), os.getenv("FB_PASSWORD"))

    assert fbi is not None

    convs = fbi.fetch_conversations(limit=3, message_limit=10)
    pprint(convs)

    assert convs is not None

    # It may not be 3 as some chats dont count
    assert len(convs) > 1

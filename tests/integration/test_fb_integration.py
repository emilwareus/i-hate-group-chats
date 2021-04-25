from ihgc.integrations.fb_integration import FBIntegration
import os
from dotenv import load_dotenv

load_dotenv()


def test_integration():

    fbi = FBIntegration(os.getenv("FB_USERNAME"), os.getenv("FB_PASSWORD"))

    assert fbi is not None

    convs = fbi.fetch_all_conversations()

    assert convs is not None
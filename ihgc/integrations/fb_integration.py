import fbchat
from datetime import datetime, timezone

# If an answere is created within 5h
# it is regarded to belong to the same session

SESSION_TIME = 5 * 60 * 60


class FBIntegration:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__session = None

    def _start_session(self):
        self.__session = fbchat.Session.login(self.__username, self.__password)

    def get_session(self):
        if self.__session is None:
            self._start_session()

        return self.__session

    def fetch_conversations(self, limit=10, message_limit=100):
        session = self.get_session()
        my_id = session.user.id
        client = fbchat.Client(session=session)

        # Fetches a list of all users you're currently chatting with, as `User` objects
        threads = client.fetch_threads(limit=limit)

        output = dict()

        for thread in threads:
            thread_info = client.fetch_thread_info(thread.id)

            if not thread_info:
                continue

            output[thread.id] = {
                "info": {
                    "is_group": isinstance(thread, fbchat.GroupData),
                    "name": thread.name,
                    "id": thread.id,
                    "message_count": thread.message_count,
                }
            }

            if output[thread.id]["info"]["is_group"]:
                output[thread.id]["info"]["participants"] = [
                    user.id for user in thread.participants
                ]

            messages = thread.fetch_messages(limit=message_limit)
            output[thread.id]["messages"] = []

            session_id = -1
            last_message = datetime(3021, 1, 1, 1, 1, tzinfo=timezone.utc)

            for message in messages:
                td = last_message - message.created_at
                if td.total_seconds() >= SESSION_TIME:
                    session_id += 1

                output[thread.id]["messages"] = [
                    {
                        "text": message.text,
                        "is_me": my_id == message.author,
                        "author": message.author,
                        "created_at": message.created_at,
                        "session_id": thread.id + "_" + str(session_id),
                    }
                ] + output[thread.id]["messages"]

                last_message = message.created_at

        return output
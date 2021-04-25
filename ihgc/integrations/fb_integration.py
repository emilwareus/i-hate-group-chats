import fbchat


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

    def fetch_all_conversations(self):
        client = fbchat.Client(session=self.get_session())

        # Fetches a list of all users you're currently chatting with, as `User` objects
        threads = client.fetch_threads(limit=10)

        return threads
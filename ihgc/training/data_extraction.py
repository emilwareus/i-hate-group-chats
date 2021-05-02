from integrations.fb_integration import FBIntegration


class DatasetBuilder:
    def __init__(self):
        self.__data = {}
        self.__fb_integration = None

    def build_fb_dataset(self, username, password):

        if self.__fb_integration is None:
            self.__fb_integration = FBIntegration(username, password)

        conversation_data = self.__fb_integration.fetch_conversations(
            self, limit=10, message_limit=100
        )

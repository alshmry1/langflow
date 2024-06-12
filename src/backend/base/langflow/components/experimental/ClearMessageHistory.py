from langflow.custom import CustomComponent
from langflow.memory import delete_messages, get_messages


class ClearMessageHistoryComponent(CustomComponent):
    display_name = "Clear Message History"
    description = "A component to clear the message history."
    icon = "ClearMessageHistory"
    beta: bool = True

    def build_config(self):
        return {
            "session_id": {
                "display_name": "Session ID",
                "info": "The session ID to clear the message history.",
            }
        }

    def build(
        self,
        session_id: str,
    ) -> None:
        delete_messages(session_id=session_id)
        data = get_messages(session_id=session_id)
        self.data = data
        return data

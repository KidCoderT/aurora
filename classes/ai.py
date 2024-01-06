from threading import Lock
from openai import AsyncOpenAI


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class AiClient(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.model = AsyncOpenAI(timeout=20.0)

    async def respond(self, *messages: list[dict]):
        response = await self.model.chat.completions.create(
            messages=messages,  # type: ignore
            model="gpt-3.5-turbo",
        )

        return response.choices[0].message.content


def setup_client():
    # initialize the client
    AiClient()

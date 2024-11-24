import asyncio
from the_talk_n_typewriter import (
    AudioInputRequest,
    TheTalkNTypewriterBase,
    TranscriptionTask,
    TranscriptionTaskStatus,
)
from grpclib.server import Server


class TheTalkNTypewriterService(TheTalkNTypewriterBase):
    async def transcribe(
        self, audio_input_request: AudioInputRequest
    ) -> TranscriptionTask:
        return TranscriptionTask(id="1", status=TranscriptionTaskStatus.PENDING)


async def main():
    server = Server([TheTalkNTypewriterService()])
    await server.start("127.0.0.1", 8089)
    await server.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

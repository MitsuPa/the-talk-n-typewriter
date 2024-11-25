import asyncio
import json
import os
import tempfile
from the_talk_n_typewriter import (
    AudioInputRequest,
    TheTalkNTypewriterBase,
    TranscriptionTask,
    TranscriptionTaskStatus,
)
from grpclib.server import Server

if os.getenv("KAGGLE_CONFIG_DIR") is None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.environ["KAGGLE_CONFIG_DIR"] = tmpdirname
os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME", "example")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY", "example")
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()

kernel_metadata = {
    "id": "",
    "title": "Translation Gummy",
    "code_file": "code_file.py",
    "language": "python",
    "kernel_type": "script",
    "is_private": True,
    "enable_gpu": True,
    "enable_tpu": False,
    "enable_internet": True,
    "keywords": [],
    "dataset_sources": [],
    "kernel_sources": [],
    "competition_sources": [],
    "model_sources": [],
}


class TheTalkNTypewriterService(TheTalkNTypewriterBase):
    async def transcribe(
        self, audio_input_request: AudioInputRequest
    ) -> TranscriptionTask:
        kaggle_username = os.getenv("KAGGLE_USERNAME")
        kaggle_key = os.getenv("KAGGLE_KEY")
        kernel_metadata["id"] = f"{kaggle_username}/translation-gummy"
        with open(os.path.join(tmpdirname, "kernel-metadata.json"), "w") as new_f:
            json.dump(kernel_metadata, new_f)
        push_file = 'print("Pushing code file to Kaggle")'
        with open(os.path.join(tmpdirname, kernel_metadata["code_file"]), "w") as new_f:
            new_f.write(push_file)
        api.authenticate()
        result = api.kernels_push(tmpdirname)
        if result is None or result.error:
            raise Exception(result)
        return TranscriptionTask(id="1", status=TranscriptionTaskStatus.PENDING)


async def main():
    server = Server([TheTalkNTypewriterService()])
    await server.start("0.0.0.0", 8089)
    await server.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: the_talk_n_typewriter/the_talk_n_typewriter.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class WhisperImplementation(betterproto.Enum):
    FASTER_WHISPER = 0
    WHISPER = 1


class WhisperModel(betterproto.Enum):
    LARGE_V3 = 0
    LARGE_V2 = 1
    LARGE_V1 = 2
    LARGE_V3_TURBO = 3


class TranscriptionTaskStatus(betterproto.Enum):
    PENDING = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    FAILED = 3


@dataclass(eq=False, repr=False)
class AudioInputRequest(betterproto.Message):
    intput_urls: List[str] = betterproto.string_field(1)
    whisper_implementation: "WhisperImplementation" = betterproto.enum_field(2)
    whisper_model: "WhisperModel" = betterproto.enum_field(3)
    word_timestamps: bool = betterproto.bool_field(4)
    retain_input_file: bool = betterproto.bool_field(5)
    check_duplicate: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class TranscriptionTask(betterproto.Message):
    id: str = betterproto.string_field(1)
    input_url: str = betterproto.string_field(2)
    status: "TranscriptionTaskStatus" = betterproto.enum_field(4)


class TheTalkNTypewriterStub(betterproto.ServiceStub):
    async def transcribe(
        self,
        audio_input_request: "AudioInputRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TranscriptionTask":
        return await self._unary_unary(
            "/the_talk_n_typewriter.TheTalkNTypewriter/Transcribe",
            audio_input_request,
            TranscriptionTask,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class TheTalkNTypewriterBase(ServiceBase):

    async def transcribe(
        self, audio_input_request: "AudioInputRequest"
    ) -> "TranscriptionTask":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_transcribe(
        self, stream: "grpclib.server.Stream[AudioInputRequest, TranscriptionTask]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.transcribe(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/the_talk_n_typewriter.TheTalkNTypewriter/Transcribe": grpclib.const.Handler(
                self.__rpc_transcribe,
                grpclib.const.Cardinality.UNARY_UNARY,
                AudioInputRequest,
                TranscriptionTask,
            ),
        }

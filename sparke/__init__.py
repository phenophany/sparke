from typing import Dict

from typing import Dict
import logging
import sqlite3
import sparke.config
from sparke.config import Settings, System
from sparke.api import API
from sparke.api.models.Collection import Collection
from sparke.api.types import (
    CollectionMetadata,
    Documents,
    EmbeddingFunction,
    Embeddings,
    IDs,
    Include,
    Metadata,
    Where,
    QueryResult,
    GetResult,
    WhereDocument,
    UpdateCollectionMetadata,
)

__settings = Settings()

__version__ = "0.4.13"

def PersistentClient(path: str = "./chroma", settings: Settings = Settings()) -> API:
    """
    Creates a persistent instance of Chroma that saves to disk. This is useful for
    testing and development, but not recommended for production use.

    Args:
        path: The directory to save Chroma's data to. Defaults to "./chroma".
    """
    settings.persist_directory = path
    settings.is_persistent = True

    return Client(settings)


def HttpClient(
    host: str = "localhost",
    port: str = "8000",
    ssl: bool = False,
    headers: Dict[str, str] = {},
    settings: Settings = Settings(),
) -> API:
    """
    Creates a client that connects to a remote Chroma server. This supports
    many clients connecting to the same server, and is the recommended way to
    use Chroma in production.

    Args:
        host: The hostname of the Chroma server. Defaults to "localhost".
        port: The port of the Chroma server. Defaults to "8000".
        ssl: Whether to use SSL to connect to the Chroma server. Defaults to False.
        headers: A dictionary of headers to send to the Chroma server. Defaults to {}.
    """

    settings.chroma_api_impl = "chromadb.api.fastapi.FastAPI"
    settings.chroma_server_host = host
    settings.chroma_server_http_port = port
    settings.chroma_server_ssl_enabled = ssl
    settings.chroma_server_headers = headers

    return Client(settings)


def Client(settings: Settings = __settings) -> API:
    """Return a running chroma.API instance"""

    system = System(settings)

    # telemetry_client = system.instance(Telemetry)
    api = system.instance(API)

    system.start()

    # Submit event for client start
    # telemetry_client.capture(ClientStartEvent())

    return api
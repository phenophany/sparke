from sparke.api.types import EmbeddingFunction, Documents, Embeddings
from typing import Optional

#get the api key from the .env file
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # This loads the .env file in the root directory of the project
# openai.api_key  = os.environ['OPENAI_API_KEY']

class OpenAIEmbeddingFunction(EmbeddingFunction):
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "text-embedding-ada-002",
        organization_id: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
    ):
        """
        Initialize the OpenAIEmbeddingFunction.
        Args:
            api_key (str, optional): Your API key for the OpenAI API. If not
                provided, it will raise an error to provide an OpenAI API key.
            organization_id(str, optional): The OpenAI organization ID if applicable
            model_name (str, optional): The name of the model to use for text
                embeddings. Defaults to "text-embedding-ada-002".
            api_base (str, optional): The base path for the API. If not provided,
                it will use the base path for the OpenAI API. This can be used to
                point to a different deployment, such as an Azure deployment.
            api_type (str, optional): The type of the API deployment. This can be
                used to specify a different deployment, such as 'azure'. If not
                provided, it will use the default OpenAI deployment.
            api_version (str, optional): The api version for the API. If not provided,
                it will use the api version for the OpenAI API. This can be used to
                point to a different deployment, such as an Azure deployment.

        """
        try:
            import openai
        except ImportError:
            raise ValueError(
                "The openai python package is not installed. Please install it with `pip install openai`"
            )

        if api_key is not None:
            openai.api_key = api_key
        # If the api key is still not set, raise an error
        elif openai.api_key is None:
            openai.api_key = os.environ['OPENAI_API_KEY']
            # raise ValueError(
            #     "Please provide an OpenAI API key. You can get one at https://platform.openai.com/account/api-keys"
            # )

        if api_base is not None:
            openai.api_base = api_base

        if api_version is not None:
            openai.api_version = api_version

        if api_type is not None:
            openai.api_type = api_type

        if organization_id is not None:
            openai.organization = organization_id

        self._client = openai.Embedding
        self._model_name = model_name

    def __call__(self, texts: Documents) -> Embeddings:
        # replace newlines, which can negatively affect performance.
        texts = [t.replace("\n", " ") for t in texts]

        # Call the OpenAI Embedding API
        embeddings = self._client.create(input=texts, engine=self._model_name)["data"]

        # Sort resulting embeddings by index
        sorted_embeddings = sorted(embeddings, key=lambda e: e["index"])  # type: ignore

        # Return just the embeddings
        return [result["embedding"] for result in sorted_embeddings]


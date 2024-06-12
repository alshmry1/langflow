from typing import List, Union

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.vectorstores import VectorStore

from langflow.custom import CustomComponent
from langflow.field_typing import Text
from langflow.helpers.record import docs_to_data
from langflow.schema import Data


class LCVectorStoreComponent(CustomComponent):
    display_name: str = "LC Vector Store"
    description: str = "Search a LC Vector Store for similar documents."

    def search_with_vector_store(
        self,
        input_value: Text,
        search_type: str,
        vector_store: Union[VectorStore, BaseRetriever],
        k=10,
        **kwargs,
    ) -> List[Data]:
        """
        Search for data in the vector store based on the input value and search type.

        Args:
            input_value (Text): The input value to search for.
            search_type (str): The type of search to perform.
            vector_store (VectorStore): The vector store to search in.

        Returns:
            List[Data]: A list of data matching the search criteria.

        Raises:
            ValueError: If invalid inputs are provided.
        """

        docs: List[Document] = []
        if input_value and isinstance(input_value, str) and hasattr(vector_store, "search"):
            docs = vector_store.search(query=input_value, search_type=search_type.lower(), k=k, **kwargs)
        else:
            raise ValueError("Invalid inputs provided.")
        data = docs_to_data(docs)
        self.status = data
        return data

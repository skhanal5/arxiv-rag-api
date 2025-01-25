from haystack import Pipeline
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore


class IngestionPipeline:
    def __init__(self):
        self.document_store = InMemoryDocumentStore()
        self.document_splitter = DocumentSplitter(
            split_by="word", split_length=512, split_overlap=32
        )
        self.document_embedder = SentenceTransformersDocumentEmbedder(
            model="BAAI/bge-small-en-v1.5"
        )
        self.document_writer = DocumentWriter(self.document_store)
        self.indexing_pipeline = Pipeline()
        self.indexing_pipeline.add_component(
            "document_splitter", self.document_splitter
        )
        self.indexing_pipeline.add_component(
            "document_embedder", self.document_embedder
        )
        self.indexing_pipeline.add_component("document_writer", self.document_writer)

        self.indexing_pipeline.connect("document_splitter", "document_embedder")
        self.indexing_pipeline.connect("document_embedder", "document_writer")

    def run(self, docs: dict):
        self.indexing_pipeline.run({"document_splitter": {"documents": docs}})

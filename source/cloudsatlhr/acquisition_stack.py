from aws_cdk import (core )

from .ingestion_stack import IngestionStack
from .data_store_stack import DataStoreStack

class AcquisitionStack(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.datastore_stack = DataStoreStack(self, "DataStoreStack")
        self.ingestion_stack = IngestionStack(self, "IngestionStack", target_table=self.datastore_stack.table)

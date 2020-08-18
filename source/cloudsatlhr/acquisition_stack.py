from aws_cdk import (core )

from .timer_stack import TimerStack
from .data_store_stack import DataStoreStack

class AcquisitionStack(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.timer_stack = TimerStack(self, "TimerStack")
        self.datastore_stack = DataStoreStack(self, "DataStoreStack")

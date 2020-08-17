from aws_cdk import (core )

from .timer_stack import TimerStack

class AcquisitionStack(core.Stage):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.timer_stack = TimerStack(self, "TimerStack")

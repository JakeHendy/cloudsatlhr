from aws_cdk import (core, aws_events as events)


class TimerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        five_minute_timer = events.Rule(
            self,
            "FiveMinuteTimer",
            enabled=True,
            schedule=events.Schedule.rate(core.Duration.minutes(5)))

        self.five_minute_timer = five_minute_timer

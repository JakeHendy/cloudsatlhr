from aws_cdk import (core, aws_dynamodb as ddb, aws_events as events,
                     aws_lambda as lambda_, aws_lambda_python as pylambda)


class IngestionStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, target_table: ddb.Table, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        five_minute_timer = events.Rule(
            self,
            "FiveMinuteTimer",
            enabled=True,
            schedule=events.Schedule.rate(core.Duration.minutes(5)))

        self.five_minute_timer = five_minute_timer

        feed_scanner_lambda = pylambda.PythonFunction(self, "FeedScannerLambda",
                                                      function_name="CloudsatLHR Feed Scanner",
                                                      entry="lambdas/feed_scanner/",
                                                      index="app/index.py",
                                                      runtime=lambda_.Runtime.PYTHON_3_7
                                                      )
        self.feed_scanner_lambda = feed_scanner_lambda

        target_table.grant_write_data(feed_scanner_lambda)
        target_table.grant_read_data(feed_scanner_lambda)

        five_minute_timer.add_target(feed_scanner_lambda)
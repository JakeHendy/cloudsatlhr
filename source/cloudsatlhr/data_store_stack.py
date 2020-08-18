from aws_cdk import (core, aws_dynamodb as ddb)


class DataStoreStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = ddb.Table(self, "DataStoreDynamoDBTable",
                          table_name="CatLHR-DataStore",
                          partition_key=ddb.Attribute(
                              name="uuid",
                              type=ddb.AttributeType.STRING
                          ),
                          sort_key=ddb.Attribute(
                              name="date",
                              type=ddb.AttributeType.STRING
                          ))

        self.table = table

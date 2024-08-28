from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    # aws_sqs as sqs,
    Duration,
)
from constructs import Construct
from compliant_cdk_lib import Compliant


class DemoProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket_props = s3.BucketProps(
            bucket_name="dino-my-bucket",
        )

        bucket = Compliant.s3.Bucket(self, "CompliantBucket", bucket_props)

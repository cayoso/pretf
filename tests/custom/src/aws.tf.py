from pretf import tf
from pretf_aws import get_frozen_credentials


def terraform(aws_profile, aws_region, **kwargs):
    """
    This function would normally be a generator,
    but it can also be a regular function that returns a list.

    This also demonstrates returning a standard dictionary
    instead of using the tf object.

    This also shows how to use pretf_aws to get AWS credentials
    and use them in multiple providers. This allows for a single
    Terraform stack to manage resources in multiple accounts.
    However, in this test I am using the same account twice.

    The result of this file (aws.tf.json) is in .gitignore
    to avoid publishing AWS credentials.

    """

    # Normally you would not need to use creds here,
    # and rely on environment variables set by terraform.tf.py
    # but this shows how to work with multiple AWS accounts.

    creds = get_frozen_credentials(profile_name=aws_profile)

    tf_block = tf(
        "provider.aws",
        {
            "region": aws_region,
            "access_key": creds.access_key,
            "secret_key": creds.secret_key,
            "token": creds.token,
        },
    )

    dict_block = {
        "provider": {
            "aws": {
                "alias": "london",
                "region": "eu-west-2",
                "access_key": creds.access_key,
                "secret_key": creds.secret_key,
                "token": creds.token,
            }
        }
    }

    return [tf_block, dict_block]

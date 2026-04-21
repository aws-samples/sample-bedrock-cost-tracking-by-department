## Split generative AI costs by team using Amazon Bedrock

Sample code for the AWS blog post "Split generative AI costs by team using Amazon Bedrock."

This sample demonstrates how to route Amazon Bedrock model invocations through department-specific application inference profiles for per-department cost tracking, and includes an IAM ABAC policy for restricting department access.

**This is sample code for non-production usage. You should work with your security and legal teams to meet your organizational security, regulatory and compliance requirements before deployment.**

### Files

- `invoke_by_department.py` — Python code snippet showing how to route Bedrock invocations through department-specific inference profiles
- `iam-abac-policy.json` — IAM policy using attribute-based access control (ABAC) to restrict each department to their own inference profile

### Prerequisites

- Python 3.12 with boto3 1.35.7 or later
- Amazon Bedrock model access enabled
- Application inference profiles created and tagged per department

### Usage

Replace the placeholder values in both files with your actual AWS account ID and inference profile ARNs before use.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

import boto3
from botocore.exceptions import ClientError

client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Replace with your actual inference profile ARNs from the Amazon Bedrock console
DEPARTMENT_PROFILES = {
    'HR': 'arn:aws:bedrock:us-east-1:111122223333:application-inference-profile/abc123',
    'Accounting': 'arn:aws:bedrock:us-east-1:111122223333:application-inference-profile/def456',
    'IT': 'arn:aws:bedrock:us-east-1:111122223333:application-inference-profile/ghi789',
}

# Implement based on your authentication system.
# Examples:
#   - Extract from SAML/OIDC claims: token['custom:department']
#   - Query from user database: db.get_user_department(user_id)
#   - Retrieve from session: session['department']
department = get_department_from_user_session()

if department not in DEPARTMENT_PROFILES:
    raise ValueError(f"Unknown department: {department}")

try:
    response = client.converse(
        modelId=DEPARTMENT_PROFILES[department],
        messages=[{'role': 'user', 'content': [{'text': 'Your prompt here'}]}],
        inferenceConfig={'maxTokens': 300}
    )
except ClientError as e:
    print(f"Error invoking model: {e}")
    raise

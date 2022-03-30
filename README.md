# CodeGuru_Profiler_Lambda_Insights_Lambda_Powertools_For_Python

Hello, and welcome!

This is a SAM application that will deploy:

- An API Gateway REST API
- Python 3.9 Lambda Function
- CodeGuru Profiler Group

This application demonstrates a few things:

- CloudWatch Lambda Insights
- CodeGuru Python Lambda profiling
- Lambda Powertools for Python
- Profiling import time of Python modules
- AWS X-Ray tracing from the REST API, through the Lambda execution environment, through the AWS SDK for Python code
- How to deploy an AWS SAM REST API using SAM templating, but avoiding the item mentioned in this GitHub issue where it creates a stage named “Stage” by default: https://github.com/aws/serverless-application-model/issues/191

How to generate X-Ray traces and profiling group data:
- A X-Ray trace will show up upon the first request sent and doesn’t require special instructions.
- For profiling group data to display in the CodeGuru Profiler console, you must have the Lambda function be invoked multiple times in two consecutive 5 minute windows. For example, throughout the course of 5 minutes have the function be invoked around 10 times. Immediately following this first 5 minute window, repeat the same process for another 5 minutes. Then wait 5 more minutes (we’re now at the 15 minute mark) and profiling data should appear in the CodeGuru Profiler console.

This is intended for learning how to have a high degree of observability of your Lambda function, and all resources, documentation, and reference material is commented in the code or template.yaml. The reason why this was developed is because the Lambda console has these features available in the "Monitor" tab (view below screenshot), however it takes some time to setup. You can launch this SAM application and begin to explore these features fairly quick!

<img width="1142" alt="Console" src="https://user-images.githubusercontent.com/22535268/160693385-ec7b95d1-fdd2-4b85-88ca-86716c3b05f1.png">

Prerequisites:
- An AWS Account
- The AWS CLI installed and configured
- The AWS SAM CLI installed (supports Linux/Windows/MacOS) : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
- Python 3.9 installed

Deployment steps:
```
sam build
sam deploy --guided
sam delete <insert your provided stack name>
```

Future additions (no gurantees):
- Integrate AWS Appconfig and use its feature flag Lambda extension to enable/disable advanced observability without redeployments when errors occur.
  - https://aws.amazon.com/blogs/mt/introducing-aws-appconfig-feature-flags-in-preview/
  - https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html
 - Recorded demo of all of the above (minus Prerequisites)

Feel free to send pull requests or make issues should you have something to touch up, update, patch, or discuss.

- T

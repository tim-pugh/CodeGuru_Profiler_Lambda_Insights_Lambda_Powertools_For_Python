#A deep dive into AWS Lambda observability brought to you by Tim Pugh! (https://github.com/tim-pugh/CodeGuru_Profiler_Lambda_Insights_Lambda_Powertools_For_Python)
import json
import os
#import requests
#import logging #Not needed, unless you want to do advanced logging with CodeGuru Profiler: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-enabling-logs.html
from aws_lambda_powertools import Metrics, Logger, Tracer #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
from codeguru_profiler_agent import with_lambda_profiler
import time

#from aws_lambda_powertools.logging.logger import set_package_logger #https://awslabs.github.io/aws-lambda-powertools-python/latest/#debug-mode Enables Powertools Layer Debugging
#set_package_logger() #https://awslabs.github.io/aws-lambda-powertools-python/latest/#debug-mode Enables Powertools Layer Debugging

logger = Logger() #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
tracer = Tracer() #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
metrics = Metrics() #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/

#logger.info("Lambda Powertools Metrics Namespace %s", os.environ["POWERTOOLS_METRICS_NAMESPACE"]) #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
#logger.info("Lambda Powertools Metrics Namespace %s", os.environ["POWERTOOLS_SERVICE_NAME"]) #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
#logging.getLogger('codeguru_profiler_agent').setLevel(logging.INFO) #Not needed, unless you want to do advanced logging with CodeGuru Profiler: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-enabling-logs.html

@metrics.log_metrics(capture_cold_start_metric=True) #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
@logger.inject_lambda_context(log_event=True) #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
@tracer.capture_lambda_handler #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
@with_lambda_profiler()
def lambda_handler(event, context):

#    logger.debug(event) #https://awslabs.github.io/aws-lambda-powertools-python/latest/ and https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    time.sleep(1) #Why do we sleep  here you may ask :) ? If you're python code is extra fast, code guru profiler may not have enough time to capture profiling data! So, we sleep, enabling codeguru profiler enough time to do its work, and disregard the sleep item in the profiler review. Note: this is NOT NECESSARY IF YOU'RE CODE BY DEFAULT EXECUTES LONG ENOUGH TO BE PROFILED SO CONSIDER REMOVING THIS SPECIFIC TO YOUR FUNCTION CODE!
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

import os
import boto3
import json
import argparse
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')


def metric(namespace, metricname, value):
    """
    :param namespace: NameSpace of the metric
    :param metricname: Name of the metric
    :param value: The value of the metric

    :return: Returns the response of putmetricdata request sent to CloudWatch
    """
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': metricname, 'Value': value
            },
        ],
        Namespace=namespace
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take metric inputs')
    parser.add_argument('--namespace', '-n', required=True, type=str, help='Namespace of the metric')
    parser.add_argument('--metricname', '-m', required=True, type=str, help='Metric name')
    parser.add_argument('--value', '-v', required=False, type=float, help='Value of the metric')

    #	parser.add_argument('--statistic', required=False, type=str, help='statistic of the metric')
    #	parser.add_argument('--dimensions', required=False, type=list, help='Dimensions of the metric')
    #	parser.add_argument('--timestamp', required=False, type=datetime, help='timestamp of the datapoint')

    args = parser.parse_args()

    metric(args.namespace, args.metricname, args.value)

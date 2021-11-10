#!/usr/bin/env python3

import json
import os
import boto3

def seed_db(seeds):
    dynamodb = boto3.resource('dynamodb')
    tbl = dynamodb.Table(os.getenv('DYNAMODB_TABLE_NAME'))
    for seedval in seeds:
        # should be a dict of { question: 1, answer: 1234 }
        tbl.put_item(Item=seedval, ReturnValues=None)

def handle(event, *unused):
    print('In Handler')
    print(event)
    seeds = json.loads(event['body'])
    print(seeds)
    seed_db(seeds)

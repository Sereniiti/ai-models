import json
import logging
import boto3
import datetime
import random
import time

from botocore.exceptions import ClientError

def lambda_handler(event, context):
       rating=random.randint(0, 11)
       text='You are good'
       body=json.loads(event['body'])
       text=body['text']
       text=text.replace(',','').replace('.','').replace('!','')
       words = text.split()
       test=(list(map(' '.join, zip(words[:-1], words[1:]))))
       randomlist = random.sample(range(0, 11), len(test))
       list_string = map(str, randomlist)
       explanation=(list(map(', rating : '.join, zip(test[:-1],list_string))))
       x={'text':text,'steps':'facts','explanation':explanation,'tipgroup':'judgemental','inputime':int(time.time()),'outputime':int(time.time()),'rating':rating}
       return {
            'status':200,
            'body': x
        }
    

import json
import xml.etree.ElementTree as ET
import boto3

# Nome del bucket. TODO: sostituire con il nome del proprio bucket.
DEFAULT_BUCKET = 'mdv-xmlresults-bucket'

def lambda_handler(event, context):

    # STEP 1: recupero della strina XML nel bucket S3 corrispondente all'ID passato come parametro
    s3 = boto3.resource('s3')
    try:
        raceid = event['queryStringParameters']['id']  # è il parametro specificato con "?id=" in coda all'URL
        bucket_name = DEFAULT_BUCKET
        object_name = str(raceid) + '.xml'
        obj = s3.Object(bucket_name, object_name)
        xmlstr = obj.get()['Body'].read()
    except s3.meta.client.exceptions.NoSuchKey:
        return {
            'statusCode': 404,
            'body': json.dumps("ERROR: Race ID not found.")
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps("ERROR: id parameter not specified.")
        }
    
    # STEP 2: parsing dell'XML con la libreria standard di Python.
    # Attenzione all'uso del namespace gestito con la variabile _ns
    root = ET.fromstring(xmlstr)
    _ns = {'':'http://www.orienteering.org/datastandard/3.0'}
    class_names_elements = root.findall('./ClassResult/Class/Name', _ns)
    classes = [x.text for x in class_names_elements]

    return {
        'statusCode': 200,
        'body': json.dumps(classes)
    }

import json
import boto3

# Nome del bucket. TODO: sostituire con il nome del proprio bucket.
DEFAULT_BUCKET = 'mdv-xmlresults-bucket'

def lambda_handler(event, context):
    
    # A seconda del tipo di metodo HTTP si fanno cose diverse:
    # - GET  -> si restituisce una stringa di saluto. Serve solo per assicurarsi che tutto stia funzionando, verrà eliminato in seguito
    # - POST -> ci si aspetta che il body della richiesta contenga l'XML e che ci sia il paramtero raceid.
    #           La stringa XML ricevuta viene salvata nel oggetto S3 (file) "RACEID.xml"
    # - PUT  -> si restituisce l'oggetto event per vedere cosa contiene. Serve solo per DEBUG. Verrà cambiato in seguito.
    
    httpMethod = event['requestContext']['http']['method']
    
    if httpMethod == 'GET':
        res = {
            'statusCode': 200,
            'body': json.dumps('Ciao from Lambda!')
        }
    elif httpMethod == 'POST':
        xmlstring = event['body']
        object_name = event['queryStringParameters']['raceid'] + '.xml'
        put_to_bucket(content=xmlstring, object_name=object_name)
        res = {'statusCode': 200, 'body': 'File updloaded.'}
    elif httpMethod == 'PUT':
        res = {'statusCode': 200, 'body': json.dumps(str(event))}
    else:
        res = {'statusCode': 405, 'body': 'Method Not Allowed'}
    return res


def put_to_bucket(bucket_name=DEFAULT_BUCKET, object_name='prova.xml', content=None):
    assert check_xml(content)
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, object_name)
    obj.put(Body=content)


def check_xml(xml_string):
    # TODO XML validation
    return True
import json

def lambda_handler(event, context):
    def add(x, y):
        x = int(x)
        y = int(y)
        return x + y
    
    def sub(x, y):
        x = int(x)
        y = int(y)
        return x - y
    
    def mul(x, y):
        x = int(x)
        y = int(y)
        return x * y
    
    def div(x, y):
        x = int(x)
        y = int(y)
        return x / y
    
    # get query string param inputs
    x = int(event['queryStringParameters']['x'])
    y = int(event['queryStringParameters']['y'])
    op = event['queryStringParameters']['op']
    
    # log inputs
    print(f"x:{x}, y:{y}, op:{op}")
    
    # prepare the response_body
    res_body = {}
    res_body['x'] = x
    res_body['y'] = y
    res_body['op'] = op
    
    if op == 'add':
        res_body['add_result'] = add(x, y)
    elif op == 'sub':
        res_body['sub_result'] = sub(x, y)
    elif op == 'mul':
        res_body['mul_result'] = mul(x, y)
    elif op == 'div':
        res_body['div_result'] = div(x, y)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid operation'})
        }
    
    # prepare http response
    http_res = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(res_body)
    }
    
    return http_res

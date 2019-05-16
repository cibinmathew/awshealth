
import boto3

from flask import Flask, jsonify
app = Flask(__name__)

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html

# Boto 3
AWS_ACCESS_KEY_ID = 'xxxx'
AWS_SECRET_ACCESS_KEY = 'xxxx'
region_name = 'us-east-2'


@app.route('/awshealth')
def hello_world():
    try:
        ec2 = boto3.client('ec2', region_name=region_name,
                           aws_access_key_id=AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                           )
    except Exception as error:
        print(str(error))
        return jsonify({'Error': "Unexpected Error occured"}), 500

    instances = ec2.describe_instances()
    output = []
    for reservation in instances['Reservations']:
        output.extend([{'id': instance['InstanceId'],
                        "instance-type": instance['InstanceType'],
                        "instance-state": instance['State']['Name']}
                       for instance in reservation['Instances']])

    return jsonify(output), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

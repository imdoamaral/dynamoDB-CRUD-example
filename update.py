from decimal import Decimal
from pprint import pprint
import boto3

def update_movie(title, year, rating, plot, actors, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': rating,
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    update_response = update_movie(
        "Dune", 2021, 8, "Dune tells the story of Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding",
        ["Timothée Chalamet", "Rebecca Ferguson", "Zendaya"])
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)

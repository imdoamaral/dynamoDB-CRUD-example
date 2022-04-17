from pprint import pprint
import boto3

def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Movies')
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response

if __name__ == '__main__':
    movie_resp = put_movie("Dune", 2021,
                           "Dune tells the story of Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding", "8.1")
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)

import json
import pandas as pd
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    #Data Extraction using api
    api_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=8fabcce4f9edbeb2e9d7c0ca50f620aa&language=en-US&page=1'
    df = pd.DataFrame()
    response = requests.get(api_url)
    if(response.status_code == 200):
        for i in range(1,5):
            response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
            temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
            df = pd.concat([df,temp_df],ignore_index=True)
    else:
        print('Error: ', response.status_code)
    fileName = "/tmp/extracted_movies_data.csv"
    df.to_csv(fileName, index=False)

    #Saving Data onto S3
    s3 = boto3.client('s3')
    bucket_name = "etl-pipeline-demo-cg"
    object_key = f"data/extracted_data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    s3.upload_file(fileName, bucket_name, object_key)
    
    return {
        'statusCode': 200,
        'body': f"Data Extracted and uploaded to S3://{bucket_name}/{object_key}"
    }

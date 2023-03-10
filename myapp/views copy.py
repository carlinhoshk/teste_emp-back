from django.http import JsonResponse
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

account_name = 'bloobstream'
account_key = 'iDdGLcoy7DFiIEMJcaFHlFioFYHjPvdRjN8pdsPnujYGqz/QKzKBWcTen7jGAvBSgbn3eO37zpT6+AStFzGXKw=='

def blob_api(request):
    bucket_name = request.GET.get('bucket_name')
    object_key = request.GET.get('object_key')
    
    
    blob_service_client = BlobServiceClient(account_url=f'https://{account_name}.blob.core.windows.net/', credential=account_key)

    container_client = blob_service_client.get_container_client(bucket_name)
    blob_client = container_client.get_blob_client(object_key)
    
    csv_string = blob_client.download_blob().content_as_text(encoding='latin-1')


    df = pd.read_csv(io.StringIO(csv_string), delimiter=";")
    
    print(df.head())
    
    response_data = {
        'bucket_name': bucket_name,
        'object_key': object_key,
    }

    return JsonResponse(response_data)

from .orm import objorm
from .orm import engine
from sqlalchemy.orm import sessionmaker
from django.http import JsonResponse
from azure.storage.blob import BlobServiceClient
from sqlalchemy.orm import sessionmaker
import pandas as pd
import warnings

import io
from io import StringIO

account_name = 'bloobstream'
account_key = 'iDdGLcoy7DFiIEMJcaFHlFioFYHjPvdRjN8pdsPnujYGqz/QKzKBWcTen7jGAvBSgbn3eO37zpT6+AStFzGXKw=='

Session = sessionmaker(bind=engine)
session = Session()

def blob_api(request):
    bucket_name = request.GET.get('bucket_name')
    object_key = request.GET.get('object_key')
    
    
    blob_service_client = BlobServiceClient(account_url=f'https://{account_name}.blob.core.windows.net/', credential=account_key)

    container_client = blob_service_client.get_container_client(bucket_name)
    blob_client = container_client.get_blob_client(object_key)
    warnings.filterwarnings("ignore", message="The default value of regex will change", category=FutureWarning)
    
    csv_string = blob_client.download_blob().content_as_text(encoding='latin-1')


    df = pd.read_csv(io.StringIO(csv_string), delimiter=";")
    
    #print(df.head())
    df["Doc Originador"] = (df["Doc Originador"].str.replace(".", "").str.replace("/", "").str.replace("-", ""))
    df["Doc Cedente"] = (df["Doc Cedente"]
        .astype(str)
        .astype(str)
        .str.replace(".", "")
        .str.replace("/", "")
        .str.replace("-", "")
    )
    df["CPF/CNPJ"] = (df["CPF/CNPJ"].str.replace(".", "").str.replace("/", "").str.replace("-", ""))
    df["Valor do Empréstimo"] = df["Valor do Empréstimo"].str.replace(",", ".")
    df["Parcela R$"] = (df["Parcela R$"].str.replace(",", ".").str.replace("[a-zA-Z]", ""))
    df["Preço de Aquisição"] = df["Preço de Aquisição"].astype(str).str.replace(",", ".")
    df["Data de Emissão"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")
    df["Data de Vencimento"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")

    for i, row in df.iterrows():
        session.add(
        objorm(
            row["Originador"],
            row["Doc Originador"],
            row["Cedente"],
            row["Doc Cedente"],
            row["CCB"],
            row["Id"],
            row["Cliente"],
            row["CPF/CNPJ"],
            row["Endereço"],
            row["CEP"],
            row["UF"],
            row["Valor do Empréstimo"],
            row["Parcela R$"],
            row["Total Parcelas"],
            row["Parcela #"],
            row["Data de Emissão"],
            row["Data de Vencimento"],
            row["Preço de Aquisição"],
        )
    )

    session.commit()
    response_data = {
        'bucket_name': bucket_name,
        'object_key': object_key,
    }

    return JsonResponse(response_data)












# import pandas as pd
# import io

# Session = sessionmaker(bind=engine)
# session = Session()

# account_name = 'bloobstream'
# account_key = 'iDdGLcoy7DFiIEMJcaFHlFioFYHjPvdRjN8pdsPnujYGqz/QKzKBWcTen7jGAvBSgbn3eO37zpT6+AStFzGXKw=='

# def blob_api(request):
#     bucket_name = request.GET.get('bucket_name')
#     object_key = request.GET.get('object_key')
    
#     try:
#         process(bucket_name, object_key)
#     except:
#         return JsonResponse({'error': 'Something went wrong1'}, status=500)
    
#     try:
#         session.commit()
#     except:
#         session.rollback()
#         return JsonResponse({'error': 'Something went wrong2'}, status=500)
    
#     return JsonResponse({'status': 'error'}, status=400)

    
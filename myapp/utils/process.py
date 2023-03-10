import os
from myapp.utils import tr_df
from myapp.banco import bancoORM
import pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient

account_name = 'bloobstream'
account_key = 'iDdGLcoy7DFiIEMJcaFHlFioFYHjPvdRjN8pdsPnujYGqz/QKzKBWcTen7jGAvBSgbn3eO37zpT6+AStFzGXKw=='
blob_service_client = BlobServiceClient(account_url=f'https://{account_name}.blob.core.windows.net/', credential=account_key)


def process(bucket_name, object_key, session):
    
    container_client = blob_service_client.get_container_client(bucket_name)
    blob_client = container_client.get_blob_client(object_key)

    csv_string = blob_client.download_blob().content_as_text(encoding='latin-1')

    df = pd.read_csv(StringIO(csv_string), delimiter=";")
    df = tr_df(df)
    
    for i, row in df.iterrows():
        session.add(
            bancoORM(
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
<!DOCTYPE html>
<html>
<head>
	<title>README</title>
</head>
<body>
	<h1>Projeto Processamento CSV</h1>
	<p>Este é um projeto simples que demonstra o uso do Django para criar uma API que se conecta ao Azure Blob Storage, lê um arquivo CSV e o processa no banco de dados usando SQLAlchemy.</p>
	<h2>Como usar essse projeto</h2>
	<ol>
		<li>Clone este repositório.</li>
        <li>Ative o ambiente virtual usando o comando abaixo:</li>
		<pre><code>$ source env/bin/activate</code></pre>
        <pre><code>$ PS C:\> env\Scripts\Activate.ps1</code></pre>
        <pre><p>depois execute o servidor django</p><code>$ python manage.py runserver<pre><code>
    </ol>
	<h2>Como usar a API</h2>
	<p>Para usar a API, envie uma solicitação GET com os parâmetros bucket_name e object_key para a URL <code>localhost:8000/blob_api/</code>.</p>
	<h3>Exemplo de solicitação</h3>
	<pre>
		<code>
			GET blob_api/?bucket_name=mybucket&object_key=myfile.csv HTTP/1.1
            Host: localhost:8000
		</code>
	</pre>
	<h2>Dependências</h2>
	<ul>
		<li>Django</li>
		<li>Pandas</li>
		<li>SQLAlchemy</li>
		<li>Azure Blob Storage</li>
	</ul>
	<h2>Autor</h2>
	<ul>
		<li>Carlos Oliveira</li>
	</ul>
</body>
</html>

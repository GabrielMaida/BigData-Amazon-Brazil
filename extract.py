import zipfile

with zipfile.ZipFile('amazon-brazil.zip', 'r') as zip_file:

	zip_file.extractall()
	print('Sucesso na extração')

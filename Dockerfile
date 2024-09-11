# Use uma imagem base com Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

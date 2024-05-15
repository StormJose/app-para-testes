# App para testes


## Instalação

Para criar um Ambiente Virtual para um projeto em Python / Django:

```
  python -m venv "nome_do_ambiente"
```

No Windows, insira o caminho onde o arquivo /activate foi gerado para ativar o **Ambiente Virtual:**

```
"nome_do_ambiente"\Scripts\activate
```


Agora instale as dependências do projeto:

```
pip install -r requirements.txt
```


Atualizando as dependências do projeto :

```
pip freeze > requirements.txt
```


No diretório raiz, inicialize a aplicação:

```
python manage.py runserver
```

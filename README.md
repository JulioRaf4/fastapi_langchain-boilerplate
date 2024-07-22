Certifique-se de ter o `Poetry` instalado. Você pode instalar o `Poetry` seguindo as instruções na [documentação oficial](https://python-poetry.org/docs/#installation).

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio/backend```

2. Instale
    ```poetry install```

3. Inicie o ambiente virtual
    ```poetry shell```

4. Iniciando o projeto
    No diretorio ./backend
    ```uvicorn service.main:app --reload```

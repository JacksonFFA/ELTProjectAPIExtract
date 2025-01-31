# ETL com Python e Requests

## Descrição do Projeto

Este projeto implementa um processo de ETL (Extract, Transform, Load) utilizando Python e a biblioteca requests. O objetivo é extrair dados de uma API, transformá-los conforme a necessidade e carregá-los em um banco de dados.

## Tecnologias Utilizadas

Python 3.x

Requests

Pandas

SQLAlchemy

SQLite (ou outro banco de dados configurável)

## Estrutura do Projeto

/etl_project
│── main.py          # Script principal de ETL
│── extract.py       # Módulo de extração de dados
│── transform.py     # Módulo de transformação de dados
│── load.py          # Módulo de carregamento de dados
│── config.py        # Configurações do projeto
│── requirements.txt # Dependências do projeto
│── README.md        # Documentação do projeto

## Instalação

1. Clone este repositório:

    git clone https://github.com/seu-usuario/etl_project.git
    Navegue até o diretório do projeto:
    cd etl_project

2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

3. Instale as dependências:
    ``` bash
   pip install -r requirements.txt
   ```

Uso

4. Execute o processo ETL:
    ```bash
   python erc/extract.py
   python erc/transform.py
   python erc/load.py
   ```

## Contribuição

Fique à vontade para contribuir enviando pull requests ou relatando issues.

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
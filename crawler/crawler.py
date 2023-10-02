import requests
import pandas as pd


def run_crawler_fbi(tabela, conexao, schema):
    page = [1, 2, 3, 4, 5]  ## pega apenas as 5 primeiras páginas

    for pagina in page:
        url = f"https://api.fbi.gov/@wanted?pageSize=20&page={pagina}&sort_on=modified&sort_order=desc"

        requisicao = requests.get(url).json()

        lista_criminosos = []

        for criminoso in requisicao["items"]:
            entrada_criminoso = {
                "procurado_id": criminoso["@id"],
                "procurado_apelido": criminoso["legat_names"],
                "data_de_nascimento": criminoso["dates_of_birth_used"],
                "cor_cabelo": criminoso["hair"],
                "cor_olhos": criminoso["eyes"],
                "procurado_peso": criminoso["weight"],
                "procurado_altura": criminoso["height_max"],
                "procurado_profissao": criminoso["occupations"],
                "marcas_cicatrizes": criminoso["scars_and_marks"],
                "procurado_ncic": criminoso["ncic"],
                "recompensa": criminoso["reward_max"],
                "aviso": criminoso["warning_message"],
                "local_nascimento": criminoso["place_of_birth"],
                "nacionalidade": criminoso["nationality"],
                "sexo": criminoso["sex"],
                "raca": criminoso["race"],
            }

            lista_criminosos.append(entrada_criminoso)

    dataframe_criminosos = pd.DataFrame(lista_criminosos)
    dataframe_criminosos.to_sql(tabela, conexao, schema)


# Nome da tabela
tabela = "procurado"
# Nome do schema
schema = "public"
# Dados de conexão: exemplo: postgresql://myuser:mypassword@localhost:5432/mydatabas`
conexao = "postgresql://postgres:postgres@localhost:5432/idwall"

run_crawler_fbi(tabela, conexao, schema)

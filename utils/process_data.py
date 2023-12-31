#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-IMPORTS

import inflection # A biblioteca inflection é uma ferramenta útil para manipulação de strings em Python
import pandas as pd

#Código dos países para auxiliar no tratamento dos dados no dataframe
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

#Código de cores para auxiliar no tratamento dos dados no dataframe
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

# Renomeia as colunas do DataFrame para que sigam a convenção snake_case, removendo espaços e aplicando capitalização de título. O DataFrame resultante com as colunas renomeadas é retornado.
def rename_columns(dataframe):
    df = dataframe.copy()

    title = lambda x: inflection.titleize(x)

    snakecase = lambda x: inflection.underscore(x)

    spaces = lambda x: x.replace(" ", "")

    cols_old = list(df.columns)

    cols_old = list(map(title, cols_old))

    cols_old = list(map(spaces, cols_old))

    cols_new = list(map(snakecase, cols_old))

    df.columns = cols_new

    return df

# As funç~oes abaixo são responsáveis por mapear alguns dados do dataframe e modificá-los de a cordo com os dicionários criados no início desse código
def country_name(country_id):
    return COUNTRIES[country_id]


def color_name(color_code):
    return COLORS[color_code]


def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

# Ajusta a ordem das colunas do dataframe
def adjust_columns_order(dataframe):
    df = dataframe.copy()

    new_cols_order = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df.loc[:, new_cols_order]

# Essa é a função principal que lê o endereço de um dataframe e aplica todos os passos criados acima e mais alguns e depois retorna e salva o dataframe modificado em um novo arquivo .csv
def process_data(file_path):
    df = pd.read_csv(file_path)

    df = rename_columns(df)

    df = df.dropna()

    df["price_type"] = df.loc[:, "price_range"].apply(lambda x: create_price_tye(x))

    df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x))

    df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x))

    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    df = df.drop(df[(df["cuisines"] == "Drinks Only")].index)

    df = df.drop(df[(df["cuisines"] == "Mineira")].index)

    df = df.drop_duplicates()

    df = adjust_columns_order(df)

    df.to_csv("./data/processed/data.csv", index=False)

    return df

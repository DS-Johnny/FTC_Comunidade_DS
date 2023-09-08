import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def read_processed_data():
    return pd.read_csv("./data/processed/data.csv")

# Filtra os dados para incluir apenas os restaurantes dos países especificados, agrupa esses dados por país e cidade e conta a quantidade de restaurantes em cada cidade, cria um gráfico de barras que mostra as 10 cidades com mais restaurantes na base de dados, onde as cidades são representadas no eixo x e a quantidade de restaurantes no eixo y, com a cor representando o país.
def top_cities_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country", "city"]]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 10 Cidades com mais Restaurantes na Base de Dados",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig

# Filtra os restaurantes dos países especificados, mas desta vez seleciona apenas aqueles com uma média de avaliação maior ou igual a 4 e cria um gráfico de barras mostrando as 7 cidades com restaurantes de alta avaliação.
def top_best_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] >= 4) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com Restaurantes com média de avaliação acima de 4",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig

# Filtra os restaurantes dos países especificados, mas desta vez seleciona apenas aqueles com uma média de avaliação menor ou igual a 2.5 e cria um gráfico de barras mostrando as 7 cidades com restaurantes de baixa avaliação.
def top_worst_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] <= 2.5) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig

# Filtra os restaurantes dos países especificados e conta quantos tipos culinários diferentes existem em cada cidade. Ela cria um gráfico de barras mostrando as 10 cidades com mais tipos culinários distintos, onde as cidades são representadas no eixo x e a quantidade de tipos culinários únicos no eixo y, com a cor representando o país.
def most_cuisines(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["cuisines", "country", "city"]]
        .groupby(["country", "city"])
        .nunique()
        .sort_values(["cuisines", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="cuisines",
        text="cuisines",
        color="country",
        title="Top 10 Cidades mais restaurantes com tipos culinários distintos",
        labels={
            "city": "Cidades",
            "cuisines": "Quantidade de Tipos Culinários Únicos",
            "country": "País",
        },
    )

    return fig

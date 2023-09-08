import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

#  Esta função simplesmente lê e carrega um arquivo CSV chamado "data.csv" localizado na pasta "./data/processed/" e retorna os dados como um DataFrame do pandas.
def read_processed_data():
    return pd.read_csv("./data/processed/data.csv")

# Esta função recebe uma lista de países como entrada, filtra os dados para incluir apenas os restaurantes dos países especificados, agrupa esses dados por país e conta a quantidade de restaurantes em cada país. Em seguida, ela cria um gráfico de barras que mostra a quantidade de restaurantes registrados por país usando a biblioteca Plotly Express.
def countries_restaurants(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country"]]
        .groupby("country")
        .count()
        .sort_values("restaurant_id", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="restaurant_id",
        text="restaurant_id",
        title="Quantidade de Restaurantes Registrados por País",
        labels={
            "country": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        },
    )

    return fig

# Esta função recebe uma lista de países como entrada. Ela filtra os dados para incluir apenas as cidades dos países especificados, agrupa esses dados por país e conta a quantidade de cidades únicas em cada país. Em seguida, ela cria um gráfico de barras que mostra a quantidade de cidades registradas por país.
def countries_cities(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["city", "country"]]
        .groupby("country")
        .nunique()
        .sort_values("city", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="city",
        text="city",
        title="Quantidade de Cidades Registrados por País",
        labels={
            "country": "Paises",
            "city": "Quantidade de Cidades",
        },
    )

    return fig

# Filtra os dados para incluir apenas as avaliações dos restaurantes dos países especificados, agrupa esses dados por país e calcula a média das avaliações em cada país. Em seguida, ela cria um gráfico de barras que mostra a média de avaliações feitas por país.
def countries_mean_votes(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["votes", "country"]]
        .groupby("country")
        .mean()
        .sort_values("votes", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="votes",
        text="votes",
        text_auto=".2f",
        title="Média de Avaliações feitas por País",
        labels={
            "country": "Paises",
            "votes": "Quantidade de Avaliações",
        },
    )

    return fig

# Filtra os dados para incluir apenas o preço médio de um prato para duas pessoas dos restaurantes dos países especificados, agrupa esses dados por país e calcula a média dos preços em cada país. Em seguida, ela cria um gráfico de barras que mostra a média de preços de pratos para duas pessoas por país.
def countries_average_plate(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["average_cost_for_two", "country"]]
        .groupby("country")
        .mean()
        .sort_values("average_cost_for_two", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="average_cost_for_two",
        text="average_cost_for_two",
        text_auto=".2f",
        title="Média de Preço de um prato para duas pessoas por País",
        labels={
            "country": "Paises",
            "average_cost_for_two": "Preço de prato para duas Pessoas",
        },
    )

    return fig

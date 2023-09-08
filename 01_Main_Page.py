#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=IMPORTS
import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

#IMPORT CUSTOM PACKAGES THAT TREATS THIS DATA
from utils import general_data as gd
from utils.process_data import process_data


RAW_DATA_PATH = f"./data/raw/data.csv"


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-CREATE SIDEBAR ON STREAMLIT

def create_sidebar(df):
    image_path = "./img/" # Caminho até a imagem
    image = Image.open(image_path + "logo.png") # Utiliza a biblioteca Pillow (PIL) para carregar a imagem logo na variável image

    col1, col2 = st.sidebar.columns([1, 4], gap="small") # Cria duas colunas no sidebar, uma coluna ocupa 1/5 do espaço, a outra coluna ocupa 4/5 do espaço, há um gap pequeno entre elas 
    col1.image(image, width=35) # exibe a logo
    col2.markdown("# Fome Zero")

    st.sidebar.markdown("## Filtros")

    #Cria um componente de seleção multipla no sidebar
    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    st.sidebar.markdown("### Dados Tratados")

    processed_data = pd.read_csv("./data/processed/data.csv") # Caminho até os dados tratados
    
    #Cria um botão de download dos dados tratados/processados
    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )
    
    #Retorna a seleção de países feita pelo usuário
    return list(countries)



#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Create a folium map

def create_map(dataframe):
    f = folium.Figure(width=1920, height=1080) # define um objeto figura de mapa folium com as dimensões

    m = folium.Map(max_bounds=True).add_to(f) # Adiciona um mapa à figura f, O argumento max_bounds=True permite que o mapa ajuste automaticamente os limites para incluir todos os marcadores.

    marker_cluster = MarkerCluster().add_to(m) # Cria um cluster de marcadores para agrupar vários marcadores próximos no mapa. Isso melhora a usabilidade quando há muitos marcadores próximos uns dos outros.

    for _, line in dataframe.iterrows():
        # Extrai do dataframe as informações que serão utilizadas nos markers
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'
        
        # Um bloco HTML é criado para exibir informações sobre o restaurante, como nome, preço médio, tipo de culinária e classificação agregada. As informações são formatadas nesse bloco HTML.
        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)
        
        #Cria um popup personalizado para o marcador do restaurante. O popup contém o bloco HTML com as informações formatadas.
        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )
        
        # Cria um marcador no mapa Folium com base nas coordenadas de latitude e longitude do restaurante. O popup personalizado é associado a este marcador, e um ícone personalizado é definido com base na cor e em um ícone "home" da biblioteca FontAwesome.
        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)
    # Exibe o mapa interativo dentro de um elemento Streamlit chamado folium_static
    folium_static(m, width=1024, height=768)

#create_map(df)

# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Função Principal para iniciar o app
def main():

    df = process_data(RAW_DATA_PATH) # Esta função carrega e prepara os dados para uso posterior no aplicativo.
    
    # Configura a página do aplicativo Streamlit. Define o título da página, o ícone da página como um emoji de gráfico e o layout como "wide" (amplo), que é uma configuração de layout para ocupar mais espaço horizontal na tela.
    st.set_page_config(page_title="Home", page_icon="📊", layout="wide")

    selected_countries = create_sidebar(df) # Chama a função que ao mesmo tempo que cria o sidebar, também retorna a seleção de países feita pelo usuário

    st.markdown("# Fome Zero!")

    st.markdown("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")

    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")

    restaurants, countries, cities, ratings, cuisines = st.columns(5) # Cria colunas para separar e organiza as métricas de negócio
    
    # Abaixo temos a exibição das métricas, que utiliza as respecitivas colunas, e os valores são obtidos através da função de tratamento de dados importada de utils
    restaurants.metric(
        "Restaurantes Cadastrados",
        gd.qty_restaurants(df),
    )

    countries.metric(
        "Países Cadastrados",
        gd.qty_countries(df),
    )

    cities.metric(
        "Cidades Cadastrados",
        gd.qty_cities(df),
    )

    ratings.metric(
        "Avaliações Feitas na Plataforma",
        f"{gd.qty_ratings(df):,}".replace(",", "."),
    )

    cuisines.metric(
        f"Tipos de Culinárias\nOferecidas",
        f"{gd.qty_cuisines(df):,}",
    )
    
    # FILTRA EM UM DATAFRAME APENAS AS INFORMAÇÕES DOS PAÍSES SELECIONADOS 
    map_df = df.loc[df["country"].isin(selected_countries), :]

    create_map(map_df) # Chama a função que cria o mapa e que leva como argumento o dataframe filtrado pela seleção do usuário

    return None #Esta função não retorna nenhum valor

if __name__ == "__main__":
    main()
    
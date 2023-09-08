#=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-= IMPORTS
import streamlit as st

import utils.countries_data as cdt


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Cria Sidebar no Streamlit
def make_sidebar(df):
    st.sidebar.markdown("## Filtros")
    
    #Cria um componente de seleção multipla no sidebar
    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return list(countries) # retorna os países selecionados


def main():
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    # Chama uma função chamada read_processed_data do módulo cdt para carregar dados processados
    df = cdt.read_processed_data()
    
    # Chama a função que cria o sidebar e filtra os países selecionados pelo usuário
    countries = make_sidebar(df)

    st.markdown("# :earth_americas: Visão Países")
    
    # A seguir são gerados gráficos utilizando as funções criadas em 'utils/countries_data.py' e exibidos no streamlit utilizando a função plotly_chart()
    fig = cdt.countries_restaurants(countries)

    st.plotly_chart(fig, use_container_width=True)

    fig = cdt.countries_cities(countries)

    st.plotly_chart(fig, use_container_width=True)

    votes, plate_price = st.columns(2)

    with votes:
        fig = cdt.countries_mean_votes(countries)

        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = cdt.countries_average_plate(countries)

        st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":
    main()
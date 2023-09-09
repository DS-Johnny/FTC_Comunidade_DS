# Projeto final do Fast Track Course da Comunidade DS
---
## Problema de negócio:
A startup chamada Fome Zero é um marketplace fictício de restaurantes. Seu core business é facilitar o enontro e negociações de clientes e restaurantes.
Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

O CEO precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às perguntas de negócio.

---
## Os Dados
O conjunto de dados que representam o contexto está disponível na plataforma do
Kaggle. O link para acesso aos dados :
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

---
## Premissas Assumidas para a análise
- Marketplace foi o modelo de negócio assumido.
- As 3 principais visões consideradas para as análises foram: Países, Cidades e Culinária 


---
## Desenvolvimento do projeto
Com o objetivo de facilitar a organização do código das páginas *Streamlit*, o tratamento dos dados foi modularizado incluindo também as análises feitas utilizando a biblioteca *Pandas* e os gráficos utilizando a biblioteca *Plotly*.

O resultado final é um painel online hospedado no *Streamlit Cloud* que pode ser acessado através do link: https://ftcfomezero.streamlit.app/


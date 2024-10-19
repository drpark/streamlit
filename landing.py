import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('data_sites_web.xlsx', index_col=0, header=0)
data.columns = data.columns.str.replace("'", " ", regex=True)

st.set_page_config(page_title="Ch'tis websites analysis")
# Titre de l'application
st.title("Ch'tis websites analysis")

# Ajouter du texte
st.write('Analyse comparative par indicateur')

# ajouter un selecteur
option = st.selectbox(
    'Quel parametre souhaitez vous comparer ?',
    data.columns)


# Afficher le site selectionne
st.bar_chart(data[option], x_label="Site web", y_label="valeur en %")


# diagramme arrainée
# Ajouter un sélecteur pour choisir le site
site = st.selectbox(
    'Quel site souhaitez-vous analyser ?',
    data.index)  # Colonne des sites



# Afficher le site selectionne
df = pd.DataFrame(dict(
    # attention utliser loc plutot que iloc , iloc pour i nombre
    r=data.loc[site],
    theta=data.columns))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)

st.plotly_chart(fig)


# Ajouter du texte
st.write('Vitesse des sites par ordre croissant')


sorted=data.sort_values(by="Vitesse de chargement", ascending=True)
sorted.to_csv('data_sites_web_sorted.csv')
sorted = pd.read_csv('data_sites_web_sorted.csv')
plt.figure(figsize=(10, 6))

sns.barplot(x=sorted['Sites internet '], y=sorted['Vitesse de chargement'],
            data=sorted, palette='Blues_d')

# Rotation des labels de l'axe x pour qu'ils ne se chevauchent pas
plt.xticks(rotation=45, ha='right')



# Afficher le graphique dans Streamlit
st.pyplot(plt)

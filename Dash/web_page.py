# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_jadot_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Jadot.csv')
fig_jadot_hashtag = px.bar(df_jadot_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Jadot")

df_roussel_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Roussel.csv')
fig_roussel_hashtag = px.bar(df_roussel_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Roussel")

df_zemmour_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Zemmour.csv')
fig_zemmour_hashtag= px.bar(df_zemmour_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Zemmour")

df_pecresse_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Pécresse.csv')
fig_pecresse_hashtag = px.bar(df_pecresse_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Pecresse")

df_macron_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Macron.csv')
fig_macron_hashtag = px.bar(df_macron_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Macron")

df_lepen_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Lepen.csv')
fig_lepen_hashtag = px.bar(df_lepen_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Lepen")

df_poutou_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Poutou.csv')
fig_poutou_hashtag = px.bar(df_poutou_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Poutou")

df_hidalgo_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Hidalgo.csv')
fig_hidalgo_hashtag = px.bar(df_hidalgo_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Hidalgo")

df_dupontaignan_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Dupont-Aignan.csv')
fig_dupontaignan_hashtag = px.bar(df_dupontaignan_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Dupont-Aignan")

df_arthaud_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Arthaud.csv')
fig_arthaud_hashtag = px.bar(df_arthaud_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Arthaud")

df_lassalle_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Lassalle.csv')
fig_lasalle_hashtag = px.bar(df_lassalle_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Lasalle")

df_melenchon_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Mélenchon.csv')
fig_melenchon_hashtag = px.bar(df_melenchon_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(x="Thèmes"), range_y = [0,50], title= "Mélenchon")

app.layout = html.Div(children=[
    html.H1(children='TX00 - Présentation des résultats'),

    html.H2(children='''
       Résultat par hashtag
    '''),

    dcc.Graph(
        id='Jadot hashtag',
        figure=fig_jadot_hashtag
    ),
    dcc.Graph(
        id='Roussel hashtag',
        figure=fig_roussel_hashtag
    ),
    dcc.Graph(
        id='Zemmourhashtag',
        figure=fig_zemmour_hashtag
    ),
    dcc.Graph(
        id='Pecress hashtag',
        figure=fig_pecresse_hashtag
    ),
    dcc.Graph(
        id='Macron hashtag',
        figure=fig_macron_hashtag
    ),
    dcc.Graph(
        id='Lepen hashtag',
        figure=fig_lepen_hashtag
    ),
    dcc.Graph(
        id='Poutou hashtag',
        figure=fig_poutou_hashtag
    ),
    dcc.Graph(
        id='Hidalgo hashtag',
        figure=fig_hidalgo_hashtag
    ),
    dcc.Graph(
        id='Dupont Aignan hashtag',
        figure=fig_dupontaignan_hashtag
    ),
    dcc.Graph(
        id='Arthaud hashtag',
        figure=fig_arthaud_hashtag
    ),
    dcc.Graph(
        id='Lasalle hashtag',
        figure=fig_lasalle_hashtag
    ),
    dcc.Graph(
        id='Melenchon hashtag',
        figure=fig_melenchon_hashtag
    ),



])

if __name__ == '__main__':
    app.run_server(debug=True)
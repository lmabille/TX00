# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options



#COMPTES

df_jadot_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Jadot.csv')
fig_jadot_comptes = px.bar(df_jadot_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50],title= "Répartition des tweets du compte officiel du candidat Jadot").update_layout(xaxis_title="Thèmes politiques")

df_roussel_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Roussel.csv')
fig_roussel_comptes = px.bar(df_roussel_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies", range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Roussel").update_layout(xaxis_title="Thèmes politiques").update_layout(xaxis_title="Thèmes politiques")

df_zemmour_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Zemmour.csv')
fig_zemmour_comptes= px.bar(df_zemmour_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Zemmour").update_layout(xaxis_title="Thèmes politiques")

df_pecresse_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Pécresse.csv')
fig_pecresse_comptes = px.bar(df_pecresse_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Pécresse").update_layout(xaxis_title="Thèmes politiques")

df_macron_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Macron.csv')
fig_macron_comptes = px.bar(df_macron_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Macron").update_layout(xaxis_title="Thèmes politiques")

df_lepen_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Lepen.csv')
fig_lepen_comptes = px.bar(df_lepen_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Lepen").update_layout(xaxis_title="Thèmes politiques")

df_poutou_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Poutou.csv')
fig_poutou_comptes = px.bar(df_poutou_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Poutou").update_layout(xaxis_title="Thèmes politiques")

df_hidalgo_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Hidalgo.csv')
fig_hidalgo_comptes = px.bar(df_hidalgo_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Hidalgo").update_layout(xaxis_title="Thèmes politiques")

df_dupontaignan_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Dupont-Aignan.csv')
fig_dupontaignan_comptes = px.bar(df_dupontaignan_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Dupont-Aignan").update_layout(xaxis_title="Thèmes politiques")

df_arthaud_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Arthaud.csv')
fig_arthaud_comptes = px.bar(df_arthaud_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Arthaud").update_layout(xaxis_title="Thèmes politiques")

df_lassalle_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Lassalle.csv')
fig_lasalle_comptes = px.bar(df_lassalle_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Lasalle").update_layout(xaxis_title="Thèmes politiques")

df_melenchon_comptes = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/comptes/Mélenchon.csv')
fig_melenchon_comptes = px.bar(df_melenchon_comptes, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Mélenchon").update_layout(xaxis_title="Thèmes politiques")

#HASHTAG
df_jadot_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Jadot.csv')
fig_jadot_hashtag = px.bar(df_jadot_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50],title= "Répartition des tweets du compte officiel du candidat Jadot").update_layout(xaxis_title="Thèmes politiques")

df_roussel_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Roussel.csv')
fig_roussel_hashtag = px.bar(df_roussel_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Roussel").update_layout(xaxis_title="Thèmes politiques").update_layout(xaxis_title="Thèmes politiques")


df_zemmour_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Zemmour.csv')
fig_zemmour_hashtag=  px.bar(df_zemmour_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Zemmour").update_layout(xaxis_title="Thèmes politiques")


df_pecresse_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Pécresse.csv')
fig_pecresse_hashtag = px.bar(df_pecresse_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Pécresse").update_layout(xaxis_title="Thèmes politiques")

df_macron_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Macron.csv')
fig_macron_hashtag = px.bar(df_macron_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Macron").update_layout(xaxis_title="Thèmes politiques")

df_lepen_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Lepen.csv')
fig_lepen_hashtag = px.bar(df_lepen_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Lepen").update_layout(xaxis_title="Thèmes politiques")

df_poutou_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Poutou.csv')
fig_poutou_hashtag = px.bar(df_poutou_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Poutou").update_layout(xaxis_title="Thèmes politiques")

df_hidalgo_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Hidalgo.csv')
fig_hidalgo_hashtag = px.bar(df_hidalgo_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Hidalgo").update_layout(xaxis_title="Thèmes politiques")

df_dupontaignan_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Dupont-Aignan.csv')
fig_dupontaignan_hashtag = px.bar(df_dupontaignan_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Dupont-Aignan").update_layout(xaxis_title="Thèmes politiques")

df_arthaud_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Arthaud.csv')
fig_arthaud_hashtag = px.bar(df_arthaud_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Arthaud").update_layout(xaxis_title="Thèmes politiques")

df_lassalle_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Lassalle.csv')
fig_lasalle_hashtag = px.bar(df_lassalle_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Lasalle").update_layout(xaxis_title="Thèmes politiques")

df_melenchon_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/hashtags/Mélenchon.csv')
fig_melenchon_hashtag = px.bar(df_melenchon_hashtag, x=["ecologie", "economie", "education", "immigration", "sante", "securite_defense"], y="tweets_lies",labels=dict(tweets_lies="Tweets associés au thème (en %)"), range_y = [0,50], title="Répartition des tweets du compte officiel du candidat Mélenchon").update_layout(xaxis_title="Thèmes politiques")
#SERIE TEMPORELLE
df_melenchon_time_account = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/temporelle/time/melenchon_time_account')
fig_melechon_time_account = px.histogram(df_melenchon_time_account, x="date", y=df_melenchon_time_account.columns,hover_data={"date": "|%B %d, %Y"},title='Nombre de tweets par thème de Janvier à Avril 2022 du compte officiel du candidat Roussel',labels=dict(variable="Thèmes politiques")).update_layout(xaxis_title="Date",yaxis_title="Nombre de tweets")
fig_melechon_time_account.update_traces(xbins_size="D1")
fig_melechon_time_account.update_xaxes(
    tickformat="%b\n%Y",
    ticklabelmode="period")

df_melenchon_time_hashtag = pd.read_csv('/home/lumabill/Documents/TX00/Dash/Graph/temporelle/time/melenchon_time_hashtag.csv')
fig_melechon_time_hashtag = px.histogram(df_melenchon_time_hashtag, x="date", y=df_melenchon_time_hashtag.columns,
              hover_data={"date": "|%B %d, %Y"},
              title="Nombre de tweets par thème de Janvier à Avril 2022 liés au hashtag 'Roussel'",
              labels=dict(variable="Thèmes politiques")).update_layout(xaxis_title="Date",yaxis_title="Nombre de tweets")
fig_melechon_time_hashtag.update_traces(xbins_size="D1")
fig_melechon_time_hashtag.update_xaxes(
    #dtick="M1",
    tickformat="%b\n%Y",
    ticklabelmode="period")






app.layout = html.Div(children=[
    html.H1(children='TX00 - Présentation des résultats'),

    html.H2(children='''
           Résultat par Comptes
        '''),
    dcc.Graph(
        id='Jadot comptes',
        figure=fig_jadot_comptes
    ),
    dcc.Graph(
        id='Roussel comptes',
        figure=fig_roussel_comptes
    ),
    dcc.Graph(
        id='Zemmour comptes',
        figure=fig_zemmour_comptes
    ),
    dcc.Graph(
        id='Pecress comptes',
        figure=fig_pecresse_comptes
    ),
    dcc.Graph(
        id='Macron comptes',
        figure=fig_macron_comptes
    ),
    dcc.Graph(
        id='Lepen comptes',
        figure=fig_lepen_comptes
    ),
    dcc.Graph(
        id='Poutou comptes',
        figure=fig_poutou_comptes
    ),
    dcc.Graph(
        id='Hidalgo comptes',
        figure=fig_hidalgo_comptes
    ),
    dcc.Graph(
        id='Dupont Aignan comptes',
        figure=fig_dupontaignan_comptes
    ),
    dcc.Graph(
        id='Arthaud comptes',
        figure=fig_arthaud_comptes
    ),
    dcc.Graph(
        id='Lasalle comptes',
        figure=fig_lasalle_comptes
    ),
    dcc.Graph(
        id='Melenchon comptes',
        figure=fig_melenchon_comptes
    ),
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
    html.H2(children='''
       Séries temporelles
    '''),
    dcc.Graph(
        id='Melenchon time account',
        figure=fig_melechon_time_account
    ),
dcc.Graph(
        id='Melenchon time hashtags',
        figure=fig_melechon_time_hashtag
    ),
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")
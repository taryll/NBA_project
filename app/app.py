import streamlit as st
import pandas as pd
import pickle

df_path_interim = "../data/interim/"

df_player_stats = pd.read_csv(df_path_interim + "df_player_stats_app.csv")
drop_columns = ['league_id', 'team_id', 'min', 'id', 'full_name', 'season_id', 'player_id', 'fg_pct', 'fg3_pct', 'ft_pct']

model1 = pickle.load(open("../models/model1", 'rb'))

st.write("# NBA Player Predicting 2k Rating")

user_input = st.text_input("Input the player name", "Stephen Curry")
user_input = " ".join(user_input.split()).lower()
condition = (df_player_stats['full_name'].str.lower() == user_input).any()

if condition:
    df_predict_input = df_player_stats[df_player_stats['full_name'].str.lower() == user_input]

    X = df_predict_input.drop(drop_columns, axis = 1)

    predict = model1.predict(X.drop(['rating'], axis = 1)).round(2)[0]
    actual = X['rating'].to_numpy()[0]

    st.write(f"Rating predicted: {predict}")
    st.write(f"Rating actual value: {actual}")

else:
    st.write(f"Sorry, we don't have this name in our database. Try another one")








# st.table(df_player_rating_stats_filter)
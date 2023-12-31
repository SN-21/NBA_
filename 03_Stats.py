import streamlit as st
import pandas as pd

from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.library.parameters import MeasureTypeDetailedDefense
from nba_api.stats.endpoints import leaguedashteamshotlocations

row1_1, row1_2, row1_3 = st.columns((3, 2, 3))

with row1_1:
    st.title(" ")

with row1_2:
    st.title("__TEAM STATS__")

with row1_3:
    st.title(" ")


def DfIndexNameToTeamname(df):
    df_new_index = df.set_axis(
        [
            "Atlanta Hawks",
            "Boston Celtics",
            "Brooklyn Nets",
            "Charlotte Hornets",
            "Chicago Bulls",
            "Cleveland Cavaliers",
            "Dallas Mavericks",
            "Denver Nuggets",
            "Detroit Pistons",
            "Golden State Warriors",
            "Houston Rockets",
            "Indiana Pacers",
            "LA Clippers",
            "Los Angeles Lakers",
            "Memphis Grizzlies",
            "Miami Heat",
            "Milwaukee Bucks",
            "Minnesota Timberwolves",
            "New Orleans Pelicans",
            "New York Knicks",
            "Oklahoma City Thunder",
            "Orlando Magic",
            "Philadelphia 76ers",
            "Phoenix Suns",
            "Portland Trail Blazers",
            "Sacramento Kings",
            "San Antonio Spurs",
            "Toronto Raptors",
            "Utah Jazz",
            "Washington Wizards",
        ]
    )

    return df_new_index


def drop_columns (df, drop_columns):
    df_drop = df.drop (drop_columns, axis= 1)
    
    return df_drop


def style_format (df, format_columns):
    df_style = df.style.format (format_columns)
    
    return df_style

teamstats_a = leaguedashteamstats.LeagueDashTeamStats(
    last_n_games=82, measure_type_detailed_defense="Advanced"
)
df_adovenced = teamstats_a.league_dash_team_stats.get_data_frame()

df_adovenced_new_index = DfIndexNameToTeamname(df_adovenced)

adovenced_drop_columns = ["TEAM_ID", "MIN", "TEAM_NAME"]

df_adovenced_new_index_drop = drop_columns (df_adovenced_new_index, adovenced_drop_columns)


adovenced_format_columns =     {
        "W_PCT": "{:.3f}",
        "E_OFF_RATING": "{:.1f}",
        "OFF_RATING": "{:.1f}",
        "E_DEF_RATING": "{:.1f}",
        "DEF_RATING": "{:.1f}",
        "E_NET_RATING": "{:.1f}",
        "NET_RATING": "{:.1f}",
        "E_PACE": "{:.1f}",
        "AST_RATIO": "{:.1f}",
        "PACE": "{:.2f}",
        "PACE_PER40": " {:.1f}",
        "AST_TO": "{:.1f}",
        "AST_PCT": "{:.3f}",
        "OREB_PCT": "{:.3f}",
        "DREB_PCT": "{:.3f}",
        "REB_PCT": "{:.3f}",
        "TM_TOV_PCT": "{:.3f}",
        "EFG_PCT": "{:.3f}",
        "TS_PCT": "{:.3f}",
    }

df_adovenced_fin = style_format (df_adovenced_new_index_drop, adovenced_format_columns)


teamstats_scoring = leaguedashteamstats.LeagueDashTeamStats(
    last_n_games=30, measure_type_detailed_defense="Scoring"
)

df_scoring = teamstats_scoring.league_dash_team_stats.get_data_frame()

df_scoring_new_index = DfIndexNameToTeamname(df_scoring)

scoring_drop_columns = ["TEAM_ID", "MIN", "TEAM_NAME"]

df_scoring_new_index_drop = drop_columns (df_scoring_new_index, scoring_drop_columns)

scoring_format_columns = {"W_PCT": "{:.3f}",
        "PCT_FGA_2PT": "{:.3f}",
        "PCT_FGA_3PT": "{:.3f}",
        "PCT_PTS_2PT": "{:.3f}",
        "PCT_PTS_2PT_MR": "{:.3f}",
        "PCT_PTS_3PT": "{:.3f}",
        "PCT_PTS_FB": "{:.3f}",
        "PCT_PTS_FT": "{:.3f}",
        "PCT_PTS_OFF_TOV": "{:.3f}",
        "PCT_PTS_PAINT": "{:.3f}",
        "PCT_AST_2PM": " {:.3f}",
        "PCT_UAST_2PM": "{:.3f}",
        "PCT_AST_3PM": "{:.3f}",
        "PCT_UAST_3PM": "{:.3f}",
        "PCT_AST_FGM": "{:.3f}",
        "PCT_UAST_FGM": "{:.3f}",}


df_scoring_style = style_format (df_scoring_new_index_drop, scoring_format_columns)



teamstats_defense = leaguedashteamstats.LeagueDashTeamStats(
    last_n_games=82, measure_type_detailed_defense="Defense"
)

df_defense = teamstats_defense.league_dash_team_stats.get_data_frame()

df_defense_new_index = DfIndexNameToTeamname(df_defense)

defense_drop_columns = ["TEAM_ID", "MIN", "TEAM_NAME"]

df_defense_new_index_drop = drop_columns (df_defense_new_index, defense_drop_columns)

defense_format_columns = {
        "W_PCT": "{:.3f}",
        "DEF_RATING": "{:.1f}",
        "DREB_PCT": "{:.3f}",
        "OPP_PTS_OFF_TOV": "{:.0f}",
        "OPP_PTS_2ND_CHANCE": "{:.0f}",
        "OPP_PTS_FB": "{:.0f}",
        "OPP_PTS_PAINT": "{:.0f}",
    }

df_defense_style = style_format (df_defense_new_index_drop, defense_format_columns)



shot_location = leaguedashteamshotlocations.LeagueDashTeamShotLocations (last_n_games= 82)
df = shot_location.shot_locations.get_data_frame ()

df.columns = ['_'.join(col).strip() for col in df.columns.values]

new_index = [
            "Atlanta Hawks",
            "Boston Celtics",
            "Brooklyn Nets",
            "Charlotte Hornets",
            "Chicago Bulls",
            "Cleveland Cavaliers",
            "Dallas Mavericks",
            "Denver Nuggets",
            "Detroit Pistons",
            "Golden State Warriors",
            "Houston Rockets",
            "Indiana Pacers",
            "LA Clippers",
            "Los Angeles Lakers",
            "Memphis Grizzlies",
            "Miami Heat",
            "Milwaukee Bucks",
            "Minnesota Timberwolves",
            "New Orleans Pelicans",
            "New York Knicks",
            "Oklahoma City Thunder",
            "Orlando Magic",
            "Philadelphia 76ers",
            "Phoenix Suns",
            "Portland Trail Blazers",
            "Sacramento Kings",
            "San Antonio Spurs",
            "Toronto Raptors",
            "Utah Jazz",
            "Washington Wizards",
        ]

df.index = new_index

shot_location_drop_columns = ["_TEAM_ID", "_TEAM_NAME"]

df_shot_location_drop = drop_columns (df, shot_location_drop_columns)

shot_location_format_columns = {'Restricted Area_FG_PCT': "{:.3f}", 
                                'In The Paint (Non-RA)_FG_PCT': "{:.3f}",
                                'Mid-Range_FG_PCT': "{:.3f}",
                                'Left Corner 3_FG_PCT': "{:.3f}",
                                'Right Corner 3_FG_PCT': "{:.3f}",
                                'Above the Break 3_FG_PCT': "{:.3f}",
                                'Backcourt_FG_PCT': "{:.3f}",
                                'Corner 3_FG_PCT': "{:.3f}",}

df_shot_location_style = style_format (df_shot_location_drop, shot_location_format_columns)




tab1, tab2, tab3, tab4 = st.tabs(["Adovenced Stats", "Scoring Stats", "Defence Stats", "Shot Location"])
with tab1:
    st.dataframe(df_adovenced_fin, use_container_width=True)

with tab2:
    st.dataframe(df_scoring_style, use_container_width=True)

with tab3:
    st.dataframe(df_defense_style, use_container_width=True)

with tab4:
    st.dataframe(df_shot_location_style, use_container_width=True)
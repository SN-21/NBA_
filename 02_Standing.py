import streamlit as st
import pandas as pd

from st_aggrid import AgGrid
from nba_api.stats.endpoints import leaguestandingsv3

row1_1, row1_2, row1_3 = st.columns((3, 2, 3))

with row1_1:
    st.title(" ")

with row1_2:
    st.title("__STANDING__")

with row1_3:
    st.title(" ")

standing_v3 = leaguestandingsv3.LeagueStandingsV3()
df_st = standing_v3.standings.get_data_frame()

df = df_st.sort_values("TeamCity")


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


df_standing = DfIndexNameToTeamname(df)


def DfstandingColumnOrderChange(df):
    df_standing_column_order_change = df[
        [
            "WINS",
            "LOSSES",
            "WinPCT",
            "ConferenceGamesBack",
            "Conference",
            "ConferenceRecord",
            "PlayoffRank",
            "HOME",
            "ROAD",
            "L10",
            "OT",
            "ThreePTSOrLess",
            "TenPTSOrMore",
            "LongWinStreak",
            "LongLossStreak",
            "strCurrentStreak",
            "ClinchedPlayoffBirth",
            "ClinchedPlayIn",
            "EliminatedConference",
            "AheadAtHalf",
            "BehindAtHalf",
            "TiedAtHalf",
            "AheadAtThird",
            "BehindAtThird",
            "TiedAtThird",
            "OppOver500",
            "PointsPG",
            "OppPointsPG",
            "DiffPointsPG",
            "vsEast",
            "vsWest",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    ]

    return df_standing_column_order_change


df_standing_change = DfstandingColumnOrderChange(df_standing)

df_standing_change_style = df_standing_change.style.format(
    {
        "W_PCT": "{:.3f}",
        "ConferenceGameBack": "{:.1f}",
    }
)

df_standing_east = df_standing_change.query('Conference == "East"')
df_standing_west = df_standing_change.query('Conference == "West"')

df_standing_east1 = df_standing_east.sort_values("PlayoffRank")
df_standing_east2 = df_standing_east1.drop(["Conference"], axis=1)

df_standing_west1 = df_standing_west.sort_values("PlayoffRank")
df_standing_west2 = df_standing_west1.drop(["Conference"], axis=1)

df_standing_east_style = df_standing_east2.style.format(
    {
        "WinPCT": "{:.3f}",
        "ConferenceGamesBack": "{:.1f}",
    }
)


df_standing_west_style = df_standing_west2.style.format(
    {
        "WinPCT": "{:.3f}",
        "ConferenceGamesBack": "{:.1f}",
    }
)
# st.sidebar.header("Standing")
# if st.sidebar.checkbox("Standing"):
tab1, tab2 = st.tabs(["East standing", "West standing"])
with tab1:
    st.dataframe(df_standing_east_style)

with tab2:
    st.dataframe(df_standing_west_style)

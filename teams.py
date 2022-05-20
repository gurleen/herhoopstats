from dataclasses import dataclass
from typing import List

import pandas as pd

from request import make_request


@dataclass
class Team:
    season: str
    team: str
    games_played: int
    wins: int
    losses: int
    win_pct: float
    ppg: float
    opp_ppg: float
    net_ppg: float
    pts_per_100_pos: float
    opp_pts_per_100_pos: float
    net_pts_per_100_pos: float
    pace: float
    link: str

    


def get_teams_df() -> pd.DataFrame:
    df = make_request("https://herhoopstats.com/stats/ncaa/research/team_single_seasons/?min_season=2022&max_season=2022&division=1&games=all&stats_to_show=summary&submit=true")
    df.rename(columns={
        "SEASON": "season",
        "Team": "team",
        "G": "games_played",
        "win": "wins",
        "loss": "losses",
        "Win%": "win_pct",
        "PTS": "ppg",
        "OPP PTS": "opp_ppg",
        "Net PTS": "net_ppg",
        "Off Rtg": "pts_per_100_pos",
        "Def Rtg": "opp_pts_per_100_pos",
        "Net Rtg": "net_pts_per_100_pos",
    }, inplace=True)
    df["win_pct"] = df["win_pct"].str.rstrip("%").astype(float)
    return df

def get_teams() -> List[Team]:
    df = get_teams_df()
    return [Team(**data) for data in df.to_dict(orient="records")]

def get_summary_df(team: dict) -> pd.DataFrame:
    path = team["link"]

    df = make_request()
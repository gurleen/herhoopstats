from dataclasses import asdict, dataclass, fields
from enum import Enum
from json import dumps


def cast_or_none(type, value):
    try:
        return type(value)
    except ValueError:
        return None


class StructMixin:
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                setattr(self, field.name, cast_or_none(field.type, value))

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return dumps(self.to_dict())


@dataclass
class Team(StructMixin):
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


@dataclass
class TeamStatistic(StructMixin):
    name: str
    value: float
    percentile: int
    rank: str


class TeamStatisticType(Enum):
    SUMMARY = 0
    SUMMARY_ADVANCED = 1
    SHOOTING = 2
    OPP_SHOOTING = 3
    REBOUNDING = 4
    OPP_REBOUNDING = 5
    OTHER = 6
    OPP_OTHER = 7
    SCORING_TOTALS = 8
    OPP_SCORING_TOTALS = 9
    OTHER_TOTALS = 10
    OPP_OTHER_TOTALS = 11


@dataclass
class Player(StructMixin):
    name: str
    games_played: int
    games_started: int
    minutes_per_game: float
    points_per_game: float
    fgm: float
    fga: float
    fg_pct: float
    twopt_made: float
    twopt_attempted: float
    twopt_pct: float
    threept_made: float
    threept_attempted: float
    threept_pct: float
    ftm: float
    fta: float
    ft_pct: float
    off_reb: float
    def_reb: float
    tot_reb: float
    ast_per_game: float
    to_per_game: float
    stl_per_game: float
    blk_per_game: float
    pf_per_game: float
    link: str

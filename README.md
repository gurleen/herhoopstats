# Her Hoop Stats

Provides access to the [Her Hoops Stats](https://herhoopstats.com) service for women's basketball (WNBA/NCAA) statistics. Subscription required.

## Installation

Python >= 3.5

`pip install herhoopstats`

## Usage

```python
from herhoopstats.api import HerHoopStats

api = HerHoopStats(email="<EMAIL>", password="<PASSWORD>")

teams = api.get_teams()
drexel = [t for t in teams if t.team == "Drexel"][0]
stats = api.get_team_statistics(drexel)
roster = api.get_roster_for_team(drexel)
```
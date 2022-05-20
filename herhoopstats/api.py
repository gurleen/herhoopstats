from typing import List, Literal, TypeVar

import bs4
import mechanicalsoup
import requests

from herhoopstats.structs import Team, Player, TeamStatistic, TeamStatisticType


T = TypeVar("T")


HERHOOPSTATS_BASE_URL = "https://herhoopstats.com"
HERHOOPSTATS_LOGIN_URL = "https://herhoopstats.com/accounts/login/"


class HerHoopStats:
    _browser: mechanicalsoup.StatefulBrowser

    def __init__(self, email: str, password: str) -> None:
        self._browser = mechanicalsoup.StatefulBrowser()
        self._browser.open(HERHOOPSTATS_LOGIN_URL)
        self._browser.select_form()
        self._browser["email"] = email
        self._browser["password"] = password
        self._browser.submit_selected()

    def _get_table(self, page: requests.Response, table_idx: int = 0):
        return page.soup.find_all("table")[table_idx]

    def _get_table_data(
        self, table: bs4.element.Tag, attach_links: bool = False
    ) -> list:
        table_data = [
            [cell.text.strip().rstrip("%") for cell in row("td")] for row in table("tr")
        ][1:]
        if attach_links:
            links = [tag["href"] for tag in table.find_all("a")]
            for row, link in zip(table_data, links):
                row.append(link)
        return table_data

    def _get_table_at_page(
        self, url: str, convert_to: T, table_idx: int = 0, attach_links: bool = False
    ) -> List[T]:
        response = self._browser.get(url)
        table = self._get_table(response, table_idx)
        table_data = self._get_table_data(table, attach_links=attach_links)
        return [convert_to(*data) for data in table_data]

    def get_teams(
        self,
        min_season: int = 2022,
        max_season: int = 2022,
        divison: Literal[1, 2, 3] = 1,
    ) -> List[Team]:
        full_url = (
            f"https://herhoopstats.com/stats/ncaa/research/"
            f"team_single_seasons/?min_season={min_season}&max_season={max_season}&division={divison}"
            f"&games=all&stats_to_show=summary&submit=true"
        )
        return self._get_table_at_page(full_url, Team, attach_links=True)

    def get_team_statistics(
        self, team: Team, stat_type: TeamStatisticType = TeamStatisticType.SUMMARY
    ) -> List[TeamStatistic]:
        full_url = f"{HERHOOPSTATS_BASE_URL}{team.link}"
        return self._get_table_at_page(
            full_url, TeamStatistic, table_idx=stat_type.value
        )

    def get_roster_for_team(self, team: Team) -> List[Player]:
        full_url = f"{HERHOOPSTATS_BASE_URL}{team.link}"
        return self._get_table_at_page(
            full_url, Player, table_idx=12, attach_links=True
        )

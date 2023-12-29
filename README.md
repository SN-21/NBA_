# NBA\_

## nba_api is the APIs of NBA.com

it use of 'streamlit' and 'nba_api'

```python
import streamlit as st
import pandas as pd
```

[streamlit](https://github.com/streamlit/streamlit)
[nba_api](https://github.com/swar/nba_api/tree/master)
[NBA.com](https://www.nba.com/)

## GameScore

```python
from nba_api.live.nba.endpoints import boxscore, scoreboard
from nba_api.stats.endpoints import boxscoreusagev2
from nba_api.stats.endpoints import playbyplay
```

it show today's game score
and tab's show

- Game information

  - Location is Matches were played arena,arena city and arena state
  - Attendance is attend Number of visitors
  - Officials is 3official that's games official

- Inactive player

  - away and home team inactive player name and inactive reason

- Team stats

  - it's show team traditinal stats like 'FGM'

- Game Chart

  - it's show game chart like biglead etc

- Box Score

  - it's show game boxscore (traditional)

- Usage

  - it's show game each player usage

- Play by play
  - it's show every each play

## Standing

- It's standing of Eastern Conference and Western Confrence

## Stats

- It's team stats that adovenced , scoring and defense

## Leader

- It's League stats leader per game and total

## Lineup

- It's league best lineup minutes 50minutes

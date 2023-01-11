"""Calculating Some Advanced Stats For Caleb Love."""


class Player:
    stats: dict[str, int]

    def __init__(self, game: dict[str, int]) -> None:
        """Constructor of the class."""
        self.stats = game
    
    def true_shooting(self) -> float:
        """Returns a player's true shooting percentage from a game."""
        result: float = (self.stats["pts"]) / (2 * (self.stats["fga"] + (0.44 * self.stats["fta"])))
        return result
    
    def effective_fg_percentage(self) -> float:
        """Calculates a player's effective feild goal percentage for a game."""
        result: float = (self.stats["fgm"] + (0.5 * self.stats["3pm"])) / (self.stats["fga"])
        return result


love_vs_marquette: Player = Player({"pts": 23.0, "fgm": 6.0, "fga": 15.0, "fta": 7.0, "3pm": 6.0, "ast": 1.0, "stl": 0.0, "tov": 2.0})
print(f"Stats vs Marquette: {love_vs_marquette.true_shooting()}") 
print(love_vs_marquette.effective_fg_percentage())

love_vs_baylor: Player = Player({"pts": 5.0, "fgm": 1.0, "fga": 6.0, "fta": 2.0, "3pm": 1.0, "ast": 2.0, "stl": 1.0, "tov": 6.0})
print(f"Love stats vs Baylor: {love_vs_baylor.true_shooting()}")
print(love_vs_baylor.effective_fg_percentage())

love_vs_ucla: Player = Player({"pts": 30.0, "fgm": 11.0, "fga": 24.0, "fta": 2.0, "3pm": 6.0, "ast": 4.0, "stl": 0.0, "tov": 1.0})
print(f"Love stats vs UCLA: {love_vs_ucla.true_shooting()}")
print(love_vs_ucla.effective_fg_percentage())


love_vs_stpeters: Player = Player({"pts": 14.0, "fgm": 6.0, "fga": 17.0, "fta": 1.0, "3pm": 2.0, "ast": 4.0, "stl": 0.0, "tov": 2.0})
print(f"Love stats vs St. Peters: {love_vs_stpeters.true_shooting()}")
print(love_vs_stpeters.effective_fg_percentage())


love_vs_duke: Player = Player({"pts": 28.0, "fgm": 11.0, "fga": 20.0, "fta": 4.0, "3pm": 3.0, "ast": 1.0, "stl": 0.0, "tov": 4.0})
print(f"Love stats vs Duke: {love_vs_duke.true_shooting()}")
print(love_vs_duke.effective_fg_percentage())


love_vs_kansas: Player = Player({"pts": 13.0, "fgm": 5.0, "fga": 24.0, "fta": 2.0, "3pm": 1.0, "ast": 2.0, "stl": 0.0, "tov": 4.0})
print(f"Love stats vs Kansas: {love_vs_kansas.true_shooting()}")
print(love_vs_kansas.effective_fg_percentage())
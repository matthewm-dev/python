def split_players_into_teams(players):
    """
    Split a list of players into two teams based on even and odd indices.
    Args:
        players (list): List of player names
    Returns:
        tuple: (even_indexed_players, odd_indexed_players)
    """
    even = players[::2]    # Items at indices 0, 2, 4, ...
    odd = players[1::2]    # Items at indices 1, 3, 5, ...
    return even, odd

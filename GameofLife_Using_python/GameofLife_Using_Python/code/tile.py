class Tile:
    """
Represents one board tile.

Each Tile has:
- name: display label for CLI
- tile_type: used by rule logic (e.g., START, EVENT, PAYDAY, RETIRE)
- cash_effect: deterministic cash change applied on landing
"""

    def __init__(self, name: str, tile_type: str, cash_effect: int = 0) -> None:
        self._name = name
        self._type = tile_type
        self._cash_effect = cash_effect

    @property
    def name(self) -> str:
        return self._name

    @property
    def tile_type(self) -> str:
        return self._type

    @property
    def cash_effect(self) -> int:
        return self._cash_effect
    
    
    
    
    
    # --- AI ASSISTANCE LOG ---
# AI support was used for:
# - Structuring object-oriented class design
# - Refining modular responsibilities
# - Debugging indentation and import errors
# - Improving pytest test structure
# - Configuring Sphinx autodoc documentation
#
# All suggestions were reviewed, adapted, and manually tested.
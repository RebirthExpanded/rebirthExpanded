"""Luxio (ME - POR 27 -- JP M3 026, the art here).

Stage 1 Lightning Pokemon, evolves from Shinx. HP 90, weakness Fighting x2,
no resistance, retreat 1.

  Ability  Fighting Roar  If your opponent's Active Pokemon is a Pokemon ex,
                          this Pokemon can evolve during your first turn or
                          the turn you play it.
  Static Shock [LC] 40

may_evolve_early lifts both the first-turn and the just-played gates, read
live: the opponent's Active must be a Pokemon ex when the evolution is
offered.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, is_pokemon_ex
from spirit.game.models.board import board_of
from spirit.game.session.passives import Passive, carrier_pokemon


class FightingRoarPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        board = board_of(pokemon)
        if board is None:
            return False
        opponent = next((pid for pid in board.player_ids
                         if pid != pokemon.owning_player_id), None)
        active = board.active_pokemon(opponent) if opponent else None
        return active is not None and is_pokemon_ex(active.archetype_id)


card = PokemonCardDef(
    guid="c3ea08d2-042d-5e81-8901-42d03435f546",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    family_id=403,
    abilities=[
        Ability(title="Fighting Roar",
                game_text="If your opponent's Active Pokémon is a Pokémon ex, this Pokémon can evolve during your first turn or the turn you play it.",
                passive=FightingRoarPassive()),
        Attack(title="Static Shock", game_text="",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=40),
    ],
)

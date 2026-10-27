"""Garbodor (ME4 57 -- JP M4 055; English CRI/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_pokemon_tool


class GloomyGarbagePassive(Passive):
    """The opponent's Active Pokemon with a Pokemon Tool attached does 20
    less damage with its attacks (before Weakness and Resistance)."""

    def modify_damage_dealt(self, calc, carrier):
        a = calc.attacker
        if not (calc.is_attack and a is not None and a.owning_player_id != carrier.owning_player_id):
            return
        if calc.board.active_pokemon(a.owning_player_id) is not a:
            return
        if any(is_pokemon_tool(c) for c in a.children):
            calc.amount = max(0, calc.amount - 20)


card = PokemonCardDef(
    guid="bedcd9a4-3a90-5251-9cfa-927b02da31e4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Gloomy Garbage",
            game_text="Attacks used by your opponent's Active Pokémon that has a Pokémon Tool attached do 20 less damage (before applying Weakness and Resistance).",
            passive=GloomyGarbagePassive(),
        ),
        Attack(
            title="Sludge Bomb",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)

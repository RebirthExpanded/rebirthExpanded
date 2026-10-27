"""Zoroark ex (MEZ 7 -- JP MEZ 007; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="495b299c-8bac-5675-b1d9-c26bdb259b3b",
    key="MEZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroarkex.Name",
    display_name="Zoroark ex",
    searchable_by=["Zoroark ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=7,
    set_code="MEZ",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Riotous Beating",
            game_text="This attack does 20 damage for each of your Pokémon in play.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine"), 20),
        ),
        Attack(
            title="Slash Down",
            game_text="During your next turn, this Pokémon can't use Slash Down.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)

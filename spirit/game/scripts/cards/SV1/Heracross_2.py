"""Heracross (SV1 2 -- JP SV1V 002; English SVI/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="76fd5feb-e58b-5efd-90c4-a795b666b10e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Superpowered Throw",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_defender_retreat, 30, base=10),
        ),
        Attack(
            title="Horn Attack",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)

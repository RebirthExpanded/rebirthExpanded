"""Stoutland (SV3 172 -- JP SVD 096; English OBF/172). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx) -> int:
    d = ctx.opponent_active()
    return effective_retreat_cost(ctx.board, d) if d is not None else 0


card = PokemonCardDef(
    guid="4145aa58-b278-53be-8c22-973361888bd2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=172,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Chomp Chomp Panic",
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(_defender_retreat, 50),
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)

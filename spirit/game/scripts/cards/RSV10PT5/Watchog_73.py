"""Watchog (RSV10PT5 73 -- JP SV11W 071; English WHT/153, WHT/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


async def focus_energy(ctx):
    await pc.apply_own_next_turn_boost(ctx, 160, "Hyper Fang")


card = PokemonCardDef(
    guid="61af062e-1f2e-5a13-a1de-e5f17ef6877a",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, this Pokémon's Hyper Fang attack's base damage is 240.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=focus_energy,
        ),
        Attack(
            title="Hyper Fang",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.flip_or_nothing(),
        ),
    ],
)

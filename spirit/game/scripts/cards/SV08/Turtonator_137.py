"""Turtonator (SV08 137 -- JP SV7a 044; English SSP/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _defender_ex(ctx) -> bool:
    return ctx.defender is not None and "ex" in (subtypes_for(ctx.defender.archetype_id) or [])


async def fully_singe(ctx):
    d = ctx.opponent_active()
    if d is not None and _defender_ex(ctx) and not ctx.effects_blocked(d) and ctx.attached_energies(d):
        await ctx.discard_energy_from(d, 1, minimum=1, prompt="Choose an Energy to discard")


card = PokemonCardDef(
    guid="741deced-4235-579d-abae-d99845557fd6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=776,
    abilities=[
        Attack(
            title="Fully Singe",
            game_text="Discard an Energy from your opponent's Active Pokémon ex.",
            cost={PokemonTypes.FIRE: 1},
            effect=fully_singe,
        ),
        Attack(
            title="Steaming Stomp",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

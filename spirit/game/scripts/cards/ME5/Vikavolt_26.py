"""Vikavolt (ME5 26 -- JP M5 025; English PBL/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _voltaic(ctx) -> bool:
    return any(getattr(def_for(e.archetype_id), "display_name", None) == "Voltaic Lightning Energy"
               for e in ctx.attached_energies(ctx.attacker))


async def giga_railgun(ctx):
    if _voltaic(ctx):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="c7d86cc7-6eb1-527b-b6b2-bf3894c1f98a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Quick Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=ac.snipe_attack(50, pool="any"),
        ),
        Attack(
            title="Giga Railgun",
            game_text="If this Pokémon has no Voltaic Lightning Energy attached, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=260,
            effect=giga_railgun,
        ),
    ],
)

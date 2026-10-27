"""Snorlax (ME6A 95 -- JP M6a 095; English 30C/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon



class GoodSleepPassive(Passive):
    """Remaining Asleep through Pokemon Checkup heals all damage (Ability)."""

    def heals_when_stays_asleep(self, pokemon, carrier):
        return pokemon is carrier


async def collapse(ctx):
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="af4fa8db-9060-5e26-9315-3d9645879622",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Ability(
            title="Good Sleep",
            game_text="If this Pokémon remains Asleep during Pokémon Checkup, heal all damage from this Pokémon.",
            passive=GoodSleepPassive(),
        ),
        Attack(
            title="Collapse",
            game_text="This Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=collapse,
        ),
    ],
)

"""Slaking (SV2 162 -- JP SV2P 062; English PAL/162). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon



class StirAndSnoozePassive(Passive):
    """Asleep: flip 2 coins at Checkup; any tails keeps it Asleep."""

    def sleep_checkup_coins(self, pokemon, carrier):
        return 2 if pokemon is carrier_pokemon(carrier) else 0


async def slackers_headstrike(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="38b563cc-06a0-5c0e-a265-9274b35ee7e6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=162,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Stir and Snooze",
            game_text="If this Pokémon is Asleep, flip 2 coins instead of 1 during Pokémon Checkup. If either of them is tails, this Pokémon is still Asleep.",
            passive=StirAndSnoozePassive(),
        ),
        Attack(
            title="Slacker's Headstrike",
            game_text="This Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=slackers_headstrike,
        ),
    ],
)

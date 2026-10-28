"""Spinda (SV4 151 -- JP SV4K 058; English PAR/151). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions


def _has_condition(pokemon, *conditions) -> bool:
    have = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [] if pokemon is not None else []
    return any(CLIENT_SPECIAL_CONDITION_NAMES[c] in have for c in conditions)



class TangledFeetPassive(Passive):
    """Confused: an attack's damage is prevented on heads (an Ability)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and target is me and calc.amount > 0 and _has_condition(me, SpecialConditions.CONFUSED)):
            return None
        results = await ctx.flip_coins(1, "Tangled Feet", source=me, flipper_id=me.owning_player_id)
        return 0 if results and results[0] else None


async def teetering_steps(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="7d244c9f-a876-58eb-8d4b-d9ecf124d51f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Ability(
            title="Tangled Feet",
            game_text="If this Pokémon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            passive=TangledFeetPassive(),
        ),
        Attack(
            title="Teetering Steps",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=teetering_steps,
        ),
    ],
)

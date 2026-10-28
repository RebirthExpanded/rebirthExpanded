"""Flamigo (SV3 185 -- JP SV3 099; English OBF/185). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def synchronized_feathers(ctx):
    if any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Flamigo" for p in ctx.my_bench()):
        await ac.snipe_attack(60, pool="bench", also_base=True)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="ea21560b-b7c0-564c-90ae-7a98f5155a0a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title="Peck",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Synchronized Feathers",
            game_text="If Flamigo is on your Bench, this attack also does 60 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=synchronized_feathers,
        ),
    ],
)

"""Scovillain (SV3 25 -- JP SV3 011; English OBF/25, PAF/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class DoubleTypePassive(Passive):
    """In play: Grass and Fire type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        return [PokemonTypes.GRASS.value, PokemonTypes.FIRE.value]


async def spicy_headbutt(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="64a413dd-da5d-5c10-801f-b01a8fdd8012",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name",
    display_name="Scovillain",
    searchable_by=["Scovillain", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pokémon is in play, it is Grass and Fire type.",
            passive=DoubleTypePassive(),
        ),
        Attack(
            title="Spicy Headbutt",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=spicy_headbutt,
        ),
    ],
)

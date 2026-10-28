"""Scizor (SV3 141 -- JP SV3 077; English OBF/141, OBF/205, PAF/191). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _has_ability(pokemon) -> bool:
    return any(isinstance(e, dict) and e.get("abilityType") not in (None, "Attack")
               for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or []))


async def punishing_scissors(ctx):
    n = sum(1 for p in ctx.opponent_pokemon_in_play() if _has_ability(p))
    await ctx.deal_damage(10 + 50 * n)


card = PokemonCardDef(
    guid="45281e05-6194-5554-b0b3-0b901598c7d6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=141,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Punishing Scissors",
            game_text="This attack does 50 more damage for each of your opponent's Pokémon in play that has an Ability.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=punishing_scissors,
        ),
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.METAL: 2},
            damage=70,
        ),
    ],
)

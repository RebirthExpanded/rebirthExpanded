"""Kilowattrel (SV045 22 -- JP SV4a 070; English PAF/146, PAF/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card


def _united_wings(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c)
               and any(getattr(a, "title", "") == "United Wings" for a in getattr(def_for(c.archetype_id), "abilities", [])))


async def united_thunder(ctx):
    n = _united_wings(ctx)
    if n:
        await ac.snipe_attack(10 * n, pool="bench")(ctx)


card = PokemonCardDef(
    guid="80942a25-ca55-54de-b288-487066be0242",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="United Thunder",
            game_text="This attack does 10 damage for each Pokémon in your discard pile that has the United Wings attack to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=united_thunder,
        ),
        Attack(
            title="Speed Wing",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

"""Misty's Gyarados (SV10 49 -- JP SV9a 026; English DRI/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred

from spirit.game.session.effects import is_pokemon_card


async def splashing_panic(ctx):
    top = list(ctx.deck_top(7))
    if top:
        await ctx.discard_cards(top)
    hits = sum(1 for c in top if is_pokemon_card(c) and _named("Misty's ")(c))
    if hits:
        await ctx.deal_damage(70 * hits)


card = PokemonCardDef(
    guid="3facd4ba-fac5-52db-bba7-ffec6259e49b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGyarados.Name",
    display_name="Misty's Gyarados",
    searchable_by=["Misty's Gyarados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Splashing Panic",
            game_text="Discard the top 7 cards of your deck, and this attack does 70 damage for each Misty's Pokémon that you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=70,
            damage_operator="x",
            effect=splashing_panic,
        ),
        Attack(
            title="Waterfall",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)

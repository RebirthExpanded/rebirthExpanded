"""Kecleon (ME6 57 -- JP M6 057; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


async def colorful_whip(ctx):
    pool = [c for c in ctx.hand() if is_pokemon_card(c)]
    picks = []
    if pool:
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Reveal any number of Pokémon from your hand.")
        if picks:
            await ctx.reveal_cards(picks)
    kinds = set()
    for c in picks:
        kinds.update(c.get_attribute(AttrID.POKEMON_TYPES) or [])
    await ctx.deal_damage(30 * len(kinds))


card = PokemonCardDef(
    guid="b0684728-5462-50cd-ad46-9ede0925c926",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Attack(
            title="Colorful Whip",
            game_text="Reveal any number of Pokémon from your hand. This attack does 30 damage for each type of Pokémon you revealed in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=colorful_whip,
        ),
    ],
)

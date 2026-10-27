"""Alcremie (SV07 65 -- JP SV7 044; English SCR/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.session.effects import is_pokemon_card


async def colorful_confection(ctx):
    types = {t.value for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e)
             for t in PokemonTypes if t != PokemonTypes.COLORLESS and is_energy_of_type(e, t)}
    if types:
        picks = await ctx.search_deck(lambda c: is_pokemon_card(c) and bool(types & set(c.get_attribute(AttrID.POKEMON_TYPES) or [])),
                                      count=5, minimum=0, prompt="Choose up to 5 Pokémon.")
        if picks:
            await ctx.put_in_hand(picks)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="73fb446a-0889-55d3-b2a2-36fadc8b4f9e",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Attack(
            title="Colorful Confection",
            game_text="Search your deck for up to 5 Pokémon that are the same type as any Basic Energy attached to this Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=colorful_confection,
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

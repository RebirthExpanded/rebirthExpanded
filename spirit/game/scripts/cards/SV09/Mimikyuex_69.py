"""Mimikyu ex (SV09 69 -- JP SVM 054; English JTG/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def mischievous_hands(ctx):
    pool = list(ctx.opponent_pokemon_in_play())
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=min(2, len(pool)),
                                   prompt="Choose 2 of your opponent's Pokémon")
    for p in picks:
        await ctx.deal_damage(30, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="b7e6b348-c420-5bd3-b230-b004748e109c",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyuex.Name",
    display_name="Mimikyu ex",
    searchable_by=["Mimikyu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=69,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=778,
    abilities=[
        Attack(
            title="Mischievous Hands",
            game_text="Choose 2 of your opponent's Pokémon and put 3 damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=mischievous_hands,
        ),
        Attack(
            title="Ghostly Trip",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)

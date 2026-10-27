"""Spectrier (ME2PT5 98 -- JP M2a 080; English ASC/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def phantasmal_barrage(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool:
        await ctx.discard_cards(pool)
    targets = ctx.opponent_pokemon_in_play()
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon to place 12 damage counters on") if targets else None
    if target is not None:
        await ctx.deal_damage(120, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="ebd62467-148c-5220-9f2f-9094c7d3a16c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spectrier.Name",
    display_name="Spectrier",
    searchable_by=["Spectrier", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=897,
    abilities=[
        Attack(
            title="Spooky Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Phantasmal Barrage",
            game_text="Discard all Energy from this Pokémon and place 12 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=phantasmal_barrage,
        ),
    ],
)

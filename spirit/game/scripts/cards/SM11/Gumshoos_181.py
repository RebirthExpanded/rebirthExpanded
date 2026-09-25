"""Gumshoos (SM - Unified Minds 181/236 -- JP SM11 078/094).

Stage 1 Colorless Pokemon, evolves from Yungoos. HP 100, weakness Fighting
x2, retreat 1.

  Alert Headbutt  [CC] 90  If your opponent's Active Pokemon is a Pokemon-GX
                           or Pokemon-EX, this attack's base damage is 30.

Pokemon-EX is the uppercase XY/BW mechanic, not a Scarlet & Violet ex.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import subtypes_for
from spirit.game.data_utils import Attack, PokemonCardDef


async def alert_headbutt(ctx):
    defender = ctx.defender
    subtypes = subtypes_for(defender.archetype_id) if defender is not None else []
    await ctx.deal_damage(30 if ("GX" in subtypes or "EX" in subtypes) else 90)


card = PokemonCardDef(
    guid="4e197395-768a-54ad-abe7-02186550c787",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=['Gumshoos', 'Stage 1', 'Gumshoos'],
    subtypes=['Stage 1'],
    collector_number=181,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Attack(title="Alert Headbutt", game_text="If your opponent's Active Pokémon is a Pokémon-GX or Pokémon-EX, this attack's base damage is 30.",
               cost={PokemonTypes.COLORLESS: 2}, damage=90,
               effect=alert_headbutt),
    ],
)

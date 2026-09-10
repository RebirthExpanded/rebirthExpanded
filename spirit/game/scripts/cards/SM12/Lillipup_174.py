"""Lillipup (SM - Cosmic Eclipse 174/236).

Basic Colorless Pokemon. HP 60, weakness Fighting x2, no resistance,
retreat 1.

  Baby-Doll Eyes [C]      The Defending Pokemon can't retreat during your
                          opponent's next turn.
  Tackle         [CCC] 40

Scrafty's Corner without the damage: ctx.lock_retreat on the defender,
guarded by effects_blocked so a Pokemon shielded from attack effects keeps
its retreat.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def baby_doll_eyes(ctx):
    """No damage; the Defending Pokemon can't retreat next turn."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="502ab2aa-25c8-59ca-8031-1a431d30d996",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic", "Lillipup"],
    subtypes=["Basic"],
    collector_number=174,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Baby-Doll Eyes",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=baby_doll_eyes,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

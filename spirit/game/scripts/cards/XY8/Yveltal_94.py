"""Yveltal (XY - BREAKthrough 94/162 -- JP XY8-Br 042/059, the art here).

Basic Darkness Pokemon. HP 130, weakness Lightning x2, resistance Fighting
-20, retreat 2.

  Ability: Fright Night  As long as this Pokemon is your Active Pokemon,
                         each Pokemon Tool card in play has no effect.
  Pitch-Black Spear [DCC] 60  This attack does 60 damage to 1 of your
                              opponent's Benched Pokemon-EX. (Don't apply
                              Weakness and Resistance for Benched Pokemon.)

Fright Night is Jamming Tower's suppresses_tool, switched on only while
Yveltal sits in the Active Spot -- every Tool on both sides, its own too.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive


class FrightNightPassive(Passive):
    def suppresses_tool(self, tool, carrier):
        return is_in_active_spot(carrier)


async def pitch_black_spear(ctx):
    await ctx.deal_damage()
    targets = [p for p in ctx.opponent_bench() if "EX" in subtypes_for(p.archetype_id)]
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Benched Pokémon-EX") or targets[0]
    await ctx.deal_damage(60, target=target)


card = PokemonCardDef(
    guid="98f0eb1f-8787-5f9b-afd2-48eec3bbe66b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Ability(
            title="Fright Night",
            game_text="As long as this Pokémon is your Active Pokémon, each Pokémon Tool card in play has no effect.",
            passive=FrightNightPassive(),
        ),
        Attack(
            title="Pitch-Black Spear",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=pitch_black_spear,
        ),
    ],
)

"""Diancie {*} (SM - Forbidden Light 74/131 -- JP SM6 051/094, the art here).

Basic Fighting Pokemon, Prism Star. HP 120, weakness Grass x2, no
resistance, retreat 2.

  Princess's Cheers  (Ability)  As long as this Pokemon is on your Bench,
                                your [F] Pokemon's attacks do 20 more damage
                                to your opponent's Active Pokemon (before
                                applying Weakness and Resistance).
  Diamond Rain       [FFF] 90   Heal 30 damage from each of your Benched
                                Pokemon.

Princess's Cheers is a team boost with a carrier condition: it counts only
while Diancie sits on the Bench, so an Active Diancie's own Diamond Rain
gets nothing from it. Prism Star: one per deck, and it goes to the Lost
Zone instead of the discard pile (both handled by the rarity / subtype).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import TeamDamageBoostPassive, is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type


class PrincessesCheersPassive(TeamDamageBoostPassive):
    """+20 for your [F] attackers while the carrier is on the Bench."""

    def __init__(self):
        super().__init__(20, attacker_pred=lambda p: is_pokemon_of_type(p, PokemonTypes.FIGHTING))

    def modify_damage_dealt(self, calc, carrier):
        if is_in_active_spot(carrier):
            return
        super().modify_damage_dealt(calc, carrier)


async def diamond_rain(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="87471d4c-d496-5afc-a807-c251f1f80080",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DianciePrismStar.Name",
    display_name="Diancie {*}",
    searchable_by=["Diancie", "Basic", "Prism Star"],
    subtypes=["Basic", "Prism Star"],
    collector_number=74,
    set_code="SM6",
    rarity=Rarities.Prism,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Cheers",
            game_text="As long as this Pokémon is on your Bench, your [F] Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=PrincessesCheersPassive(),
        ),
        Attack(
            title="Diamond Rain",
            game_text="Heal 30 damage from each of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
            effect=diamond_rain,
        ),
    ],
)

"""Hydreigon ex (SV - White Flare 067/086 -- JP SV11W 062/086, the art here).

Stage 2 Darkness Pokemon-ex (evolves from Zweilous). HP 330, weakness
Grass x2, retreat 3.

  Greedy Eater  (Ability)  If your opponent's Basic Pokemon is Knocked
                           Out by damage from an attack used by this
                           Pokemon, take 1 more Prize card.
  Dark Bite     [DDDCC] 200  During your opponent's next turn, the
                             Defending Pokemon can't retreat.

The bonus Prize is the knockout resolver's prize hook, gated three ways:
the KO'd Pokemon is a Basic, it was this Hydreigon's attack, and the
knockout came from that attack's DAMAGE.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon


class GreedyEaterPassive(Passive):
    """+1 Prize when this Pokemon's attack damage Knocks Out a Basic."""

    stacking_key = "GreedyEater"

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if ctx.attacker is not holder or not ctx.is_attack_effect():
            return count
        if pokemon.owning_player_id == holder.owning_player_id:
            return count
        if pokemon.entity_id not in ctx.attack_damage:
            return count
        if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value \
                or not is_basic_pokemon(pokemon):
            return count
        return count + 1


card = PokemonCardDef(
    guid="6c0e1eaa-59c0-5b03-8367-e167f339daca",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigonex.Name",
    display_name="Hydreigon ex",
    searchable_by=["Hydreigon ex", "Stage 2", "ex", "Hydreigonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=67,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Greedy Eater",
            game_text="If your opponent's Basic Pokémon is Knocked Out by damage from an attack used by this Pokémon, take 1 more Prize card.",
            passive=GreedyEaterPassive(),
        ),
        Attack(
            title="Dark Bite",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)

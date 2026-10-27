"""Steelix (ME6 38 -- JP M6 038; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


class HighDensityArmorPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if (calc.is_attack and calc.is_opposing and me is calc.target
                and me.get_attribute(AttrID.HP, 0) >= effective_max_hp(calc.board, me)):
            calc.amount = max(0, calc.amount - 60)


async def hard_swing(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="717ba32a-d4bd-5da0-a530-964d75585807",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Ability(
            title="High-Density Armor",
            game_text="If this Pokémon has full HP, it takes 60 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=HighDensityArmorPassive(),
        ),
        Attack(
            title="Hard Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=hard_swing,
        ),
    ],
)

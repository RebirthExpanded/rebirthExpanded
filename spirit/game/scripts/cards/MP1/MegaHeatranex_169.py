"""Mega Heatran ex (MP1 169 -- JP MP 169; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID
from spirit.game.session.passives import effective_max_hp


class HighDensityArmorPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if (calc.is_attack and calc.is_opposing and me is calc.target
                and me.get_attribute(AttrID.HP, 0) >= effective_max_hp(calc.board, me)):
            calc.amount = max(0, calc.amount - 60)


card = PokemonCardDef(
    guid="222788ff-bb6a-51ae-a5c4-7f54f89dbcd6",
    key="MP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHeatranex.Name",
    display_name="Mega Heatran ex",
    searchable_by=["Mega Heatran ex", "Basic", "ex", "SV_Mega"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=169,
    set_code="MP1",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=485,
    abilities=[
        Ability(
            title="High-Density Armor",
            game_text="If this Pokémon has full HP, it takes 60 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=HighDensityArmorPassive(),
        ),
        Attack(
            title="Gigantic Press",
            game_text="During your next turn, this Pokémon's Gigantic Press attack does 140 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 3},
            damage=140,
            effect=pc.boost_own_next_turn(140, "Gigantic Press"),
        ),
    ],
)

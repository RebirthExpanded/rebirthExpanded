"""Cubone (SV035 104 -- JP SV2a 104; English MEW/104). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac



class CheeringBonePassive(Passive):
    """On your Bench: your Marowak's attacks do 30 more to the opponent's Active."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if (calc.is_attack and calc.is_opposing and calc.to_active and attacker is not None
                and attacker.owning_player_id == carrier.owning_player_id
                and carrier._containing_area_name() == "bench"
                and attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Marowak"):
            calc.amount += 30
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonCardDef(
    guid="022faaf7-98ae-55f6-937a-c3df8f5e2492",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=104,
    abilities=[
        Ability(
            title="Cheering Bone",
            game_text="As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=CheeringBonePassive(),
        ),
        Attack(
            title="Hit Twice",
            game_text="Flip 2 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=10),
        ),
    ],
)

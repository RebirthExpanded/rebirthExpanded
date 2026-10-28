"""Dachsbun (SV045 39 -- JP SV1S 034; English PAF/161, PAF/39, SVI/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])



class WellBakedBodyPassive(Passive):
    """Can't be Burned; no damage from the opponent's Fire Pokemon."""

    def blocks_special_conditions(self, target, condition, carrier):
        return target is carrier_pokemon(carrier) and condition in (
            SpecialConditions.BURNED, getattr(SpecialConditions.BURNED, "value", None), "Burned")

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None and _of_type(calc.attacker, PokemonTypes.FIRE))


card = PokemonCardDef(
    guid="00af374d-d6a6-53b1-b73a-c0679ad2d336",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbun.Name",
    display_name="Dachsbun",
    searchable_by=["Dachsbun", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    family_id=926,
    abilities=[
        Ability(
            title="Well-Baked Body",
            game_text="This Pokémon can't be Burned. Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon.",
            passive=WellBakedBodyPassive(),
        ),
        Attack(
            title="Headbutt Bounce",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

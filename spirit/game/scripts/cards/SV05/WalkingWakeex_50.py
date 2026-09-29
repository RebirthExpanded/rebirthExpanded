from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.passives import Passive, carrier_pokemon


class AzureSeasPassive(Passive):
    """This Pokemon's attack damage ignores effects on the opponent's Active."""

    def attacks_ignore_target_effects(self, attacker, carrier):
        return carrier_pokemon(carrier) is attacker


def _defender_conditioned(ctx) -> bool:
    d = ctx.defender
    return d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS))

card = PokemonCardDef(
    guid="1822e876-f55b-53d2-80fc-7a1e2b7e1fb6",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWakeex.Name",
    display_name="Walking Wake ex",
    searchable_by=["Walking Wake ex", "Basic", "ex", "Ancient", "WalkingWakeex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=50,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1009,
    abilities=[
        Ability(
            title="Azure Seas",
            game_text="Damage from attacks used by this Pok\u00e9mon isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            passive=AzureSeasPassive(),
        ),
        Attack(
            title="Catharsis Roar",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_defender_conditioned, 120),
        ),
    ],
)

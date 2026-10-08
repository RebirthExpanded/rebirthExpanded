"""Regice (SM - Crimson Invasion 28/111 -- JP SM4A 014/050, the art here).

Basic Water Pokemon. HP 130, weakness Metal x2, retreat 3.

  Ability: Iceberg Shield  If you have Regirock in play, prevent all
                           effects of attacks, including damage, done to
                           this Pokemon by your opponent's Stage 2 Pokemon.
  Frost Smash [WCC] 70
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.models.board import board_of
from spirit.game.session.passives import Passive, carrier_pokemon


def _regirock_in_play(carrier) -> bool:
    board = board_of(carrier)
    if board is None:
        return False
    return any(getattr(def_for(p.archetype_id), "display_name", None) == "Regirock"
               for p in board.pokemon_in_play(carrier.owning_player_id))


def _opposing_stage2(attacker, carrier) -> bool:
    return (attacker is not None and attacker.owning_player_id != carrier.owning_player_id
            and attacker.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value)


class IcebergShieldPassive(Passive):
    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.target is carrier_pokemon(carrier)
                and _opposing_stage2(calc.attacker, carrier) and _regirock_in_play(carrier))

    def blocks_attack_effects(self, target, carrier, source=None):
        return (target is carrier_pokemon(carrier) and _opposing_stage2(source, carrier)
                and _regirock_in_play(carrier))


card = PokemonCardDef(
    guid="61963c9a-5c15-502e-a268-fe61bedb78d9",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Iceberg Shield",
            game_text="If you have Regirock in play, prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Stage 2 Pokémon.",
            passive=IcebergShieldPassive(),
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

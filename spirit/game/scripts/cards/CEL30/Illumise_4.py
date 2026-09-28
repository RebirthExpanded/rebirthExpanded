from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.models.board import board_of
from spirit.game.card_effects.passives_common import weakness_multiplier_passive


def _volbeat_in_play(calc, carrier) -> bool:
    """Any attack on an Active Pokemon, while this Illumise's owner has Volbeat in play."""
    if not calc.to_active:
        return False
    board = board_of(carrier)
    return board is not None and any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Volbeat"
        for p in board.pokemon_in_play(carrier.owning_player_id))

card = PokemonCardDef(
    guid="e8ab1e53-9749-5b5e-895f-056584767e93",
    key="CEL30",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="CEL30",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Ability(
            title="Supereffective Pheromones",
            game_text="If you have Volbeat in play, apply Weakness for both Active Pok\u00e9mon as \u00d73.",
            passive=weakness_multiplier_passive(3, when=_volbeat_in_play),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

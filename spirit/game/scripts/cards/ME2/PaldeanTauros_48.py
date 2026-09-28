from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.attributes import AttrID
from spirit.game.models.board import board_of
from spirit.game.card_effects.attacks_common import count_in_play, damage_per, recoil_attack
from spirit.game.session.passives import effective_max_hp


def _damaged_tauros(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    board = board_of(pokemon)
    return "Tauros" in name and board is not None and \
        pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)

card = PokemonCardDef(
    guid="2d5d1477-4ecb-5d55-b7a8-6766e41c0c9a",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic", "PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Charge",
            game_text="This attack does 40 damage for each of your Pok\u00e9mon that has \"Tauros\" in its name that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _damaged_tauros), 40),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=recoil_attack(20),
        ),
    ],
)

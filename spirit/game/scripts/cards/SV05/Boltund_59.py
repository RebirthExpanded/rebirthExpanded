"""Boltund (SV05 59 -- JP SVHM 005; English TEF/59). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_lightning(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.LIGHTNING)


def _on_bench(board, player_id, pokemon) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return bench is not None and pokemon.parent is bench



def _benched(p) -> bool:
    return p.parent is not None and p.parent.get_attribute(AttrID.NAME) == "bench"
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonCardDef(
    guid="c0fb6e7e-afcb-5551-94d3-f5f3b0d20a88",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    abilities=[
        Attack(
            title="Electrifying Dash",
            game_text="Search your deck for up to 2 Basic Lightning Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=su.search_attach_energy(_basic_lightning, count=2, target_pred=_benched, prompt="Choose up to 2 Basic Lightning Energy cards to attach to your Benched Pokémon."),
        ),
    ],
)

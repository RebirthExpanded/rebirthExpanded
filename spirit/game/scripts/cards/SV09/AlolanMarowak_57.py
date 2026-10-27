"""Alolan Marowak (SV09 57 -- JP SVM 047; English JTG/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


card = PokemonCardDef(
    guid="210d0af0-ff2a-5828-935b-ef30fb38f8d9",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 90),
        ),
        Attack(
            title="Will-O-Wisp",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

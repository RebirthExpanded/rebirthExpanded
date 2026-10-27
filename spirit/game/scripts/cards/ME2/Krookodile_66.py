"""Krookodile (ME2 66 -- JP M2 055; English PFL/66). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


card = PokemonCardDef(
    guid="710018a3-e7e1-5e4c-b23d-fd6b6c388ed3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Vengeful Fang",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 160 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 160),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)

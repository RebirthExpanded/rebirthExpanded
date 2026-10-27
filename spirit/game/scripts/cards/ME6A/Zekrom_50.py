"""Zekrom (ME6A 50 -- JP M6a 050; English 30C/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



def _has_energy_type(t):
    def cond(ctx) -> bool:
        return any(is_energy_of_type(e, t) for e in ctx.attached_energies(ctx.attacker))
    return cond


card = PokemonCardDef(
    guid="86fe7dd0-9502-56c1-b6ea-5b04deb4b202",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Nitro Thunder",
            game_text="If this Pokémon has any Fire Energy attaches, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_has_energy_type(PokemonTypes.FIRE), 80),
        ),
    ],
)

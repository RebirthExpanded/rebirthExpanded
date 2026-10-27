"""Cacturne (ME6 5 -- JP M6 005; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import AbilityTypes
from spirit.game.data_utils import ABILITIES_BY_ID


def _with_ability(ctx) -> int:
    n = 0
    for p in ctx.opponent_pokemon_in_play():
        for e in p.get_attribute(AttrID.PIE_ABILITIES) or []:
            a = ABILITIES_BY_ID.get(e.get("abilityID")) if isinstance(e, dict) else None
            if a is not None and a.ability_type == AbilityTypes.POKE_ABILITY:
                n += 1
                break
    return n


card = PokemonCardDef(
    guid="4a81ba8f-3a45-5f7b-8ddb-5ec8a12a5cc4",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Direct Hit",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(30, pool="any"),
        ),
        Attack(
            title="Punishment Needle",
            game_text="This attack does 50 more damage for each of your opponent's Pokémon in play that has an Ability.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_with_ability, 50, base=10),
        ),
    ],
)

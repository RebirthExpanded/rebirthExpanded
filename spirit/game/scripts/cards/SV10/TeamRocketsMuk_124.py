"""Team Rocket's Muk (SV10 124 -- JP SV10 068; English DRI/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _conditions(ctx) -> int:
    d = ctx.opponent_active()
    return len(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if d is not None else 0


card = PokemonCardDef(
    guid="d8b27f19-d071-5da0-be5e-29053b262100",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMuk.Name",
    display_name="Team Rocket's Muk",
    searchable_by=["Team Rocket's Muk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsGrimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Gooped Up",
            game_text="Your opponent's Active Pokémon is now Confused. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.condition_attack(SpecialConditions.CONFUSED, no_retreat=True),
        ),
        Attack(
            title="Hazardous Venom",
            game_text="This attack does 100 damage for each Special Condition affecting your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=ac.damage_per(_conditions, 100),
        ),
    ],
)

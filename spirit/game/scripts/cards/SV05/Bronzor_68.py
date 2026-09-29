from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import is_pokemon_of_type


def _defender_psychic(ctx) -> bool:
    return ctx.defender is not None and is_pokemon_of_type(ctx.defender, PokemonTypes.PSYCHIC)

card = PokemonCardDef(
    guid="133fbb5c-1422-5846-9205-773006e701ca",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=436,
    abilities=[
        Attack(
            title="Mirror Attack",
            game_text="If your opponent's Active Pok\u00e9mon is a [P] Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(_defender_psychic, 30),
        ),
    ],
)

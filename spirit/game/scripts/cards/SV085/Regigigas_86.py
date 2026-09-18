from spirit.game.data_utils import PokemonCardDef, Attack, subtypes_for
from spirit.game.card_effects.attacks_common import bonus_if


def _defender_is_tera(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and "Tera" in subtypes_for(defender.archetype_id)
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a5ba5f71-7921-5f7b-bde9-5c9ec4e9efb7",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas","Basic","Regigigas"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Jewel Breaker",
            game_text="If your opponent's Active Pokémon is a Tera Pokémon, this attack does 230 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_defender_is_tera, 230),
        ),
    ],
)

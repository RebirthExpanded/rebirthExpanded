from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _has_hide_n_sneak(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", None) == "Hide 'n' Sneak":
            return True
    return False


def _four_or_more_hide_n_sneak(ctx):
    return sum(1 for c in ctx.discard_pile() if _has_hide_n_sneak(c)) >= 4


card = PokemonCardDef(
    guid="71eb30d6-8ef0-5c0a-b729-83c221c406df",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise","Basic","Dhelmise"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Vengeful Anchor",
            game_text="If you have 4 or more Pokémon that have the Hide 'n' Sneak Ability in your discard pile, this attack does 140 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_four_or_more_hide_n_sneak, 140),
        ),
    ],
)

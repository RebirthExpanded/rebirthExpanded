from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import is_pokemon_ex
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import TeraRulePassive

card = PokemonCardDef(
    guid="efe75b2e-e65c-5bf0-8f79-617f6501c452",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Tera", "Miraidonex"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=73,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Hadron Spark",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and is_pokemon_ex(ctx.defender.archetype_id), 120),
        ),
    ],
)

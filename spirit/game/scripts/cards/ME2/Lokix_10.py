from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play

card = PokemonCardDef(
    guid="463fa108-c588-5071-98b0-b2d3c143ca6f",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1", "Lokix"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Jumping Shot",
            game_text="Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=remove_self_from_play("deck"),
        ),
    ],
)

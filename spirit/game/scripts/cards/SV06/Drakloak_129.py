from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import look_at_top_2_keep_1
from spirit.game.card_effects.support_common import requires_deck

# Pidgeotto's Air Mail is the same Ability, so the effect is shared.
recon_directive = look_at_top_2_keep_1


card = PokemonCardDef(
    guid="177b666d-9e56-4c45-90cf-981cbd51672c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    display_name="Drakloak",
    searchable_by=["Drakloak", "Stage 1", "Drakloak"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    family_id=885,
    abilities=[
        Ability(
            title="Recon Directive",
            game_text=(
                "Once during your turn, you may look at the top 2 cards of "
                "your deck and put 1 of them into your hand. Put the other "
                "card on the bottom of your deck."
            ),
            activation=Activations.ONCE_PER_TURN,
            # Nothing to look at, nothing to do: not offered on an empty deck.
            condition=requires_deck(),
            effect=recon_directive,
        ),
        Attack(
            title="Dragon Headbutt",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)


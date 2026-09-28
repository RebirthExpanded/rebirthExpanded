from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class SoSubmergedPassive(Passive):
    """On the Bench: no damage from, and no effects of, opposing attacks."""

    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing and calc.target is carrier
                and not is_in_active_spot(carrier))

    def blocks_attack_effects(self, target, carrier, source=None):
        return target is carrier and not is_in_active_spot(carrier)

card = PokemonCardDef(
    guid="76e8cf4c-8aa3-5fdf-a720-9e5ac823c08a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    display_name="Misty's Magikarp",
    searchable_by=["Misty's Magikarp", "Basic", "MistysMagikarp"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Ability(
            title="So Submerged",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon.",
            passive=SoSubmergedPassive(),
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

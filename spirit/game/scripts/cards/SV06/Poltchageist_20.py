from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive


class StorehouseHideawayPassive(Passive):
    """On the Bench: no damage from, and no effects of, opposing attacks
    (Misty's Magikarp's So Submerged)."""

    def prevents_damage(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing and calc.target is carrier
                and not is_in_active_spot(carrier))

    def blocks_attack_effects(self, target, carrier, source=None):
        return target is carrier and not is_in_active_spot(carrier)

card = PokemonCardDef(
    guid="09c48256-e8f6-5050-8cd5-235080badf41",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist", "Basic", "Poltchageist"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1012,
    abilities=[
        Ability(
            title="Storehouse Hideaway",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon.",
            passive=StorehouseHideawayPassive(),
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)

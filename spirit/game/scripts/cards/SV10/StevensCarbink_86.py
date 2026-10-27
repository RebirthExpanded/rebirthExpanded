"""Steven's Carbink (SV10 86 -- JP SVOD 003; English DRI/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred



def _stone_palace_protects(target, carrier) -> bool:
    return (target.owning_player_id == carrier.owning_player_id
            and carrier._containing_area_name() == "bench" and _named("Steven's ")(target))


card = PokemonCardDef(
    guid="6cca9843-7b68-52cb-a9e8-78b7caf5af00",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensCarbink.Name",
    display_name="Steven's Carbink",
    searchable_by=["Steven's Carbink", "Basic"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=703,
    abilities=[
        Ability(
            title="Stone Palace",
            game_text="As long as this Pokémon is on your Bench, all of your Steven's Pokémon take 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Stone Palace doesn't stack.",
            passive=pc.takes_less_passive(30, protects=_stone_palace_protects, stack_key="Stone Palace"),
        ),
        Attack(
            title="Magical Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)

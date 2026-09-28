from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive


def _is_rotom(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return "Rotom" in name


class MultiAdapterPassive(Passive):
    """Your Pokemon with "Rotom" in their name may hold 2 Pokemon Tools."""

    def tool_capacity(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id or not _is_rotom(pokemon):
            return 1
        return 2

card = PokemonCardDef(
    guid="b35c4c63-f23a-5ace-86b2-b3f5098ce30d",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotomex.Name",
    display_name="Rotom ex",
    searchable_by=["Rotom ex", "Basic", "ex", "Rotomex"],
    subtypes=["Basic", "ex"],
    collector_number=29,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Multi Adapter",
            game_text="Each of your Pok\u00e9mon that has \"Rotom\" in its name may have up to 2 Pok\u00e9mon Tool cards attached. If this Ability goes away, discard Pok\u00e9mon Tools from those Pok\u00e9mon until only 1 remains on each.",
            passive=MultiAdapterPassive(),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import recoil_attack


def _is_hops(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Hop's ")


class ExtraHelpingsPassive(Passive):
    """+30 from your Hop's Pokemon's attacks to the opposing Active, before
    W/R; one Extra Helpings at a time however many Snorlax are in play."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return
        if not _is_hops(attacker) or getattr(calc, "_extra_helpings_applied", False):
            return
        calc._extra_helpings_applied = True
        calc.amount += 30

card = PokemonCardDef(
    guid="eb7a40ea-20f2-5266-8ebf-a84ef9a0ae5e",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSnorlax.Name",
    display_name="Hop's Snorlax",
    searchable_by=["Hop's Snorlax", "Basic", "HopsSnorlax"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Extra Helpings",
            game_text="Attacks used by your Hop's Pok\u00e9mon do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack.",
            passive=ExtraHelpingsPassive(),
        ),
        Attack(
            title="Dynamic Press",
            game_text="This Pok\u00e9mon also does 80 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=recoil_attack(80),
        ),
    ],
)

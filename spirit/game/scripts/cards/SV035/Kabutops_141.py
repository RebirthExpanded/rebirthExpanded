"""Kabutops (SV035 141 -- JP SV2a 141; English MEW/141). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc



class AncientWayPassive(Passive):
    """Weakness for the opponent's Active Pokemon is applied as x4."""

    def modify_weakness(self, calc, carrier):
        attacker = calc.attacker
        if (attacker is not None and attacker.owning_player_id == carrier.owning_player_id
                and calc.target.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(calc.target)):
            calc.weakness_multiplier = 4


card = PokemonCardDef(
    guid="e560d1df-20d7-5a08-b869-0ebe6d6d0044",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=141,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Ancient Way",
            game_text="Apply Weakness for your opponent's Active Pokémon as ×4 instead.",
            passive=AncientWayPassive(),
        ),
        Attack(
            title="Draining Blade",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=su.heal_attack(30),
        ),
    ],
)

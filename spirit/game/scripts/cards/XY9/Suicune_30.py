"""Suicune (XY - BREAKpoint 30/122 -- JP XY9 020/080, the art here).

Basic Water Pokemon. HP 120, weakness Lightning x2, retreat 2.

  Wind Protection  (Ability)  As long as this Pokemon is your Active
                              Pokemon, prevent all effects of attacks from
                              your opponent's Pokemon done to your
                              Pokemon. (Existing effects are not removed.)
  Aurora Beam      [WWC] 110

Big Parasol's shield printed as an Ability on the Pokemon itself, so an
Ability lock switches it off where the Tool's would keep working.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class _WindProtectionPassive(Passive):
    """While Suicune is Active, its whole side is shielded from opposing
    attack EFFECTS (damage is not an effect)."""

    def blocks_attack_effects(self, target, carrier, source=None):
        return (is_in_active_spot(carrier)
                and target.owning_player_id == carrier.owning_player_id)


card = PokemonCardDef(
    guid="91e86568-4c9c-577a-a2cb-aecce5a3f251",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Wind Protection",
            game_text="As long as this Pokémon is your Active Pokémon, prevent all effects of attacks from your opponent's Pokémon done to your Pokémon. (Existing effects are not removed.)",
            passive=_WindProtectionPassive(),
        ),
        Attack(
            title="Aurora Beam",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)

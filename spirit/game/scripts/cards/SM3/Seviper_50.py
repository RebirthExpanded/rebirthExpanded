"""Seviper (SM - Burning Shadows 50/147 -- JP SM3N 018/051, the art here).

Basic Psychic Pokemon. HP 100, weakness Psychic x2, retreat 2.

  Ability: More Poison  Put 1 more damage counter on your opponent's
                        Poisoned Pokemon during Pokemon Checkup.
  Venomous Fang [PCC] 30  Your opponent's Active Pokemon is now Poisoned.

The extra counter is part of the Poison tick (modify_poison_counters), so
it stacks with Perilous Jungle, Radiant Hisuian Sneasler, Toxicroak,
Pecharunt and a second Seviper.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import opponent_poison_bonus_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="bc857dd0-f1c3-51b4-8955-540f0c146ebf",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Ability(
            title="More Poison",
            game_text="Put 1 more damage counter on your opponent's Poisoned Pokémon during Pokémon Checkup.",
            passive=opponent_poison_bonus_passive(1),
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)

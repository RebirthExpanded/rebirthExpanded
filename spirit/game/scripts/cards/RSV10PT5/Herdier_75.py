"""Herdier (SV - White Flare 75/086).

Stage 1 Colorless Pokemon. HP 90, weakness Fighting x2, no resistance,
retreat 1.

  Roar      [C]      Switch out your opponent's Active Pokemon to the
                     Bench. (Your opponent chooses the new Active Pokemon.)
  Lunge Out [CCC] 70

Roar is gust_attack with opponent_chooses: the switch is theirs to make,
not yours, which is the whole difference from a Gust. No damage, so the
printed damage it deals is nothing.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="ec6c592e-a6c0-56da-ac04-bd19ea085992",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    display_name="Herdier",
    searchable_by=["Herdier", "Stage 1", "Herdier"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Roar",
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)

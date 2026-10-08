"""Alakazam ex (SV - 151 65/165 -- JP SV2a 065/165, the art here).

Stage 2 Psychic Pokemon ex, evolves from Kadabra. HP 310, weakness
Darkness x2, resistance Fighting -30, retreat 1.

  Mind Jack         [CC] 90+  30 more damage for each of your opponent's
                              Benched Pokemon.
  Dimensional Hand  [PP] 120  This attack can be used even if this Pokemon
                              is on the Bench.

Dimensional Hand is offered for a Benched Alakazam ex too
(Attack(usable_from_bench) -> legal_actions._bench_attack_entries); the
damage goes to the opponent's Active as usual and the turn ends.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="b8014c78-0878-57c0-85b0-5c038729bb24",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazamex.Name",
    display_name="Alakazam ex",
    searchable_by=["Alakazam ex", "Stage 2", "ex", "Alakazamex"],
    subtypes=["Stage 2", "ex"],
    collector_number=65,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 30, base=90),
        ),
        Attack(
            title="Dimensional Hand",
            game_text="This attack can be used even if this Pokémon is on the Bench.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            usable_from_bench=True,
        ),
    ],
)

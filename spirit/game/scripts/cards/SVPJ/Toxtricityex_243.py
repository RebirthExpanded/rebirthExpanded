"""Toxtricity ex (SVPJ 243 -- JP SVP 243; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="337d8295-4136-5d91-b79a-a23b3f9e38a2",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name",
    display_name="Toxtricity ex",
    searchable_by=["Toxtricity ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=243,
    set_code="SVPJ",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Strum Thunder",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=ac.self_energy_discard_attack(count=2),
        ),
    ],
)

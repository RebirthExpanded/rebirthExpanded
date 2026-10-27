"""Tohoku's Pikachu (SVPJ 260 -- JP SVP 260; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="53698b16-a1e0-51d4-95fb-48556fb5efac",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TohokusPikachu.Name",
    display_name="Tohoku's Pikachu",
    searchable_by=["Tohoku's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=260,
    set_code="SVPJ",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Renewal Open!",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Dancing Around",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)

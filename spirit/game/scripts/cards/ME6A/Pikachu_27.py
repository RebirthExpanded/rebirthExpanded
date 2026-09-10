"""Pikachu (JP M6a 027/103 -- 30th Celebrations 11/30).

Basic Lightning. HP 60, weakness Fighting x2, retreat 1, regulation
mark J.

  Ability  Hide  As long as this Pokemon is on the Bench, it takes no
                 damage or effects from your opponent's Pokemon's attacks.

  Petit Electric  [L] 10

Hide is a bench-only shield and it covers both halves at once -- the
damage (a snipe or a spread that reaches the Bench does nothing to it) and
the effects (an attack that would move it, discard from it or condition it
does nothing either). Both hooks read the same question: is the carrier
sitting on the Bench right now.

The clause is only about ATTACKS, so an Ability or a Trainer still reaches
this Pikachu on the Bench -- Boss's Orders drags it up, and once it is
Active the shield is off.

It is an Ability, so an ability lock switches it off like any other.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


def _on_bench(pokemon) -> bool:
    return pokemon is not None and pokemon._containing_area_name() == "bench"


class HidePassive(Passive):
    """On the Bench: no damage and no effects from the opponent's attacks."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        return bool(calc.is_attack and calc.is_opposing
                    and calc.target is holder and _on_bench(holder))

    def blocks_attack_effects(self, target, carrier, source=None):
        holder = carrier_pokemon(carrier)
        return target is holder and _on_bench(holder)


card = PokemonCardDef(
    guid="3ecbb83a-0501-5eaf-ad64-a5ba172e8429",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Ability(
            title="Hide",
            game_text="As long as this Pokémon is on the Bench, it takes no damage or effects from your opponent's Pokémon's attacks.",
            passive=HidePassive(),
        ),
        Attack(
            title="Petit Electric",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)

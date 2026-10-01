from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class PoisonSacsPassive(Passive):
    """While this Muk is in play, the opponent's Poisoned Pokemon stay
    Poisoned when they evolve or devolve. With Galarian Weezing's
    Neutralizing Gas arriving by that very evolution, the evolving
    Pokemon's owner picks which comes first (the engine asks)."""

    def keeps_poison_through_evolution(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        return holder is not None and pokemon.owning_player_id != holder.owning_player_id

card = PokemonCardDef(
    guid="ea70824d-ae1d-5cd6-9382-c85c4d0a09c7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Poison Sacs",
            game_text="The Special Condition Poisoned is not removed when your opponent's Pok\u00e9mon evolve or devolve.",
            passive=PoisonSacsPassive(),
        ),
        Attack(
            title="Toxic Secretion",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)

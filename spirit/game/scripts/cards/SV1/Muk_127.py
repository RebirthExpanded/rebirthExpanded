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
    guid="6e13c870-21a4-5340-a28f-c0898519f2ad",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Poison Sacs",
            game_text="Your opponent's Poisoned Pok\u00e9mon don't recover from that Special Condition when they evolve or devolve.",
            passive=PoisonSacsPassive(),
        ),
        Attack(
            title="Toxic Strike",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)

"""Gengar (ME3 50 -- JP M3 049; English POR/50). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon


class InfiniteShadowPassive(Passive):
    """Knocked Out by damage from an opponent's attack: to the hand (the
    attached cards are discarded). An Ability, so a lock stops it."""

    def knockout_destination(self, pokemon, carrier):
        if pokemon is carrier and getattr(pokemon, "ko_by_opposing_attack_damage", False):
            return "hand"
        return None


card = PokemonCardDef(
    guid="64337008-c049-5bd4-9974-093fbe7d68e2",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Infinite Shadow",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, put it into your hand instead of the discard pile. (Discard all attached cards.)",
            passive=InfiniteShadowPassive(),
        ),
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(ac.count_bench("opponent"), 30, base=10),
        ),
    ],
)

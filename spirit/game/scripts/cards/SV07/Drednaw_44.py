"""Drednaw (SV07 44 -- JP SV7 026; English SCR/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac



class ImperviousShellPassive(Passive):
    """Prevents opposing attack damage of 200 or more (an Ability)."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if calc.is_attack and calc.is_opposing and target is carrier_pokemon(carrier) and calc.amount >= 200:
            return 0
        return None


card = PokemonCardDef(
    guid="1e347b8d-9e85-51e3-a1c6-7893f397bded",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name",
    display_name="Drednaw",
    searchable_by=["Drednaw", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    family_id=833,
    abilities=[
        Ability(
            title="Impervious Shell",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon if that damage is 200 or more.",
            passive=ImperviousShellPassive(),
        ),
        Attack(
            title="Hard Crunch",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 80),
        ),
    ],
)

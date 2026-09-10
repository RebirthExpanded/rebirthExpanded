"""Clefairy (XY - Evolutions 63/108 -- JP CP6 061/087).

Basic Fairy. HP 40, weakness Metal x2, resistance Darkness -20, retreat 1.

  Sing       [C]    Flip a coin. If heads, your opponent's Active Pokemon
                    is now Asleep.
  Metronome  [CCC]  Choose 1 of your opponent's Active Pokemon's attacks
                    and use it as this attack.

The narrowest of the copy attacks: their ACTIVE only, where Zoroark-GX's
Trickster-GX reaches their whole board and Liepard's Assist reaches your
own Bench. All three share the copy path, so the chosen attack keeps its
own effects and the re-entry guard stops a Metronome copying a Metronome
into a loop.

The Energy cost paid is Clefairy's own; the copied attack's cost is not
required, which is what "use it as this attack" means.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef, def_for


async def metronome(ctx):
    """Use one of their Active's attacks as this attack."""
    defender = ctx.opponent_active()
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = [(defender, ability)
                  for ability in (getattr(definition, "abilities", None) or [])
                  if isinstance(ability, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="1d9b478d-c4ce-5124-b966-27c027bf4a4f",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title="Sing",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Metronome",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=metronome,
        ),
    ],
)

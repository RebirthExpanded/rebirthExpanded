"""Empoleon (SM - Cosmic Eclipse 56/236 -- JP SM11b 011/049).

Stage 2 Water Pokemon, evolves from Prinplup. HP 160, weakness Lightning
x2, retreat 2.

  Recall    [C]       Choose an attack from 1 of this Pokemon's previous
                      Evolutions and use it as this attack.
  Aquafall  [CC] 130  Discard all Energy from this Pokemon.

Recall is Incineroar (SWSH12)'s Secret Attack: the cards under this Pokemon
that belong to its evolution line supply the attacks.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import def_for, evolves_from_chain
from spirit.game.session.effects import full_stack, is_pokemon_card
from spirit.game.data_utils import Attack, PokemonCardDef


def _logic_name(definition):
    spec = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    return spec.get("value") if isinstance(spec, dict) else None


async def recall(ctx):
    names = set(evolves_from_chain(ctx.attacker.archetype_id))
    candidates = []
    for card in full_stack(ctx.attacker)[1:]:
        if not names or not is_pokemon_card(card):
            continue
        definition = def_for(card.archetype_id)
        if definition is None or _logic_name(definition) not in names:
            continue
        for ability in getattr(definition, "abilities", []):
            if isinstance(ability, Attack):
                candidates.append((card, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="c499e75d-af1d-52b5-bdee-529210e63cb9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=['Empoleon', 'Stage 2', 'Empoleon'],
    subtypes=['Stage 2'],
    collector_number=56,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(title="Recall", game_text="Choose an attack from 1 of this Pokémon's previous Evolutions and use it as this attack.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=recall),
        Attack(title="Aquafall", game_text="Discard all Energy from this Pokémon.",
               cost={PokemonTypes.COLORLESS: 2}, damage=130,
               effect=self_energy_discard_attack(all_energy=True)),
    ],
)

"""M Charizard-EX (XY - Flashfire 69/106 -- JP XY2 015/080).

Mega Evolution Pokemon-EX, Dragon, evolves from Charizard-EX. HP 230,
weakness Fairy x2, retreat 3.

  Wild Blaze  [RRDCC] 300  Discard the top 5 cards of your deck.

  Mega Evolution rule: When 1 of your Pokemon becomes a Mega Evolution
  Pokemon, your turn ends.
  Pokemon-EX rule: When a Pokemon-EX has been Knocked Out, your opponent
  takes 2 Prize cards.

The pool's first XY-era Mega Evolution. The client's stage list has no
Mega stage, so it is a Stage 1 that evolves from Charizard-EX by name,
carrying the "MEGA" subtype that data_utils already counted as a rule box
worth 2 Prizes. The Mega Evolution rule is the new part: perform_evolution
asks mega_evolution_ends_turn once the Mega is on top, and the action that
brought it there -- a play from the hand, or an effect like Wally -- ends
the turn after it resolves. A Spirit Link Tool would waive that through
mega_evolution_keeps_turn; none is in the pool yet.

Being a Dragon Pokemon-EX, its attack is reachable from the discard pile
by Regidrago VSTAR's Apex Dragon and by Mewtwo & Mew-GX's Perfection.

Charizard-EX itself is not in the pool yet; when it is, its archetype name
must be "...pokemon.CharizardEX.Name" (the convention Jirachi-EX and
Shaymin-EX follow) for this card's evolves_from to find it.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="0602814c-d015-5f6c-b996-8f10b3e9c86c",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "Mega", "EX", "MCharizardEX",
                   "Charizard"],
    subtypes=["Stage 1", "MEGA", "EX"],
    collector_number=69,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Wild Blaze",
            game_text="Discard the top 5 cards of your deck.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.DARKNESS: 1,
                  PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=mill_attack(5, opponent=False),
        ),
    ],
)

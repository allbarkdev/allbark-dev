---
title: "Week four: a monster is just a hero the DM runs"
description: "The DM got the same combat wheel the players have, monster hits now land conditions on heroes' phones, Hold Person and Bless finally do what they say, and heroes picked up companions. Here's how Cerberus learned to run the other side of the fight."
week: 2026-W43
app: Cerberus
image: /assets/devlog/2026-w43/og.png
image_alt: "The Bark Blog, week 43: Week four, a monster is just a hero the DM runs, beside a screenshot of the DM's combat wheel for a Goblin Boss reading Attack 1 of 2"
og_shot: /assets/devlog/2026-w43/dm-wheel-multiattack.png
---

Week three, Cerberus learned to celebrate. Week four, the DM finally got to play too. Monsters take
real turns on the same combat wheel the heroes use, their hits put conditions on the heroes'
phones, and spells like Hold Person and Bless actually do what they say at the table. Heroes also
picked up companions: familiars, steeds, summoned spirits, figurines, each with a card of its own.

That was 52 merged pull requests, split between Opus and Fable again. Most of the week's fixes
came from playing whole fights end to end, over and over, so this post goes deep on the DM's
wheel, on making effects land, and on how the testing worked. The rest gets the usual one breath at
the end.

## A monster is just a hero the DM runs

The first DM screen was its own thing. Monster cards with an attack panel, aiming chips stuffed
inside the card, and a bottom bar for Next turn and End combat. It worked, kind of. But the players
already had a combat wheel that was pretty good at running a turn, and the DM was off doing
something completely different.

So I wanted the monsters on the same wheel and sheet the players use. It's easier, it's more
condensed, and picking a target felt like it belonged in a pop-up, not crammed into the attack
card. Fable mocked up three layouts and three target pickers side by side. I went with the "arena"
layout and a grid of faces for aiming, because the grid fits a lot more targets in the same space.

Then I pushed it further. I didn't want a copy of the player's screen with monster stuff bolted on.
I wanted the *same component*. Mechanically there's honestly not a lot of difference between a
player's hero and a monster the DM controls. The DM is basically running a bunch of heroes at once,
and should get to their saves, reactions and resources just as easily.

So Fable turned the player's in-fight sheet into a "fighter frame" that anything can stand in. An
adapter fills it in, and each role adds its own tools around the edges. Monsters went in first.

{% include shot.html src="/assets/devlog/2026-w43/dm-wheel-multiattack.png" alt="The DM's phone in round 1: a rail of three goblin tokens with their Initiatives (22, 21, 7) and an Add tile, then the Goblin Boss, AC 17 and 21 of 21 HP, with its combat wheel reading Attack 1 of 2, Bonus Action and Reaction around an End Turn hub" caption="The Goblin Boss, on the same wheel a hero gets. This is from the day it shipped. The **Add a creature** row under the wheel got cut later in the week." %}

Here's how a stat block maps onto the wheel. The turn order runs across the top as a rail of
tokens, each one a face in a ring of health with its Initiative on the shoulder. Attacks go under
Attack, and Multiattack counts down ("Attack 1 of 2"). Bonus Actions, Reactions, Legendary Actions
and Recharge sit where a hero's resources would. Tap an attack and a grid of faces comes up to pick
who's getting hit.

{% include shot.html src="/assets/devlog/2026-w43/dm-aim-grid.png" alt="The DM's wheel dimmed behind a Scimitar sheet reading '+4 to hit · at whom?' with two goblin faces to pick, AC 15 each, and a Just roll button" caption="Goblins fighting goblins. Part of the testing was letting monsters go after each other." %}

### It has to actually spend the turn

The first version looked right and played wrong. My monsters could keep attacking forever, and
there was no roll card popping up, just dice sounds coming from somewhere. So Fable made the wheel
spend a monster's turn exactly the way it spends a hero's, and every DM roll now goes up on the same
roll card the players see. The players' sheets show the same rail, too.

The roll card got one more DM-flavored change. A monster's attack used to show the damage roll
right next to the hit, which kind of ruins the moment. Now a monster's attack rolls its d20 alone,
and the damage stays hidden until the DM taps Roll damage. Multiattack was the other drag, since
you had to go back through the wheel for every swing. Now it chains the way a hero's Extra Attack
already did, with a Next attack button right on the roll card. Fable built both.

## Effects that land

Plenty of spells and monster abilities used to just be text. Hold Person said the target was
Paralyzed, and then... nothing changed. This week Opus made them actually change the creature
they hit:

- **Hold Person, Bane, Command and Blindness** roll the target's save on the DM's screen and put
  the condition on.
- **A Ghoul's Claw paralyzes the hero** on their own phone.
- **Conditions end on their own clock**, no one has to remember to take them off.
- **Hitting a Paralyzed creature** rolls with Advantage, and crits up close.
- **Bless adds its d4** to attacks and saves, and a Life cleric's slot heals add Disciple of Life.
- **Charmed creatures can't attack their charmer.**

### Read the stat block, not a new data field

Then there were the monsters whose best moves did nothing. The aboleth's Lash could be used over
and over and never hit anyone. When we counted, 32 of the SRD's 79 Legendary Actions did nothing,
because their text just points at another attack ("makes one Tentacle attack") or at a spell
("uses Spellcasting to cast Fear"). 25 of them cast a spell.

There was a lazy version of the fix on the table, and I wasn't into it. The other easy way out was
adding new fields to every monster in the data. Instead, Opus taught the engine to read the stat
block's own text at runtime and follow the pointer. The nice side effect is that a homebrew stat
block written the SRD way just works too.

## Play the fight, don't patch it

Once the wheel landed, the plan was simple: play whole fights from the DM's side. Open a table, add
monsters, seat two heroes, fight, and have the monsters go after each other too.

I set one rule for it. No working around a broken skill with the table's manual tools, so no typing
in damage, healing or conditions by hand. That ruled out the easy pass. If Hold Person only "works"
because the DM adds Paralyzed manually, that's broken, and it got logged as broken.

Fable wrote it up as a reusable test plan with its own harness and logged the first run. We ran it
three times over Oct 22 and 23, fixing each run's findings before the next one. Then came a full
sweep of every way the app gets used on Oct 24: 2 blockers, 9 places the rules came out wrong, 17
rough spots and 20 bits of polish. A Companions-only pass after that found 1 more blocker and 3
more rules problems. Everything got fixed the same day, except one finding that turned out not to
be a bug.

Some favorites from the pile:

- **A monster that went down for nobody.** A hero's killing blow dropped the creature on the hero's
  phone, and then the DM's device overwrote it with its old copy of the table. So the creature stood
  right back up for everyone and kept its turn. Pretty rude. It was an ordering problem: the DM
  screen now applies the incoming table first, then runs its own updates. Fable fixed it.
- **Two blockers that were one-liners in disguise.** Coins in a loot parcel reused a number an item
  already had and crashed the dialog. And the import prompt's Replace and Keep buttons silently did
  nothing, because they handed the database a live reactive object instead of plain data.
- **The one that wasn't a bug.** The sweep flagged "Stunned keeps movement." Under SRD 5.2, Stunned
  doesn't stop movement the way the older rule did, so the code was right and the test plan got the
  fix instead.

## Heroes get companions

Once anything could stand in the fighter frame, companions were the obvious next thing. Find
Familiar, Find Steed, Summon Dragon, Giant Insect, Animate Dead, Pact of the Chain, the Figurines of
Wondrous Power, Bag of Tricks and more now put a creature on the hero's sheet. Fable built it.

Each companion is a token under the hero's chips. Tap it and you get its card, in the same frame the
DM runs monsters in: HP, AC, a combat wheel of its attacks, checks and features.

{% include shot.html src="/assets/devlog/2026-w43/companion-row.png" alt="A level 5 Human Fighter's sheet with a 'Boar is here. Open Boar' notice at the top and two companion tokens, Mastiff and Boar, under the Condition and Cast on me chips" caption="A Fighter with a Mastiff and a Boar. Good dogs only. And one boar." %}

{% include shot.html src="/assets/devlog/2026-w43/owl-familiar-card.png" alt="An Owl familiar's card: Tiny Fey, CR 0, 1 of 1 HP, AC 11, 5 ft Speed, with its combat wheel (Action, Reaction: Nothing, Bonus Action: Nothing), a Darkvision 120 ft chip, and Name, Send away and Dismiss buttons" caption="An Owl familiar, 1 HP of pure courage. Spot the bug: it says Round 1 out of combat. Fixed the same day." %}

Companions take their turn right after their hero, and leave when their timer or the spell's
Concentration runs out. At a DM's table, Opus gave them their own seat, so monsters can go after
them too. The Companions test pass caught a nasty one: a companion dropping to 0 HP crashed the
sheet, because its card was still open while the creature left the list. Now the card closes first,
and you get the "drops to 0 and vanishes" notice with an Undo. Backing out of a summon picker also
refunds the slot, charges and Concentration it had just spent.

## The table's front door

Setting up a table got some love too. The DM picks which homebrew packs a session allows, and a
hero who needs another pack waits at the door with a Let in button or an X. Opus built that one.

{% include shot.html src="/assets/devlog/2026-w43/pack-door.png" alt="The DM's table screen with a glowing card at the top: Brynn Ironjaw, tagged 'Hound Master (homebrew example)', with a gold Let in button and an X, above 'Waiting for players', a Packs row and an empty loot pile" caption="Brynn brought a homebrew pack. The DM decides if it comes in." %}

It also got sound and motion. Creatures pop into their seats, a hero sitting down gets a chime and
a gold glow, and Start combat plays a horn. Players don't see the DM's monsters until the fight
starts, because spoilers. And after playing it on my own phone, Start combat goes straight into the
first turn now instead of making you tap again.

## Also in the pile

The rest of the week, in one breath: in Wild Shape the combat wheel is the Beast's, with spells only
once you have Beast Spells and the next attack following the form's Multiattack, spell slots as one tile per level with free casts as chips, a
[homebrew pack checker and format guide](/homebrew/) that points at the line and column of a
broken pack file, joining a table by a six-digit code or QR when the Wi-Fi hides it (built, and
still being tested between real phones), the local table recovering quietly when the app comes
back, a slimmer monster header on the DM screen, Guidance, Divine Smite and Evasion fixes from the
full sweep, and moving everything that shipped out of the roadmap and into the diary.

That's week four. See you next week.

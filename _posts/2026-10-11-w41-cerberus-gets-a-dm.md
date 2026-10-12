---
title: "Week two: the week Cerberus got a DM"
description: "A DM screen that runs the fight, damage that lands where it's aimed, buffs that show up on the right sheet, actual battle music, and a playtest that found 101 things. Here's how the table came together."
week: 2026-W41
app: Cerberus
image: /assets/devlog/2026-w41/og.png
image_alt: "The Bark Blog, week 41: Week two, the week Cerberus got a DM, beside a screenshot of a hero's sheet with Haste active"
og_shot: /assets/devlog/2026-w41/haste-on-bo.png
---

Week one was all about one hero and one turn. Week two, Cerberus learned to sit at a table. A DM
can run the whole fight from their own device, damage goes where you aim it, and when someone casts
Haste on you, it actually shows up on your sheet. Then we played the entire app start to finish for
the first time, and honestly, it had notes. 101 of them.

That was 91 merged pull requests, which is way too much for one post. So this one sticks to the
table, the soundtrack and the playtest, and everything else gets crammed into one breath at the end.

## The DM's device is the table

The idea started pretty simple: a DM hosts a session, players join it, the DM tracks initiative,
and everyone gets dropped into their turn automatically.

We still liked solo mode, where you track your own turns, so we didn't want to throw it out. The
trick was that a table only presses buttons a player already had. The DM's device starts each hero's
turn on that player's sheet and ends combat for everybody. Players still roll their own Initiative
and end their own turns, because that's what you'd do at a real table anyway.

Leave the table and you're just back on your normal sheet. Nothing to undo.

The DM gets a screen of their own, and it's stacked: all 329 monster stat blocks from the SRD 5.2,
monster cards that track HP, conditions, Recharge and Legendary Actions, and prepared fights rated
with the SRD's encounter difficulty for your party. On a tablet it splits in two, initiative on the
left and whoever's up on the right.

{% include shot.html src="/assets/devlog/2026-w41/dm-screen-tablet.png" alt="The DM screen on a tablet. On the left, the initiative order for round 1 with Goblin Warrior 2 (21), Goblin Boss (13) and Goblin Warrior (4), and a prepared fight called Goblin ambush, 3 monsters, Moderate for 4 at level 1. On the right, Goblin Warrior 2's card: AC 15, 10 of 10 HP, Scimitar and Shortbow attacks with Roll buttons, Nimble Escape and saving throws." caption="Initiative on the left, whoever's up on the right. Three goblins, rated Moderate for a level 1 party of four." wide=true %}

One rule decides where every number lives: **the DM's device owns the monsters, and each phone owns
its own hero.** Monster HP lives on the DM's screen. Your HP lives on your phone, and your phone
applies your Resistances. Players only ever see a monster's name and whether it's **Bloodied**,
which is the SRD 5.2 word for half HP or less. We went looking for more terms like that and nope,
Bloodied is the only one.

Then we flipped it around: the DM should get the same kind of view of the heroes. So your actual
HP number never leaves your phone either. The DM sees Healthy, Bloodied, Dying, Stable or Dead, plus your AC and conditions. Enough to run the fight, and nobody's sheet is an open
book.

## Don't just show the fight, track it

The first DM screen showed you the monsters. Cool, but you were still doing all the math yourself.
The better idea: damage rolls should just take the health off. Whoever's attacking or casting, DM or
player, picks who they're aiming at, and the HP popup only sticks around for the odd manual fix.

So that's what we built. Roll damage, pick who you're hitting, and the number lands on the right
device after Immunities and Resistances. The old "type in your HP change" popup is only around now
for Hit Dice and manual fixes.

{% include shot.html src="/assets/devlog/2026-w41/player-deal.png" alt="A player's phone in combat after an Unarmed Strike damage roll of 3 bludgeoning, with a button reading Deal 3 to Goblin Boss, comes off its HP on the DM's screen." caption="Three whole damage. The Goblin Boss is shaking." %}

Saves work the same way. An area spell or a breath weapon asks who got caught in it and rolls damage
once. A Fireball rolls its 8d6 a single time, then every creature saves on its own screen with its
own bonus, and anyone who makes it takes half.

{% include shot.html src="/assets/devlog/2026-w41/fire-breath.png" alt="A Young Red Dragon's card on the DM's phone after Fire Breath: DC 17 Dex save, 75 fire. Ana rolls a DC 17 Dexterity save on their phone, and a Goblin Warrior rolls 9, fails, takes 75 and drops." caption="One roll of 16d6 for everybody. Ana gets to roll a save on their own phone. The goblin does not have a great day." %}

The same planning thread also asked for a real dice switch. Turn it on and the app asks for your
physical roll and you just type in the number.

## Buffs follow the target

This one started small. We had Concentration going on Fly and the chip said "10 min" turn after turn
after turn. It looked frozen. It wasn't. The timer was running fine, the chip was just rounding. So
now timed effects count rounds in combat (100, 99, 98, all the way down to "Last round") and show a
clock outside of it. They tick on your turn and end themselves.

{% include shot.html src="/assets/devlog/2026-w41/poisoned-timer.png" alt="A level 5 Monk's sheet with a Poisoned card: Disadvantage on attack rolls and ability checks, 0:58 left, lasts a set time then ends on its own, from a giant spider bite, with a Remove Poisoned button." caption="Effects know how long they last, and who to blame." %}

Fixing that showed the next gap. Spells without Concentration, like Mage Armor, weren't tracked at
all, and Mage Armor should only count while you're not wearing armor. Then the table made a third
thing pretty obvious: you're already picking a target, so the buff should just land on that hero's
sheet.

And now it does. Ana casts Haste on Bo, a level 5 Fighter, and Bo's phone says so. AC goes from 16
to 18, Speed goes from 30 to 60 feet, and both go right back the second Ana's Concentration drops.

{% include shot.html src="/assets/devlog/2026-w41/haste-on-bo.png" alt="Bo's sheet with a banner reading Ana cast Haste on you. AC shows 18 and Speed 60 ft, and a Haste card counts down from 0:57, lasting while Ana concentrates on it, with an End Haste button. Below it, Mage Armor is marked Not in effect." caption="Ana's Haste lands on Bo's sheet, timer and all." %}

The same timers also brought Rage upkeep, Dash adding to your movement, and condition saves that
roll themselves.

## Making it sound like a fight

Sounds were working. They just weren't doing much for anybody. Honestly? A little meh. Nobody was
getting hyped over a dice clack.

The first free pack was very utility-grade. So we built an audition page and went through it
on a phone with headphones, tagging every clip for a moment: a roll, a nat 20, a nat 1, a hit, a
spell, coins. Candidates came from CC0 game audio and the free, royalty-free GDC game audio bundles.
That's 230 GB across ten years of bundles, which sounds like a lot, and it turned out to be wide but
not deep. The whole decade had only a handful of real dice recordings, so every single one made the
cut.

97 clips survived, plus 60 spell sounds. For now each moment plays a random pick from its set, and
sounds for specific spells are on the list for later.

Music had a pretty clear brief: rolling Initiative should feel like you've just walked into the
fight, the way battle music fires up in a game.

After auditioning, we skipped intros and victory fanfares for now and just jump straight into a
combat loop. Exploring music cuts into battle when you roll Initiative and fades back out when
combat ends.

Music has its own switch, separate from Sounds, and it starts **off**. Picture five phones at a real
table all blasting battle music over the DM's own playlist. Yeah, no.

The music did break one thing, just not the app. Bundling about 21 MB of it pushed the Android test
build to 31 MB, which is over a 10 MB attachment limit on the step that shares test builds. Every
check passed. Only that last step fell over. The fix posts a download link instead. We kept the
music bundled anyway so it works offline from the very first launch, because offline-first is one of
our core rules.

## The first full playtest

After two weeks of moving fast, nobody had played the whole app end to end in one sitting. So we
did. We wrote up 36 scenarios covering the builder, level-up, the sheet, solo combat, table play,
accessibility and sound, and ran every one from a wiped device.

It found 101 things. Zero blockers, thankfully: 10 major, 49 minor and 42 polish. We agreed with 93,
tweaked 8, tossed none, and the fixes landed the next day in six focused batches.

The big ones:

- **Rules the sheet didn't enforce yet.** Dropping to 0 HP did nothing, and some class actions,
  like Reckless Attack, Flurry of Blows and some Channel Divinity options, just weren't there.
- **The builder picked a class's key abilities from its saving throws** instead of its primary
  ability.
- **The combat wheel sorted its rings alphabetically**, so a caster's real spells got buried.
- **Table play worked end to end. Rejoining after a page reload didn't.**

Two of the tweaks changed direction. You now pick your target *before* you roll, so a crit card
never needs a button for every monster, and that one already shipped. The sheet's top bar and
resource dock are up for a rethink.

One more bug got caught before it merged. Replaying a table session in two browser windows showed a
player's sheet sometimes starting their turn again right after they ended it. Fixed, and each
sheet's round now stays in step with the table's.

Which brings us to the honest part. Table play was built and tested between browser windows. The
native Wi-Fi plugin compiles for iOS and Android, but we haven't played a table across real phones
yet. That's next.

## Also in the pile

The rest of the week, in one breath: a free dice roller with keep and drop notation, every SRD magic
item in the inventory and store with attunement and charges, mounts, vehicles, food, lodging and
services in the store, a smoother spin and snap on the combat wheel, two rounds of sheet and combat
layout rework, Quickened spells lighting up both resources they spend, and a move to SvelteKit 3.

That's week two. See you next week.

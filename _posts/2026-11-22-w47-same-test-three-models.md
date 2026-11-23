---
title: "Week eight: same test, three models"
description: "We ran the same player test on Fable, Opus and Sonnet to see who should do our testing. Then five more test passes chased the last majors while spells that linger, like Stinking Cloud and Earthquake, came to Cerberus. Plus the app got its face: a dog."
week: 2026-W47
app: Cerberus
image: /assets/devlog/2026-w47/og.png
image_alt: "The Bark Blog, week 47: Week eight, same test, three models, beside a phone in round 1 with a Stinking Cloud notice above the combat wheel"
og_shot: /assets/devlog/2026-w47/stinking-cloud.png
---

Week seven was about counting the features that did nothing. Week eight was the grind that comes
after: five more full test passes, 14 through 18, each one fixed before the next started. The bar
is zero majors. We got close on most tracks and kept missing by exactly one on another.

But before any of that, I wanted to settle a question that had been bugging me. Who should
actually be running these tests?

## Same test, three models

Pass 14 was the first one I ran on Fable 5.2. When it was done, I wanted to know how it stacked
up against Opus and Sonnet. So we ran the player test again on Opus 5.5 and Sonnet 5.5, from the
same brief and the same commit.

Here's how it shook out:

- **Fable** found the most real issues, 4 minor and 7 polish, and nine of them were ones the other
  two missed. It also covered the most ground.
- **Opus** was the fastest, at about 39 minutes. It caught three real issues Fable missed, covered
  less, and filed one false positive.
- **Sonnet** stopped after 17 minutes of a 90 minute budget, with no findings.

So Fable runs the test passes now, and Opus is the fallback and the second pair of eyes. I did put
pass 15 on Opus anyway, and Fable ran the rest.

Honestly, take it with a grain of salt. It's one run per model on one track. A strong hint, not a
benchmark. And one thing almost skewed it: Fable's run paused partway through, and that got logged
as a crash. It wasn't. It was a usage limit, and the run picked right back up after a nudge. That
went down as a capacity cost, not a model failure, which seemed like the fair call.

## Spells that stick around

The big new ground this week was spells that don't just go off and end. They sit on the field and
keep doing things, round after round.

Stinking Cloud is the poster child. Every creature inside it gets asked for a Constitution save as
its turn starts, every turn, and a hero who's caught in it loses their action. Web, Sleet Storm,
Earthquake and Power Word Stun now work the same way at a table.

{% include shot.html src="/assets/devlog/2026-w47/stinking-cloud.png" alt="A Wizard's phone in round 1 with the combat wheel showing End turn, a 'Stinking Cloud, 10 rounds' chip under it, and a notice reading 'Stinking Cloud: Ogre 2 is in the Stinking Cloud: a Constitution save as its turns start. Hexer is in the Stinking Cloud... Mo is in the Stinking Cloud...'" caption="The ogre's in the cloud. So is Mo. Mo is on our side." %}

The DM sees it from the other end. The saves roll in on the table, one notice at a time.

{% include shot.html src="/assets/devlog/2026-w47/earthquake-table.png" alt="The DM's table in round 1 with the order down the left (Adult Black Dragon, Zone, Zara, a Draconic Spirit, Hexer, Quake, Thora, Mo, Ogre 2), three heroes marked Concentrating, and a notice at the top: 'Quake's Earthquake: Adult Black Dragon's Dexterity save: 20 against DC 17, saved.'" caption="A Cleric named Quake cast Earthquake. The dragon rolled a 20. Some days." wide=true %}

Faerie Fire got the same care: each creature caught makes a Dexterity save, and attacks against
the ones outlined get Advantage until Concentration ends. A mummy's Rotting Fist curse now plays on
heroes and companions too, all the way to turning its victim to dust, and Remove Curse can lift it
off a friend's companion.

## Zero majors, minus one

Every pass is judged on one thing per track: are there any majors left? The player, classes and
homebrew tracks mostly cleared that bar this week. Homebrew had none all week.

The fight track is where the new spells landed, and it found exactly one major on every pass from
15 to 18. Each fix opened new ground, and the next pass found the gap in it. Pass 17's major was
inside the brand new lingering spell code. Pass 18's was in Concentration. Each round got fixed
before the next one started, and the leftovers rolled into the next round's fixes.

Is that slower than I hoped? Yep. But it's the same thing as last week. The passes are measuring
what's actually playable, and I'd rather they keep doing that than tell me what I want to hear.

It also got me asking what the passes cover in the first place. I wanted to be sure they'd done
at least some high level play and some multiclassing, so we started an audit of what the passes
have and haven't touched.

## The app got its face

Cerberus had been running on the placeholder icon and splash. Not anymore. Opus swapped them for a
dog emblem: a gold dog's head in a gold ring, on the app's dark background.

{% include shot.html src="/assets/devlog/2026-w47/dog-emblem-icon.png" alt="The Cerberus app icon at several sizes and shapes: a gold outlined dog's head with floppy ears inside a gold ring, on a near-black rounded square, a circle, and the splash screen's portrait and landscape frames" caption="One head, not three. We're saving the other two." wide=true %}

When I asked where the puppy came from, the answer was Lucide's dog icon. That's the same
open-source icon set the app already uses for its interface, so it gets credited on the About
screen like the rest. No AI art in Cerberus, the icon included.

Around the same time, the app stopped calling itself a 5E app. The way I see it, Cerberus is a
TTRPG companion that only plays one game right now. It isn't built around that one game. So
"Fifth Edition" shows up on its own lobby tile and its own screen, and everywhere else (the About
screen, the homebrew site, the README) Cerberus is a TTRPG companion. TTRPG is well known and
shorter anyway. It follows from the lobby we built back in week five: the app's shape already
pointed past one game, and now the words do too.

## Also in the pile

- **Companions aim for themselves.** If a player controls a companion, I wanted it to get its own
  target tap, since a player might want it going after a different enemy than their hero. Now it
  does, and its hit waits for Deal just like a hero's.
- **Rest swaps moved onto the sheet.** Weapon Mastery, a Druid's land, Wild Shape forms, Hunter's
  Prey and a Wizard's cantrip all swap from there now. Level-up gives Bard, Sorcerer and Warlock
  one spell swap a level.
- **The hit point pick comes first.** On the level-up Ready screen it's now at the top, and it
  glows until you take it.

{% include shot.html src="/assets/devlog/2026-w47/level-up-hp-pick.png" alt="A Fighter's level-up Ready screen, 'Vex, Level 1 to 2', with '+8 fixed' picked over 'Roll d10' for hit points, an optional Fighting Style swap, Action Surge 0 to 1, and a gold Reach level 2 button" caption="Vex took the fixed 8. Vex is a sensible Fighter." %}

- **Dead means dead.** A dead hero uses, casts and attacks nothing until someone revives them, and
  Exhaustion 6 kills.
- **Easier to get people to the table.** Until a hero sits, the DM's Table tab shows the join code
  and QR right on the empty table instead of behind a small icon. Once someone sits, it folds back
  to the chip next to the table's name.
- **Grip buttons match.** The one-hand and two-hand damage buttons look the same now, and the
  two-hand one hides when both grips roll the same die. No point in a button that does the same
  thing.
- A Multiattack's free uses come once on the DM's monsters, Prone lasts until the hero stands, and
  an imported homebrew pack is never the device's own to edit or share.

## What didn't go great

A bug came back. I got stuck on the store page again and couldn't swipe back, and I was pretty
sure we'd fixed that already. We had. It just never got a test. This time it did, and the fix
covers the inventory and every popup, not only the store. Then there was a flicker during the
back swipe, and that one took two tries. Opus got it on the second: popups no longer slide out
twice.

We also ran out of hosted build minutes for the month on Nov 20. Partly our own doing, since we'd
just split the checks into more parallel jobs so they'd run faster. Which, sure, they did. My
question was why we were leaning on hosted builds at all for things my own machine can run for
free, so the checks run there now.

65 PRs merged, 21 test runs, and one major per fight pass that just would not quit. That's week
eight. See you next week.

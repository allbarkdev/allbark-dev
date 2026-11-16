---
title: "Week seven: we counted the features that did nothing"
description: "Test passes kept finding major bugs, so we stopped and asked why. The answer was a pile of class features that were only text on a card. Cerberus got an audit that counted them, a sheet page cut from 13,258 lines to 1,251, and area spells that can hit your friends."
week: 2026-W46
app: Cerberus
image: /assets/devlog/2026-w46/og.png
image_alt: "The Bark Blog, week 46: Week seven, we counted the features that did nothing, beside a Fireball damage card listing a dragon, goblins and a bandit as targets"
og_shot: /assets/devlog/2026-w46/fireball-targets.png
---

Week six ended with nine rounds of testing and the bug counts going down. Week seven started with
more rounds, and they kept finding majors. Not niche stuff either. Real things a player would hit.

So I stopped and asked the obvious question: are we finding a handful of niche issues, or the
same kind of real issue every time? We went back over the last few test passes looking for a
theme, and there was one. A lot of class features were text on a card. You could tap them, they
spent your action, and then nothing happened.

That's this week. We counted them, built a test that keeps the count going down, and made most of
them work. And to make that possible, the 13,000-line page behind the character sheet finally
got broken up for real. About 85 merged PRs.

## Features that did nothing

Honestly, I'd assumed this was already true. From the very start, when we brought in everything
from the SRD, the whole point was for Cerberus to play like a game: if a feature does something
at the table, the app does it. Turns out that idea lived in my head more than in the
instructions. So we wrote it down. We ran a quiz of 16 questions on how the app should behave,
and my answers became written rules. The one that matters here: nothing ships unfinished unless
the app literally can't do it yet.

Then we counted. Sonnet wrote an audit script that goes through every SRD class, subclass and
species feature, finds the ones with no rules data behind them, and sorts each one by what (if
anything) makes it work. The first count was 131 features with no effects in the data, and 73 of
those had nothing behind them at all. Just text.

The script came with a test, and the test is the part I like. It fails if a new feature does
nothing without a written reason. It also fails if something on the list starts working and
nobody takes it off the list. So the list can only shrink, and it can't quietly lie in either
direction.

Opus took the first big swing at it: on-hit features like Divine Strike and Primal Strike, Hunter
and Thief features, luck and Initiative features, auras, senses, saves and healing. Over the rest
of the week the fixes kept coming: smites, defenses, Quivering Palm, Indomitable, Cloud's Jaunt,
Holy Nimbus, and Divine Intervention actually casting a Cleric spell.

Magic items got the same treatment. The parts we used to leave "to the table" now play: the Ring
of the Ram, Iron Bands, the Sun Blade, the Pearl of Power, found charges and magic ammunition.
Bestow Curse is done end to end, including a monster cursing a hero. And the combat wheel had its
own version of the problem, wedges that spent your action and did nothing else, so those are
checked by tests now too.

By Sunday it was 82 features with no effects data, and only 15 with nothing behind them. Most of
those 15 are covered somewhere else, or are the player's call on purpose. Walking on walls, say.
The app doesn't need to know which wall.

## The refactor that wasn't

Here's the less fun part. Breaking up the character sheet page had been on the plan for a while.
Several passes had worked on it. And when I actually looked, the file was still over 12,000
lines. That one bugged me. I asked pretty directly how a planned refactor had barely moved, and
whether we needed rules so the work matched what was claimed. Then I asked to see the plan
before anything started, instead of just saying go.

It wasn't about tidiness. The page ran most of the taps itself, which meant a dead tap could only
be caught by clicking around in a browser. That's exactly why the "does nothing" features slipped
past every test pass.

The real breakup started with one small thing: a CI check that fails if the page gets any
bigger. At that point it was 13,258 lines. Then Fable moved the game logic out one area at a time,
each step its own PR: hero state and Hit Points, feature uses, a fight's turns and the wheel,
the roll card, casting, the hero's seat at the DM's table, and finally the markup into
components. Nine steps, merged in order in one day. Opus picked up the follow-ups, moving the
last rule checks out of the components and testing them.

The page is 1,251 lines now. The logic lives in thirteen "play" modules (turn, fight, attack,
cast, table, wheel, uses and so on) that unit tests can drive directly. So new tests go through
every feature use, every wedge of the wheel and every button on the roll card, without a browser.
Each one has a list that fails both ways, same idea as the audit.

From a player's side, nothing changed except two small fixes. Which is kind of the point.

## Fireball doesn't care who your friends are

Friendly fire almost got left out as a "table call". I didn't want that. Area spells hitting
your allies is part of how the spells are meant to work, so Opus built it in.

Now when you cast Fireball at a table, the damage card lists the creatures first, then your allies
and their companions, then you. You say who's in the blast.

{% include shot.html src="/assets/devlog/2026-w46/fireball-targets.png" alt="A Fireball damage card at a table, 'Dexterity save DC 14, half on a success', listing buttons for Fireball on an Adult Black Dragon, two Goblin Warriors, a Bandit and a Pirate, then on six allies by name, each marked Sculpt Spells, and last 'Fireball on you'" caption="The dragon's first in line. You're last. You're always last." %}

Each ally rolls their own save on their own phone. An Evoker's Sculpt Spells and Careful
Spell spare allies automatically, up to however many they cover.

{% include shot.html src="/assets/devlog/2026-w46/ally-save.png" alt="A Ranger's phone, Bloodied at 12 of 44 HP, with the wheel reading 'Waiting for the DM' and a save card: 'Dexterity save, DC 14 (Sol's Fireball (Careful))', a d20 showing 2 for a total of 8, stamped FAILED" caption="Sol's Fireball, Ren's phone, a natural 2. Ren would like a word with Sol." %}

Two more table things landed alongside it. A seated hero's checks, saves and free dice now show
up on the DM's screen and on the other players' sheets, like "Brynn · Perception · 17", so nobody
has to shout their roll across the table. And a phone that drops off the table's Wi-Fi keeps
playing. What it did while it was gone lands when it reconnects, in order, and only once.

## Bigger screens

On an iPad in landscape, the sheet goes two panes: your hero and the combat wheel on the left,
the tabs on the right. Fable built that one. The DM's table gets the same idea, with the
initiative order on the left and the open creature on the right.

{% include shot.html src="/assets/devlog/2026-w46/ipad-dm-table.png" alt="The DM's table on an iPad: 'Friday Night Table', round 1, with the order on the left (Brynn Ironjaw 25, Owlbear 20, two Worgs, Sister Maeve, Thorga Ashmane, Isolde Starweave), a passive Perception, Insight and Investigation table for the heroes, and on the right the Owlbear's card with 59 of 59 HP, its combat wheel and its checks" caption="Round 1. The Owlbear rolled a 20 and is feeling great about it." wide=true %}

Regular iPhones stay upright. They just didn't look good on their side.

## What didn't go great

Merge conflicts, again. Lots of fix threads were working on the same few files in parallel, so
merging one PR would knock the next two out of shape, and one of them conflicted again right
after its fix. That stayed the main friction all week.

The majors didn't stop overnight either. Pass 12's fight run found a blocker and five majors.
Pass 13 found five majors and zero blockers. Each round got fixed before the next one started.
Better, not done.

And the counting itself was a good little lesson. The task going in guessed about 124 features
were doing nothing. The script found 131. Which is why the test checks the list both ways now.

## Also in the pile

A tap that closes a card never presses whatever's behind it. That bug had come back a few times,
once dressed up as "saving the player a tap", so it's a written UI rule now. Heals and Bardic
Inspiration get built once for every device. Bane, Hex, Vicious Mockery, Weapon Mastery, Stunning
Strike and Open Hand apply on the hero's own phone. Ability and tool checks show Disadvantage.
And test passes 10 through 13 all got their fix rounds.

That's week seven. See you next week.

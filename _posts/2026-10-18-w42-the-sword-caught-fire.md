---
title: "Week three: the week the sword actually caught fire"
description: "Every SRD magic item now does something on the sheet, level ups get a gold burst, the combat wheel learned to move, and the dice roller turned into a shaker. Here's how Cerberus learned to celebrate."
week: 2026-W42
app: Cerberus
image: /assets/devlog/2026-w42/og.png
image_alt: "The Bark Blog, week 42: Week three, the week the sword actually caught fire, beside a screenshot of a gold level-up burst reading Bram reached level 5"
og_shot: /assets/devlog/2026-w42/level-up.png
---

Week two, Cerberus learned to sit at a table. Week three, it learned to celebrate, and its magic
items stopped being paragraphs. Level ups, checks, rests and Initiative all got fanfare, the combat
wheel got motion, and by the end of the week every SRD magic item either does something on your
sheet or says exactly what it leaves to the table.

That was 70 merged pull requests, split between Opus and Fable. Two of them
were dependency bumps, so, 68 if you're counting the fun ones. This post goes deep on the items, the
fanfare and the wheel, and the rest gets the usual one breath at the end.

## Items that actually do things

Right after I reworked attunement, I went looking at what the items themselves did. The answer was:
not much. The store was full of magic items that were really just text telling you what they
*should* be doing. A Flame Tongue was a longsword with a nice paragraph attached.

Fable's first pass gave 37 items hand-written mechanics and flagged everything else as "left to the
table." Honestly, that's a reasonable first move, and it showed me where I wanted the line. If it's
SRD, the engine should run it. A table flag is fine for homebrew the engine can't express yet, or for
things that are purely narrative. A Bag of Holding isn't narrative. It's just a place to put stuff.

So instead of more flags, the engine grew vocabulary. Items now speak the same effect language as
class features, and they only apply while the item is carried, worn or attuned, whichever its text
asks for. On top of that, Fable added weapon riders, Immunity, printed DCs, consumables, charged
casting at higher levels, several uses per item, Climb and Swim Speeds, roll tables, containers
and Spell Scrolls.

What that looks like on the sheet:

- **A Flame Tongue hit offers "Add Flame Tongue 2d6".** The sword actually catches fire now. Hence
  the title.
- **Spells from items land with your spells**, at the item's printed DC, and they spend its charges.
  Higher levels are offered at their charge cost.
- **Potions are a Bonus Action** that heals straight onto the sheet and uses one up.
- **Spell Scrolls come as one kind per SRD spell**, with the DC 10 + level check when the spell is
  above your level.
- **Bags of Holding and backpacks hold items.** And a Bag of Holding can't go inside another Bag of
  Holding, because we've all seen how that ends.
- **The Wand of Wonder and friends roll their SRD tables**, as data.

Some things still need a person, like stepping onto another plane. Those stay "At the table", but
now each one says exactly what in one sentence instead of shrugging.

{% include shot.html src="/assets/devlog/2026-w42/wand-of-fireballs.png" alt="A phone character sheet's Cast Fireball panel reads 'Level 3 Evocation · Wand of Fireballs · Save DC 15', with one cast option, 'Free · Wand of Fireballs, 5 left, back on a Long Rest', above an '8d6 Fire, Dexterity save DC 15, half on a success' card and a gold Cast Free button, while the dimmed spell list behind it shows Fireball tagged 'Wand of Fireballs · Always prepared'" caption="An early capture. Wand's DC, wand's charges, wand's Fireball. Spot the two bugs: it says Free and a Long Rest, and the wand recharges at dawn. Both got fixed by the end of the week." %}

### Spells from items aren't your spells

This one's subtle and I'm glad we got it right. Under the SRD's rule for spells cast from items, a
wand's Fireball uses the wand's DC and the wand's charges, never your own slots. So the cast panel
and the combat wheel only offer the item's costs for item spells. Items that boost your spell DC,
like the Robe of the Archmagi, raise your own casting but never a printed DC.

### Not taking the easy way out

The tempting version was a "table only" checkbox on anything hard. Doing it properly meant teaching
the engine new tricks. A Rod of Lordly Might is several items in one, so an item can have several
uses. Potions of Giant Strength set your Strength while they last, and your saves, attacks and
carrying weight follow along.

To keep all that honest, there's a content test that checks every DC, die, save, level and charge
count against the item's own text. If the data says one thing and the item says another, it fails.

## Fanfare for the moments the table cheers

Leveling up used to save and dump you back on your sheet. That's it. It's the biggest moment in a
campaign and the app treated it like a form submission.

I wanted some fanfare right at the end of the wizard, before you head back to the sheet. So now
there's a gold burst and a chime, and Opus made the gains arrive as headlines.

The real design call was the order. What changes how you play (a subclass, Extra Attack, new
spells) goes first, and the arithmetic (HP, Proficiency Bonus, slots) comes after. Past five
headlines it says "and N more on your sheet", so it never turns into a list.

{% include shot.html src="/assets/devlog/2026-w42/level-up.png" alt="A dark phone screen with a large gold 5 glowing in a burst of rays. Below it: 'Level up. Bram reached level 5. Fighter 5.' Four gold-edged headline cards read New feature Extra Attack, New feature Tactical Shift, Hit Points +8, and Proficiency Bonus +3, above a gold 'To your sheet' button" caption="Extra Attack first, math second. Bram earned this." %}

Checks and saves got the same treatment, with the same rule: only fire when there's something to
say. When the DC is known, a check stamps Passed, Saved or Failed and washes the screen edges green
or red. When it isn't, nothing gets stamped. A manual check from the sheet also stopped asking you
whether you passed, because that was just one more tap.

Short and Long Rests got their own fanfare too, and rolling Initiative now lifts the number off the
roll card and flies it up to the Combat line.

## A wheel that moves like it means it

I wanted the combat wheel to feel more mechanical. Think Transformers, a ton of parts all moving in
sync. We prototyped three takes side by side and recorded each one with the same taps:

- **Iris**: aperture blades.
- **Gearbox**: plates folding up in 3D.
- **HUD**: a radar sweep that draws each wedge.

I picked HUD. Then I wanted it in reverse when combat ends, so the wheel sweeps itself back out of
existence. Then I liked the iris more than I expected, so we split the job: the sweep for the wheel
showing up and leaving, and the iris blades for moving between rings. Fable built all of it. A ring
of light also pings out from the hub when your turn starts.

{% include shot.html src="/assets/devlog/2026-w42/wheel-iris.png" alt="A phone character sheet for Hild, a level 5 dwarf cleric on 7 of 43 hit points, in round 1 of a fight, with her circular combat wheel opening a ring of spells (Cure Wounds, Guiding Bolt, Spirit Guardians, Bless, Bane, Hold Person) as the last wedges twist into place around a Back button" caption="Mid-iris. Hild's on 7 HP, so she'd like the Cure Wounds wedge to hurry up." %}

Once the motion and the light were showing whose turn it was, the "On your turn" and "Ready"
captions weren't saying anything new, so they went. Screen readers still hear them. The wheel is now
the only combat view, too. The old list option is gone.

The glow behind the wheel took three tries. Even the third one reached way too far out and came out
kind of egg-shaped. Then I spotted why: the buttons were a little see-through, so the glow stacked up
on top of them. Solid wedges, gaps for the glow to come through, no outer ring.
Fixed.

## The dice shaker

The free roller from last week had a lot going on. What I actually wanted was simple: every tap on
a die tosses that die into the pile, and the total keeps counting. The first rework still had too
much stuff around it. So Opus cut it down to the die buttons, the same 3D dice the character sheet
uses, Reset and Toss dice. That's the whole screen now.

I also wanted a d100, which is really just two d10s, so that's how it rolls: a tens die and a ones
die.

{% include shot.html src="/assets/devlog/2026-w42/dice-shaker.png" alt="A dice tray on a dark phone screen holding five 3D dice: two percentile d10s showing 80 and 90, two d10s showing 7 and 8, and a d6 showing 4. The total reads 189 for 2d100 + 1d6. Below are buttons for d4 through d100, Reset, and a gold Toss dice button" caption="2d100 + 1d6 = 189. No idea what you'd roll that for. It's fun to shake though." %}

## Attunement is a rule, not a toggle

Attuning to an item worked exactly like equipping it. I'd seen language about it taking a Short Rest
and asked whether that was right. Nope. In SRD 5.2 you spend a Short Rest focused on the item. So
with strict rules on, attuning or ending attunement takes a Short Rest, one item per rest, never in
a fight and never at 0 HP. Opus built that one.

The same conversation reshaped the loadout. Attunement can cover things you're also holding, or
extra stuff like rings and cloaks, so the two needed to look different. Now it's two rows: armor and
both hands on top, three violet attunement sockets below.

{% include shot.html src="/assets/devlog/2026-w42/attunement-sockets.png" alt="A phone showing a hero's inventory: Leather Armor and a dagger in hand on top with an empty off hand, and below them three violet attunement sockets, two holding a Ring of Protection and a Cloak of Protection and the third still open, labeled Attuned 2 / 3, a Short Rest each" caption="Hands up top, attunement down below. One socket still open." %}

The store got the same kind of rethink. Magic items used to sit in their own tab, badly grouped,
with nothing past a short blurb. Now the store opens on a market of stalls, one per content pack,
with shelves by what an item is. A magic longsword sits with the longswords. Fable built the market
and a single detail card that every item opens.

## Filming the shorts turned into QA

Every daily short gets filmed in the real app, and this week filming kept tripping over bugs. A "Saved" notice showed up while the d20 was still tumbling, which kind of spoils the roll.
The armor card showed the hero's total AC instead of the armor's own. Opus fixed both.

The Wand of Fireballs short alone found five more: "At will" on casts that actually cost charges, a
Cleric being offered her own slot for the wand's Fireball, a socket that just said "Wand", "back on
a Long Rest" for a wand that recharges at dawn, and a DM log calling three Magic Missile darts "Dart
1". Fable fixed all five in one go. Another short caught the spell level arrow sitting right on top
of the cast button.

Two more sneaky ones: on spinning rings of nine or more options, hidden wedges kept a backing that
ate taps in some spots, and on iOS a swipe inside a popup still moved the page behind it. Both
fixed.

## Also in the pile

The rest of the week, in one breath: loot parcels the DM shares as a file, swipe back instead of
back buttons with the top bar moved into the hero menu, dice sounds that match how many dice you
rolled, an attack card that goes straight to damage with Miss in red, strict rules on the dock's
cards mid-fight, temp HP in the damage preview, a coin number pad, sheet tabs for Checks, Spells,
Resources and Features, the roll history dropped, tool checks with the SRD Utilize uses and DCs,
Wild Shape locking spellcasting, a crowded spell ring that opens by kind and then by level, a
"Kennel Armory" pack of homebrew test items, packs that are simply on or off, a sweep through the
whole app cutting explainer text that was just repeating what the buttons already said, and a pile
of layout and mobile fixes.

Tests once the item work landed: 439 in the rules engine, 214 for content and 274 in the app.

That's week three. See you next week.

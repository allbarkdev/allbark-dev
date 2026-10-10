---
title: "Week one: from an empty repo to a combat wheel"
description: "A 5E character builder, a tap-to-roll table sheet and three versions of a combat screen in seven days. Here's the rule we set on day one, and how the turn became a wheel."
week: 2026-W40
app: 5E character builder
image: /assets/devlog/2026-w40/og.png
image_alt: "The Bark Log, week 40: Week one, from an empty repo to a combat wheel, beside a screenshot of the combat wheel"
og_shot: /assets/devlog/2026-w40/wheel-wedges.png
---

Seven days ago the repo for our new app was empty. Seventy-three merged pull requests later it's
a guided character builder for 5E, a table-side sheet you tap to roll from, and a combat mode we
designed three times in two days. All twelve classes from the 5E System Reference Document are in,
levels 1 to 20, and that part was done by day three.

That's too much for one post, so this one sticks to the two stories that shaped everything else:
a rule we set on day one, and how a turn of combat turned into a wheel.

## Day one: save the choices, never the numbers

A 5E character sheet is a pile of derived numbers. Your Athletics bonus comes from your Strength,
your proficiency bonus, your class, maybe your background, maybe a feat. Store those numbers and
every rules fix turns into a data migration, and every screen has to be careful not to let you
build something illegal.

So on day one we decided that a character is saved as **the list of choices the player made**, and
nothing else. A pure rules engine re-derives the whole sheet from those choices every time. The
builder doesn't decide what to ask you next. It asks the engine which questions are still open and
only shows those.

That one call is what makes the builder hard to get wrong. Validation lives in the engine, not in
the screens. Every option is a card or chip that says what it gives you, and **Next** stays locked
until the step is valid, with the reason right there: "pick 1 more", or "You already have
Athletics".

{% include shot.html src="/assets/devlog/2026-w40/wizard-choices.png" alt="Builder step titled Skills & Feats. Skill choices are tappable chips with their bonus, Perception is picked, and Athletics and Intimidation are greyed out and marked Yours because the character already has them." caption="Skills you already have show up as *Yours* instead of letting you pick them twice." %}

The same engine powers everything after the builder. Finish a character and you land on a table
sheet where tapping any ability, saving throw, skill or initiative rolls it, with advantage and
disadvantage applied for you. Attack and damage rolls, HP tracking with death saves, and short
rests followed the same day. The engine's test suite went from 53 to 81 tests on day one alone.

{% include shot.html src="/assets/devlog/2026-w40/sheet-advantage.png" alt="A Fighter's table sheet with saving throws and skills listed. Athletics carries an ADV badge, and a roll card shows two d20s, 11 and 2, with the 11 kept for a total of 16." caption="Athletics with advantage: roll two, keep the 11, add 5." %}

One small detail we like: HP is stored as **damage taken**, not current HP. Level up and your max HP
goes up, but the wounds you're carrying stay put, because that's what actually happened.

Nothing derived is ever saved, so a character also survives rule fixes. If we get a number wrong
and fix it, every saved character is right the next time it opens.

We also had to pick a platform. Justin was drawn to Flutter for a game-like feel. The honest
comparison was that Flutter's 2D edge is small for an app like this and shows up mostly on low-end
Android phones. The web gives you a sheet you can open on a laptop at the table, or send to your
DM as a link, and an offline web app for free. We'd also already shipped Byte on Svelte, which
gave us a template to start from. So we went with Svelte, web first, wrapped for iOS and Android.

## Combat, three ways in two days

### Version one: a very good menu

The first combat view tracked your Action, Bonus Action and Reaction each turn and listed
everything you could do with them. It worked. It also read like a restaurant menu, not a turn.

Justin's notes on it came in four parts. The action bar belongs at the bottom. The "next roll"
footer takes up a lot of room for something you rarely touch. Cards for things the turn guide
already offers shouldn't show up twice. And the common stuff, attacking and casting, deserves a
bigger stage than "Study". Most of all, clicking Attack should *lead* somewhere: to your next
attack, or to the things that ride along with one. It shouldn't just leave every other action
sitting there.

### Version two: a turn with a direction

So the turn bar moved to the bottom, the footer shrank to a small Adv/Dis toggle, duplicate cards
hide during combat, and attacks and spells became big tiles. Taking the Attack action now locks the
turn into a sequence, "Attack 2 of 3", with **Next attack** and **Done attacking**.

{% include shot.html src="/assets/devlog/2026-w40/attack-flow.png" alt="Mid-turn Fighter. The Attack section glows with the label Attack 2 of 2 and weapon tiles for Unarmed Strike, Greatsword, Flail and Javelin, plus a Done attacking button. Bonus Action and Reaction sections sit below." caption="Mid-turn, the Attack action is a sequence you step through." %}

One idea from this round turned into a dead end. Justin's sketch of the attack flow included
swapping an attack for a cantrip. In the SRD 5.2 rules only monsters get to do that. So instead the
flow offers what the rules really do tie to an attack: the extra attack from a Light weapon (and
Nick, which folds that extra attack into the Attack action itself), and once-per-turn riders like
Sneak Attack.

### Version three: the wheel

Then Justin dug up an old project. Years ago he built an infinite radial menu in Unity, designed
for combat action menus in games, especially on mobile:

> Have the HP card shown as a circle in the middle with action, bonus action, reaction buttons
> surrounding it.

He also asked for a green-to-red glow around the HP, for a little extra pizzazz.

It fit better than we expected, because a turn was already a tree: Action, Bonus Action or
Reaction, then attacks, spells or features, then the thing that actually does it. That meant the
wheel could be a new *view* over the same engine state, not a second combat system to keep in sync.
Day one's rule paid off again. Pick something and it moves to the center with its details and a
**Use** button.

{% include shot.html src="/assets/devlog/2026-w40/wheel-first.png" alt="The first combat wheel on a Rogue's sheet. The breadcrumb reads Turn, Action, Attack, and a Shortsword attack at plus 7 for 1d6 plus 4 piercing sits in the green center ring with an Attack button, with other weapons around it." caption="The first wheel: drill down from Action to Attack to a weapon, and it lands in the middle." %}

### Rectangles around a circle never look right

Our first try put three rounded buttons at 12, 4 and 8 o'clock. It looked lopsided whichever way
we nudged it, because a rectangle is wider than it is tall, and no amount of padding fixes that.
The fix was a different shape: three equal 120° segments.

Justin still didn't like the gaps between the buttons on the top layer. He wanted "Rhombus like buttons coming out from the center like the old Simon says", plus "an almost
mechanical animation like a sci fi door opening and closing."

So we got touching wedges with dark seams, and a door. When you move between layers, the old panels
twist into the center, the HP circle gives a little clunk, and the new panels twist out one by one
with a slight overshoot. With reduced motion turned on, the layer just swaps.

{% include shot.html src="/assets/devlog/2026-w40/wheel-wedges.png" alt="The combat wheel on a Sorcerer's sheet: HP 72 of 72 in a green ring at the center, surrounded by three touching wedges for Action, Bonus Action and Reaction, with the round bar and spell slots below." caption="Three touching wedges, HP in the middle." %}

{% include clip.html src="/assets/devlog/2026-w40/wheel-door.mp4" poster="/assets/devlog/2026-w40/wheel-door-poster.png" label="Screen recording of the combat wheel switching layers: the wedges twist into the center and new ones twist out." caption="The door animation. This was captured in a headless browser, so it's choppier here than on a phone." %}

A few more things the round shape made us think about:

- **Don't move buttons under a thumb.** The wheel puts the options you use most at 12 o'clock, but
  it only re-sorts when combat starts. Anything that appears or disappears mid-turn lands at the
  bottom, so nothing you were about to tap slides away.
- **Long spell lists on a round menu.** About eight labeled options fit around a ring on a phone.
  Rings that would be crowded split into another layer (Spells, then by level), and only what still
  doesn't fit spins, with arrows. Most rings never need to.
- **A bug we only found by re-checking.** After the wheel shipped, we re-ran a Rogue's turn and
  rolled damage before closing the result. The wheel marked the Nick extra attack "Action used",
  which it wasn't. We fixed it in the same change.

## Our first outside tester

This week our Android tester went through the builder and sent 17 numbered notes, plus
three more comments. All but two were handled in a single change.

The biggest one: picking a species, class or background auto-advanced right past the tab that
explained what it gives you, so nobody ever saw it. Now tapping a card opens what it gives you right
under it, with a **Choose** button, and the separate tab is gone. The steps also now go Class,
Background, Species, which is the order the SRD 5.2 itself uses.

Point buy used to start from the standard array, so you had to lower every score before you could
spend anything. Now every score starts at 8 with 27 points, and you can't move on until you've spent
them all. Rolled stats got a roll counter, with a little ribbing as the number climbs, because the
tester asked for one.

The review step now labels every feature, skill and tool with where it came from:

{% include shot.html src="/assets/devlog/2026-w40/review-sources.png" alt="The builder's review step listing features and feats, each labeled with its source, such as Origin Languages from background Soldier, Skillful from species Human, and Second Wind from class Fighter." caption="Every line says where it came from." %}

The tester was right about most things and wrong about one. He flagged that multiclassing listed an
ability requirement for the class he already had. But SRD 5.2 really does require a 13 in your
current class's main ability as well as the new one's. The rule stayed, and the badges now say
"to multiclass out" and "to multiclass in" so it stops looking like a bug. A question about weapon
proficiency turned out to be correct per the rules too. The real confusion was Weapon Mastery, which
now explains itself right where you pick it.

He also asked for an equipment store. Justin's reaction: the SRD has equipment, and new characters
start with gold to buy their own gear, so it should be there. It shipped the same day.

## Also in the pile

The rest of the week, in one breath: the remaining species and backgrounds, 3D dice, a UX pass for
every class, phone notch safe areas, groundwork for the native iOS and Android builds, a motion and
focus pass, previews of the bonus when you pick a skill, icons on the builder cards, equipping weapons
and an inventory, Metamagic when casting, a strict rules mode, an in-app feedback button, a fix for
crit damage, and effect chips in combat.

That's week one. The Bark Log will be back next week with what came next.

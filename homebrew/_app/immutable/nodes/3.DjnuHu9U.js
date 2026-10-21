import{$ as e,A as t,B as n,H as r,K as i,M as a,Q as o,U as s,V as c,W as l,Z as u,_ as d,et as f,t as p,y as m}from"../chunks/BKHGcPE7.js";import"../chunks/-fHkCWoL.js";import{n as h,t as g}from"../chunks/Cv2Ght7N.js";var _=new URL(`../assets/pack.schema.DCooBC2B.json`,import.meta.url).href,v=a(`<meta name="description" content="How Cerberus homebrew packs are put together: the manifest, IDs, building on the SRD, and effects."/>`),y=a(`<h1>The homebrew pack format</h1> <p class="dek">Everything in Cerberus, the SRD included, is a pack: a JSON file with a short manifest and a list
	of entries. Write your own to add subclasses, feats, items and more, then <a>check it here</a> before you share it.</p> <p class="downloads svelte-yugg08"><a class="button" download="hound-master.pack.json">Example: a subclass</a> <a class="button" download="kennel-armory.pack.json">Example: magic items</a> <a class="button" download="pack.schema.json">JSON Schema</a></p> <section class="svelte-yugg08"><h2 class="svelte-yugg08">The manifest</h2> <pre><code></code></pre> <ul class="svelte-yugg08"><li class="svelte-yugg08"><code>id</code> is what heroes remember the pack by, so keep it once you've shared it.</li> <li class="svelte-yugg08"><code>version</code> is your content's version. <code>formatVersion</code> is this format's,
			and is <code>1</code>.</li> <li class="svelte-yugg08"><code>namespace</code> is a short prefix that goes in front of every ID in your pack, so two
			packs can never clash. <code>srd</code> is taken.</li> <li class="svelte-yugg08"><code>license</code> says how others may use your work, and <code>attribution</code>, if your
			license needs one, is shown on the app's About screen.</li></ul></section> <section class="svelte-yugg08"><h2 class="svelte-yugg08">Building on the SRD</h2> <p>A pack can use its own entries and those of the packs it lists in <code>dependencies</code>,
		nothing else. List <code>srd-5.2</code> to point at SRD classes, spells, items and features by
		their IDs, like <code>srd:class.fighter</code> or <code>srd:spell.fireball</code>.</p> <p>To add an option to a choice another pack offers, such as a new Fighter subclass, use <code>extensions</code>. The new option only shows up for heroes using your pack.</p></section> <section class="svelte-yugg08"><h2 class="svelte-yugg08">Entries</h2> <pre><code></code></pre> <p>Each entry has an <code>id</code> (your namespace, a colon, then a type and a name in
		kebab-case), a <code>type</code>, a <code>name</code>, an optional one-line <code>description</code>, and its <code>effects</code>. The types are <code>class</code>, <code>subclass</code>, <code>species</code>, <code>background</code>, <code>feature</code>, <code>feat</code>, <code>spell</code>, <code>item</code>, <code>package</code> and <code>creature</code>. The key in <code>entries</code> must match the <code>id</code>.</p></section> <section class="svelte-yugg08"><h2 class="svelte-yugg08">Effects</h2> <p>Effects say what an entry does, in plain data. Cerberus applies them in order and does the math,
		so you never write a number the app could work out. Any effect can take <code>level</code> to switch on from that character level.</p> <pre><code></code></pre> <ul class="svelte-yugg08"><li class="svelte-yugg08"><strong>grant</strong> adds something: a proficiency, a feature, a spell, a language, advantage
			on a roll.</li> <li class="svelte-yugg08"><strong>modify</strong> changes a number like Speed, max HP or AC. Amounts can be a number, <code>"proficiency"</code> or <code>"level"</code>.</li> <li class="svelte-yugg08"><strong>choice</strong> asks the player to pick, and grants each pick.</li></ul> <p>Features and feats can also carry limited <code>uses</code> per rest, with their own rolls. The JSON
		Schema lists every target and option, and the examples show most of them in use. Editors that read
		JSON Schemas, like VS Code, can check a pack as you type once you map the schema to your pack files
		in their settings.</p></section> <section class="svelte-yugg08"><h2 class="svelte-yugg08">A few rules</h2> <ul class="svelte-yugg08"><li class="svelte-yugg08">Write your own words. Only the SRD 5.2 is free to copy; other books are not.</li> <li class="svelte-yugg08">Homebrew is labeled as homebrew in the builder and on the sheet.</li> <li class="svelte-yugg08">Pack files stay yours. Cerberus reads them and never uploads them.</li></ul></section>`,1);function b(a,b){o(b,!0);var x=y();m(`yugg08`,e=>{var i=v();n(()=>{r.title=`Homebrew pack format · All Bark`}),t(e,i)});var S=i(l(x),2),C=i(s(S));e(),f(S);var w=i(S,2),T=s(w),E=i(T,2),D=i(E,2);f(w);var O=i(w,2),k=i(s(O),2),A=s(k);A.textContent=`{
  "id": "my-hound-pack",
  "name": "Hound Master",
  "version": "1.0.0",
  "formatVersion": 1,
  "namespace": "hound",
  "publisher": "Your name",
  "license": { "name": "CC-BY-4.0", "url": "https://creativecommons.org/licenses/by/4.0/" },
  "dependencies": [{ "id": "srd-5.2" }],
  "extensions": [
    { "choice": "srd:class.fighter.subclass", "add": ["hound:subclass.fighter.hound-master"] }
  ],
  "entries": { … }
}`,f(k),e(2),f(O);var j=i(O,4),M=i(s(j),2),N=s(M);N.textContent=`"hound:feature.hound-master.loyal-companion": {
  "id": "hound:feature.hound-master.loyal-companion",
  "type": "feature",
  "name": "Loyal Companion",
  "description": "A hound fights at your side.",
  "effects": [
    { "kind": "grant", "target": "advantage", "value": "skill.perception", "level": 3 }
  ]
}`,f(M),e(2),f(j);var P=i(j,2),F=i(s(P),4),I=s(F);I.textContent=`{ "kind": "grant", "target": "proficiency.skill", "value": "athletics" }
{ "kind": "grant", "target": "feature", "value": "hound:feature.keen-nose", "level": 3 }
{ "kind": "modify", "target": "speed", "amount": 5 }
{ "kind": "modify", "target": "hp.max", "amount": "level" }
{ "kind": "choice", "id": "hound:feat.pack-tactics.skill", "label": "Pick a skill",
  "choose": 1, "target": "proficiency.skill", "from": ["perception", "survival"] }`,f(F),e(4),f(P),e(2),c(e=>{d(C,`href`,e),d(T,`href`,h),d(E,`href`,g),d(D,`href`,_)},[()=>p(`/`)]),t(a,x),u()}export{b as component};
# What actually happens to your accounts when you die

**A sourced teardown of every digital-legacy service, password manager, and platform "legacy contact" feature — and the two questions none of them answer together.**

Researched and published by [CairnVault](https://cairnvault.app). Every claim below was verified against the vendor's own live documentation on **2 August 2026**, with the URL and the exact wording recorded. Where we could not verify something, we say so and leave the claim out. Corrections are welcome — see [Corrections](#corrections).

*This is a comparison of how products work. It is not legal advice.*

> 📖 **Prefer to read it as a web page?** [cairnvault.github.io/digital-legacy-teardown](https://research.cairnvault.app/digital-legacy-teardown/)
> · 🎬 **Prefer 4 minutes of video?** [What happens to your online accounts when you die](https://youtu.be/AHOkf6vYjrE)
> · 📄 [Full source list](SOURCES.md) · 🔍 [Open verification questions](https://github.com/cairnvault/digital-legacy-teardown/issues) — help us close them
>
> ❓ **Just want your own question answered?** This document compares *products*. If you are here
> because someone died, or because you are trying to work out what to set up, start with
> [**15 questions about digital death, answered from primary sources**](https://research.cairnvault.app/digital-legacy-answers/)
> — Google, Apple, Facebook, password managers, crypto, wills and RUFADAA, each answered on its own page.

---

## The short version

There are exactly two hard questions in this category:

1. **Does the provider actually verify that you died** — or does it just measure whether you stopped logging in, or take a stranger's word for it?
2. **Can the provider read your data?** If a staff member can grant someone access to your vault, then the staff can read your vault.

Almost every product answers one of these well. We could not find one that answers both.

|  | **Provider CAN read your data** | **Provider CANNOT read your data** |
|---|---|---|
| **Death NOT verified** | Everplans, GoodTrust, Apple, Google, Meta, every password manager | CipherWill, AbsentKey, Passdown, IronClad Family |
| **Death IS verified** | Trustworthy | *(empty — see the disclosure at the end)* |

The bottom-right cell is the interesting one, and the reason it is empty is structural, not accidental: the moment you let an employee review a death certificate and click "grant access," you have given up on the provider being unable to read the data. Doing both at once requires splitting the key so that the company's half is useless alone, and running the review process on the *authorisation* rather than on the data.

---

## 1. The platforms you already use

### Apple — Legacy Contact

Apple's Digital Legacy programme is the best of the big-platform options, and it still has a hole precisely where families need it most.

From Apple's own support page, [*How to add a Legacy Contact for your Apple Account*](https://support.apple.com/en-us/102631) (accessed 2 August 2026), verbatim:

> "Your Legacy Contact can't access certain information. Inaccessible data includes movies, music, books, or subscriptions you purchased with your Apple Account, and **data stored in your iCloud Keychain (payment information, passwords, and passkeys)**."

Read that again. The one category of data that would actually let a family settle an estate — **the passwords** — is the specific category Apple excludes. Your photos, messages, notes and device backups can pass to your legacy contact. The keys to everything else cannot.

And to use it at all, your contact needs two things, per the same page:

> "To file an access request after you pass away, they need: The access key that you generate when you choose them as your Legacy Contact — Your death certificate"

The access key is a string Apple generates when you set this up. If you never set it up, or your family cannot find the key, this route is closed. Apple does operate a separate legal-request process for that situation, but it is a different, slower path with no guarantee.

**Verdict: real death verification (a certificate is genuinely required), no passwords.**

### Google — Inactive Account Manager

Google's tool notifies people you designate after you stop using your account. It performs **no death verification whatsoever** — it is a silence timer. You choose an inactivity period (Google's documented options run from 3 months to 18 months*), and up to **10** trusted contacts can be notified when it elapses.

That is a genuine gap, in both directions: a long hospital stay, a sabbatical, or simply switching to a different email can fire it early; and if your family does not know it exists, it may fire into nobody's inbox.

Google separately operates a request process for the accounts of deceased users, but it is discretionary and explicitly does not promise access.

**Verdict: no death verification, and most people who have it do not know they have it.**

> \* The 3-to-18-month range is corroborated across multiple independent secondary sources but we could not confirm it with a verbatim quote from Google's own page, so treat the exact endpoints as approximate. The part that matters — that the trigger is inactivity and nothing else — is confirmed.

### Meta / Facebook — Legacy Contact

A legacy contact can manage a memorialised profile: write a pinned post, update the profile picture, respond to friend requests, and — per Meta's own help documentation — **request the removal of the account**.

What they cannot do is **log in as you or read your private messages**. Meta is explicit about that, and it is the correct privacy decision. It is also, from an estate-settlement point of view, close to useless: memorialisation is a grief feature, not an inheritance feature.

**Verdict: no death verification for the feature itself, and it was never designed to transfer anything.**

> **A correction we are making to our own earlier draft:** we had previously written that a Facebook legacy contact cannot delete the account. Meta's live help page lists requesting account removal as something a legacy contact *can* do. We were wrong; this version is corrected.

### Microsoft — the strictest of all

Microsoft's current published position on access to a deceased person's account requires a **subpoena or court order**, and even then success is not guaranteed. Two narrow exceptions exist for documentation-only requests in Germany and China.

There is no self-service legacy-contact feature. Older references to a "Next of Kin" process date from Microsoft's Hotmail era and do not appear in the current documentation.

**Verdict: the most restrictive major platform. Plan around it, not through it.**

---

## 2. Password managers: the dead end almost everyone assumes will save them

This is the section where our own research changed our minds, so we are going to be precise about it.

The widely repeated claim — including in an earlier draft of our own materials — is that password-manager emergency access *requires the survivor to already be a paying subscriber*. **That is not true, and we are retracting it.** We checked all seven vendors' documentation and the "paying" half is wrong almost everywhere.

What is actually true is both narrower and, in our view, more damning.

| Vendor | Emergency access exists? | What the *survivor* needs | Delay | Death verification |
|---|---|---|---|---|
| **Bitwarden** | Yes | A Bitwarden account — **free is explicitly fine** | Grantor-set, minimum 1 day | **None** |
| **LastPass** | Yes | Any LastPass account, need not be Premium | Grantor-set | **None** |
| **Proton Pass** | Yes (shipped ~Aug 2025) | A Proton account — free is fine | Grantor-set | **None** |
| **NordPass** | Yes | Free users can be recipients* | Grantor-set | **None** |
| **Keeper** | Yes | Unresolved from primary docs — we will not guess | Grantor-set | **None** |
| **1Password** | **No such feature at all** | — | — | — |
| **Dashlane** | Discontinued | — | — | — |

> \* NordPass's support article blocks automated fetching; the "free users can be recipients" line is taken from NordPass's own blog and support-page snippets rather than a full page we retrieved ourselves. Keeper's recipient requirement we simply could not resolve from primary documentation, and we are not going to guess.

Bitwarden's documentation is admirably clear on the point ([Emergency Access](https://bitwarden.com/help/emergency-access/)):

> "Anyone with a free or premium Bitwarden account on the same Bitwarden server can be designated as a trusted emergency contact."

So the honest version of the criticism is this:

**1. Every single one of them is a silence timer.** Not one of the seven performs any death or incapacity verification. The mechanism is universally: your contact requests access → you have a window to refuse → if you do not respond, access opens. That is a design that cannot distinguish a funeral from a two-week holiday with no signal. If you are in an ICU, unconscious, your emergency contact can request your vault and the clock will run out on you.

**2. The survivor still has to set up an account with your vendor, correctly, while grieving.** Free, yes. But a bereaved 68-year-old has to discover which password manager their spouse used, create an account on it, and complete a request flow. That is a real barrier at the worst possible moment, even at $0.

**3. What is released is a raw vault dump.** Several hundred credentials in a list, with no indication of which three actually matter, which subscriptions are still charging the estate, or what to do first. It is data, not instructions.

**4. 1Password — the market leader by reputation — has no mechanism at all.** Its "Emergency Kit" is a self-recovery PDF, and 1Password's own guidance is:

> "It's important that you don't share your Emergency Kit with anyone."

The intended workaround is to print it and put it in a safe. That is not a product feature; that is a piece of paper. (1Password's Families "account recovery" does not fill the gap either — it resets the password of a *living* member who then completes the reset themselves. A dead person cannot complete that step.)

**5. Dashlane's automated emergency-contact feature was discontinued.** What remains is a manual encrypted export or live sharing between two people who are both present.

---

## 3. The dedicated digital-legacy services

### Everplans — $99.99/year

The closest structural analogue to a legacy vault, and the honour system is right at the centre of it.

A designated "Deputy" reports that you have died. Everplans then emails *you* and waits. From Everplans' own blog ([Keep Things Private Until After You're Gone](https://www.everplans.com/blog/keep-things-private-until-after-youre-gone)):

> "After reporting your death, the Deputy must wait while Everplans attempts to contact you via email with the opportunity to block the unlocking."

> "You can choose a wait time for your unlockers of up to 30 days."

(Everplans has also been quoted describing the floor of that range as **as short as three hours**; we found that figure reproduced by a third party quoting Everplans rather than on a page we could fetch ourselves, so treat the exact floor as second-hand.)

**We could find no mention of a death certificate anywhere in the release process Everplans documents.** If nobody clicks the "I'm not dead" link in the email, the vault opens.

On encryption, we want to be scrupulous, because we had this wrong too. Everplans' [security page](https://www.everplans.com/everplans-security) says:

> "all your data is encrypted with a combination of public/private key encryption and AES256 encryption, with uniquely generated keys for each user and Everplan."

> "Everplans administrators can never see the plan information that you fill out or any documents that you upload."

> "Our strict internal procedures prevent any Everplan employee or administrator from gaining access to your account, beyond a limited set of data necessary to help grant you access to your account."

The page never uses the words "zero-knowledge," "end-to-end," or "client-side." So it neither claims nor disclaims the architecture. What it describes is a **policy** promise — strict internal procedures — carrying its own stated carve-out, rather than a mathematical one. That distinction matters: a policy can be changed, subpoenaed, or breached. It is not the same as a company that never receives the key.

*Ownership, for context:* Everplans was acquired by National Guardian Life Insurance in January 2021 and by Precoa, a pre-need funeral marketing company, in October 2024 — both confirmed on Everplans' own site. It now operates as a wholly-owned subsidiary of a funeral-industry parent.

### GoodTrust — $149 first year, then $39/year

A dead man's switch, described plainly in [GoodTrust's own support article](https://support.mygoodtrust.com/support/solutions/articles/66000503696-what-is-the-dead-man-switch-and-how-does-it-work-):

> "select how often you would like us to check-in, 1-4 times a month/year"

> "if you don't reply after 3 times, the dead man's switch will be activated"

Miss three check-ins and your contacts get your documents, devices, accounts and directives. There is no certificate and no human review.

Their [security page](https://mygoodtrust.com/security) describes SSL in transit, AES-256 at rest in "our secure databases," 2FA and SOC 2. It contains **zero occurrences** of "zero-knowledge," "end-to-end encryption," "client-side encryption," or any statement that GoodTrust cannot access your data. This is a conventional server-side architecture: GoodTrust holds the keys.

### Trustworthy — $0 to $40/month

Trustworthy is the most interesting case in the whole category, because it is the one company that genuinely does verify death — and that is exactly what creates its problem.

Per [Trustworthy's legacy-access page](https://www.trustworthy.com/legacy-access-invitation), the survivor submits a request, provides a government ID, uploads a death certificate, and "Trustworthy's team will review and validate the documents." Once approved, access is granted.

That is a real, human-reviewed process, and it is better than every timer above. But look at what it implies: **if Trustworthy's staff can grant a stranger access to your vault, Trustworthy can access your vault.** Access granted by a company is access the company has.

Their marketing does make a strong-sounding confidentiality claim ([FAQ](https://www.trustworthy.com/faq)):

> "Trustworthy uses 'aliasing,' a method that scrambles data to make it unreadable. These aliases are irreversible and cannot be solved — not even by the Trustworthy team."

Read carefully, that claim is **scoped to specific tokenised fields** — passwords, account numbers, Social Security numbers, notes. It is not a claim about your uploaded documents. And your uploaded documents are precisely what their AI features operate on. From [their own product blog](https://www.trustworthy.com/blog/revolutionary-ai-features), "Autopilot":

> "analyzes hundreds of document types, powered by AI... automatically extracts key metadata, and generates concise natural language summaries."

Their FAQ also confirms documents are "automatically captured from your Gmail and organized in your Trustworthy account."

**An AI cannot summarise a document it cannot read.** These two claims live on different pages and are never reconciled. We are not alleging bad faith — the tokenised-field claim is probably accurate as written. We are pointing out that the scope of "not even we can read it" is much narrower than a customer skimming the homepage would assume.

*(For the record: Trustworthy's Series A was **$15M**, led by Valor Siren Ventures in April 2022, bringing total funding to $19.7M. We had previously written "$19.7M Series A" — that was a misreading of the press release and we have corrected it.)*

### CipherWill — free tier, or $40/year

An independent product with a genuine client-side encryption architecture — philosophically the closest thing to us in the category, and the one we most wanted to be fair to.

Its release trigger is an inactivity countdown, and CipherWill documents it precisely ([how the execution timeline works](https://www.cipherwill.com/i/how-execution-timeline-works)):

- **Day 3** of silence — activity check
- **Day 30** — urgent attention
- **Day 90** — last call
- **Day 100** — **key release to beneficiaries**
- **Day 200** — zero-data purge

Any activity resets the clock. Which means the question that decides whether your data is released is not "did this person die" but "did this person log in within 100 days." A hospitalisation, a lost phone, a lost 2FA device, or a long trip is indistinguishable from death.

On the cryptography, their homepage carries this trust line verbatim:

> "Your data is secured with: 256-bit AES Encryption • Zero Knowledge Proofs • Elliptic Curve Cryptography (BLS12-381 & SECP256K1 Curves) • One Time Pad Encryption • Lattice based Encryption (CRYSTALS-KYBER)."

Claiming AES *and* zero-knowledge proofs *and* elliptic-curve *and* one-time-pad *and* lattice-based post-quantum encryption simultaneously is unusual, and no technical paper substantiating the combination appears to exist. Their client code is open source — genuinely commendable — but the **server**, which is the component that decides when to release your data, is not.

---

## 4. So what would actually solve this?

Not a product pitch — a specification. If you are evaluating anything in this category, including us, these are the questions worth asking:

1. **What exactly triggers release?** If the answer contains the word "inactivity," a coma triggers it and a lost password prevents it.
2. **Who reviews the death claim, and can that reviewer also open the vault?** If the same party does both, the encryption is a policy, not a mechanism.
3. **What does my survivor need in advance?** An account? An app? A subscription? Every requirement is a failure point at the exact moment your family is least capable of clearing it.
4. **What do they receive?** A credential dump, or a sequenced set of instructions?
5. **What happens if the company dies before I do?** Ask specifically, and get the answer in writing. This category has a long history of shutdowns — the site that once catalogued digital-legacy services, The Digital Beyond, lists a graveyard of them, and closures have continued: Cake's consumer site now redirects to a funeral-services network rather than operating independently. A vault whose company folds is a vault nobody can open.
6. **Can I get my data out, and can my family, without the company's cooperation?**

---

## 5. Disclosure: who wrote this, and what we built

This research was done by **[CairnVault](https://cairnvault.app)**, and we are not a neutral party — we built a product in this category, so read accordingly. That is exactly why every claim above links to the vendor's own words rather than to our characterisation of them. Check them.

What we built, stated plainly so you can hold it to the same standard:

- Your vault key is derived **on your device** from your master password plus a Secret Key generated on your device, using **Argon2id**. It never reaches us.
- Every field is encrypted with **XChaCha20-Poly1305** before it leaves your browser.
- When you seal the plan, the vault key is **split in two**. Your contacts hold one half, encrypted to keys they generated themselves; we hold the other. **Neither half alone reveals anything.**
- Both halves are wrapped with a hybrid of **X25519 and ML-KEM-768** (NIST FIPS 203), so a future quantum computer cannot retroactively open a vault sealed today.
- Release requires a **death certificate reviewed by a human**, followed by a **48-hour cooling-off window** in which a living planner can cancel a mistaken or fraudulent claim.
- Your survivor needs **no CairnVault account and no subscription** — their key file works on its own.
- What they receive is a **sequenced walkthrough** of your plan, printable: who to notify, then which accounts, then which subscriptions are still charging.
- **$79 one-time** to build and seal a plan. **$29/year optional** maintenance. Building a plan and naming contacts is free; you pay at seal.

And the things we are not going to pretend about:

- **We have not had an external third-party security audit.** For a product making cryptographic claims, that is table stakes and we have not done it yet. It is the first thing we would spend money on.
- **Our death verification is a trained human reviewing a certificate**, not an integration with a government death registry. That is stronger than a timer and weaker than an automated registry check.
- **One nuance in the zero-knowledge claim:** because we relay the invitation email, our mail path transiently handles a one-time secret used to hand a contact their key. It is documented not to be logged, but a maliciously modified backend could in principle capture it at that moment. So the precise claim is not "mathematically impossible under all conditions" — it is "we hold one half of a split key, and never your password or Secret Key."
- **The empty quadrant is our own assessment**, made on 2 August 2026 after searching specifically for anyone who occupies it. The nearest miss we found was IronClad Family, which makes strong zero-knowledge claims but whose own support documentation says "Support cannot release documents manually, even with paperwork" — implying an automated trigger rather than certificate review. If you know of a product that genuinely does both, tell us and we will update this table.

---

## Method, and what we could not verify

Everything above was checked against the vendor's live documentation on **2 August 2026**. Some pages block automated fetching; where that happened we have said so rather than filling the gap from memory.

**Claims we deliberately left out because we could not verify them from a primary source:**

- That Apple permanently deletes a deceased person's account three years after legacy access is granted. Widely repeated; we could not confirm it on Apple's own documentation, so it does not appear above.
- That a death certificate plus a court order alone are insufficient for Apple without an access key. The evidence we found points the other way — Apple appears to operate a separate legal-request route.
- That Trust & Will's digital vault is Everplans white-labeled. Neither company's site substantiates it. Dropped.
- Any verbatim quotation from CipherWill's FAQ on death verification — that page renders via JavaScript and we could not retrieve it.
- A precise current funding total for GoodTrust; published sources conflict.

**Claims we retracted from our own earlier materials** are marked in the text above: the password-manager "must be a paying subscriber" claim, the Facebook account-deletion claim, and Trustworthy's Series A size.

*Vendor terms change. Re-verify before relying on any of this. Not legal advice.*

---

## Corrections

This document is only worth anything if it is correct, so corrections are treated as the
most valuable contribution anyone can make to it — including corrections that make us
look worse.

**How to send one.** [Open an issue](https://github.com/cairnvault/digital-legacy-teardown/issues/new)
with the claim you are disputing and a link to the page that contradicts it. If you would
rather not do it in public, use the contact form at
[cairnvault.app/contact](https://cairnvault.app/contact). If you work for a vendor named
here and think we have characterised your product wrongly, we will correct the text and
record the correction below with the date — we will not quietly edit it.

**Open verification questions.** Several claims in this category are widely repeated and,
as far as we can tell, unsourced. We have filed each one as an issue rather than
publishing it, and we would genuinely like help closing them:
[open verification questions](https://github.com/cairnvault/digital-legacy-teardown/issues?q=is%3Aissue+is%3Aopen+label%3Averification).

### Correction log

| Date | What changed | Why |
|---|---|---|
| 2026-08-02 | Retracted: *"password-manager emergency access requires the survivor to already be a paying subscriber."* | False. Bitwarden's own documentation: *"Anyone with a free or premium Bitwarden account… can be designated as a trusted emergency contact."* Same at LastPass, Proton Pass and NordPass. This claim was in our own earlier marketing; it is now retracted everywhere. |
| 2026-08-02 | Retracted: *"a Facebook legacy contact cannot delete the account."* | Meta's live help page lists requesting account removal as something a legacy contact can do. |
| 2026-08-02 | Corrected: Trustworthy's Series A was **$15M** (April 2022, led by Valor Siren Ventures), not $19.7M. | $19.7M is cumulative funding. We had misread the press release. |
| 2026-08-02 | Dropped: *"Trust & Will's digital vault is Everplans white-labeled."* | Neither company's site substantiates it, and we could find no primary source. |
| 2026-08-02 | Softened: Everplans' encryption description, from *"admits server-side AES-256 with company-held keys"* to a description of what their security page actually says. | Their page is *silent* on zero-knowledge; it makes a policy promise with a stated staff-access carve-out. Overstating it would have been the same error we criticise others for. |
| 2026-08-02 | Removed: Apple's *"3-year deletion"* policy and *"a court order is insufficient."* | Could not be confirmed from Apple's own documentation, and the second appears to be wrong. |
| 2026-08-03 | Added this correction log, and filed the unresolved claims as public issues. | The list of what we could not verify was buried at the bottom of the document; it should be actionable. |

---

*Published by CairnVault — [cairnvault.app](https://cairnvault.app). Corrections and additions are welcome: open an issue on this repository, or use the contact form at [cairnvault.app/contact](https://cairnvault.app/contact). If you are a vendor named here and think we have characterised your product wrongly, say so and we will correct it in the text and record the correction.*

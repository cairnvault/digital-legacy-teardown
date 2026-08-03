# Sources

Every claim in the teardown traces to one of the pages below. All were accessed on
**2 August 2026**. Where a page could not be retrieved by automated fetch, that is
recorded explicitly — those claims are either attributed to a named secondary
source or omitted from the teardown entirely.

If a vendor believes we have characterised their product incorrectly, please open
an issue. We will correct it and record the correction in the README.

---

## Platforms

| Claim | Source | Retrieved |
|---|---|---|
| Apple Legacy Contact excludes iCloud Keychain (passwords, passkeys, payment info) and purchased media | https://support.apple.com/en-us/102631 | fetched, full text |
| Apple requires both an access key and a death certificate | https://support.apple.com/en-us/102631 | fetched, full text |
| Google Inactive Account Manager notifies up to 10 contacts | Google Account Help — Inactive Account Manager | fetched |
| Google Inactive Account Manager performs no death verification | Google Account Help — Inactive Account Manager | fetched |
| Google's separate process for a deceased user's account is discretionary | Google Account Help — submit a request regarding a deceased user's account | fetched |
| Google inactivity period options span 3–18 months | corroborated across multiple independent secondary sources; **not** confirmed by verbatim quote from Google's own page — marked with an asterisk in the teardown | snippet only |
| Meta legacy contact cannot log in or read private messages | Facebook Help Centre — memorialised accounts / legacy contact | fetched |
| Meta legacy contact **can** request removal of the account | Facebook Help Centre — legacy contact | fetched |
| Microsoft requires a subpoena or court order; narrow documentation-only exceptions for Germany and China | support.microsoft.com — accessing the account of a deceased user | fetched |

## Password managers

| Claim | Source | Retrieved |
|---|---|---|
| Bitwarden: grantor needs Premium or a paid org | https://bitwarden.com/help/emergency-access/ | fetched |
| Bitwarden: "Anyone with a free or premium Bitwarden account… can be designated as a trusted emergency contact" | https://bitwarden.com/help/emergency-access/ | fetched |
| Bitwarden: minimum wait time is one day | https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/ | fetched |
| LastPass: grantee needs any LastPass account, not necessarily Premium | LastPass support — Emergency Access | snippet (support site 403s automated fetch) |
| Proton Pass: emergency access shipped ~August 2025; contact may hold a free account | Proton Pass support documentation | fetched |
| NordPass: free users can be recipients | NordPass blog + support article | snippet (support.nordpass.com 403s automated fetch) |
| Keeper: recipient's account requirement not resolvable from primary docs | — | **unresolved; stated as unresolved in the teardown** |
| 1Password has no emergency access feature; Emergency Kit is self-recovery | https://support.1password.com/emergency-kit/ | snippet |
| 1Password: "It's important that you don't share your Emergency Kit with anyone." | https://support.1password.com/emergency-kit/ | snippet |
| 1Password Families recovery requires the member to be alive and complete the reset | https://support.1password.com/family-recovery-plan/ | snippet |
| Dashlane's automated emergency-contact feature was discontinued | Dashlane support / release notes | snippet (support.dashlane.com 403s automated fetch) |
| No vendor of the seven performs death or incapacity verification | all of the above, read together | — |

## Digital-legacy services

| Claim | Source | Retrieved |
|---|---|---|
| Everplans Premium is $99.99/year | https://www.everplans.com/pricing | fetched |
| Everplans: deputy reports death, owner is emailed and may block the unlock | https://www.everplans.com/blog/keep-things-private-until-after-youre-gone | fetched |
| Everplans: "You can choose a wait time for your unlockers of up to 30 days." | https://www.everplans.com/blog/keep-things-private-until-after-youre-gone | fetched |
| Everplans: three-hour floor on the objection window | third party quoting Everplans; the definitive help-centre article returned HTTP 403 on every attempt — flagged as second-hand in the teardown | secondary |
| Everplans: no death certificate found in the documented release process | absence across every page retrieved; the help-centre deputy article was 403-blocked, so this is an absence-of-evidence finding and is stated as such | partial |
| Everplans encryption language, verbatim | https://www.everplans.com/everplans-security | fetched |
| Everplans acquired by National Guardian Life, January 2021 | https://www.everplans.com/blog/national-guardian-life-insurance-company-ngl-acquires-everplans | fetched |
| Everplans acquired by Precoa, October 2024 | https://www.everplans.com/about and https://www.everplans.com/blog/everplans-has-a-new-home | fetched |
| GoodTrust pricing: $149 first year, then $39/year | https://support.mygoodtrust.com/support/solutions/articles/66000513649 | fetched |
| GoodTrust dead man's switch, verbatim | https://support.mygoodtrust.com/support/solutions/articles/66000503696-what-is-the-dead-man-switch-and-how-does-it-work- | fetched |
| GoodTrust security page contains no zero-knowledge / end-to-end / client-side claim | https://mygoodtrust.com/security | fetched |
| Trustworthy pricing tiers | https://www.trustworthy.com/pricing | fetched |
| Trustworthy legacy access: request, government ID, death certificate, team review | https://www.trustworthy.com/legacy-access-invitation | fetched |
| Trustworthy "aliasing… not even by the Trustworthy team", scoped to tokenised fields | https://www.trustworthy.com/faq | fetched |
| Trustworthy Autopilot AI analyses documents and generates summaries | https://www.trustworthy.com/blog/revolutionary-ai-features | fetched |
| Trustworthy Series A was $15M (Valor Siren Ventures, April 2022); $19.7M total raised | PR Newswire, 7 April 2022 | fetched |
| CipherWill pricing: free tier, $40/year | https://www.cipherwill.com/pricing | fetched |
| CipherWill release timeline: day 3 / 30 / 90 / 100 / 200 | https://www.cipherwill.com/i/how-execution-timeline-works | fetched |
| CipherWill trust-badge encryption line, verbatim | cipherwill.com homepage and /how-it-works | fetched |
| CipherWill client code is open source; no server-side repository | https://github.com/CipherwillHQ/cipherwill | fetched |
| IronClad Family: "Support cannot release documents manually, even with paperwork" | support.ironcladfamily.com | fetched |

---

## Deliberately excluded

These claims appear in other write-ups of this category, including earlier drafts
of our own. We could not verify them from a primary source, so they do **not**
appear in the teardown:

- Apple permanently deleting a deceased user's account three years after legacy access is granted.
- A death certificate plus court order alone being insufficient for Apple absent an access key. The evidence found points the other way.
- Trust & Will's digital vault being an Everplans white-label. Neither company's site substantiates it.
- Any verbatim quotation of CipherWill's FAQ answer on death verification — that page renders via JavaScript and could not be retrieved.
- A precise current funding total for GoodTrust — published sources conflict.
- "The average person has 100+ online accounts." This traces to password-manager vendor marketing, not to independent research.
- Specific historical counts of digital-legacy company closures from The Digital Beyond — the list exists, the specific counts could not be re-confirmed.

## Retracted from our own earlier materials

- **"Password-manager emergency access requires the survivor to already be a paying subscriber."** False for Bitwarden, LastPass, Proton Pass and NordPass — a free recipient account is sufficient. Unresolved for Keeper. Retracted.
- **"A Facebook legacy contact cannot delete the account."** Meta's help documentation lists requesting removal as something a legacy contact can do. Retracted.
- **"Trustworthy raised a $19.7M Series A."** The Series A was $15M; $19.7M is cumulative. Corrected.

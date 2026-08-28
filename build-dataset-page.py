#!/usr/bin/env python3
"""Regenerate docs/dataset.html from docs/data/digital-legacy-comparison.json.

The dataset JSON is the single source of truth. The CSV and this HTML page are
both derived from it, so the human-readable table can never drift from the
machine-readable file underneath it. Run after editing the JSON:

    python3 build-dataset-page.py
"""
import json, csv, html, pathlib, re

HERE = pathlib.Path(__file__).parent
DATA = HERE / 'docs' / 'data' / 'digital-legacy-comparison.json'
d = json.loads(DATA.read_text(encoding='utf-8'))

# --- CSV, regenerated from the same source -------------------------------
COLS = ['id','name','vendor','category','releaseTrigger','verifiesDeath',
        'providerCanReadUserData','passwordsIncluded','delay','price',
        'verificationStatus','sources','notes']
with open(HERE/'docs'/'data'/'digital-legacy-comparison.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL); w.writerow(COLS)
    for r in d['records']:
        w.writerow([' | '.join(r[c]) if c=='sources' else r.get(c,'') for c in COLS])

STYLE = (HERE/'docs'/'index.html').read_text(encoding='utf-8')
STYLE = re.search(r'<style>.*?</style>', STYLE, re.S).group(0)

e = html.escape
BASE = 'https://research.cairnvault.app/digital-legacy-teardown'

CAT = {'platform_legacy_feature':'Platform legacy feature',
       'password_manager':'Password manager',
       'digital_legacy_service':'Digital-legacy service'}
TRIG = {'death_certificate_human_review':'Death certificate, human review',
        'inactivity_timer':'Inactivity timer',
        'contact_initiated_silence_timer':'Contact-initiated silence timer',
        'legal_process_only':'Legal process only',
        'none':'No release mechanism'}

def cell(v):
    return {'yes':'Yes','no':'No','partial':'Partial','scoped':'Scoped','unknown':'Unknown',
            'not applicable':'—','self-reported':'Self-reported'}.get(v, e(str(v)))

rows = []
for r in d['records']:
    src = ' '.join(f'<a href="{e(u)}" rel="nofollow noopener" target="_blank">src</a>' for u in r['sources'])
    rows.append(
        f'<tr id="{e(r["id"])}">'
        f'<td><strong>{e(r["name"])}</strong><br><span style="color:var(--mute);font-size:.9em">{e(r["vendor"])}</span></td>'
        f'<td>{e(CAT.get(r["category"], r["category"]))}</td>'
        f'<td>{e(TRIG.get(r["releaseTrigger"], r["releaseTrigger"]))}</td>'
        f'<td>{cell(r["verifiesDeath"])}</td>'
        f'<td>{cell(r["providerCanReadUserData"])}</td>'
        f'<td>{cell(r["passwordsIncluded"])}</td>'
        f'<td>{cell(r["verificationStatus"])} {src}</td>'
        f'</tr>')

DOI = '10.5281/zenodo.21894423'
DOI_URL = f'https://doi.org/{DOI}'
ZENODO_URL = 'https://zenodo.org/records/21894423'

schema = {
  "@context":"https://schema.org","@type":"Dataset",
  "name": d['name'], "description": d['description'],
  "url": d['url'], "version": d['version'],
  "identifier": DOI_URL,
  "sameAs": ZENODO_URL,
  "license":"https://creativecommons.org/licenses/by/4.0/",
  "isAccessibleForFree": True,
  "dateCreated": d['dateCreated'], "dateModified": d['dateModified'],
  "creator":{"@type":"Organization","name":"CairnVault Research","url":"https://cairnvault.app"},
  "publisher":{"@type":"Organization","name":"CairnVault","url":"https://cairnvault.app"},
  "keywords":["digital legacy","digital estate planning","password manager","legacy contact",
              "RUFADAA","inheritance","end-to-end encryption","death verification"],
  "measurementTechnique":"Manual review of each vendor's own published documentation, fetched and quoted verbatim. Fields that could not be established from a primary source are recorded as \"unknown\" rather than inferred.",
  "variableMeasured":[{"@type":"PropertyValue","name":k,"description":v}
                      for k,v in d['fieldDefinitions'].items()],
  "distribution":[
    {"@type":"DataDownload","encodingFormat":"application/json",
     "contentUrl":f"{BASE}/data/digital-legacy-comparison.json"},
    {"@type":"DataDownload","encodingFormat":"text/csv",
     "contentUrl":f"{BASE}/data/digital-legacy-comparison.csv"}],
}

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Digital legacy provider comparison — the open dataset (JSON + CSV)</title>
<meta name="description" content="An open, sourced dataset of what {len(d['records'])} password managers, platform legacy-contact features and digital-legacy services actually do when a user dies. Scored on two questions: does it verify death, and can the provider read your data. JSON and CSV, CC BY 4.0.">
<link rel="canonical" href="{BASE}/dataset.html">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CairnVault Research">
<meta property="og:title" content="Digital legacy provider comparison — the open dataset">
<meta property="og:description" content="{len(d['records'])} providers, scored on whether they verify death and whether they can read your data. Every field carries the source it was read from. JSON + CSV, CC BY 4.0.">
<meta property="og:url" content="{BASE}/dataset.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/json" href="{BASE}/data/digital-legacy-comparison.json" title="Digital legacy provider comparison (JSON)">
<link rel="alternate" type="text/csv" href="{BASE}/data/digital-legacy-comparison.csv" title="Digital legacy provider comparison (CSV)">
<script type="application/ld+json">{json.dumps(schema, indent=1)}</script>
{STYLE}
<script>window.goatcounter={{path:function(p){{return 'research'+p}}}}</script>
<script data-goatcounter="https://cairnvault.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body>
<header class="masthead"><div class="wrap">
  <a class="brand" href="{BASE}/">CairnVault <span>Research</span></a>
  <nav class="sub"><a href="{BASE}/">The teardown</a><a href="{BASE}/sources.html">Sources</a><a href="{BASE}/dataset.html">Dataset</a><a href="https://research.cairnvault.app/digital-legacy-answers/">Answers</a><a href="https://github.com/cairnvault/digital-legacy-teardown">GitHub</a><a href="https://cairnvault.app">CairnVault</a></nav>
</div></header>
<div class="wrap">
<article>
<h1>The digital legacy provider comparison, as an open dataset</h1>

<p class="lede">{len(d['records'])} providers — every major password manager, every big-platform
legacy-contact feature, and the dedicated digital-legacy services — scored on the only two
questions that decide whether any of this works. Machine-readable, CC&nbsp;BY&nbsp;4.0, and every
field carries the URL it was read from.</p>

<div class="cta">
  <h2>Download</h2>
  <p><a href="{BASE}/data/digital-legacy-comparison.json"><strong>JSON</strong></a> — full records with notes, sources and field definitions.<br>
     <a href="{BASE}/data/digital-legacy-comparison.csv"><strong>CSV</strong></a> — flat table, one row per provider.</p>
  <p>Version {d['version']}, last modified {d['dateModified']}. Reuse it under
     <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a>;
     attribution and a link back are all we ask.</p>
</div>

<h2>The two questions</h2>

<p><strong>Does the provider actually verify that you died</strong> — or does it just notice that
you stopped logging in? And <strong>can the provider read your data?</strong> Almost every product
in this category answers one of these well and the other badly.</p>

<blockquote><p>{e(d['keyFinding'])}</p></blockquote>

<h2>The table</h2>

<p>This is generated from the JSON file above, so it cannot drift from it.
&ldquo;Unknown&rdquo; means we could not establish the field from a primary source and declined to
guess — it is not a euphemism for &ldquo;no&rdquo;.</p>

<div class="tablewrap">
<table>
<thead><tr>
<th>Provider</th><th>Category</th><th>What triggers release</th>
<th>Verifies death?</th><th>Provider can read your data?</th><th>Passwords included?</th><th>Status</th>
</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>

<h2>How to read &ldquo;provider can read your data&rdquo;</h2>

<p>The answer is <em>yes</em> whenever the provider holds the keys, and also whenever the provider
can grant a third party access — because access a company is able to grant is access that company
has. It is <em>scoped</em> where a vendor's inability-to-read claim is real but covers only some
fields. It is <em>no</em> only where encryption happens on the user's device and the provider never
receives the key.</p>

<h2>Method, and the conflict of interest</h2>

<p>{e(d['disclosure'])}</p>

<p>Every claim was read from the vendor's own live documentation and quoted verbatim where the
wording carries the weight. Roughly a third of the competitive claims we started with did not
survive that check and were retracted — including three that were in our own marketing. The
<a href="https://github.com/cairnvault/digital-legacy-teardown#corrections">dated correction log</a>
and the <a href="https://github.com/cairnvault/digital-legacy-teardown/issues">open verification
questions</a> are both public.</p>

<p><strong>{e(d['notLegalAdvice'])}</strong> Vendor terms change; re-verify before relying on any
of this. If a row is wrong, <a href="https://github.com/cairnvault/digital-legacy-teardown/issues/new">open
an issue</a> — corrections are published with dates, including corrections against us.</p>

</article>

<footer class="foot">
  <p>Published by <a href="https://cairnvault.app">CairnVault</a> under
     <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a> —
     republish it, quote it, correct it. Attribution and a link back are all we ask.</p>
  <p>The narrative version is <a href="{BASE}/">the teardown</a>; every source is listed on the
     <a href="{BASE}/sources.html">sources page</a>; plain answers to specific questions are in the
     <a href="https://research.cairnvault.app/digital-legacy-answers/">answer library</a>.</p>
  <p>Vendor terms change. Re-verify before relying on any of this. <strong>Not legal advice.</strong></p>
</footer>

<h2 id="cite">How to cite this dataset</h2>
<p>This dataset is archived on Zenodo, operated by CERN, and has a permanent DOI. The DOI resolves
   for good even if this site moves or disappears — which is the point of depositing it.</p>
<p><strong>DOI:</strong> <a href="{DOI_URL}" target="_blank" rel="noopener">{DOI}</a>
   · <strong>Zenodo record:</strong> <a href="{ZENODO_URL}" target="_blank" rel="noopener">zenodo.org/records/21894423</a></p>
<pre style="white-space:pre-wrap"><code>CairnVault Research (2026). Digital Legacy Provider Comparison (Version 1.0.0)
[Data set]. Zenodo. https://doi.org/{DOI}</code></pre>
<p>BibTeX:</p>
<pre style="white-space:pre-wrap"><code>@dataset{{cairnvault_2026_digital_legacy,
  author    = {{{{CairnVault Research}}}},
  title     = {{Digital Legacy Provider Comparison}},
  year      = {{2026}},
  version   = {{1.0.0}},
  publisher = {{Zenodo}},
  doi       = {{{DOI}}},
  url       = {{{DOI_URL}}}
}}</code></pre>
<p>Licensed <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC&nbsp;BY&nbsp;4.0</a>.
   You may republish, quote or correct it; attribution and a link back are all we ask.</p>
</div>
</body>
</html>
'''
(HERE/'docs'/'dataset.html').write_text(page, encoding='utf-8')
print(f'wrote docs/dataset.html ({len(page)} bytes) and regenerated the CSV from {len(d["records"])} records')

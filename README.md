# DLUX transit: research evidence

Companion evidence for *Exit level transit data integration for offline nonvisual journey planning on braille notetakers* (manuscript in preparation; not an accepted publication).

This repository is separate from the private product repository. It contains **preserved computational outputs and aggregation tools**, not the Android application, routing engine, server, SDK, or source transport databases.

## Run

Python 3.10 or later, standard library only. No network, API key, application checkout, or device is needed.

```sh
python -m unittest test_reproduce.py
python reproduce.py
```

The second command verifies the file manifest, recomputes comparisons from individual query records, compares every aggregate metric against preserved expectations, and writes Tables 6 and 7 as CSV under `generated/`. The same run checks the external-station-center and exploratory interaction comparisons. It fails on a changed file, duplicate query, differing query set, or mismatched aggregate.

## What this can and cannot reproduce

It reproduces **aggregation of recorded route outputs**. It does not rerun routing, reconstruct source geography, validate the correctness of the private engine, or establish that its records represent actual journeys. Hashes establish file integrity and equality of retained identities; they do not prove the scientific validity of the source computation. It does not reproduce every manuscript table: historical coverage, model-ranking comparisons, device measurements, and source-provider audits require separate evidence retained by the authors.

The evaluated application is version 66, source revision `3e7bb99`. The private revision is a provenance identifier, not a publicly resolvable code reference. Recorded computations comprise 60,000 main-condition records, 11,250 exploratory interaction records, and 9,000 external-center records. Main fixed comparisons use 2,250 queries; external-center comparisons use 1,800. The baseline also includes extra destinations. These are generated evaluation queries, not participant travel traces or a representative demand sample.

## Files and schema

- `results/main/`, `results/external/`: gzip JSON Lines, one recorded query per line. `candidates` preserves order; an empty list is failure to find a route in that condition.
- `query-design.json`: fixed/extra membership, region, direction/type, and stable query/target equality tokens. Endpoints and coordinates are withheld; these tokens cannot be submitted to the app to rerun the queries.
- `conditions.json`: original single-factor overrides. Other parameters remain fixed at the evaluated snapshot.
- `comparisons.json`: explicit reference/variant pairs. Spatial sensitivity uses reconstructed references; it is not compared indiscriminately with the original baseline.
- `expected.json`: preserved aggregates without lists of original query identifiers.
- `provenance.json`: original result-file SHA-256 values, source revisions, and exported record counts. The source files themselves are not included.
- `manifest.json`: SHA-256 for every distributed payload file except this self-referential manifest.
- `user-study/`: Korean-language protocol, scoring rules, task cards, answer key, planned allocation, draft information/consent, and **header-only** recording forms. This is a proposed single-condition study, not participant evidence. Ethics arrangements, recruitment, compensation, and data retention remain to be set by the investigator.

`queryDigest` is SHA-256 of the original UTF-8 query ID. `targetDigest` is the same transformation of its target. `keyDigest` is SHA-256 of the candidate key. `itineraryDigest` hashes the same key after each literal `station<TAB>exit<TAB>stop` link is replaced by `station<TAB>stop`. This preserves the original equality rule. It does not encode every intermediate subway station. Digests are deterministic equality tokens, not a claim of anonymization or encryption. `seconds` is a modeled cost, not observed travel time.

First-route and candidate-list differences are counted only for queries where both conditions find a route. `meanModelSecondsDelta` is variant minus reference; costs under different assumptions are not observed time savings. Candidate Jaccard uses the sets of full candidate keys. The interaction factors were selected after examining single-factor results and are exploratory.

## User study

Start with `user-study/protocol.md` and `user-study/author-decisions.md`. There are 20 cases and 74 supported tasks; six unsupported tasks were excluded. The questions and answer key concern what the fixed app output says, not current transport service or field walkability. No participant responses, personal contacts, or session recordings are distributed. The investigator's public professional contact in the draft form is not participant data.

The source-based task generator is retained privately because it reads full candidate narratives. The distributed task cards and answer key are fixed materials; this repository does not claim to regenerate them from its digest-only route records.

## OpenStreetMap-derived exit data (ODbL)

The DLUX Transit app stores its data in an encrypted form. As the Open Database License requires, the parts derived from OpenStreetMap are offered here as an unrestricted copy. They are published as a separate release asset, `dlux-transit-osm-exits-20261020.zip` (release `osm-exits-20261020`), and not in this repository tree. The archive holds, for each metropolitan region, the station exit positions, the links from exits to bus stops within 300 m, and the subway segment times estimated from exit distances where no timetable was available. The Daegu lines 1–3 exits come from the Daegu Transportation Corporation, not OpenStreetMap, so they are not included. Its `README.txt` gives the file formats, and `SHA256SUMS` gives a checksum for each file.

© OpenStreetMap contributors. This data is available under the Open Database License 1.0: https://opendatacommons.org/licenses/odbl/1-0/. The bus stop identifiers come from public data released by TAGO, the Seoul Metropolitan Government, and Gyeonggi Province. The release does not include the processing rules or the application.

앱에 담긴 자료 가운데 OpenStreetMap에서 나온 출구 자료는 위 릴리스에서 ODbL 1.0으로 무료로 내려받을 수 있습니다.

## Availability and citation

Public repository: https://github.com/AssistiveAILab/dlux-transit-research

Use a tagged version and its Git commit in citations. A repository release is not a DOI-backed preservation archive; no DOI is claimed. See `CITATION.cff`. For questions on evidence not distributed here, contact hyun.ka@kaist.ac.kr. Access to nonpublic code or third-party inputs is not promised and must be arranged separately if needed for review.

See `SOURCES.md` for attribution and excluded inputs, and `LICENSE` for the narrowly scoped reuse terms. This repository provides no real-time travel advice.

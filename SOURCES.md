# Sources, rights, and exclusions

This export includes authors' computational result metrics and equality digests, a newly separated aggregation script, and investigator-authored study materials. It does not redistribute the underlying route database, provider API responses, proprietary SDK, APK, or private implementation. A result digest cannot replace source-data access for an independent rerun.

## Attribution

The private evaluated dataset integrates the following sources. References identify provenance; their inclusion here does not imply that every source allows unrestricted redistribution.

| Source | Use in underlying research | Distribution in this package |
|---|---|---|
| OpenStreetMap contributors, https://www.openstreetmap.org/copyright; ODbL 1.0, https://opendatacommons.org/licenses/odbl/1-0/ | Station exits and a bounded pedestrian-data investigation | No coordinate extract, map, or derived route database; attribution applies to route-description excerpts in task materials |
| Seoul Metropolitan Government, https://data.seoul.go.kr/dataList/OA-1095/F/1/datasetView.do and https://data.seoul.go.kr/dataList/OA-15066/F/1/datasetView.do | Bus stops/routes and headways; source notices record Korea Open Government License Type 1 attribution | Names and brief generated guidance in task materials; no source files |
| Ministry of Land, Infrastructure and Transport, TAGO, https://www.data.go.kr/data/15098529/openapi.do | Bus routes, stops, headways | No raw response or credentials |
| Daegu Transportation Corporation, https://www.data.go.kr/data/15133918/fileData.do | Official station exit positions | No coordinate source file |
| GBIS, https://www.gbis.go.kr/ | Gyeonggi route/stop files | No source spreadsheet |
| Seoul Metro and regional operators | Subway topology, journey and transfer times, station information | No original files; source details remain in the study's data provenance |
| VWorld, https://www.vworld.kr/ | Auxiliary station/exit coordinate correspondence | No API responses, coordinates, or API key; exported comparison outputs contain only equality tokens and computed metrics |
| TMAP, https://tmapapi.tmapmobility.com/ | Additional exit correspondence evidence | No response, geometry, identifier listing, or API key |
| Seoul BIS, https://t-data.seoul.go.kr/dataprovide/trafficdataviewopenapi.do?data_id=1083 | Operational field-interpretation audit | No approved API URL, response, or operational records |

The original private result-file hashes are retained in `provenance.json`. Reacquiring a provider's current data does not guarantee the same snapshot. This package does not assert that API approval grants redistribution rights, or that hashing converts restricted raw data into an openly licensed database. No underlying geographic database is offered under the tools' license.

## Scope of reuse

`LICENSE` licenses only the new aggregation/test code under MIT and authors' documentation and study instruments under CC BY 4.0, to the extent of the authors' rights. Third-party facts and any independently applicable database rights retain their original terms. The product's all-rights-reserved notice is unaffected. No license to the private routing engine or application is granted.

Study materials are drafts for research preparation. They are not evidence of institutional approval or permission to recruit participants. No user-study results are included.

"""공개된 질의별 계산 결과로 비교 집계를 재현한다. 경로 엔진은 실행하지 않는다."""
import csv
import gzip
import hashlib
import json
from pathlib import Path
import statistics

HERE = Path(__file__).resolve().parent


def compare(a, b, ids):
    counts = dict.fromkeys(('queries', 'bothFound', 'baseOnly', 'variantOnly',
                           'neitherFound', 'firstKeyChanged',
                           'firstItineraryKeyChanged', 'candidateListChanged'), 0)
    deltas, overlaps = [], []
    for q in ids:
        x, y = a[q]['candidates'], b[q]['candidates']
        counts['queries'] += 1
        if not x or not y:
            counts['baseOnly' if x else 'variantOnly' if y else 'neitherFound'] += 1
            continue
        counts['bothFound'] += 1
        kx, ky = [v['keyDigest'] for v in x], [v['keyDigest'] for v in y]
        counts['firstKeyChanged'] += kx[0] != ky[0]
        counts['firstItineraryKeyChanged'] += x[0]['itineraryDigest'] != y[0]['itineraryDigest']
        counts['candidateListChanged'] += kx != ky
        deltas.append(y[0]['seconds'] - x[0]['seconds'])
        sx, sy = set(kx), set(ky)
        overlaps.append(len(sx & sy) / len(sx | sy))
    return {**counts, 'meanModelSecondsDelta': statistics.mean(deltas) if deltas else None,
            'meanCandidateJaccard': statistics.mean(overlaps) if overlaps else None}


def main():
    manifest = json.loads((HERE/'manifest.json').read_text('utf-8'))
    for name, expected in manifest['files'].items():
        path = HERE/name
        assert path.is_file(), name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    cache = {}
    def load(name):
        if name not in cache:
            with gzip.open(HERE/'results'/f'{name}.jsonl.gz', 'rt', encoding='utf-8') as f:
                rows = [json.loads(line) for line in f]
            cache[name] = {r['queryDigest']: r for r in rows}
            assert len(cache[name]) == len(rows), name
        return cache[name]
    expected = json.loads((HERE/'expected.json').read_text('utf-8'))
    comparisons = json.loads((HERE/'comparisons.json').read_text('utf-8'))
    actual = {}
    for name, spec in comparisons.items():
        a, b = load(spec['reference']), load(spec['variant'])
        ids = [q for q in a if a[q]['fixed']]
        assert set(ids) == {q for q in b if b[q]['fixed']}, name
        groups = expected[name].keys()
        actual[name] = {group: compare(a, b, [q for q in ids if group == 'all' or a[q]['region'] == group]) for group in groups}
        assert actual[name] == expected[name], name
    output = HERE/'generated'
    output.mkdir(exist_ok=True)
    (output/'comparisons.json').write_text(json.dumps(actual, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    for table, conditions in {'table6': ['center5','centerK','common-center-vs-common-exit'],
                              'table7': ['radius200','radius400','count3','count10','walk100','walk300','wait600','wait900','speed08','speed12','road11','road15','smooth','marginal','cap3600','uncapped']}.items():
        columns = ['bothFound','baseOnly','variantOnly','neitherFound','firstItineraryKeyChanged']
        with (output/f'{table}.csv').open('w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['condition', *columns])
            for name in conditions:
                writer.writerow([name, *[actual['main/'+name]['all'][c] for c in columns]])
    print(f'PASS: {len(comparisons)} comparisons; hashes and all preserved aggregate metrics match')
    print('This reproduces aggregation from preserved outputs, not route computation or user outcomes.')


if __name__ == '__main__':
    main()

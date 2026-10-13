"""빈 결과·순서·출구 식별자 제외·비용 집계의 독립 예제로 공개 도구를 검사한다."""
import unittest
from reproduce import compare


class ComparisonTests(unittest.TestCase):
    def test_denominators_and_identity(self):
        def record(key, itinerary, seconds):
            return {'keyDigest':key, 'itineraryDigest':itinerary, 'seconds':seconds}
        a = {'a':{'candidates':[record('exit1','same',100)]}, 'b':{'candidates':[]},
             'c':{'candidates':[record('c','c',1)]}, 'd':{'candidates':[]}}
        b = {'a':{'candidates':[record('exit2','same',120)]}, 'b':{'candidates':[record('b','b',1)]},
             'c':{'candidates':[]}, 'd':{'candidates':[]}}
        r = compare(a,b,list(a))
        self.assertEqual([r[k] for k in ['queries','bothFound','baseOnly','variantOnly','neitherFound']], [4,1,1,1,1])
        self.assertEqual(r['firstKeyChanged'],1)
        self.assertEqual(r['firstItineraryKeyChanged'],0)
        self.assertEqual(r['meanModelSecondsDelta'],20)
        b['a']['candidates'][0]['itineraryDigest']='different'
        self.assertEqual(compare(a,b,list(a))['firstItineraryKeyChanged'],1)

    def test_empty(self):
        r = compare({'q':{'candidates':[]}}, {'q':{'candidates':[]}}, ['q'])
        self.assertIsNone(r['meanModelSecondsDelta'])
        self.assertIsNone(r['meanCandidateJaccard'])


if __name__ == '__main__':
    unittest.main()

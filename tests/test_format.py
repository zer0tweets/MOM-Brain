import testtools


class FormatTestCase(testtools.TestCase):

    def test_noop(self):
        self.assertEqual(2, 2)

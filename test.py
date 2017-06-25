import unittest
from compare import compare


class Test(unittest.TestCase):

    def test_primitives(self):
        self.assertTrue(compare('test1', 'test1'))
        self.assertFalse(compare('test1', 'test2'))
        self.assertFalse(compare('test2', 'test1'))

        self.assertTrue(compare(1, 1))
        self.assertFalse(compare(1, 2))
        self.assertFalse(compare(2, 1))

        self.assertTrue(compare(1.5, 1.5))
        self.assertFalse(compare(1.5, 2.5))
        self.assertFalse(compare(2.5, 1.5))

        self.assertTrue(compare(True, True))
        self.assertTrue(compare(False, False))
        self.assertFalse(compare(True, False))
        self.assertFalse(compare(False, True))

        self.assertFalse(compare('test1', 1))
        self.assertFalse(compare(1, 'test1'))
        self.assertFalse(compare('test1', True))
        self.assertFalse(compare(False, 'test1'))
        self.assertFalse(compare(1, 1.0))
        self.assertFalse(compare(1.0, 'test1'))
        self.assertFalse(compare(1.0, False))

        self.assertFalse(compare(None, None))

    def test_lists(self):
        self.assertTrue(compare(["test1", "test2", "test3"], ["test1", "test2", "test3"]))
        self.assertTrue(compare(["test1", "test2", "test3"], ["test1", "test3", "test2"]))
        self.assertFalse(compare(["test1", "test1", "test2"], ["test2", "test2", "test3"]))
        self.assertFalse(compare(['test1', 'test1', 'test2'], ['test2', 'test2', 'test3', 'test4']))
        self.assertFalse(compare(["test1", "test2", "test3"], ["test1", "test2", "test3", 'test4']))
        self.assertFalse(compare(["test1", "test2", "test3", 'test4'], ["test1", "test2", "test3"]))
        self.assertFalse(compare(["test1", "test2", "test3", 'test4'], ["test1", "test2", "test3", "test5"]))

        self.assertTrue(compare(['test1', 1, 1.0], ['test1', 1, 1.0]))
        self.assertTrue(compare(['test1', 1, 1.0], [1, 'test1', 1.0]))

        self.assertTrue(compare(['test1', True, 1], [1, 'test1', True]))

        self.assertTrue(compare(['test1', 1, False], [1, 'test1', False]))
        self.assertFalse(compare(['test1', 1, 1.0], [1, 'test1', False]))

    def test_dicts(self):
        self.assertTrue(compare({'test1': 'val1', 'test2': 'val2'}, {'test1': 'val1', 'test2': 'val2'}))
        self.assertTrue(compare({'test1': 'val1', 'test2': 'val2'}, {'test2': 'val2', 'test1': 'val1'}))
        self.assertTrue(compare({'test1': 'val1', 'test2': 2}, {'test1': 'val1', 'test2': 2}))
        self.assertTrue(compare({'test2': 2, 'test1': 'val1'}, {'test1': 'val1', 'test2': 2}))

        self.assertFalse(compare({'test2': 2, 'test1': 'val1'}, {'test1': 'val1', 'test2': 22}))

        self.assertTrue(compare({'test1': ['test11', 'test12', 'test13'], 'test2': 2},
                                {'test2': 2, 'test1': ['test11', 'test12', 'test13']}))

        self.assertTrue(compare({'test1': ['test11', 'test12', 'test13'], 'test2': 2},
                                {'test1': ['test11', 'test12', 'test13'], 'test2': 2}))

        complex1 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test31': 33,
                'test32': [3, 1, 2],
                'test33': {
                    'test333': 1,
                    'test334': 'val334'
                }
            }
        }

        complex2 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test33': {
                    'test334': 'val334',
                    'test333': 1
                },
                'test31': 33,
                'test32': [1, 2, 3],
            }
        }

        self.assertTrue(compare(complex1, complex2))

        complex3 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test31': 33,
                'test32': [3, 1, 2, 5],
                'test33': {
                    'test333': 1,
                    'test334': 'val3343'
                }
            }
        }

        complex4 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test33': {
                    'test334': 'val334',
                    'test333': 1
                },
                'test31': 33,
                'test32': [1, 3]
            }
        }

        self.assertFalse(compare(complex3, complex4))

        complex5 = {
            'test1': 1,
            'test2': 2,
            'test3': {
                'test31': 33,
                'test32': [3, 1, 2],
                'test33': {
                    'test333': 1,
                    'test334': 'val334'
                }
            }
        }

        complex6 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test33': {
                    'test334': 'val334',
                    'test333': 1
                },
                'test31': 33,
                'test32': [1, 3, 2]
            }
        }

        self.assertFalse(compare(complex5, complex6))

        complex7 = {
            'test2': 2,
            'test3': {
                'test31': 33,
                'test32': [3, 1, 2],
                'test33': {
                    'test333': 1,
                    'test334': 'val334'
                }
            }
        }

        complex8 = {
            'test1': ['test11', 'test12', 'test13'],
            'test2': 2,
            'test3': {
                'test33': {
                    'test334': 'val334',
                    'test333': 1
                },
                'test31': 33,
                'test32': [1, 3, 2]
            }
        }

        self.assertFalse(compare(complex7, complex8))

    def test_diff_types(self):
        self.assertTrue(compare([], []))
        self.assertTrue(compare({}, {}))

        self.assertFalse([], {})
        self.assertFalse({}, [])

if __name__ == '__main__':
    unittest.main()

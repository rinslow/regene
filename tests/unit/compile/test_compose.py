from unittest import TestCase

from regene.compile.compose import Peeler
from regene.compile.regular_expression import RegularExpression


class PeelerTest(TestCase):
    def test_no_hierarchy(self):
        assert list(Peeler(RegularExpression("abc+"))) == ["abc", "+"]

    def def_test_single_hierarchy(self):
        assert list(Peeler(RegularExpression("(abc)"))) == ["(abc)"]

    def test_hierarchies_one_after_another(self):
        assert list(Peeler(RegularExpression("(abc)(abc)"))) == ["(abc)",
                                                                 "(abc)"]

    def test_hierarchies_of_same_level(self):
        assert list(Peeler(RegularExpression("(abc)d(efg)"))) == ["(abc)",
                                                                  "d",
                                                                  "(efg)"]

    def test_hierarchies_of_same_level_when_group_content_is_equal(self):
        assert list(Peeler(RegularExpression("(abc)f(abc)"))) == ["(abc)",
                                                                  "f",
                                                                  "(abc)"]

    def test_hierarchies_of_same_level_of_different_types_of_braces(self):
        assert (list(Peeler(
            RegularExpression("(abc)[0-9A-Zf]{6,}"))) == ["(abc)",
                                                          "[0-9A-Zf]",
                                                          "{6,}"])

    def test_nested_hierarchies(self):
        assert list(Peeler(RegularExpression("((abc))"))) == ["((abc))"]

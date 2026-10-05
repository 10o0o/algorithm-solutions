"""Agent-authored regression checks; passing does not establish learner mastery."""

from __future__ import annotations

import contextlib
import io
import random
import runpy
import unittest
from pathlib import Path


class SegtreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Preserve the learner's script and capture its existing demonstration.
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            namespace = runpy.run_path(str(Path(__file__).resolve().parents[1] / "segtree.py"))
        cls.segtree_type = namespace["Segtree"]

    def test_singleton_and_repeated_assignment(self) -> None:
        tree = self.segtree_type([7])
        self.assertEqual(tree.query(0, 0), 7)
        for value in (3, -4, 0, 10**30):
            tree.update(0, value)
            self.assertEqual(tree.query(0, 0), value)

    def test_non_power_of_two_boundaries(self) -> None:
        values = [5, 2, 7, 1, 4]
        tree = self.segtree_type(values)
        for left in range(len(values)):
            for right in range(left, len(values)):
                self.assertEqual(tree.query(left, right), min(values[left : right + 1]))
        tree.update(0, -5)
        tree.update(4, -9)
        self.assertEqual(tree.query(0, 0), -5)
        self.assertEqual(tree.query(4, 4), -9)
        self.assertEqual(tree.query(0, 4), -9)
        self.assertEqual(tree.query(1, 3), 1)

    def test_instances_do_not_share_state(self) -> None:
        first = self.segtree_type([2, 3])
        second = self.segtree_type([-2, 0, 5])
        first.update(1, -10)
        self.assertEqual(first.query(0, 1), -10)
        self.assertEqual(second.query(0, 2), -2)

    def test_seeded_operations_match_direct_min(self) -> None:
        rng = random.Random(20261005)
        for size in (1, 2, 3, 5, 8, 9, 17, 32, 33):
            values = [rng.randint(-100, 100) for _ in range(size)]
            tree = self.segtree_type(values)
            for _ in range(80):
                index, value = rng.randrange(size), rng.randint(-100, 100)
                tree.update(index, value)
                values[index] = value
                left, right = sorted((rng.randrange(size), rng.randrange(size)))
                self.assertEqual(tree.query(left, right), min(values[left : right + 1]))
                self.assertEqual(tree.query(0, size - 1), min(values))


if __name__ == "__main__":
    unittest.main()

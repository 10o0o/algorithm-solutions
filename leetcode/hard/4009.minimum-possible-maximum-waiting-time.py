#
# @lc app=leetcode id=4009 lang=python3
#
# [4009] Minimum Possible Maximum Waiting Time
#

# @lc code=start


class Solution:
    def minMaxWaitingTime(self, demand: list[int], fuel: list[int]) -> int:
        states = {(0, 0, 0): 0}
        total_used = 0

        for i, need in enumerate(demand):
            next_states = {}

            for (used0, busy0, busy1), max_wait in states.items():
                used1 = total_used - used0

                remain0 = fuel[0] - used0
                remain1 = fuel[1] - used1

                if remain0 >= need:
                    wait = busy0

                    new_state = (
                        used0 + need,
                        need,
                        max(0, busy1 - wait),
                    )
                    new_max_wait = max(max_wait, wait)

                    next_states[new_state] = min(
                        next_states.get(new_state, float("inf")), new_max_wait
                    )

                if remain1 >= need:
                    wait = busy1

                    new_state = (
                        used0,
                        max(0, busy0 - wait),
                        need,
                    )
                    new_max_wait = max(max_wait, wait)

                    next_states[new_state] = min(
                        next_states.get(new_state, float("inf")),
                        new_max_wait,
                    )

            if not next_states:
                if i == 0:
                    return -1

                return min(states.values())

            states = next_states
            total_used += need

        return min(states.values())


# @lc code=end

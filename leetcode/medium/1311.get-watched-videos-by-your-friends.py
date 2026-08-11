#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#

# @lc code=start
class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: list[list[str]],
        friends: list[list[int]],
        id: int,
        level: int,
    ) -> list[str]:
        cur_level = 0
        cur_list = [id]
        visited = {id}

        while cur_level != level:
            nxt_list = []

            for cur_id in cur_list:
                nxt_friends = friends[cur_id]

                for nxt_friend in nxt_friends:
                    if nxt_friend in visited:
                        continue

                    visited.add(nxt_friend)
                    nxt_list.append(nxt_friend)

            cur_level += 1
            cur_list = nxt_list

        video_count = {}

        for friend_id in cur_list:
            for video in watchedVideos[friend_id]:
                video_count[video] = video_count.get(video, 0) + 1

        return sorted(video_count, key=lambda video: (video_count[video], video))


# @lc code=end

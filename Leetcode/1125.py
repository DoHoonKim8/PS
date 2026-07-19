from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # (state key) -> (people subset)
        dp = {}
        people_to_req_skills = {}
        for i in range(len(people)):
            person_skills = set(people[i]) & set(req_skills)
            mask = 0
            for skill in person_skills:
                mask |= (1 << req_skills.index(skill))
            people_to_req_skills[i] = mask

        dp[0] = set()
        for mask in range(1 << len(req_skills)):
            if mask not in dp:
                continue
            for i in range(len(people)):
                if i in dp[mask]:
                    continue
                added_mask = people_to_req_skills[i]
                new_mask = mask | added_mask
                if new_mask not in dp or len(dp[new_mask]) > len(dp[mask]) + 1:
                    dp[new_mask] = dp[mask].copy()
                    dp[new_mask].add(i)
        return list(dp[(1 << len(req_skills)) - 1])

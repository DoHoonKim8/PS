from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = dict()

    def add(self, emails):
        for email in emails:
            if email not in self.parent:
                self.parent[email] = emails[0]
            else:
                self.union(email, emails[0])

    def find(self, email):
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        self.parent[rb] = ra

    def merged_emails(self):
        merged = defaultdict(list)
        for email, parent in self.parent.items():
            merged[self.find(parent)].append(email)
        return merged

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merged = UnionFind()
        names = dict()
        for account in accounts:
            names[account[1]] = account[0]
            merged.add(account[1:])
        merged_emails = merged.merged_emails()
        result = []
        for parent, emails in merged_emails.items():
            res = []
            res.append(names[parent])
            res.extend(sorted(emails))
            result.append(res)
        return result

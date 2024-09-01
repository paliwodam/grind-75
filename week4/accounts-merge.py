# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

from typing import List
from collections import defaultdict

class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def DFS(mail, edges, visited, mail_group):
            visited[mail] = True
            mail_group.append(mail)

            for neigh in edges[mail]:
                if not visited[neigh]:
                    DFS(neigh, edges, visited, mail_group)
            return mail_group

        accounts_dict = defaultdict(list)
        for account in accounts:
            name, *emails = account
            accounts_dict[name].append(emails)

        result = []
        for name, accounts in accounts_dict.items():
            edges = defaultdict(list)
            for mails in accounts:
                for mail in mails:
                    edges[mail].extend(other_mail for other_mail in mails if mail != other_mail)
            
            visited = {mail: False for mail in edges.keys()}

            for mail in edges.keys():
                if not visited[mail]:
                    mail_group = sorted(DFS(mail, edges, visited, []))
                    result.append([name] + mail_group)

        return result
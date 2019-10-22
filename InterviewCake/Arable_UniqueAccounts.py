import unittest



def unique_accounts(accounts):

    distinct_accounts = {}
    for account in accounts:
        name = account[0]
        if name in distinct_accounts:
            emails = distinct_accounts.get(name)
            for email_set in emails:
                if email_set.intersection(account[1:]):
                    email_set.update(account[1:])
                    break
                else:
                    emails.append(set(account[1:]))
                    break
        else:
            emails = []
            emails.append(set(account[1:]))
            distinct_accounts[name] = emails
    accounts = []
    for name in distinct_accounts:
        for email_set in distinct_accounts[name]:
            details = [name]
            details.extend(sorted(email_set))
            accounts.append(details)
    print(accounts)
    return accounts

class TestCase(unittest.TestCase):
    def test1(self):
        accounts = [
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        expected = [
            ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
        self.assertEqual(unique_accounts(accounts), expected)
    def test2(self):

        accounts = [
            ["David", "David0@m.co", "David1@m.co"],
            ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"],
            ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"]
        ]
        expected = [
            ["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]
        ]
        self.assertEqual(unique_accounts(accounts), expected)

if __name__ == "__main__":
    unittest.main()



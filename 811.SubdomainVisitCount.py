"""
A website domain like "discuss.leetcode.com"
consists of various subdomains. At the top level, we have "com",
at the next level, we have "leetcode.com", and at the lowest level,
"discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of
visits this domain received), followed by a space, followed by the address.
An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like
a list of count-paired domains, (in the same format as the input,
and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input:
["9001 discuss.leetcode.com"]
Output:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation:
We only have one website domain: "discuss.leetcode.com". As discussed above,
the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and
"wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times,
"com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

The length of cpdomains will not exceed 100.
The length of each domain name will not exceed 100.
Each address will have either 1 or 2 "." characters.
The input count in any count-paired domain will not exceed 10000.
The answer output can be returned in any order.

"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if cpdomains == []:
            return []
        else:
            domains = []
            for i in range(len(cpdomains)):
                d_  = Domain(cpdomains[i])
                domains.append(d_)
                temp = self.parse(d_)
                domains.extend(self.parse(d_))

            ret_dom =[]
            ret_dom.append(domains[0])
            for i in range(1,len(domains)):
                for j in range(len(ret_dom)):
                    if domains[i].domain == ret_dom[j].domain:
                        ret_dom[j].num +=domains[i].num
                        break
                    if j == len(ret_dom)-1:
                        ret_dom.append(domains[i])
            ret = []
            for i in range(len(ret_dom)):
                ret.append(str(ret_dom[i].num) + ' ' + ret_dom[i].domain)
        return ret

    def parse(self, domain_):
        ret =[]
        for i in range(len(domain_.d_parts)-1):
            str_ = ""
            for j in range(i+1,len(domain_.d_parts)-1):
                str_ = str_ + domain_.d_parts[j] + '.'
            str_ = str_ + domain_.d_parts[-1] #add the last
            str_ = str(domain_.num) + " " + str_
            d_ = Domain(str_)
            ret.append(d_)
        return ret


class Domain:
    def __init__(self,domain_):
        try:
            self.num = int(domain_.split(' ')[0])
            self.domain = domain_.split(' ')[1]
            self.d_parts = self.domain.split('.')

        except:
            self.num = -1
            self.domain  = ""
            self.d_parts = []

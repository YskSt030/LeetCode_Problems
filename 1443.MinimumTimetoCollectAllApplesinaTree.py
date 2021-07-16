"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, 
which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. 
Return the minimum time in seconds you have to spend in order to collect all apples 
in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] 
means that exists an edge connecting the vertices fromi and toi. Additionally, 
there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, 
otherwise, it does not have any apple.

 

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. 
One optimal path to collect all apples is shown by the green arrows.  

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. 
One optimal path to collect all apples is shown by the green arrows.  

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Constraints:

1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
"""
Info = collections.namedtuple('Info', ('found', 'dist'))
print(Info)
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        # build an adjacency list to represent the tree using `edges`
        tree = collections.defaultdict(list)
        print(tree)
		# You don't need to make it undirected since the structure represents a tree
        for u, v in edges:
            tree[u].append(v)
        print(tree)
        # A recursive helper function that find the lowest apple and passes
        # the information (is apple found, distance from the lowest apple to the current node)
        # to the upper node
        
        def traverse(node):
            if node not in tree:
                return Info(hasApple[node], 0)
            curr_dist, apple_found = 0, hasApple[node]
            for child in tree[node]:
                info = traverse(child)
                curr_dist += 2 + info.dist if info.found else 0
                apple_found |= info.found
            fin_dist = curr_dist + 2 if apple_found else curr_dist
            return Info(apple_found, curr_dist)
        
        # Get the information from the starting vertex 0
        return traverse(0).dist
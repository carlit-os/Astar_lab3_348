import common


def find_end(atlas):
    for rdx, row in enumerate(atlas):
        for cdx, num in enumerate(row):
            if num == 3:
                result = Node(rdx, cdx)
                return result


def index(node, atlas):  # indexes a node in atlas
    return atlas[node.x][node.y]


def nodeDepth(child, adult, parent):
    parentDepth = index(adult, parent)[2]  # previous depth
    return parentDepth + 1

    pass


def astar_search(atlas):
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1
    found = False
    frontier = []
    parent = [[0 for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
    start_node = find_start(atlas, parent)  # marks node with 5/breadcrumb and sets parent depth to 0
    end_node = find_end(atlas)  # returns end obj

    mazeStats = SearchStats(start_node, end_node)

    while not mazeStats.isclosed() and index(mazeStats.getCurr(),
                                             atlas) != 3:  # atlas[node.x][node.y] \\\\ index(mazeStats.getCurr(),
        # atlas) != 3
        mazeStats.deepen()
        for child in expand(mazeStats.getCurr(), atlas):
            frontier.append((mazeStats.fn(child, mazeStats.getCurr(), parent), child))  # place child in frontier

            parent[child.x][child.y] = [mazeStats.getCurr().x, mazeStats.getCurr().y,
                                        nodeDepth(child, mazeStats.getCurr(),
                                                  parent)]  # adds back trace to parent array
        # frontier.sort()  # sort according to f(n)
        if frontier.__len__() == 0:
            break

        frontier.sort(key=lambda tup: (tup[0], tup[1].y, tup[1].x))

        mazeStats.close(mazeStats.getCurr())  # add curr node to close
        atlas[mazeStats.getCurr().x][mazeStats.getCurr().y] = 4  # mark with 4, consider combining
        frontier.sort(key=lambda tup: (tup[0], tup[1].y, tup[1].x))
        mazeStats.setCurr(frontier.pop(0)[1])  # set curr node to next kid

    # performs back trace if possible
    if index(mazeStats.getCurr(), atlas) == 3:

        # while len(frontier) != 0:
        #    drain = frontier.pop()[1]
        #    atlas[drain.x][drain.y] = 4

        atlas[mazeStats.getCurr().x][mazeStats.getCurr().y] = 5
        trace(mazeStats.getCurr(), parent, atlas)
        return True  # consider editing the value of found here

    return found


# object def for a spot in the maze
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def manhattan(currNode, endNode):  # calculates manhattan distance for a given node

    return abs(currNode.x - endNode.x) + abs(currNode.y - endNode.y)


# object def for search stats
class SearchStats:
    def __init__(self, currNode, endNode):
        self.currNode = currNode
        self.endNode = endNode
        self.closed = set()
        self.depth = 0

    def deepen(self):
        self.depth += 1  # increments the depth

    def close(self, shutNode):  # closes a node
        self.closed.add(shutNode)

    def isclosed(self):  # checks if currNode is in closed
        return self.currNode in self.closed

    def traversed(self):  # counts up expanded nodes
        return len(self.closed) + 1

    def newVisit(self, newNode):  # adds to set of expanded nodes
        self.closed.add(newNode)

    def fn(self, probe, adult, parent):  # returns f(n) for a given node
        return parent[adult.x][adult.y][2] + manhattan(probe, self.endNode)

    def getCurr(self):
        return self.currNode

    def setCurr(self, freshNode):
        self.currNode = freshNode

    def getDepth(self):
        return self.depth


def find_start(atlas, parent):  # finds start node, adds to frontier, marks with 5
    for rdx, row in enumerate(atlas):
        for cdx, num in enumerate(row):
            if num == 2:
                result = Node(rdx, cdx)

                atlas[result.x][result.y] = 5

                parent[rdx][cdx] = [None, None, 0]
                return result


def in_range(x, y):  # checks if node is inside of the atlas
    return 0 <= x <= (common.constants.MAP_HEIGHT - 1) and 0 <= y <= (common.constants.MAP_WIDTH - 1)


def trace(curr_node, parent, atlas):
    # curr_node is the goal node

    while parent[curr_node.x][curr_node.y][2] != 0:  # while we haven't gotten back to start

        parentx = parent[curr_node.x][curr_node.y][0]  # previous coordinates
        parenty = parent[curr_node.x][curr_node.y][1]

        atlas[parentx][parenty] = 5  # breadtrail of correct path
        curr_node = Node(parentx, parenty)


def expand(curr_node, atlas):  # returns a list of 0 nodes counterclockwise from right of curr
    # print("indexing atlas[%d][%d]" % (curr_node.x, curr_node.y))
    candidates = []

    curr_node.x = curr_node.x - 1
    candidates.append([curr_node.x, curr_node.y])  # space above of currnode
    # print("checking right")
    # print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y - 1
    curr_node.x = curr_node.x + 1  # space left of currnode
    candidates.append([curr_node.x, curr_node.y])
    # print("checking above")
    # print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y + 1
    curr_node.x = curr_node.x + 1
    candidates.append([curr_node.x, curr_node.y])  # space below currnode
    # print("checking left")
    # print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.x = curr_node.x - 1
    curr_node.y = curr_node.y + 1  # space right of currnode
    candidates.append([curr_node.x, curr_node.y])
    # ("checking right")
    # print("indexed atlas[%d][%d]" % (curr_node.x, curr_node.y))

    curr_node.y = curr_node.y - 1  # set currnode back where it belongs
    # print("left currnode at atlas[%d][%d]" % (curr_node.x, curr_node.y))

    # ("candidates are")
    # print(candidates)
    viable = list(filter(
        lambda candidate: in_range(candidate[0], candidate[1]) and (atlas[candidate[0]][candidate[1]] == 0 or
                                                                    atlas[candidate[0]][candidate[1]] == 3),
        candidates))

    # print("we're left with")
    # print(viable)

    return list(map(lambda candidate: Node(candidate[0], candidate[1]), viable))

class Node(object):
    def __init__(self, mx, my, cx, cy, m_round):
        self.mx = mx
        self.my = my
        self.cx = cx
        self.cy = cy
        self.m_round = m_round
        self.out_d = 0
        self.g = set()
        self.win_state = None


class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    continue
                if grid[i][j] == 'C':
                    cx = i
                    cy = j
                elif grid[i][j] == 'M':
                    mx = i
                    my = j
                elif grid[i][j] == 'F':
                    fx = i
                    fy = j

        cnt = 0
        node_dict = {}
        for x1 in range(m):
            for y1 in range(n):
                if grid[x1][y1] == '#':  # 必须是合法单元格
                    continue
                for x2 in range(m):
                    for y2 in range(n):
                        if grid[x2][y2] == '#':
                            continue
                        if x1 == fx and y1 == fy and x2 == fx and y2 == fy:  # 不会同时出现在食物所在的位置
                            continue

                        if x1 == fx and y1 == fy:  # 老鼠在上一次操作之后到达了食物，因此只需要记录轮到猫行动的这个状态
                            node_dict[(x1, y1, x2, y2, 0)] = Node(x1, y1, x2, y2, 0)
                        elif x2 == fx and y2 == fy:  # 猫在上一次操作之后到达了食物，因此只需要记录轮到老鼠行动的这个状态
                            node_dict[(x1, y1, x2, y2, 1)] = Node(x1, y1, x2, y2, 1)
                        elif x1 == x2 and y1 == y2:  # 猫在上一操作之后抓到了老鼠，因此只需要记录轮到老鼠行动的这个状态
                            node_dict[(x1, y1, x2, y2, 1)] = Node(x1, y1, x2, y2, 1)
                        else:
                            node_dict[(x1, y1, x2, y2, 0)] = Node(x1, y1, x2, y2, 0)
                            node_dict[(x1, y1, x2, y2, 1)] = Node(x1, y1, x2, y2, 1)

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # 预处理pre_state以及out_d
        for node in node_dict.values():
            if node.mx == fx and node.my == fy:  # 无需考察老鼠吃到食物的下一个状态
                continue
            if node.cx == fx and node.cy == fy:  # 无需考察猫吃到食物的下一个状态
                continue
            if node.mx == node.cx and node.my == node.cy:  # 无需考察猫逮到老鼠的下一个状态
                continue

            if node.m_round == 1:
                step_range = mouseJump
                nowx, nowy = node.mx, node.my
            else:
                step_range = catJump
                nowx, nowy = node.cx, node.cy

            for index in range(4):
                for l in range(1, step_range + 1):
                    x = dx[index] * l + nowx
                    y = dy[index] * l + nowy

                    if x < 0 or x == m or y < 0 or y == n or grid[x][y] == '#':
                        break
                    if node.m_round == 1:
                        if x == node.cx and y == node.cy:  # 当前是老鼠行动，老鼠不可能走到猫所在的位置
                            continue
                        next_node = node_dict[(x, y, node.cx, node.cy, 0)]
                    else:
                        next_node = node_dict[(node.mx, node.my, x, y, 1)]

                    node.out_d += 1
                    next_node.g.add(node)

            node.out_d += 1

            node_dict[(node.mx, node.my, node.cx, node.cy, 1 - node.m_round)].g.add(node)

        q = []
        for node in node_dict.values():
            if (node.mx == fx and node.my == fy) or (node.cx == fx and node.cy == fy) or (
                    node.mx == node.cx and node.my == node.cy):  # 三种终局状态均设置为必败
                node.win_state = False
                q.append(node)

        l = 0
        r = len(q)
        round = 0
        while l < r and round < 1000:
            round += 1
            for node in q[l: r]:
                if not node.win_state:  # 当前状态必败，那么上一个状态必胜
                    for pre_node in node.g:
                        if pre_node.win_state is None:
                            pre_node.win_state = True
                            q.append(pre_node)
                else:
                    for pre_node in node.g:
                        pre_node.out_d -= 1
                        if pre_node.out_d == 0:  # 所有可到达的状态都是必胜，那么必败
                            pre_node.win_state = False
                            q.append(pre_node)

            l, r = r, len(q)

        if node_dict[(mx, my, cx, cy, 1)].win_state:
            return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.canMouseWin(["M.C...F"], 1, 4))

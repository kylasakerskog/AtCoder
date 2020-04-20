class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 各ノードをDFSで巡回しつつ、親ノードをdictionaryに保存していく
    def traverse(self, node, parents):
        if node is None:
            return parents
        if node.left is not None:
            parents[node.left] = node
            self.traverse(node.left, parents)
        if node.right is not None:
            parents[node.right] = node
            self.traverse(node.right, parents)

        return parents

    # ノードp, qのLCAを探索するメソッド
    def lowestCommonAncestor(self, root, p, q):
        # 各ノードをkey、その親をvalueに持つdictionaryを作成しておく
        parents = {root: None}
        parents = self.traverse(root, parents)

        # 一方のノード（ここではp）の祖先を保存しておくためのsetを用意する
        ancestors = set()
        # 自分自身がLCAになる可能性もあるため、まずは自身をセットする
        parent = p

        # pの親を辿っていき、祖先となるノードを全てsetに保存していく
        while parent is not None:
            ancestors.add(parent)
            parent = parents[parent]

        # 次にqから親を辿っていき、pの祖先とぶつかった時点でLCAとみなす
        node = q
        while node not in ancestors:
            node = parents[node]

        return node


N = int(input())
l = set()
for i in range(N):
    a, b = map(int,input().split())
    if l not in a:
        l.append(a)
        node = TreeNode(a)
    if node.left is None:
        a.left = TreeNode(b)
    else:
        a.right = TreeNode(b)


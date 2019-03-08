content = open("./alphabeta.txt", 'r').read()
str_nodes, str_edges = content.split()
# print(str_nodes, str_edges)


tree = {}
for item in str_nodes.strip('{()}').split('),('):
  name, kind = item.split(',')
  tree[name] = {'kind':kind}
  tree[name]['children'] = [] 
  tree[name]['has_child_node'] = True 
# print(tree)

for item in str_edges.strip('{()}').split('),('):
  a1, a2 = item.split(',')
  if a2.isdigit():
    tree[a1]['has_child_node'] = False  # if a node does not have child node, then 'children' attribute stores two value of leaf nodes
    tree[a1]['children'].append(float(a2)) 
    # tree[a1]['weight'] = int(a2)
  else:
    tree[a1]['children'].append(a2)
print(tree)


LeafNodesExamined = 0

def minimax(root='A', depth=float('inf'), alpha=-float('inf'), beta=float('inf')):
  node = tree[root]
  if depth == 0:
#     print("slkdfsklf")
    return -float('inf') if node['kind'] == 'MAX' else float('inf') 
  if node['has_child_node'] == False:
    global LeafNodesExamined
    LeafNodesExamined += 2
    return max(node['children']) if node['kind'] == 'MAX' else min(node['children']) 

  if node['kind'] == 'MAX':
    maxEval = -float('inf')
    for child in node['children']:
      Eval = minimax(child, depth-1, alpha, beta)
#       print(Eval, maxEval)
      maxEval = max(maxEval, Eval)
#       print(alpha, Eval)
      alpha = max(alpha, Eval)
      if beta <= alpha:
        break 
    return maxEval
  else:
    minEval = +float('inf') 
    for child in node['children']:
      Eval = minimax(child, depth-1, alpha, beta)
      minEval = min(minEval, Eval)
#       print(minEval, Eval)
      beta = min(minEval, Eval)
#       print(beta)
      beta = min(beta, Eval)
#       print(beta)
      if beta <= alpha:
        break
    return minEval 

minimax('A')
print(LeafNodesExamined)
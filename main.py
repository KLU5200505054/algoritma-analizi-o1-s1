def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if node.is_terminal_node():
        return node.get_node_value()

    if maximizing_player:
        v = float("-inf")
        for child_node in node.get_children_nodes():
            v = max(v, alpha_beta_pruning(child_node, alpha, beta, False))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = float("inf")
        for child_node in node.get_children_nodes():
            v = min(v, alpha_beta_pruning(child_node, alpha, beta, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v
def list_files(current_node, current_path=""):
    file_list = []
    for node in current_node:
        node_vals = current_node[node]
        if node_vals is None:
            file_list.append(current_path + "/" + node)
        else:
            file_list.extend(list_files(node_vals, current_path + "/" + node))
    return file_list

# my version
def list_files2(current_node, current_path=""):
    empty_list = []

    if current_node is None:
        return empty_list
    
    for node, value in current_node.items():
        if value == None:
            new_file_path = current_path + '/' +  node
            empty_list.append(new_file_path)
        else:
            empty_list.extend(list_files(current_node[node], f'{current_path}/{node}'))
    return empty_list
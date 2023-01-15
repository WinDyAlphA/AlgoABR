def delete_val(ABR, val):
    if not ABR:
        return None
    if val < ABR.val:
        ABR.left = delete_val(ABR.left, val)
    elif val > ABR.val:
        ABR.right = delete_val(ABR.right, val)
    else:
        if not ABR.left:
            return ABR.right
        if not ABR.right:
            return ABR.left
        min_val = find_min(ABR.right)
        ABR.val = min_val
        ABR.right = delete_val(ABR.right, min_val)
    return ABR

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current.val
def move_disks(n, from_tower, to_tower, aux_tower, sol):
    # base case
    if n == 1:
        sol.append("Move disk 1 from %s to %s"%(from_tower, to_tower))
        return sol
    else:
        # move n-1 disks to auxillary tower
        move_disks(n-1, from_tower, aux_tower, to_tower, sol)
        # move nth disk to final tower
        sol.append("Move disk %s from %s to %s"%(n, from_tower, to_tower))
        # move the n-1 disks from the auxillary to final tower
        move_disks(n-1, aux_tower, to_tower, from_tower,sol)
        # remember that sol is a list object, so you are passing
        # along its reference when you call the function recursively
        # and the recursive calls modify the original list
        return sol

a=move_disks(4,"A", "B", "C", [])
print(a)

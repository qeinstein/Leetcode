function isBalanced(root: TreeNode | null): boolean {
  function maxDepth(root: TreeNode | null): number {
    if (root === null) {
      return 0;
    }
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);
    return (left > right ? left : right) + 1;
  }

  if (root === null) {
    return true;
  }

  let leftDepth = maxDepth(root.left);
  let rightDepth = maxDepth(root.right);

  if (leftDepth > rightDepth) {
    if (leftDepth - rightDepth > 1) {
      return false;
    }
  } else {
    if (rightDepth - leftDepth > 1) {
      return false;
    }
  }

  return isBalanced(root.left) && isBalanced(root.right);
}
# Name:         Zhoushuai (Andrew) Wu
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Pset 5: Binary Search Tree
# Term:         Summer 2018


class TreeNode:

    def __init__(self, key, val = None, parent = None, \
        l_child = None, r_child = None):
        self.key = key
        self.val = val
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child


    def has_parent(self):
        return self.parent != None


    def has_l_child(self):
        return self.l_child != None


    def has_r_child(self):
        return self.r_child != None


    def replace_node_data(self, key, val, l_child = None, r_child = None):
        self.key = key
        self.val = vall
        self.l_child = l_child
        self.r_child = r_child
        if self.l_child != None:
            self.l_child.parent = self
        if sef.r_child != None:
            self.r_child.parent = self


class BinarySearchTree:

    def __init__(self, key = None, val = None):
        if key == None:
            self.root = None
        else:
            self.root = TreeNode(key, val)


    def insert_helper(self, key, val, current):
        if key <= current.key:
            if current.has_l_child():
                self.insert_helper(key, val, current.l_child)
            else:
                current.l_child = TreeNode(key, val, current)
        elif key > current.key:
            if current.has_r_child():
                self.insert_helper(key, val, current.r_child)
            else:
                current.r_child = TreeNode(key, val, current) 


    def insert(self, key, val):
        if self.root == None:
            self.root = TreeNode(key, val)
        else:
            self.insert_helper(key, val, self.root)
        

    def get(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current
        elif current.key < key:
            return self.get(current.r_child, key)
        elif current.key > key:
            return self.get(current.l_child, key)


    def remove_leaf(self, t_node):
        if t_node == t_node.parent.l_child:
            t_node.parent.l_child == None
        elif t_node == t_node.parent.r_child:
            t_node.parent.r_child =- None
   

    def find_succ(self, node):
        succ = None
        if node.r_child != None:
            succ  = node.r_child
            while succ.l_child != None:
                succ = succ.l_child
        else:
            if node.parent != None:
                if node.parent.l_child == node:
                    succ = self.parent
                else:
                    node.parent.r_child = None
                    succ = self.find_succ(node.parent)
                    node.parent.r_child = node
        return succ


    def splice_out(self, succ):
        if succ.l_child == None and succ.r_chil == None:
            if succ.parent.l_child == succ:
                succ.parent.l_child = None
            elif succ.parent.r_child == succ:
                succ.parent.r_child == None
        elif succ.l_child != None:
            if succ.parent.l_child == succ:
                succ.parent.l_child = succ.l_child
            else:
                succ.parent.r_child = succ.l_child
            succ.l_child.parent = succ.parent
        elif succ.r_child != None:
            if succ.parent.l_child == succ:
                succ.parent.l_child = succ.r_child
            else:
                succ.parent.r_child = succ.r_child
            succ.r_child.parent = succ.parent


    def remove_have_both_children(self, t_node):
        succ = find_succ(t_node)
        self.splice_out(succ)
        t_node.key == succ.key
        t_node.val = succ.val
        

    def remove_have_one_child_if(self, t_node):
        if t_node.parent.l_child == t_node:
            t_node.l_child.parent = t_node.parent
            t_node.parent.l_child = t_nodel_child
        elif t_node.parent.r_child == t_node:
            t_node.l_child.parent = t_node.parent
            t_node.parent.r_child = t_node.l_child
        else:
            t_node.replace_node_data(t_node.l_child.key, \
                t_node.l_child.val, t_node.l_child.l_child, \
                t_node.l_child.r_child) 


    def remove_have_one_child_else(self, t_node):
        if t_node.parent.l_child == t_node:
            t_node.r_child.parent = t_node.parent
            t_node.parent.l_child = t_noder_child
        elif t_node.parent.r_child == t_node:
            t_node.r_child.parent = t_node.parent
            t_node.parent.r_child = t_node.r_child
        else:
            t_node.replace_node_data(t_node.r_child.key, \
                t_node.r_child.val, t_node.r_child.l_child, \
                t_node.r_child.r_child) 


    def remove_have_one_child(self, t_node):
        if t_node.l_child != None:
            self.remove_have_one_child_if(t_node)
        else:
            self.remove_have_one_child_else(t_node)
        


    def remove(self, t_node):
        if t_node.l_child == None and t_node.r_child == None:  # target node is leave, no children, lonley AF
            self.remove_leaf(t_node)
        elif t_node.l_child != None and t_node.l_child != None:  # target node has both kids
            self.remove_have_both_children(t_node)
        else:  # single kid
            self.remove_have_one_child(t_node)


    def delete(self):
        if self.root.key == key:
            self.root == None
        elif self.root == None:
            t_node = self.get(key, self.root)
            if t_node != None:
                self.remove(t_node)
        

    
    def contains_helper(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return True
        elif node.key < key:
            return self.contains_helper(node.r_child, key)
        elif node.key > key:
            return self.contains_helper(node.l_child, key)


    def contains(self, key):
        node = self.root
        return self.contains_helper(node, key)


    def find_min(self):
        current = self.root
        while current.has_l_child():
            current = current.l_child
        return current

    
    def find_max(self):
        current = self.root
        while current.has_r_child():
            current = current.r_child
        return current


    def inorder_list(self):

        def inorder_helper(node):
            if node == None:
                return []
            lst_left = inorder_helper(node.l_child)
            lst_mid = [node.key]
            lst_right = inorder_helper(node.r_child)       
            return lst_left + lst_mid + lst_right

        return inorder_helper(self.root)


    def preorder_list(self):

        def preorder_helper(node):
            if node == None:
                return []
            lst_left = preorder_helper(node.l_child)
            lst_mid = [node.key]
            lst_right = preorder_helper(node.r_child)       
            return lst_mid + lst_left + lst_right

        return preorder_helper(self.root)


    def postorder_list(self):

        def postorder_helper(node):
            if node == None:
                return []
            lst_left =postorder_helper(node.l_child)
            lst_mid = [node.key]
            lst_right = postorder_helper(node.r_child)       
            return lst_left + lst_right + lst_mid

        return postorder_helper(self.root)











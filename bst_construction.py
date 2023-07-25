class BST:
    def __init__(self, val):
        self.val = val
        self.lc = None 
        self.rc = None     
     
    def insert(self, val): 
        cn = self 
        while True: 
            if val < cn.val:
                if cn.lc is None:
                    cn.lc = BST(val)
                    break
                else:
                    cn = cn.lc
            else:
                if cn.rc is None:
                    cn.rc = BST(val)
                    break
                else:
                    cn = cn.rc
        return self                                                    

    def contains(self, val):
        cn = self
        while cn is not None:
            if val < cn.val:
                cn = cn.lc
            elif val > cn.val:
                cn = cn.rc
            else:
                return True
        return False

    def remove(self, val, pn = None): 
        cn = self
        while cn is not None:
            if val < cn.val:
                pn = cn
                cn = cn.lc
            elif val > cn.val:
                pn = cn
                cn = cn.rc
            else: 
                if cn.lc is not None and cn.rc is not None:
                    cn.val = cn.rc.get_min_val() 
                    cn.rc.remove(cn.val, cn)
                elif pn is None:
                    if cn.lc is not None:
                        cn.val = cn.lc.val
                        cn.rc = cn.lc.rc
                        cn.lc = cn.lc.lc
                    elif cn.rc is not None:
                        cn.val = cn.rc.val
                        cn.lc = cn.rc.lc
                        cn.rc = cn.rc.rc
                    else:
                        cn.val = None
                elif pn.lc == cn:
                    pn.lc = cn.lc if cn.lc is not None else cn.rc
                elif pn.rc == cn:
                    pn.rc = cn.lc if cn.lc is not None else cn.rc
                break
        return self

    def get_min_val(self):
        cn = self
        while cn.lc is not None:
            cn = cn.lc
        return cn.val

bst = BST(50)
bst.insert(30)
bst.insert(70)
print(bst.contains(30))  # Should print True
print(bst.contains(40))  # Should print False
bst.remove(30)
print(bst.contains(30))  # Should print False

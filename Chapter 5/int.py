def compare(listsuper,listsub):
       stat=None
       for element in listsuper:
           if listsuper.count(element)==listsub.count(element):
              pass
           else:
              stat=False
       if stat==None:
           for element in listsub:
               if element in listsub and element in listsuper:
                   pass
               else:
                   stat=False
       if stat==None:
           stat=True
       return stat
print compare([2,3,3],[2, 2])
        

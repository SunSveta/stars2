
def set_(coll, path, value):
      tmp_coll = coll
      for i in path[:-1]:
          if i in tmp_coll:
             tmp_coll = tmp_coll[i]
          else:
             tmp_coll[i] = {}
             tmp_coll = tmp_coll[i]
      tmp_coll[path[-1]] = value

      return coll

def line_to_record(line):
      lst=line.split(',')
      lst[0],lst[2]=int(lst[0]),int(lst[2])
      lst[3]=float(lst[3])
      dct={
            "id": lst[0],
            "name": lst[1],
            "quantity": lst[2],
            "price": lst[3]
      }
      return dct

def record_to_line(dct):
      result=','.join(str(value) for value in dct.values())
      return result

def load_inventory(filename):
        lst=[]
        with open(filename,'r') as file:
                for line in file:
                    lst.append(line_to_record(line.strip()))
        return lst

def save_inventory(filename, lst):
        with open(filename, 'w') as file:
            for l in lst:
                file.write(record_to_line(l) + '\n')

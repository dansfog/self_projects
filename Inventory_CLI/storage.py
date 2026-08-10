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

def record_to_line(record):
      result=','.join(str(value) for value in record.values())
      return result

def load_inventory(filename):
        records=[]
        with open(filename,'r') as file:
                for line in file:
                    records.append(line_to_record(line.strip()))
        return records

def save_inventory(filename, records):
        with open(filename, 'w') as file:
            for record in records:
                file.write(record_to_line(record) + '\n')

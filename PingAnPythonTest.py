import unittest

# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

def reverseInput(input):
    list,dic,tmp=[],{},input.popitem()
    while(isinstance(tmp[1],dict)):
        list.append(tmp[0])
        tmp=tmp[1].popitem()
    list.append(tmp[0])
    list.append(tmp[1])
    dic[list[1]]=list[0]
    for i in range(2,len(list)):
        tmp={}
        tmp[list[i]]=dic
        dic=tmp
    return dic

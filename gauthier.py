
def update_iterations_count(change,iterations_count):
  if change==True:
    iterations_count+=1
    print(iterations_count)
  else:
    iterations_count=0
    print(iterations_count)
  return iterations_count

def stop_condition(iterations_count,limite):
  if iterations_count > limite:
    return 0
  else:
    return 1   

if __name__== '__main__':
  import random
  iterations_count=0
  for i in range(120):
    iterations_count= update_iterations_count(True, iterations_count)
    # bool(random.getrandbits(1))
    test = stop_condition(iterations_count,50)  
    if test == False:
      break
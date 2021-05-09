import math

def comparar(x,xk,eps):
  soma = 0
  zip_object = zip(x, xk)
  for list1_i, list2_i in zip_object:
    soma = soma + math.fabs(list1_i-list2_i)

  if (soma < eps):
    return True
  else:
    return False   


def gaussJacobi(A,b,maxiter,eps):
  n = len(b)
  sol = True
  x = b.copy()
  for i in list(range(1,n+1,1)):
    if (math.fabs(A[i-1][i-1]) > 0.0):
      x[i-1] = b[i-1]/A[i-1][i-1]
    else:
      sol = False
      break
  
  if (sol):
    #print("Iteração 0")
    #print("x = ",x)
    xk = x.copy()
    #maxiter = 10
    #eps     = 0.01
    iter    = 0
 
    while (iter < maxiter):
      iter = iter + 1
      for i in list(range(1,n+1,1)):
        s = 0
        for j in list(range(1,n+1,1)):
          if ((i-1) != (j-1)):
            s = s + A[i-1][j-1]*x[j-1]

        xk[i-1] = (1/A[i-1][i-1])*(b[i-1]-s)
     
      #print("Iteração: ",iter)
      #print("xk = ",xk)
      if comparar(x,xk,eps):
        x = xk.copy()
        break    
      x = xk.copy()
     
   
  return x


def main():
    
    r1 = 10
    r2 = 20
    r3 = 30
    r4 = 40
    r5 = 50
    r6 = 60
    r7 = 70
    r8 = 80
    A = [
      [r1+r2+r5, -r2, 0, -r5],
      [-r2, r2+r3+r4, -r4, 0],
      [0, -r4, r4+r6+r7, -r6],
      [-r5, 0, -r6, r5+r6+r8]
    ]

    v1 = -10
    v2 = 3
    v3 = 49
    v4 = 36

    b = [-v1, -v2, -v3, -v4]

    x = gaussJacobi(A,b, 20,0.01)

    i = 1
    for corrente in x:
      print("i",i,": ", corrente)
      i += 1

if __name__ == "__main__":
    main()
DEF ridders(F, xl, xr, errto=0.01, imax=1000):
     """
     Return the root of a function (Using the Ridder's Method)
 
     ridders(fun, xl, xr, imax, errto)
 
     * fun: Function where find the roots
     * xl: left bound of interval
     * xr: right bound of interval
     * imax: max of iterations allowed
     * errto: tolerated error
 
     Author: Pedro Garcia [sawp@sawp.com.br]
     License: Creative Commons
              <http ://creativecommons.org/licenses/by-nc-nd/2.5/br/>
     """
     x = 0
     iterCount = 0
     errno = 1     
 
     while errno > errto and iterCount < imax:          
          fr = F(xr)
          fl = F(xl)
          d0 = abs(fr - fl)
          x = xr - fr*(xl-xr)/(fl - fr)
          fx = F(x)
 
          a = (fl - fx)/(fx - fr)
          b = (fl - fx)/(fl - a*fx)
          beta = b - 1
          alfa = a - 1
          lnb = beta - beta*beta/2 + beta*beta*beta/3
          lna = alfa - alfa*alfa/2 + alfa*alfa*alfa/3
          root = xl + d0*lnb/lna
          froot = F(root)
 
          if fl * fx < 0:
               if xl < root and root < x:
                    if fx * froot < 0:
                         xl = root
                         xr = x
                    else:
                         xr = root
               else:
                    xr = x
          elif fl * fx > 0:
               if x < root and root < xr:
                    if fx * froot < 0:
                         xl = x
                         xr = root
                    else:
                         xl = root
                         fl = froot
               else:
                    xl = x
                    fl = fx
          else:
               if fl == 0:
                    x = xl
               break
 
          errno = abs(xr - xl)
          iterCount += 1
     return x
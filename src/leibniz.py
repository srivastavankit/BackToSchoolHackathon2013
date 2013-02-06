r=input
#exec'print"%.15f"%sum((-1.)**k/(2*k+1)for k in range(r()));'*r()
exec'print"%.15f"%sum(map(lambda k:(-1.)**k/(2*k+1),range(r())));'*r()


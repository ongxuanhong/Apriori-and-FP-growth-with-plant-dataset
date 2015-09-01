# Introduction
In this experiment, I will apply Apriori and FP-Growth method for association rule mining.

Blog: https://ongxuanhong.wordpress.com/2015/08/24/apriori-va-fp-growth-voi-tap-du-lieu-plants/

# Transform plants.data into binary format
* Each row is a plant.
* First column is Latin name (species or genus), the others are states distribution.
* Binary value (y/n). y means exist in this state, n means doesn't exist in this state.
* Save data in csv format: plants.csv

# Apriori results
Generated sets of large itemsets:

Size of set of large itemsets L(1): 49

Size of set of large itemsets L(2): 167

Size of set of large itemsets L(3): 120

Size of set of large itemsets L(4): 25

Size of set of large itemsets L(5): 2

Best rules found:

 1. ct=y ma=y nj=y 3562 ==> ny=y 3524    conf:(0.99)
 2. tn=y md=y nc=y 3531 ==> va=y 3489    conf:(0.99)
 3. ct=y pe=y nj=y 3618 ==> ny=y 3571    conf:(0.99)
 4. ga=y va=y al=y sc=y 3579 ==> nc=y 3529    conf:(0.99)
 5. ga=y va=y sc=y 3882 ==> nc=y 3825    conf:(0.99)
 6. ms=y al=y nc=y sc=y 3572 ==> ga=y 3519    conf:(0.99)
 7. nj=y ny=y oh=y 3556 ==> pe=y 3502    conf:(0.98)
 8. ct=y pe=y ma=y 3784 ==> ny=y 3726    conf:(0.98)
 9. pe=y ma=y nj=y 3699 ==> ny=y 3640    conf:(0.98)
10. ga=y md=y nc=y 3551 ==> va=y 3484    conf:(0.98)

# FP-Growth results
FPGrowth found 107 rules (displaying top 10)

 1. [ma=y, nj=y, ct=y]: 3562 ==> [ny=y]: 3524   <conf:(0.99)> lift:(5.96) lev:(0.08) conv:(76.17) 
 2. [nc=y, md=y, tn=y]: 3531 ==> [va=y]: 3489   <conf:(0.99)> lift:(6.1) lev:(0.08) conv:(68.81) 
 3. [pe=y, nj=y, ct=y]: 3618 ==> [ny=y]: 3571   <conf:(0.99)> lift:(5.95) lev:(0.09) conv:(62.86) 
 4. [ga=y, al=y, va=y, sc=y]: 3579 ==> [nc=y]: 3529   <conf:(0.99)> lift:(5.79) lev:(0.08) conv:(58.22) 
 5. [ga=y, va=y, sc=y]: 3882 ==> [nc=y]: 3825   <conf:(0.99)> lift:(5.78) lev:(0.09) conv:(55.53) 
 6. [nc=y, al=y, sc=y, ms=y]: 3572 ==> [ga=y]: 3519   <conf:(0.99)> lift:(5.77) lev:(0.08) conv:(54.85) 
 7. [ny=y, nj=y, oh=y]: 3556 ==> [pe=y]: 3502   <conf:(0.98)> lift:(6.21) lev:(0.08) conv:(54.4) 
 8. [pe=y, ma=y, ct=y]: 3784 ==> [ny=y]: 3726   <conf:(0.98)> lift:(5.93) lev:(0.09) conv:(53.49) 
 9. [pe=y, ma=y, nj=y]: 3699 ==> [ny=y]: 3640   <conf:(0.98)> lift:(5.93) lev:(0.09) conv:(51.42) 
10. [ga=y, nc=y, md=y]: 3551 ==> [va=y]: 3484   <conf:(0.98)> lift:(6.05) lev:(0.08) conv:(43.76) 


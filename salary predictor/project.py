import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
def gen_dict(sal):
    dect_sal={}
    c=0
    for i in np.unique(sal):
        dect_sal[i]=c
        c+=1
    return dect_sal
def con_bin(sal,sal_dict):
    l1=[]
    for i in sal:
        for j in sal_dict:
            if(str(i)==str(j)):
                l1.append(sal_dict[j])
    return l1
def get_value(in_w_cls,in_edu,in_ocp,in_ctry,w_cls_dict,edu_dict,ocp_dict,ctry_dict):
    a=int()
    b=int()
    c=int()
    d=int()
    for i in w_cls_dict:
        if(str(i).lstrip().rstrip()==in_w_cls):
            a=w_cls_dict[i]
            break
    for i in edu_dict:
        if(str(i).lstrip().rstrip()==in_edu):
            b=edu_dict[i]
            break
    for i in ocp_dict:
        if(str(i).lstrip().rstrip()==in_ocp):
            c=ocp_dict[i]
            break
    for i in ctry_dict:
        if(str(i).lstrip().rstrip()==in_ctry):
            c=ctry_dict[i]
            break
    return a,b,c,d
#-----------------------------------------
def prediction(a,b,c,d,e,f):
    dataset= pd.read_csv('adult.data.csv')
    age= dataset.iloc[:,0].values
    w_cls= dataset.iloc[:,1].values
    edu= dataset.iloc[:,3].values
    ocp= dataset.iloc[:,6].values
    w_hrs= dataset.iloc[:,12].values
    country=dataset.iloc[:,13].values
    sal=dataset.iloc[:,14].values
    #----------------------------------------
    num_age=pd.DataFrame(age)
    
    num_w_hrs=pd.DataFrame(w_hrs)
    
    w_cls_dict= gen_dict(w_cls)
    num_w_cls= pd.DataFrame(np.array(con_bin(w_cls,w_cls_dict)))
    
    edu_dict= gen_dict(edu)
    num_edu_dict=pd.DataFrame(np.array(con_bin(edu,edu_dict)))
    
    ocp_dict= gen_dict(ocp)
    num_ocp_dict=pd.DataFrame(np.array(con_bin(ocp,ocp_dict)))
    
    ctry_dict= gen_dict(country)
    num_ctry= pd.DataFrame(np.array(con_bin(country,ctry_dict)))
    
    sal_dict= gen_dict(sal)
    bool_sal= np.array(con_bin(sal,sal_dict))
    #----------------------------------------
    result=pd.concat([num_age,num_w_cls,num_edu_dict,num_ocp_dict,num_ctry,num_w_hrs],axis=1)
    X=result.iloc[:,[0,1,2,3,4,5]].values
    #------------------------------------------------------------------------------
    navby = GaussianNB()
    navby.fit(X,bool_sal)
    #------------------------------------------------------------------------------
    in_age=(a)#int(input("ENTER AGE: "))
    in_w_hrs=(b)#int(input('ENTER WORKING HOUR: '))
    in_w_cls=(c)#str(input('ENTER WORKING CLASS: '))
    in_edu=(d)#str(input('ENTER EDUCATION: '))
    in_ocp=(e)#str(input('ENTER OCCUPATION: '))
    in_ctry=(f)#str(input('ENTER COUNTRY: '))
    i=int(in_age)
    j=int(in_w_hrs)
    val1,val2,val3,val4=get_value(in_w_cls,in_edu,in_ocp,in_ctry,w_cls_dict,edu_dict,ocp_dict,ctry_dict)
    #------------------------------------------------------------------------------
    y_pred=navby.predict([[in_age,val1,val2,val3,val4,in_w_hrs]])
    
    c=str()
    for i in sal_dict:
        if(sal_dict[i]==y_pred):
            c=str('Your Salary\n Would be '+str(i))
            break
        else:
            continue
    return c
#!/usr/bin/env python
# coding: utf-8

# ## numpy examples

# In[4]:


import numpy as np
range(0,5)


# In[5]:


## numpy arange
np.arange(0,5)


# In[14]:


## numpy linspace
np.linspace(0,20,4)


# In[15]:


np.linspace(0,20,5)


# In[17]:


np.linspace(0,100,100)


# In[6]:


## numpy step size
np.arange(0,10,2)


# In[10]:


## numpy zeros
np.zeros((3,3))


# In[11]:


np.zeros(10)


# In[12]:


## numpy ones
np.ones(5)


# In[13]:


np.ones((6,6))


# In[19]:


## numpy random
np.random.randn(3)


# In[20]:


## tek bir int dondurmesini isterken kullanilir
x= np.random.randint(1,255)
print("x = ", x)

# In[21]:


## belirttigimiz araliklarda kac tane deger istiyorsak o zaman kullaniriz
y= np.random.randint(5,1023,34)
print(" y= ",y)

# In[ ]:


## numpy reshape(yeniden boyutlandirma)


# In[28]:


myArray = np.arange(30)
print("myArray = ", myArray)


# In[29]:

print("xxxx",myArray.reshape(5,6))

# In[32]:


print("min: ",myArray.min())


# In[33]:


print("max: ", myArray.max())


# In[35]:


## max degerin hangi indexte oldugunu soyler
print(myArray.argmax(), ". index")


# In[37]:


## min degerin hangi indexte oldugunu soyler
print(myArray.argmin(), ". index")


# In[39]:


## shape size
my2Array = myArray.reshape(6,5)
print("(x,y) = ", my2Array.shape)


# In[ ]:


## Numpy Indeksler


# In[40]:


newArray = np.arange(0,15)
print("newArray = ", newArray)


# In[41]:


## indexteki degeri alma islemi
print("value: ", newArray[10])


# In[42]:


## istedigimiz index araligindaki degerleri listeletir
print("value: ", newArray[3:7])


# In[43]:


## sectigimiz araliktaki degerlerin guncellenmesini istersek
newArray[3:6] = -3
print("newArray: ", newArray)


# ## Ana dizinin icine alt diziyi olusturma, alt diziyi guncelleme ve ana dizinin degistigini gorme(Slicing islemi)

# In[44]:


mainArray = np.arange(0,40)
print("mainArray: ", mainArray)


# In[46]:


## mainArray in icinden biz subArray olusturduk
subArray = mainArray[4:11]
print("subArray: ", subArray)


# In[47]:


## subArray deki degerleri guncelledigimiz zaman mainArray in de guncellendigni gorcez(slicing islemi bu adimda yapiliyor)
subArray[:] = 999999
print("subArray: ", subArray)


# In[48]:


## mainArray in degisip degismedigini gorelim
mainArray
print("mainArray: ", mainArray)

# ## Yaptigim dedisikliklerin ana diziyi etkilemesini istemiyorsan ana dizinin kopyasini alirim,alt diziye esitlerim ve oyle calisirim
# 

# In[49]:


anaDizi = np.arange(0,24)
print("anaDizi: ", anaDizi)


# In[50]:


anaDizininKopyasi = anaDizi.copy()
print("anaDizininKopyasi: ", anaDizininKopyasi)


# In[57]:


anaDizininKopyasiSlicing = anaDizininKopyasi[3:12]
print("anaDizininKopyasiSlicing", anaDizininKopyasiSlicing)


# In[59]:


anaDizininKopyasiSlicing[:] = -1234567890
print("anaDizininKopyasiSlicing", anaDizininKopyasiSlicing)


# In[60]:


## anaDiziKopyasinda da guncelleme oldugunu gormekteyiz
print("anaDizininKopyasi: ", anaDizininKopyasi)


# In[61]:


## Fakat anaDizide herhangi bir degisiklik olmadigi belli olmakta
print("anaDizi: ", anaDizi)


# ## Matrix

# In[62]:


listem = [[10,20,30],[20,30,40],[40,50,60]]
print("listem: ", listem)


# In[63]:


## listeyi 2boyutlu matrise cevirme
matrisim = np.array(listem)
print("matrisim: ", matrisim)


# In[64]:


## matrisin ilk indeksindeki deger
print("matrisim[0]", matrisim[0])


# In[65]:


## matrisim[1][2] = matrisim[1,2]


# In[68]:


print("A ",matrisim[1][2])


# In[67]:


print("B ", matrisim[1,2])


# In[70]:


## slicing islemlerini yapmamizi saglayan gosterim
## matrisim[1:,0] -> 1.SATIRDAN ITIBAREN TUM SATIRLARDAKI 0. INDEXTEKI DEGERLERI GETIRIR
print("C ", matrisim[1:,0])


# In[72]:


print("D ", matrisim[0:,1])


# In[71]:


## 0. satirdan baslar ve 0. sutundan itibaren tum sutun degerlerini yansitir
print("E ", matrisim[0,0:])


# In[73]:


## 1. satirdan baslayip 2.sutundan itibaren tum sutunlari cekelim
print("F ", matrisim[1,2:])


# In[74]:


## 1. satirdan itibaren tum satirlardaki 2. sutun degerlerini cekelim
print("G ", matrisim[1:,2:])


# In[76]:


## satir satir elemanlari cekme islemi
list= [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
array = np.array(list)
print("array: ", array)


# In[77]:


# array in 2. satirini tamamen ceker
print("H,", array[2])


# In[80]:


## dizinin once 3.satirini sonra 0. satirini ve son olarak 1.satirini cektik
print("I ", array[[3,0,1]])


# In[94]:


## diziden istedigimiz sutunlari cekmemizi saglar
print("J ", array[:, [2,3,1]])


# In[95]:


operasyonDizisi = np.random.randint(1,100,20)
print("operasyonDizisi: ", operasyonDizisi)


# In[98]:


print("K: ", operasyonDizisi > 32)


# In[99]:


buyukSayilarDizisi = operasyonDizisi > 32
print("buyukSayilarDizisi", buyukSayilarDizisi)


# In[101]:


## belirttigimiz sarti saglayan elemanlardan olusan bir dizi olusturuyor
## bunu -> operasyonDizisi[operasyonDizisi > 32] seklinde de yazabilirdim sonuc yine ayni olurdu
print("L: ", operasyonDizisi[buyukSayilarDizisi])


# In[102]:


arrayIslemleri = np.arange(0,26)
print("arrayIslemleri:", arrayIslemleri)


# In[103]:


print("arrayIslemleri + arrayIslemleri = ", arrayIslemleri + arrayIslemleri)


# In[104]:


print("arrayIslemleri * 2 = ", arrayIslemleri * 2)


# In[105]:


## 0/0 tanimsiz oldugundan ilk eleman nan geliyor digerlerinin sonucunu yine yansitiyor
print("arrayIslemleri / arrayIslemleri = ", arrayIslemleri / arrayIslemleri)


# In[106]:


## dizinin karekokunu alma
print("np.sqrt(arrayIslemleri) = ", np.sqrt(arrayIslemleri))


# In[ ]:


## dizinin max elemanini bulma


# In[108]:


print("np.max(arrayIslemleri) = ", np.max(arrayIslemleri))


# In[110]:


print("np.min(arrayIslemleri) = ", np.min(arrayIslemleri))


# In[109]:


print("np.max(arrayIslemleri) - np.min(arrayIslemleri) = ", np.max(arrayIslemleri) - np.min(arrayIslemleri))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




# In[ ]:




# In[ ]:
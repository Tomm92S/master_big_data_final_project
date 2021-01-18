# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:50:26 2020

@author: RR
"""



import numpy as np

#to silence the errors
#np.seterr(divide='ignore', invalid='ignore')

#FUNZIONE PER CALCOLO DEL WARPING PATH E ESTRAZIONE COORDINATE ASSOCIATE AL CENTROIDE
def DTW_dist(DTW, set_of_coords, dist, k, l, x):
    if k == DTW.shape[0]-1 and l == DTW.shape[1]-1:   # da L,L siamo passati a K,L, coerentemente
        set_of_coords[l-1].append(float(x[:,l-1]))
    
    #prendiamo le tre posizioni adiacenti nella matrice
    a = DTW[k,l-1]
    b = DTW[k-1,l]     
    c = DTW[k-1,l-1]
        
    DTW_min = min(a,b,c)
    dist += DTW_min
    #print(DTW_min)
    kl_min = np.where(DTW == DTW_min)
    last_k = k #.copy()
    #print(kl_min)
    k = kl_min[0][(kl_min[0] == k) | (kl_min[0] == k-1)][0]
    
    if k == last_k:
        l = l-1
    else:
        l = kl_min[1][(kl_min[1] == l) | (kl_min[1] == l-1)][0]
        

    #print(k,',',l)
    if k == 0 and l == 0:
        #print('yes')

        return dist, set_of_coords #dist == CALCOLO DEL WARPING PATH, set_of_coords == ESTRAZIONE COORDINATE ASSOCIATE AL CENTROIDE
    
    #semnrerebbe K da inserire, perchè è l'index della serie, ma il centroide nei plot sfancula. va messo L. perchè?
    set_of_coords[l-1].append(float(x[:,l-1])) #nodo cruciale !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return DTW_dist(DTW, set_of_coords, dist = dist, k=k, l=l, x = x)
























class K_Means_DTW:
    
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):
      
        

        self.centroids = {}

        

        
        for i in range(self.k):
            #scelta dei primi centroidi. si può fare random anche. o anche meglio per velocizzare
            self.centroids[i] = data.T[i].reshape(1, len(data.T[i][~np.isnan(data.T[i])]))[0]
            
        #INIZIA IL PROCESSO ITERATIVO
        for i in range(self.max_iter):
            self.labels = {}
            

            
            bigdiz = {}
            

            #PER OGNI K....
            for k in range(self.k):
                #svuotiamo la lista che conterrà le serie associate alla k label
                self.labels[k] = []
                
                #INIZIALIZZIAMO IL DIZIONARIO CON KEY = INDICI DEL CENTROIDE, VALUES = LISTA DI COORDINATE ASSOCIATE (per ogni k si reinizializza)    
                ind = 0
                bigdiz[k] = {}
                for elem in self.centroids[k]:
                
                    bigdiz[k][ind] = []
                    ind+=1
            
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            #PER OGNI SERIE DEL DATASET CALCOLIAMO LA DISTANZA DAL CENTROIDE
            for series in data.T:
                
                ser_coords ={}
 
                distances = [] 
               #+++++++++++++++++++++++++++
                for k in range(self.k):
                    ind = 0
                    ser_coords[k] = {}
                    for elem in self.centroids[k]:
                    
                        ser_coords[k][ind] = []
                        ind+=1
                #+++++++++++++++++++++++++
                for centroid in self.centroids:
                    y = self.centroids[centroid].reshape(1,len(self.centroids[centroid][~np.isnan(self.centroids[centroid])]))
                                     
                    
                    
                    
                    n = len(self.centroids[centroid][~np.isnan(self.centroids[centroid])]) +1
                    m = len(series[~np.isnan(series)]) +1
                    DTW = np.zeros([n,m])
                    
                    DTW[0,1:] = np.inf
                    DTW[1:,0] = np.inf
                    
                    a = series.reshape(1,len(series[~np.isnan(series)]))
    
                    x = a  # is this useful?
                    #print(y)
                    #print(x)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                
                 
                    
#SIAMO QUI
                    for i in range(1,m):
                        for j in range(1, n): #centroide
                            #scegliere bene  tra 0, 1 o altro
                            
                            if i ==1:
                                flocal_x1 = 0
                                fglobal_x1 = 0
                            else:
                                #flocal_x1 = (x[:,i-1] - x[:,i-2])/x[:,i-2] #index = 0 => value = 1
                                #fglobal_x1 = (x[:,i-1] - np.sum(x[:,:i-1]/i-1))/ np.sum(x[:,:i-1]/(i-1)) #divisione per zero. dove???
# =============================================================================
                                 if np.sum(x[:,:i-1]/(i-1)) == 0:
                                     fglobal_x1 = 0
                                     flocal_x1 = (x[:,i-1] - x[:,i-2])/x[:,i-2]
                                 elif x[:,i-2] == 0:
                                     flocal_x1 = 0
                                     fglobal_x1 = (x[:,i-1] - np.sum(x[:,:i-1]/i-1))/ np.sum(x[:,:i-1]/(i-1))
                                 else:                                
                                     flocal_x1 = (x[:,i-1] - x[:,i-2])/x[:,i-2] #index = 0 => value = 1
                                     fglobal_x1 = (x[:,i-1] - np.sum(x[:,:i-1]/i-1))/ np.sum(x[:,:i-1]/(i-1)) #divisione per zero. dove???
                             
# =============================================================================
                            if i == m-1:
                                flocal_x2 = 0
                                fglobal_x2 = 0
                            else:
                                flocal_x2 = (x[:,i] - x[:,i-1])/x[:,i-1]
                                fglobal_x2 = (x[:,i-1] - np.sum(x[:,i:]/m-i))/ np.sum(x[:,i:]/(m-i))  
                                
                            
                            if j == 1:
                                flocal_y1 = 0
                                fglobal_y1 = 0
                            else:
                                #flocal_y1 = (y[:,j-1] - y[:,j-2])/y[:,j-2] #index = 0 => value = 1
                                #fglobal_y1 = (y[:,j-1] - np.sum(y[:,:j-1]/j-1))/ np.sum(y[:,:j-1]/(j-1))
                            # =============================================================================
                                 if np.sum(y[:,:j-1]/(j-1)) == 0:
                                     fglobal_y1 = 0
                                     flocal_y1 = (y[:,j-1] - y[:,j-2])/y[:,j-2]
                                
                                 elif y[:,j-2] == 0:
                                     fglobal_y1 = (y[:,j-1] - np.sum(y[:,:j-1]/j-1))/ np.sum(y[:,:j-1]/(j-1))
                                     flocal_y1 = 0
                                     
                                     
                                 else:                                
                                     flocal_y1 = (y[:,j-1] - y[:,j-2])/y[:,j-2] #index = 0 => value = 1
                                     fglobal_y1 = (y[:,j-1] - np.sum(y[:,:j-1]/j-1))/ np.sum(y[:,:j-1]/(j-1)) #divisione per zero. dove???
                             
# =============================================================================
                            
                            if j == n-1:
                                flocal_y2 = 0
                                fglobal_y2 = 0
                            else:
                                #flocal_y2 = (y[:,j] - y[:,j-1])/y[:,j-1]
                                #fglobal_y2 = (y[:,j-1] - np.sum(y[:,j:]/n-j))/ np.sum(y[:,j:]/(n-j))
                                if np.sum(y[:,j:]/(n-j)) == 0:
                                    fglobal_y2 = 0
                                    flocal_y2 = (y[:,j] - y[:,j-1])/y[:,j-1]
                                elif y[:,j-1] == 0:
                                    fglobal_y2 = (y[:,j-1] - np.sum(y[:,j:]/n-j))/ np.sum(y[:,j:]/(n-j))
                                    flocal_y2 = 0
                                else:
                                    flocal_y2 = (y[:,j] - y[:,j-1])/y[:,j-1]
                                    fglobal_y2 = (y[:,j-1] - np.sum(y[:,j:]/n-j))/ np.sum(y[:,j:]/(n-j)) 
      
                    
                            dist = abs(flocal_x1-flocal_y1)+abs(flocal_x2-flocal_y2)\
                                + abs(fglobal_x1-fglobal_y1)+abs(fglobal_x2-fglobal_y2)
    
                            
                            DTW[i,j] = dist + min([DTW[i-1,j], DTW[i,j-1], DTW[i-1,j-1]])
                    
                    #print(DTW)
                    dist, ser_coords[centroid] = DTW_dist(DTW, ser_coords[centroid], dist = DTW[-1,-1], k=DTW.shape[0]-1, l=DTW.shape[1]-1, x = x) 
                    distances.append(dist)
                    

                label = distances.index(min(distances))
                self.labels[label].append(series)
         
                for i in range(len(bigdiz[label])):
                    bigdiz[label][i] += ser_coords[label][i]
                
                
#+++UNA VOLTA FINITE TUTTE LE SERIE.....
            prev_centroids = dict(self.centroids)
          
            #CALCOLO DEI CENTROIDI
            for label in self.labels:
               
                self.centroids[label] = np.array([np.average(bigdiz[label][c], axis = 0) for c in range(0,len(self.centroids[label]))])
  

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                #print(original_centroid)
                current_centroid = self.centroids[c]
                #print(current_centroid)
                if np.sum(abs((current_centroid-original_centroid)/original_centroid*100.0)) > self.tol: #questa perc ci dice la variazione dei centroidi. Va bene così?
                    print('variazione  ',c,' = ', np.sum(abs((current_centroid-original_centroid)/original_centroid*100.0)))
                    #print('eeeer')
                    optimized = False

            if optimized:
                print('ultima variazione  ',c,' = ', np.sum(abs((current_centroid-original_centroid)/original_centroid*100.0)))
                break


    

    
    


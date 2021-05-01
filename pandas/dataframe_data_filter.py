### Importing important libries
import numpy as np
import pandas as pd

### Checking if my dataframe has the values of my list

# dataframe created
df = pd.DataFrame([1,2,3,4,5,6],columns = ['Filter'])
#list created
list2 = [1,4]

#filtering the dataframe index
ind=[df.index[df['Filter']==i].tolist() for i in list2]

flat_ind=[item for sublist in ind for item in sublist]

## Answer
df.reindex(flat_ind)

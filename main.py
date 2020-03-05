import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import ticker


# f_30mn = pd.ExcelFile('0.5f.xlsx') #opening an excel file by name nb: we can mention path here too
# base_6 = f_30mn.parse('base6-700-front-30min-1') #Copies data from excel sheet of a specific excel file 

# print(base_6.head()) #Shows first 5 entries of the data frame

f_30min_base_6 = pd.read_excel('0.5f.xlsx',0)
f_30min_base_7 = pd.read_excel('0.5f.xlsx',1)
f_30min_base_8 = pd.read_excel('0.5f.xlsx',2)

f_30min_base_6_arr = f_30min_base_6.values
f_30min_base_7_arr = f_30min_base_7.values
f_30min_base_8_arr = f_30min_base_8.values

fig, axs = plt.subplots(3,3)

axs[0,0].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,1],'-ok',markersize=3,color = 'green')
axs[0,0].set_title('Carbon wt.%')
plt.grid()
axs[0,1].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,2],'-ok',markersize=3,color ='purple')
axs[0,1].set_title('Oxygen wt.%')
plt.grid()
axs[0,2].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,3],'-ok',markersize=3,color ='brown')
axs[0,2].set_title('Aluminum wt.%')
plt.grid()
axs[1,0].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,4],'-ok',markersize=3,color ='cyan')
axs[1,0].set_title('Silicon wt.%')
plt.grid()
axs[1,1].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,5],'-ok',markersize=3,color ='olive')
axs[1,1].set_title('Chromium wt.%')
plt.grid()
axs[1,2].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,6],'-ok',markersize=3,color ='orange')
axs[1,2].set_title('Manganese wt.%')
plt.grid()
axs[2,0].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,7],'-ok',markersize=3,color ='red')
axs[2,0].set_title('Iron wt.%')
plt.grid()
axs[2,1].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,8],'-ok',markersize=3,color ='blue')
axs[2,1].set_title('Nickel wt.%')
plt.grid()
axs[2,2].plot(f_30min_base_8_arr[:,0],f_30min_base_8_arr[:,9],'-ok',markersize=3,color ='gray')
axs[2,2].set_title('Molybdenum wt.%')


for ax in axs.flat:
    ax.set(xlabel='micron')

# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()

# Create your ticker object with M ticks
M = 12
N = 5
xticks = ticker.MaxNLocator(M)
yticks = ticker.MaxNLocator(N)

# Set the yaxis major locator using your ticker object. You can also choose the minor
# tick positions with set_minor_locator.
for a in range(0,3):
    for b in range(0,3):
        axs[a,b].xaxis.set_major_locator(xticks)
        axs[a,b].locator_params(axis='y', nbins=6)
        axs[a,b].grid()
        #axs[a,b].set_xlim(np.amin(f_30min_base_6_arr[:,0]), np.amax(f_30min_base_6_arr[:,0]))
        #axs[a,b].set_ylim(np.amin(f_30min_base_6_arr[:,0]), np.amax(f_30min_base_6_arr[:,0]))

        #axs[a,b].yaxis.set_major_locator(yticks)

# # Turn on the minor TICKS, which are required for the minor GRID
# axs.minorticks_on()

# # Customize the major grid
# axs.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# # Customize the minor grid
# axs.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

#fig.tight_layout(pad = 0.05)
plt.subplots_adjust(left=0.125, bottom=0.09, right=0.9, top=0.9, wspace=0.15, hspace=0.31)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
#plt.subplots(figsize=(15,15))
fig.savefig('0.5f_base8.svg', format='svg', dpi=1200)
plt.show()



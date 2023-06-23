from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

#loading the data into numpy array from FITS file
filepath = 'asu_999999.fit'
hdul = fits.open(filepath)

# from 'hdul.info()' we can see that the first extension HDU contains the data table
df_full = hdul[1].data

# checking names of columns -->
# df_full_cols = hdul[1].columns
# print(df_full_cols.names)
# filtering out only the requires fields into a separate numpy array and calculating abs mag -->
col_HIP = df_full.field(2)
col_VMag = df_full.field(5)
col_Plx = df_full.field(8)
col_BV = df_full.field(12)
col_AbsMag = df_full.field(5) + 5 * np.log10(df_full.field(8)/100)
data = np.stack((col_HIP, col_VMag, col_Plx, col_BV, col_AbsMag),axis=1)

#cleaning data frame
data = data[~np.isnan(data).any(axis=1)]
data_T = np.transpose(data)

#plot
fig, ax = plt.subplots(figsize=(10,12))
ax.set_xlim(-0.75,2.75)
ax.set_ylim(15, -15)
ax.set_facecolor('#333333')
fig.patch.set_facecolor('#333333')
ax.set_title('H-R Diagram for Hipparcos Catalog')
ax.set_xlabel('Johnson B-V Color')
ax.set_ylabel('Absolute Magnitude')
ax.xaxis.label.set_color('#e27c7c')
ax.yaxis.label.set_color('#e27c7c')
ax.title.set_color('#e27c7c')
ax.title.set_fontsize(10)
ax.spines['left'].set_color('#e27c7c')
ax.spines['top'].set_color('#e27c7c')
ax.spines['bottom'].set_color('#e27c7c')
ax.spines['right'].set_color('#e27c7c')
ax.xaxis.label.set_fontsize(10)
ax.yaxis.label.set_fontsize(10)
ax.scatter(data_T[3], data_T[4], s=.5, edgecolors='none', color='#6cd4c5')
ax.tick_params(axis='both', labelsize=8, colors='#e27c7c')
plt.show()

hdul.close()
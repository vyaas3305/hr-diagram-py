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
df = np.stack((col_HIP, col_VMag, col_Plx, col_BV, col_AbsMag),axis=1)

#cleaning data frame
df = df[~np.isnan(df).any(axis=1)]
df_T = np.transpose(df)

#plot
fig, ax = plt.subplots(figsize=(10,12))
ax.set_xlim(-0.75,2.75)
ax.set_ylim(15, -15)
ax.set_title('H-R Diagram for Hipparcos Catalog')
ax.title.set_fontsize(10)
ax.set_xlabel('Johnson B-V Color')
ax.xaxis.label.set_fontsize(10)
ax.set_ylabel('Absolute Magnitude')
ax.yaxis.label.set_fontsize(10)
ax.scatter(df_T[3], df_T[4], s=1, edgecolors='none', color='#000000')
ax.tick_params(axis='both', labelsize=8)
plt.show()

hdul.close()
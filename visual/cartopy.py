import cartopy.crs as ccrs
import matplotlib.pyplot as plt


if __name__ == '__main__':
    plt.figure(figsize = (12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.gridlines(draw_labels=True)
    plt.show()
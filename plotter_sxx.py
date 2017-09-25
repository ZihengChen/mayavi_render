from pylab import *
from mayavi import mlab

image = np.fromfile("data/output_img.dat").reshape(80,80,80)

mlab.clf()
src = mlab.pipeline.scalar_field(image)
mlab.pipeline.iso_surface(src,contours=[1200], transparent=False, opacity=1,
                          colormap="viridis",vmin=1,vmax=1200)
mlab.pipeline.iso_surface(src,contours=[700], transparent=True, opacity=0.4,
                          colormap="viridis",vmin=1,vmax=1200)
mlab.pipeline.iso_surface(src,contours=[500,300], transparent=True, opacity=0.1,
                          colormap="viridis",vmin=1,vmax=1200)
mlab.pipeline.image_plane_widget(src,plane_orientation='y_axes',slice_index=10, opacity=0.1,
                                 colormap="hot",vmin=1,vmax=1500)
mlab.show()

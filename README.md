# mayavi_render
The input file ```data/input.txt``` is a plain text file with delimiter as " " and records as "rho x y z".

The notebook first reads in the input file and then makes a 2D distribution of density on z=0 plane for a quick glimpse.
![2D_centerslice](plot/2D_centerslice.png){ width: 300px; }

After that, I used [[mayavi][http://docs.enthought.com/mayavi/mayavi/]] to render 3D distritution. The 3D plots inlude a 3D scalar field cloud and a 3D countor plot.

![3D_countour](plot/3D_countor.png){ width: 300px; }
![3D_scalarfield](plot/3D_scalarfield.png){ width: 300px; }

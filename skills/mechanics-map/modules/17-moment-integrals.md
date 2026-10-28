来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 17 17: Appendix 2 - Moment Integrals

## 17: Appendix 2 - Moment Integrals

## 17.1: Moment Integrals

- 1D, 2D, and 3D Moment Integrals
- Force, Area/Volume, and Mass Moment Integrals
- First vs Second Moment Integrals
- Rectangular vs Polar Moment Integrals
A moment integral, as the name implies, is the general concept of using integration to determine the net moment of a force that is spread over an area or volume. Because moments are generally a force times a distance, and because distributed forces are spread out over a range of distances, we will need to use calculus to to determine the net moment exerted by a distributed force.
\[ \int M = \int F(d) * d \]
Beyond the most literal definition of a moment integral, the term "moment integral" is also general applied the process of integrating distributed areas or masses that will be resisting some moment about a set axis.
Some of the applications of moment integrals include:
- Finding point loads that are equivalent to distributed loads (the equivalent point load).
- Finding the centroid (geometric center) or center of mass for 2D and 3D shapes.
- Finding the area moment of inertia for a beam cross-section, which will be one factor in that beam's resistance to bending.
- Finding the polar area moment of inertia for a shaft cross-section, which will be one factor in that shaft's resistance to torsion.
- Finding the mass moment of inertia, indicating a body's resistance to angular accelerations.
When looking at moment integrals, there are number of different types of moment integrals. These will include moment integrals in one dimension, two dimensions, and three dimensions; moment integrals of force functions, of areas/volumes, or of mass distributions; first order or second order moment integrals; and rectangular or polar moment integrals.
Any combination of these different types is possible (for example, a first-order rectangular 2D area moment integral, or a second-order polar 3D mass moment integral). However, only some of these combinations will have practical applications and will be discussed in detail on future pages.

## 1D, 2D, and 3D Moment Integrals

Technically we can take the moment integral in any number of dimensions, but for practical purposes we will never deal with moment integrals beyond three dimensions. The number of dimensions will affect the complexity of the calculations (with three-dimensional moment integrals being more involved than one- or two-dimensional moment integrals), but the nature of the problem will dictate the dimensions needed. Often this is not listed in the type of moment integral, requiring you to assume the type based on the context of the problem.

## Force, Area/Volume, and Mass Moment Integrals

The next distinction in moment integrals is made with regard what we are integrating. Generally, we can integrate force functions over some distance, area, or volume, we can integrate the area or volume function itself, or we can integrate the mass distribution over the area or volume. Each of these types of moment integrals has a different purpose and will start with a different mathematical function to integrate, but the integration process beyond that will be very similar.

## First vs Second Moment Integrals

For moment integrals we will always be multiplying the force function, area or volume function, or mass distribution function by either a distance or a distance squared. First moment integrals just multiply the initial function by the distance, while second moment integrals multiply the function by the distance squared. Again, the type of moment integral we will use depends upon our application, with things like equivalent point load, centroids, and center of mass relying on first moment integrals, and area moments of inertia, polar moments of inertia, and mass moments of inertia relying on second moment integrals. As you can probably deduce from this list, second moment integrals, are often labeled as a moment of inertia.

## Rectangular vs Polar Moment Integrals

Finally we will talk about rectangular moment integrals versus polar moment integrals. This is a difference in how we define the distance in our moment integral. Let's start with the distinction in 2D. If our distance is measured from some axis (for example the \(x\)-axis, or the \(y\)-axis) then it is a rectangular moment integral. On the other hand, if the distance is measured from some point (such as the origin), then it is a polar moment integral.
This distinction is important for how we will take the integral. For rectangular moment integrals we will move left to right or bottom to top. For polar moment integrals we will instead take the integral by radiating out from the center point.
In three-dimensional problems, the definitions change slightly. For rectangular moment integrals, the distance will be measured from some plane (such as the \(xy\)-plane, \(xz\)-plane, or \(yz\)-plane). Again we will integrate left to right, bottom to top, or now back to front with distances corresponding to the \(x\), \(y\) or \(z\) coordinates of that point. For a polar moment integral, the distance will be measured from some axis (such as the the \(x\), \(y\), or \(z\) axis), and we will integrate by radiating outward from that axis.
- 17: Appendix 2 - Moment Integrals      17.2: Centroids of Areas via Integration
- 17: Appendix 2 - Moment Integrals

## 17.2: Centroids of Areas via Integration

- Finding the Centroid via the First Moment Integral
- Using Symmetry as a Shortcut
The centroid of an area can be thought of as the geometric center of that area. The location of the centroid is often denoted with a \(C\) with the coordinates being \((\bar{x}\), \(\bar{y})\), denoting that they are the average \(x\) and \(y\) coordinate for the area. If an area was represented as a thin, uniform plate, then the centroid would be the same as the center of mass for this thin plate.
Centroids of areas are useful for a number of situations in the mechanics course sequence, including in the analysis of distributed forces, the bending in beams, and torsion in shafts, and as an intermediate step in determining moments of inertia.
The location of centroids for a variety of common shapes can simply be looked up in tables, such as this table for 2D centroids and this table for 3D centroids. However, we will often need to determine the centroid of other shapes; to do this, we will generally use one of two methods.
- We can use the first moment integral to determine the centroid location.
- We can use the method of composite parts along with centroid tables to determine the centroid location.
On this page we will only discuss the first method, as the method of composite parts is discussed in a later section. The tables used in the method of composite parts, however, are derived via the first moment integral, so both methods ultimately rely on first moment integrals.

## Finding the Centroid via the First Moment Integral

When we find the centroid of a two-dimensional shape, we will be looking for both an \(x\) and a \(y\) coordinate, represented as \(\bar{x}\) and \(\bar{y}\) respectively. Collectively, this \((\bar{x}, \bar{y}\) coordinate is the centroid of the shape.
To find the average \(x\)-coordinate of a shape (\(\bar{x}\)), we will essentially break the shape into a large number of very small and equally sized areas, and find the average \(x\)-coordinate of these areas. To do this sum of an infinite number of very small things, we will use integration. Specifically, we will take the first rectangular area moment integral along the \(x\)-axis, and then divide that integral by the total area to find the average coordinate. We can do something similar along the \(y\)-axis to find our \(\bar{y}\) value. Writing all of this out, we have the equations below.
\[ C = ( \bar{x}, \bar{y}) \]
 \bar{x} &= \dfrac{ \displaystyle\int_{A} (dA*x)}{A} \\[4pt] \bar{y} &= \dfrac{ \displaystyle\int_{A} (dA*y)}{A}
Next let's discuss what the variable \(dA\) represents and how we integrate it over the area. The variable \(dA\) is the rate of change in area as we move in a particular direction. For \(\bar{x}\) we will be moving along the \(x\)-axis, and for \(\bar{y}\) we will be moving along the \(y\)-axis in these integrals.
As we move along the \(x\)-axis of a shape from its leftmost point to its rightmost point, the rate of change of the area at any instant in time will be equal to the height of the shape that point times the rate at which we are moving along the axis (\(dx\)). Because the height of the shape will change with position, we do not use any one value, but instead must come up with an equation that describes the height at any given value of x. We will then multiply this \(dA\) equation by the variable \(x\) (to make it a moment integral), and integrate that equation from the leftmost \(x\) position of the shape (\(x_{min}\)) to the rightmost \(x\) position of the shape (\(x_{max}\)).
To find the \(y\) coordinate of the of the centroid, we have a similar process, but because we are moving along the \(y\)-axis, the value \(dA\) is the equation describing the width of the shape times the rate at which we are moving along the \(y\) axis (\(dy\)). We then take this \(dA\) equation and multiply it by \(y\) to make it a moment integral. We will integrate this equation from the \(y\) position of the bottommost point on the shape (\(y_{min}\)) to the \(y\) position of the topmost point on the shape (\(y_{max}\)).
Using the first moment integral and the equations shown above, we can theoretically find the centroid of any shape as long as we can write out equations to describe the height and width at any \(x\) or \(y\) value respectively. For more complex shapes, however, determining these equations and then integrating these equations can become very time-consuming. That is why most of the time, engineers will instead use the method of composite parts or computer tools.

## Using Symmetry as a Shortcut

Shape symmetry can provide a shortcut in many centroid calculations. Remember that the centroid is located at the average \(x\) and \(y\) coordinate for all the points in the shape. If the shape has a line of symmetry, that means each point on one side of the line must have an equivalent point on the other side of the line. This means that the average value (AKA the centroid) must lie along any axis of symmetry. If the shape has more than one axis of symmetry, then the centroid must exist at the intersection of the two axes of symmetry.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.

## 17.3: Centroids in Volumes and Center of Mass via Integration

- Finding the Centroid of a Volume via the First Moment IntegralUsing Symmetry as a Shortcut
- Using Symmetry as a Shortcut
- Finding the Center of Mass for Non-Uniform Density Shapes
The centroid of a volume can be thought of as the geometric center of that shape. It is often denoted as \(C\), being being located at the coordinates \((\bar{x}, \bar{y}, \bar{z})\). If this volume represents a part with a uniform density (like most single material parts) then the centroid will also be the center of mass, a point usually labeled as \(G\).
Just as with the centroids of an area, centroids of volumes and the center of mass are useful for a number of situations in the mechanics course sequence, including the analysis of distributed forces, simplifying the analysis of gravity (which is itself a distributed force), and as an intermediate step in determining mass moments of inertia.
Just as with areas, the location of the centroid (or center of mass) for a variety of common shapes can simply be looked up in tables, such as this one. However, we will often need to determine the centroid or center of mass for other shapes, and to do this we will generally use one of two methods.
- We can use the first moment integral to determine the centroid or center of mass location.
- We can use the method of composite parts along with centroid tables to determine the centroid or center of mass location.
On this page we will only discuss the first method, as the method of composite parts is discussed in a later section. However, the tables used in the method of composite parts are derived via the first moment integral, so both methods ultimately rely on first moment integrals.

## Finding the Centroid of a Volume via the First Moment Integral

When we find the centroid of a three-dimensional shape, we will be looking for the \(x\), \(y\), and \(z\) coordinates (\(\bar{x}\), \(\bar{y}\), and \(\bar{z}\)) of the point that is the centroid of the shape.
Much like the centroid calculations we did with two-dimensional shapes, we are looking to find the shape's average coordinate in each dimension. We do this by summing up all the little bits of volume times the \(x\), \(y\), or \(z\) coordinate of that bit of volume and then dividing that sum by the total volume of the shape. Again we will use calculus to sum up an infinite number of infinitely small volumes. Specifically this sum will be the first rectangular volume moment integral for the shape.
\[ C = G = (\bar{x}, \bar{y}, \bar{z}) \quad \text{for constant-density shapes} \nonumber\]
Working in each of the three coordinate directions we wind up with the following three equations.
\[ \bar{x} &= \dfrac{\displaystyle \int_V (dV * x)}{V} \\[4pt] \bar{y} &= \dfrac{\displaystyle \int_V (dV * y)}{V} \\[4pt] \bar{z} &= \dfrac{\displaystyle \int_V (dV * z)}{V} \]
With these new equations we have the variable \(dV\) rather than \(dA\), because we are integrating over a volume rather than an area. This represents the rate of change of the volume as we move along an axis from one end to another. The rate of change of the volume at any point on the shape will be the cross-sectional area that is perpendicular to that axis times the rate at which we are moving along that axis. Since cross-sectional area may vary as we move along the axis, we will need to determine a formula for the cross sectional area at any point along that axis.
Using the first moment integral and the equations shown above, we can theoretically find the centroid of any volume as long as we can write an equation to describe the cross section area for each direction. For more complex shapes, however, determining these equations and then integrating these equations may become very time-consuming. For these complex shapes, the method of composite parts or computer tools will most likely be much faster.

### Using Symmetry as a Shortcut

Just as with 2D areas, shape symmetry can provide a shortcut in many centroid calculations. Remember that the centroid coordinate is the average \(x\), \(y\), and \(z\) coordinate for all the points in the shape. If the volume has a plane of symmetry, that means each point on one side of the line must have an equivalent point on the other side of the line. This means that the average value (AKA the centroid) must lie within that plane. If the volume has more than one plane of symmetry, then the centroid must exist at the intersection of those planes.

## Finding the Center of Mass for Non-Uniform Density Shapes

If a body has a non-uniform density, then the centroid of the volume and the center of mass will no longer be the same point. In these cases, we will be integrating with respect to mass, rather than integrating the volume. To do this, we will use something called a density function, which will provide the density (the mass per unit volume) in terms of the \(x\), \(y\), and/or \(z\) location. In the end, we will also be dividing by total mass, rather than dividing by total volume. The generalized equations for the center of mass are shown in the equations below.
\[ C \neq G \]
\[ G = (x_G, y_G, z_G) \]
 x_G &= \dfrac{\int_m (dm*x)}{m} = \dfrac{\int_V (\rho (x,y,z) * dV * x)}{m} \\[4pt] y_G &= \dfrac{\int_m (dm*y)}{m} = \dfrac{\int_V (\rho (x,y,z) * dV * y)}{m} \\[4pt] z_G &= \dfrac{\int_m (dm*z)}{m} = \dfrac{\int_V (\rho (x,y,z) * dV * z)}{m}
In instances of uniform density (where the density function did not vary with location and was therefore just a constant), the density constant could be moved outside of the integral. On the bottom, we could also write mass as density times volume, and the density terms on the top and bottom of the fraction would cancel out. That is why for uniform-density parts, the centroid and center of mass will be the same point.
When we have a density function that is not a constant, we will have to come up with a mathematical function for the density in terms of \(x\) and/or \(y\) and/or \(z\) locations. If density varies along more than one axis, determining the function and then integrating it may become quite difficult, and computer modeling may be advisable in these situations.
Once you have the density function, you will multiply that by the relevant \(dV\) function as discussed earlier on the page and multiply it by the variable for the relevant axis. This entire function is integrated from left to right, bottom to top, or back to front, and then that quantity is divided by mass to find the location of the center of mass.
Example \(\)
The cone shown below is four inches tall and has a four-inch-diameter base. Find the \(x\), \(y\), and \(z\) coordinates of the centroid.
Example \(\)
Find the y coordinate of the centroid for the tetrahedron shown in the image below. (The fourth vertex is at the origin)
Example \(\)
A water and ceramic slurry with a uniform density of 1100 kilograms per meter cubed enters a settling tank with a height of 1 meter and a diameter of 1 meter. After one hour in the tank, the density of the slurry at the top of the tank is measured to be 1000 kilograms per meter cubed and the density at the bottom of the tank is measured to be 1200 kilograms per meter cubed. Assume the density of the slurry varies linearly between the top and the bottom. How far has the center of mass of the slurry dropped between the initial conditions and the current state?

## 17.4: Centroids and Centers of Mass via Method of Composite Parts

- Finding the Centroid via the Method of Composite Parts
- Finding the Center of Mass via the Method of Composite Parts
As an alternative to the use of moment integrals, we can use the Method of Composite Parts to find the centroid of an area or volume or the center of mass of a body. This method is is often easier and faster that the integration method; however, it will be limited by the table of centroids you have available. The method works by breaking the shape or volume down into a number of more basic shapes, identifying the centroids or centers of masses of each part via a table of values, and then combing the results to find the overall centroid or center of mass.
A key aspect of the method is the use of these centroid tables. This is a set of tables that lists the centroids (and usually also moments of inertia) for a number of common areas and/or volumes. Some centroid tables can be found here for 2D shapes, and here for 3D shapes. The method of composite parts is limited in that we will need to be able to break our complex shape down entirely into shapes found in the centroid table we have available; otherwise, the method will not work without us also doing some moment integrals.

## Finding the Centroid via the Method of Composite Parts

Start the process by labeling an origin point and axes on your shape. It will be important to measure all locations from the same point. Next, we must break our complex shape down into several simpler shapes. This may include areas or volumes (which we will count as positive areas or volumes) or holes (which we will count as negative areas or volumes). Each of these shapes will have a centroid (\(C\)) or center of mass (\(G\)) listed on the diagram.
Once we have identified the different parts, we will create a table listing the area or volume of each piece, and the \(x\) and \(y\) centroid coordinates (or \(x\), \(y\), and \(z\) coordinates in 3D). It is important to remember that each coordinate you list should be relative to the same base origin point that you drew in earlier. You may need to mentally adjust diagrams in the centroid tables so that the shape is oriented in the right direction, and account for the placement of the shape relative to the axes in your diagram.
Once you have the areas and centroid coordinates for each shape relative to your origin point, you can find the \(x\) and \(y\) coordinate of the centroid for the overall shape with the following formulas. Remember that areas or volumes for any shape that is a hole or cutout in the design will be a negative area in your formula.
\[ \bar{x}_{total} = \frac{\sum A_i \bar{x}_i}{A_{total}} \quad\quad\quad \bar{y}_{total} = \frac{\sum A_i \bar{y}_i}{A_{total}} \]
This generalized formula to find the centroid's \(x\)-location is simply Area 1 times \(\bar{x}_1\), plus Area 2 times \(\bar{x}_2\), plus Area 3 times \(\bar{x}_3\), adding up as many shapes as you have in this fashion and then dividing by the overall area of your combined shape. The equations are the same for the \(y\)-location of the overall centroid, except you will instead be using \(\bar{y}\) values in your equations.
For centroids in three dimensions we will simply use volumes in place of areas, and we will have a \(z\) coordinate for our centroid as well as the \(x\) and \(y\) coordinates.

## Finding the Center of Mass via the Method of Composite Parts

To use the method of composite parts to find the center of mass, we simply need to adjust the process slightly. First, center of mass calculations will always be in three dimensions. Draw an origin point and some axes on your diagram we did for the centroid. We will measure all locations relative to this origin point. We will then need to break the complex shape down into simple volumes, with each simple volume being something in the centroid table we have available. Remember that when we have a part with a uniform material, the centroid and center of mass are the same point, so we will often talk about these interchangeably.
Once we have identified the different parts, we will create a table indicating the mass of each part, and the x, y, and z coordinate of the center of mass for each individual part. It is important to remember that each coordinate you list should be relative to the same base origin point, so you will need to mentally rotate and position the parts in the table on your axes.
One complicating factor with mass can be measuring the mass of the pieces separately. If we have a scale, we may simply know the overall mass without knowing the mass of the individual pieces. In these cases, you may need work backwards to calculate the density of the material (by dividing the overall mass by overall volume), and then use density times piece volume to find the mass of each piece individually. When doing this, remember to count cutouts as negative mass in your calculations. For example, for the hollow cylinder in the shape above, you would find the mass of a solid cylinder for Shape 2, then have a negative mass for the cylindrical cutout for Shape 3.
Finally, once you have the mass the and center of mass coordinates for each shape, you can find the coordinates of the center of mass for the overall volume with the following formulas.
\[ x_G = \frac{\sum m_i \bar{x}_i}{m_{total}} \quad\quad y_G = \frac{\sum m_i \bar{y}_i}{m_{total}} \quad\quad z_G = \frac{\sum m_i \bar{z}_i}{m_{total}} \]
Similar to the centroid equations, the \(x\)-equation is simply the mass of Shape 1 times \(\bar{x}_1\), plus the mass of Shape 2 times \(\bar{x}_2\), and so on for each part. After you have summed up these products for all the shapes, just divide by the total mass.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.
Example \(\)
Find the \(x\) and \(y\) coordinates of the centroid of the shape shown below.
Example \(\)
The shape shown below consists of a solid semicircular hemisphere on top of a hollow cylinder. Based on the dimensions below, determine the location of the centroid.
Example \(\)
A spherical steel tank (density = 8050 kg/m3) is filled halfway with water (density = 1000 kg/m3) as shown below. Find the overall mass of the tank and the current location of the center of mass of the tank (measured from the base of the tank).

## 17.5: Area Moments of Inertia via Integration

- Bending Stresses and the Second Area MomentCalculating the Rectangular Area Moment of Inertia via Integration
- Calculating the Rectangular Area Moment of Inertia via Integration
- Torsional Stresses and the Polar Moment of Inertia
- Calculating the Polar Area Moment of Inertia via Integration
Area moments of inertia are used in engineering mechanics courses to determine a body's resistance to bending loads or torsional loads. Specifically, the area moment of inertia refers to the second area moment integral of a shape, with \(I_{xx}\) representing the moment of inertia about the \(x\)-axis, \(I_{yy}\) representing the moment of inertia about the \(y\)-axis, and \(J_{zz}\) (also called the polar moment of inertia) representing the moment of inertia about the \(z\)-axis. The moment of inertia about each axis represents the shapes resistance to a moment applied about that respective axis. Moments about the \(x\)- and \(y\)-axes would tend to bend an object, while moments about the \(z\)-axis would tend to twist the body.
Just as with centroids, each of these moments of inertia can be calculated via integration or by using the method of composite parts and the parallel axis theorem. On this page we are going to focus on calculating the area moments of inertia via moment integrals.

## Bending Stresses and the Second Area Moment

When an object is subjected to a bending moment, that body will experience both internal tensile stresses and compressive stresses as shown in the diagram below. These stresses exert a net moment to counteract the loading moment, but exert no net force so that the body remains in equilibrium.
As we can see in the diagram, there is some central plane along which there are no tensile or compressive stresses. This is known as the neutral surface, and if there are no other forces present it will run through the centroid of the cross section. As we move up or down from the neutral surface, the stresses increase linearly. The moment exerted by this stress at any point will be the stress times the moment arm, which also linearly increases as we move away from the neutral surface. This means that the resistance to bending provided by any point in the cross section is directly proportional to the distance from the neutral axis squared. We can sum up the resistances to bending then by using the second rectangular area moment of inertia, where our distances are measured from the neutral axis.
\[ I = \int_A (dA * d^2) \] Assuming we put the origin point at the centroid and that the \(x\)-axis is the neutral surface, the distance from the neutral surface to any point is simply the \(y\) coordinate of that point. Similarly, if we apply a moment about the \(y\)-axis, and had a neutral surface that ran along the \(y\)-axis, the distance from the neutral axis would simply be the \(x\) coordinate of the point. For this reason, \(I_{xx}\) includes \(y\) as the distance, while \(I_{yy}\) includes \(x\) as the distance.
\[ I_{xx} = \int_{y_{min}}^{y_{max}} (dA * y^2) \quad\quad\quad I_{yy} = \int_{x_{min}}^{x_{max}} (dA * x^2) \]

### Calculating the Rectangular Area Moment of Inertia via Integration

To determine the area moment of inertia, start by drawing out the area under analysis, and include the axes you are taking the moment of inertia about. This is important, since the moment of inertia will vary depending on the axis chosen. In cases on bending stresses you will want to put the origin on the neutral surface, which will be at the centroid of the area. If the centroid is not given to you, you will need to determine the centroid as discussed in prior sections.
To take the moment of inertia about the \(x\)-axis through this point (\(I_{xx}\)) we will use the general formula discussed earlier. We will be moving from bottom to top, integrating the rate of change of the area as we go, and multiplying that by the \(y\)-value squared. The rate of change of area (\(dA\)) as we move upwards will be the width of the object at any given \(y\)-value times the rate at which we are moving. Unless the width remains constant, the width will need to be represented as a mathematical function in terms of \(y\).
To find the moment of inertia about the \(y\)-axis through a given point (\(I_{yy}\)) we will move left to right, using the distances from the \(y\)-axis in our moment integral (in this case the \(x\) coordinates of each point). Moving from left to right, the rate of change of the area will be the height of the shape at any given \(x\)-value times the rate at which we are moving left to right. Again, we will need to describe this with an mathematical function if the height is not constant. We will multiply this function by the \(x\)-value squared for the second moment integral, and this will give us the moment of inertia about the \(y\)-axis.

## Torsional Stresses and the Polar Moment of Inertia

When an object is subjected to a torsional moment, that object will experience internal shearing forces as shown in the diagram below. These stresses are oriented in such a way that they will counteract the torsional moment, but do not exert any net force on the shaft so that shaft stays in equilibrium.
As we can see in the diagram, there is a central axis along which there are no shearing stresses. This is known as the neutral axis, and if there are no other forces present, then this will travel through the centroid of the shaft's cross section. As we move away from the neutral axis in any direction, the stresses will increase linearly. The moment exerted by the stress at any point will be the stress times the moment arm, which also increases linearly as we move away from the neutral axis. This means that the resistance to torsional loading provided by any one point on the cross section is directly proportional the square of the distance between the point and neutral axis. We can sum up the resistances to torsional loading then using the second polar area moment of inertia, where our distances are measured from the neutral axis (\(r\)), a single point in the shaft's cross-section.
\[ J_{zz} = \int_{r_{min}}^{r_{max}} (dA * r^2) \]

## Calculating the Polar Area Moment of Inertia via Integration

The first step in determining the polar moment of inertia is to draw the area and identify the point about which we are taking the moment of inertia. In the case of torsional loading, we will usually want to pick the point at which the neutral axis travels through the shaft's cross section, which in the absence of other types of loading will be the centroid of the cross section. If the centroid is not clearly identified, you will need to determine the centroid as discussed in previous sections.
To take the moment of inertia about this central point, we will be measuring all distances outward from this point. Rather than moving left to right or top to bottom, we will instead be integrating from the center radiating outward in all directions. We will be going from the minimum distance from the center for our shape (zero unless there is a central hole in our area) to the maximum distance to the center. We will again be integrating the rate of change of area, which in this case will be a function for the circumference at a given radius times the rate as which we are moving outwards times the given radius squared.
Example \(\)
Find the rectangular moments of inertia for this shape about both the \(x\)-axis and \(y\)-axis though the centroid. Leave the answer in terms of the generic width (\(b\)) and height (\(h\)) of the rectangle.
Example \(\)
Find the polar moments of inertia for this circular area about its centroid. Leave the answer in terms of the generic radius \(R\).
Exercise \(\)
Find the polar moment of inertia of this hollow circular shape about its centroid.

## 17.6: Mass Moments of Inertia via Integration

- The Mass Moment of Inertia and Angular Accelerations
- Calculating the Mass Moment of Inertia via Integration
The mass moment of inertia represents a body's resistance to angular accelerations about an axis, just as mass represents a body's resistance to linear accelerations. This is represented in an equation with the rotational version of Newton's Second Law.
\[ F = ma \]
\[ M = I \alpha \]
Just as with area moments of inertia, the mass moment of inertia can be calculated via moment integrals or via the method of composite parts and the parallel axis theorem. This page will only discuss the integration method, as the method of composite parts is discussed on a separate page.

## The Mass Moment of Inertia and Angular Accelerations

The mass moment of inertia is a moment integral, specifically the second polar mass moment integral. To see why this relates moments and angular accelerations, we start by examining a point mass on the end of a massless stick as shown below. Imagine we want to rotate the stick about the left end by applying a moment there. We want to relate the moment exerted to the angular acceleration of the stick about this point.
To relate the moment and the angular acceleration, we need to start with the traditional form of Newton's Second Law, stating that the force exerted on the point mass by the stick will be equal to the mass times the acceleration of the point mass (\(F = m*a\)). In this case the moment will be related to the force in that the force exerted on the mass times the length of the stick (\(d\)) is equal to the moment. We can also relate the linear acceleration of the mass to its rotational counterpart in that the linear acceleration is the angular acceleration times the length of the rod (\(d\)). If we take these two substitutions and put them into the original \(F = m*a\) equation, we can wind up with an equation that relates the moment and the angular acceleration for our scenario. A simplified version of this new relationship states that the moment will be equal to the mass times the distance squared times the angular acceleration. This mass-times-distance-squared term (relating the moment and angular acceleration) forms the basis for the mass moment of inertia.
\[ F = m * a \]
\[ M = F * d \quad\quad\quad a = d * \alpha \]
\[ M = (m * d^2) * \alpha \]
Taking our situation one step further, if we were to have multiple masses all connected to a central point, the moment and angular acceleration would be related by the sum of all the mass times distance squared terms.
\[ M = \sum (m * d^2) * \alpha \]
Taking the final step, rigid bodies with mass distributed over a volume are like an infinite number of small masses about an axis of rotation. Rather than the massless sticks holding everything in place, the mass is simply held in place by the material around it. To relate the moment and angular acceleration in this case, we use integration to add up the infinite number of small mass-times-distance-squared terms.
\[ M = \int_m (dm * d^2) * \alpha \]
This moment integral which can be calculated for any given shape, called the mass moment of inertia, relates the moment and the angular acceleration for the body about a set axis of rotation.
\[ I = \int_m (dm * d^2) \]

## Calculating the Mass Moment of Inertia via Integration

The first step in calculating the mass moment of inertia is to determine the axis of rotation you will be using. Unlike mass, the mass moment of inertia is dependent upon the point and axis that we are rotating about. We can easily demonstrate this with something like a broomstick, where depending on the position and the direction of the axis we are rotating about, the broomstick can be more or less difficult to rotate.
After choosing the axis of rotation, it is helpful to draw the shape with the axis of rotation included. This is a polar integral, so we will be taking the mass integral radiating outwards from this axis of rotation.
Also, we are integrating over the mass, and the mass at any given point will be the density times the volume. If the object we are examining has a uniform density, as is often the case, we can pull that density constant outside of the integral, leaving only a integral of the volume. Density is rarely given in these instances, but if you can determine the overall mass and overall volume you can use that as well. If we put all of this into the original equation we had above, we wind up with the following.
\[ I = \rho * \int_{r_{min}}^{r_{max}} (dV * r^2) = \frac{m}{V} * \int_{r_{min}}^{r_{max}} (dV * r^2) \]
For the polar integral, we need to define \(dV\) in terms of a radius (\(r\)) moving outwards from the axis of rotation. The rate of change of the volume (\(dV\)) will be the cylindrical surface area at a given radius times the rate at which that radius is increasing (\(dr\)). The height, radius, and holes in this cylindrical surface may all be changing so this \(dV\) term may become quite complex, but technically we could find this for mathematical function for any shape. Once we have the \(dV\) function in terms of \(r\), we multiply that function by \(r^2\) and we will evaluate the integral.
Example \(\)
A thin circular disk has a mass of 6 kg and a radius of 0.3 meters. Determine the mass moment of inertia for the disk about the \(z\)-axis.
Example \(\)
Determine the mass moment of inertia about the \(z\)-axis for this general cone with base radius \(R\), height \(h\), and mass \(m\).

## 17.7: Moments of Inertia via Composite Parts and Parallel Axis Theorem

- The Parallel Axis Theorem
- Using the Method of Composite Parts to Find the Moment of Inertia
As an alternative to integration, both area and mass moments of inertia can be calculated via the method of composite parts, similar to what we did with centroids. In this method we will break down a complex shape into simple parts, look up the moments of inertia for these parts in a table, adjust the moments of inertia for position, and finally add the adjusted values together to find the overall moment of inertia. This method is known as the method of composite parts.
A key part to this process that was not present in centroid calculations is the adjustment for position. As discussed on the previous pages, the area and mass moments of inertia are dependent upon the chosen axis of rotation. Moments of inertia for the parts of the body can only be added when they are taken about the same axis. However, the moments of inertia in the table are generally listed relative to that shape's centroid. Because each part has its own individual centroid coordinate, we cannot simply add these numbers. We will use something called the Parallel Axis Theorem to adjust the moments of inertia so that they are all taken about some standard axis or point. Once the moments of inertia are adjusted with the Parallel Axis Theorem, then we can add them together using the method of composite parts.

## The Parallel Axis Theorem

When we calculated the area and mass moments of inertia via integration, one of the first things we had to do was to select a point or axis we were going to take the moment of inertia about. We then measured all distances from that point or axis, where the distances were the moment arms in our moment integrals. Because the centroid of a shape is the geometric center of an area or volume, the average distance from the centroid to any one point in a body is at a minimum. If we pick a different point or axis to take the moment of inertia about, then on average all the distances in our moment integral will be a little bit bigger. Specifically, the further we move from the centroid, the larger the average distances become.
Though this complicates our analysis, the nice thing is that the change in the moment of inertia is predictable. It will always be at a minimum when we take the moment of inertia about the centroid, or an axis going through the centroid. This minimum, which we will call \(I_C\), is the value we will look up in our moment of inertia table. From this minimum, or unadjusted value, we can find the moment of inertia value about any point \(I_P\) by adding an an adjustment factor equal to the area times distance squared for area moments of inertia, or mass times distance squared for mass moments of inertia.
\[ I_{xxP} = I_{xxC} + A * r^2 \]
\[ I_{xxP} = I_{xxC} + m * r^2 \]
This adjustment process with the equations above is the parallel axis theorem. The area or mass terms simply represent the area or mass of the part you are looking at, while the distance (\(r\)) represents the distance that we are moving the axis about which we are taking the moment of inertia. This may be a vertical distance, a horizontal distance, or a diagonal depending on the axis the moment of inertia is taken about.
Say we are trying to find the moments of inertia of the rectangle above about point \(P\). We would start by looking up \(I_{xx}\), \(I_{yy}\), and \(J_{zz}\) about the centroid of the rectangle (\(C\)) in the moment of inertia table. Then we would add on an area-times-distance-squared term to each to find the adjusted moments of inertia about \(P\). The distance we are moving the \(x\) axis for \(I_{xx}\) is the vertical distance \(r_x\), the distance we are moving the \(y\)-axis for \(I_{yy}\) is the horizontal distance \(r_y\), and the distance we would move the \(z\)-axis (which is pointing out of the page) for \(J_{zz}\) is the diagonal distance \(r_z\).
Center of mass adjustments follow a similar logic, using mass times distance squared, where the distance represents how far you are moving the axis of rotation in three-dimensional space.

## Using the Method of Composite Parts to Find the Moment of Inertia

To find the moment of inertia of a body using the method of composite parts, you need to start by breaking your area or volume down into simple shapes. Make sure each individual shape is available in the moment of inertia table, and you can treat holes or cutouts as negative area or mass.
Next you are going to create a table to keep track of values. Devote a row to each part that your numbered earlier, and include a final "total" row that will be used for some values. Most of the work of the method of composite parts is filling in this table. The columns will vary slightly with what you are looking for, but you will generally need the following.
- The area or mass for each piece (area for area moments of inertia or mass for mass moments of inertia). Remember that cutouts should be listed as negative areas or masses.
- The centroid or center of mass locations (\(x\), \(y\) and possibly \(z\) coordinates). Most of the time, we will be finding the moment of inertia about centroid of the composite shape, and if that is not explicitly given to you, you will need to find that before going further. For more details on this, see the page Centroids and Centers of Mass via Method of Composite Parts.
- The moment of inertia values about each shape's centroid. To find these values you will plug numbers for height, radius, mass, etc. into formulas on the moment of inertia table. Do not use these formulas blindly though, as you may need to mentally rotate the body, and thus switch equations, if the orientation of the shape in the table does not match the orientation of the shape in your diagram.
- The adjustment distances (\(r\)) for each shape. For this value you will want to determine how far the \(x\)-axis, \(y\)-axis, or \(z\)-axis moves to go from the centroid of the piece to the overall centroid or point you are taking the moment of inertia about. To calculate these values, generally you will be finding the horizontal, vertical, or diagonal distances between piece centroids and the overall centroids that you have listed earlier in the table. See the parallel axis theorem section of this page earlier for more details.
- Finally, you will have a column of the adjusted moments of inertia. Take the original moment of inertia about the centroid, then simply add your area times \(r^2\) term or mass times \(r^2\) term for this adjusted value.
The overall moment of inertia of your composite body is simply the sum of all of the adjusted moments of inertia for the pieces, which will be the sum of the values in the last column (or columns, if you are finding the moments of inertia about more than one axis).
Video \(\): Video lecture covering this section, delivered by Dr. Jacob Moore. YouTube source: https://youtu.be/zulGTSWF6xs.
Example \(\)
Use the parallel axis theorem to find the mass moment of inertia of this slender rod with mass \(m\) and length \(L\) about the \(z\)-axis at its endpoint.
Video \(\): Worked solution to example problem \(\), provided by Dr. Jacob Moore. YouTube source: https://youtu.be/4oN0kgDO3Yw.
Example \(\)
A beam is made by connecting two 2" x 4" beams in a T-pattern with the cross section as shown below. Determine the location of the centroid of this combined cross section and then find the rectangular area moment of inertia about the \(x\)-axis through the centroid point.
Video \(\): Worked solution to example problem \(\), provided by Dr. Jacob Moore. YouTube source: https://youtu.be/lgXlp2lRaiA.
Example \(\)
A dumbbell consists of two spheres of diameter 0.2 meter, each with a mass of 40 kg, attached to the ends of a 0.6-meter-long slender rod of mass 20 kg. Determine the mass moment of inertia of the dumbbell about the \(y\)-axis shown in the diagram.
Video \(\): Worked solution to example problem \(\), provided by Dr. Jacob Moore. YouTube source: https://youtu.be/ufewJ7CmvIs.

## 17.8: Appendix 2 Homework Problems

Exercise \(\)
A shape is bounded on the left by the \(y\)-axis, on the bottom by the \(x\)-axis, and along its remaining side by the function \(y = - \dfrac{1}{2} x^2 + 8\). Determine the \(x\) and \(y\) coordinates of the centroid of this shape via integration. (Hint: for \(\bar{y}\), work from the top down to make the math easier.)
\(\bar{x} = 1.5 \ cm, \, \bar{y} = 3.2 \ cm\)
Exercise \(\)
Determine the \(x\) and \(y\) coordinates of the centroid of the shape shown below via integration.
\(\bar{x} = 2.94 \ in, \, \bar{y} = 4.24 \ in.\)
Exercise \(\)
A water tank as shown below takes the form of an inverted, truncated cone. The diameter of the base is 4 ft, the diameter of the top is 8 ft, and the height of the tank is 4 ft. Using integration, determine the height of the center of mass of the filled tank. (Assume the tank is filled with water and the walls have negligible mass.)
\(z_c = 2.43 \ ft\)
Exercise \(\)
Use the method of composite parts to determine the centroid of the shape shown below.
\(x_c = 1.14 \ in, \, y_c = 1.39 \ in\)
Exercise \(\)
A floating platform consists of a square piece of plywood weighing 50 lbs with a negligible thickness on top of a rectangular prism of a foam material weighing 100 lbs as shown below. Based on this information, what is the location of the center of mass for the floating platform?
\(x_c = 3.33 \ ft, \, y_c = 1.33 \ ft, \, z_c = 2 \ ft\)
Exercise \(\)
Use the integration method to find the moments of inertia for the shape shown below…
- About the \(x\)-axis through the centroid.
- About the \(y\)-axis through the centroid.
\(I_{xx} = 6.075 * 10^{-7} \ m^4\)
\(I_{yy} = 5.0625 * 10^{-8} \ m^4\)
Exercise \(\)
Use the integration method to find the polar moment of inertia for the semicircle shown below about point O.
\(J_{zz} = 1017.9 \ in^4\)
Exercise \(\)
A plastic beam has a square cross-section with semicircular cutouts on the top and bottom as shown below. What is the area moment of inertia of the beam’s cross section about the \(x\) and \(y\) axes through the center point?
\(I_{xx} = 7.08 \ in^4, \, I_{yy} = 17.36 \ in^4\)
Exercise \(\)
A piece of angled steel has a cross section that is 1 cm thick and has a length of 6 cm on each side as shown below. What are the \(x\) and \(y\) area moments of inertia through the centroid of the cross section?
\(I_{xx} = I_{yy} = 35.462 \ cm^4 = 3.546 * 10^{-7} \ m^4\)
Exercise \(\)
The pendulum in an antique clock consists of a brass disc with a mass of 0.25 kg and diameter of 6 cm at the end of a slender wooden rod with a mass of 0.1 kg. Determine the mass moment of inertia of the pendulum about the top of the rod.
\(I_{zz} = 0.02026 \ kg \ m^2\)
Exercise \(\)
A space telescope can be approximated as a 600-kg cylinder with a 4-meter diameter and 4-meter height attached to two 100-kg solar panels as shown below. What is the approximate mass moment of inertia for the space telescope about the \(y\)-axis shown?
\(I_{yy} = 10,216.7 \ kg \ m^2\)
Exercise \(\)
A flywheel has an original weight of 15 pounds and a diameter of 6 inches. To reduce the weight, four two-inch diameter holes are drilled into the flywheel, each leaving half an inch to the outside edge as shown below. What was the original polar mass moment of about the center point? Assuming a uniform thickness, what is the new mass moment of inertia after drilling in the holes? (Hint: holes count as negative mass in the mass moment calculations.)
\(J_{without holes} = 0.01456 \ slug \ ft^2\)
\(J_{with holes} = 0.01060 \ slug \ ft^2\)
17.8: Appendix 2 Homework Problems is shared under a not declared license and was authored, remixed, and/or curated by LibreTexts.
- Back Matter

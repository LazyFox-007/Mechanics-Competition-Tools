来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 04 4: Statically Equivalent Systems

## 4: Statically Equivalent Systems

## 4.0: Video Introduction to Chapter 4

- 4: Statically Equivalent Systems      4.1: Statically Equivalent Systems
- 4: Statically Equivalent Systems

## 4.1: Statically Equivalent Systems

- Determining if Forces are Statically Equivalent:
- Finding a Single Equivalent Point Force:
Two sets of forces are considered statically equivalent if they cause the same set of reaction forces on a body. Because this is true, the two statically equivalent sets of forces are interchangeable in statics analysis.

## Determining if Forces are Statically Equivalent:

To determine if two sets of forces are statically equivalent, you must solve for the reaction forces in both cases. If the reaction forces are the same then the two sets of forces must be statically equivalent. For any one set of forces, there are an infinite number of sets of forces that are statically equivalent to original set of forces.

## Finding a Single Equivalent Point Force:

In statics analysis, we are usually looking to simplify a problem by turning multiple forces into a single, statically equivalent force. To find a single point force that is equivalent to multiple point forces you can use the following procedure.
- Solve for the reaction forces in the original scenario.
- Draw a new free body diagram with these reaction forces. You will also add one force with an unknown magnitude, direction, and point of application to your diagram. This is the single point load that will be equivalent to your original set of forces.
- Write out the equations of equilibrium for this scenario, including the known values for the reaction forces.
- First, solve the force equations to find the \(x\) and \(y\) components of this unknown force (or \(x\), \(y\) and \(z\) components for a 3D problem). This can be used to find the magnitude and direction of the statically equivalent point force.
- Next, use the moment equation (or equations, for 3D problems) to determine the location of the statically equivalent point force.
Example \(\)
Determine if the two sets of forces shown below are statically equivalent.

## 4.2: Resolution of a Force into a Force and a Couple

As discussed on the sections on moments, a force can have a tendency to cause both a linear and angular acceleration. For example, below is diagram of a force acting on an extended body. If we were to think about everything relative to the center of mass of this body, there would be some force acting on the center of mass that would cause the same linear acceleration and some pure moment (couple) that would cause the same angular acceleration. This would be a force and couple that is statically equivalent to the original force, though the point of application of the force changes.
The process of transforming one force applied at one point, into a force and a couple at some other point is known as resolving a force into a force and a couple. There are a few reasons that we may want to do this, but one primary reason is to find the equivalent force couple system for a complex set of forces and moments. The equivalent force couple system is used to simplify more complex analysis, and consists of a single force and a single pure moment (couple) that are statically equivalent to some more complex combination of forces and moments. An important first step in finding the equivalent force couple system is to resolve all the forces so that everything is acting at the same point.
In order to visualize the process of resolving a force into a force and a couple, you can use the process outlined in the diagram below. Imagine we have a body with a force acting at some point A. We want to resolve the force into a force and a couple about some other point B. To do this we will first add two forces to the diagram at point B. One will have the same magnitude and direction as the original force and the other will be equal and opposite to the original force. Because these two forces are equal, opposite, and collinear, this will not change the situation (it's the equivalent to adding zero to an equation). Now, with these three forces acting on the diagram, we can break it down into two sets. The first is a force acting at point B with the same magnitude and direction as the original force. The other two forces act as a couple, exerting a pure moment about point B. Finally, we can redraw the system as a force acting at point B and the pure moment acting about point B.
As a shortcut to the process described above, we can also see that the force in the equivalent force couple system will always have a magnitude and direction equal to the original force and the couple will be equal to the moment exerted by the original force about the new point of application.
Example \(\)
Resolve the force shown below to a force and a couple acting at point A.
Example \(\)
Resolve the force shown below to a force and a couple acting at point A.

## 4.3: Equivalent Force Couple System

Every set of forces and moments has an equivalent force couple system. This is a single force and pure moment (couple) acting at a single point that is statically equivalent to the original set of forces and moments.
To find the equivalent force couple system, you simply need to follow the steps below.
- First, choose a point to take the equivalent force couple system about. Any point will work, but the point you choose will affect the final values you find for the equivalent force couple system. Traditionally, this point will either be the center of mass of the body or some connection point for the body.
- Next, resolve all the forces not acting though that point to a force and a couple acting at the point you chose.
- To find the "force" part of the equivalent force couple system, add together all the force vectors. This will give you the magnitude and the direction of the force in the equivalent force couple system.
- To find the "couple" part of the equivalent force couple system, add together any moment vectors (this could be moments originally acting on the body, or moments from the resolution of the forces into forces and couples). This will give you the magnitude and direction of the pure moment (couple) in the equivalent force couple system.
Example \(\)
Find the equivalent force couple system for the forces shown below about point A.

## 4.4: Distributed Forces

- Representing Distributed Forces:
- Analyzing Distributed Forces:
A distributed force is any force where the point of application of the force is an area or a volume. This means that the "point of application" is not really a point at all. Though distributed forces are more difficult to analyze than point forces, distributed forces are quite common in real world systems so it is important to understand how to model them.
Distributed forces can be broken down into surface forces and body forces. Surface forces are distributed forces where the point of application is an area (a surface on the body). Body forces are forces where the point of application is a volume (the force is exerted on all molecules throughout the body). Below are some examples of surface and body forces.

## Representing Distributed Forces:

Distributed forces are represented as a field of vectors. This is drawn as a number of discrete vectors along a line, over a surface, or over a volume, that are connected with a line or a surface as shown below.
Though these representations show a discrete number of individual vectors, there is actually a magnitude and direction at all points along the line, surface, or body. The individual vectors represent a sampling of these magnitudes and directions.
It is also important to realize that the magnitudes of distributed forces are given in force per unit distance, area, or volume. We must integrate the distributed force over its entire range to convert the force into the usual units of force.

## Analyzing Distributed Forces:

For analysis purposes in statics and dynamics, we will usually substitute in a single point force that is statically equivalent to the distributed force in the problem. This single point force is called the equivalent point load, and it will cause the same accelerations or reaction forces as the distributed force while simplifying the math. However, in analysis that focuses on the strength of materials where the bodies are not rigid, this substitution will not work as the distributed forces will not cause the same deformations and stresses as the point force.

## 4.5: Equivalent Point Load

- Finding the Equivalent Point Load
- Using Integration in 2D Surface Force Problems:
- Using the Area and Centroid in 2D Surface Force Problems:
- Using Integration in 3D Surface Force Problems:
- Using Volume and Center of Volume in 3D Surface Force Problems:
- Using Integration in Body Force Problems:
An equivalent point load is a single point force that will have the same effect on a body as the original loading condition, which is usually a distributed force. The equivalent point load should always cause the same linear acceleration and angular acceleration as the original force it is equivalent to (or cause the same reaction forces if the body is constrained). Finding the equivalent point load for a distributed force often helps simplify the analysis of a system by removing the integrals from the equations of equilibrium or equations of motion in later analysis.

## Finding the Equivalent Point Load

When finding the equivalent point load, we need to find the magnitude, direction, and point of application of a single force that is equivalent to the distributed force we are given. In this course we will only deal with distributed forces with a uniform direction, in which case the direction of the equivalent point load will match the uniform direction of the distributed force. This leaves the magnitude and the point of application to be found. There are two options available to find these values:
- We can find the magnitude and the point of application of the equivalent point load via integration of the force functions.
- We can use the area/volume and the centroid/center of volume of the area or volume under the force function.
The first method is more flexible, allowing us to find the equivalent point load for any force function that we can make a mathematical formula for (assuming we have the skill in calculus to integrate that function). The second method is usually faster, assuming that we can look up the values for the area or volume under the force curve and the values for the centroid or center of volume for the area under the curve.

## Using Integration in 2D Surface Force Problems:

Finding the equivalent point load via integration always begins by determining the mathematical formula that is the force function. The force function mathematically relates the magnitude of the force \((F)\) to the position \((x)\). In this case the force is acting along a single line, so the position can be entirely determined by knowing the \(x\) coordinate, but in later problems we may also need to relate the magnitude of the force to the \(y\) and \(z\) coordinates. In our example above, we can relate magnitude of the force to the position by stating that the magnitude of the force at any point in Newtons per meter is equal to the \(x\) position in meters plus one.
The magnitude of the equivalent point load will be equal to the area under the force function. This will be the integral of the force function over its entire length (in this case, from \(x = 0\) to \(x = 2\)).
\[ F_{eq} = \int\limits_{x \, min}^{x \, max} F(x) \, dx \]
Now that we have the magnitude of the equivalent point load such that it matches the magnitude of the original force, we need to adjust the position \((x_{eq})\) such that it would cause the same moment as the original distributed force. The moment of the distributed force will be the integral of the force function \((F(x))\) times the moment arm about the origin \((x)\). The moment of the equivalent point load will be equal to the magnitude of the equivalent point load that we just found times the moment arm for the equivalent point load \((x_{eq})\). If we set these two things equal to one another and then solve for the position of the equivalent point load \((x_{eq})\) we are left with the following equation.
\[ x_{eq} = \frac{\int\limits_{x \, min}^{x \, max} (F(x) * x) \, dx}{F_{eq}} \]
Now that we have the magnitude, direction, and position of the equivalent point load, we can draw the point load in our original diagram. This point force can be used in place of the distributed force in further analysis.

## Using the Area and Centroid in 2D Surface Force Problems:

As an alternative to using integration, we can use the area under the force curve and the centroid of the area under the force curve to find the equivalent point load's magnitude and point of application respectively.
The magnitude \((F_{eq})\) of the equivalent point load will be equal to the area under the force function. We can find this area using calculus, but there are often easier geometry-based ways of finding the area under the force function.
The equivalent point load will also travel through centroid of the area under the force function. This allows us to find the value for \(x_{eq}\). The centroid for many common shapes can be looked up in tables, and the parallel axis theorem can be used to determine the centroid of more complex shapes (see the Appendix page on centroids for more details).

## Using Integration in 3D Surface Force Problems:

With surface force in a 3D problem, the force is distributed over a surface, rather than along a single line. To find the magnitude of the equivalent point load we will again start by finding the mathematical equation for the force function. Because the force is distributed over an area rather than just a line, the magnitude of the force may be related to both the \(x\) and the \(y\) coordinate, rather than just the \(x\) coordinate as before.
The magnitude of the equivalent point load \((F_{eq})\) will be equal to the volume under the force curve. To calculate this value we will integrate the force function over the area that the force is applied to. To integrate this function \(F(x,y)\) in terms of the area, we will need to break the integral down further, integrating over \(x\) and then integrating over \(y\).
\[ F_{eq} = \int F(x,y) \, dA = \int\limits_{y \, min}^{y \, max} \left( \, \int\limits_{x \, min}^{x \, max} F(x,y) \, dx \right) \, dy \]
Once we solve for the magnitude of the equivalent point load, we can then solve for the position of the equivalent point load. Since the force is spread over a surface, we will need to calculate both the \(x\) \((x_{eq})\) and the \(y\) \((y_{eq})\) coordinates for the position. The process for solving for these values is similar to what was done with only an \(x\) value, except we change the moment arm value to match the equivalent point load coordinate we are looking for.
\[ x_{eq} = \frac{\int (F(x,y) * x) \, dA}{F_{eq}} \]
\[ y_{eq} = \frac{\int (F(x,y) * x) \, dA}{F_{eq}} \]
In each of the equations above, we will need to expand out the area integral into \(x\) and \(y\) integrals (as we did for \(F_{eq}\)) in order to be able to solve them.

## Using Volume and Center of Volume in 3D Surface Force Problems:

Just as in the 2D problems, there are some available shortcuts to finding the equivalent point load in 3D surface force problems. For a force spread over an area, the magnitude \((F_{eq})\) of the equivalent point load will be equal to the volume under the force function. The equivalent point load will also travel through the center of volume of the volume under the force function. This should allow you to determine both \(x_{eq}\) and \(y_{eq}\).
The center of volume for a shape will be the same as the center of mass for a shape if the shape is assumed to have uniform density. It should be possible to look these values up for common shapes in a table. Again, the parallel axis theorem can be used to find the center of volume for more complex shapes (See the Center of Mass page in Appendix 2 for more details).

## Using Integration in Body Force Problems:

When we jump to body forces, the magnitude of our force will vary with \(x\), \(y\), and \(z\) coordinates. This means that our force function can include all of these variables \((F(x,y,z))\). To find the magnitude of the equivalent point load we integrate over the volume, breaking the volume integral down into \(x\), \(y\), and then \(z\) integrals.
 F_{eq} &= \int F(x,y,z) \, dV \\ &= \int\limits_{z \, min}^{z \, max} \left( \, \int\limits_{y \, min}^{y \, max} \left( \, \int\limits_{x \, min}^{x \, max} F(x,y,z) \, dx \right) \, dy \right) \, dz
To find the point of application of the equivalent point load, we will need to find all three coordinate positions. To do this, we will expand out the equations we used with two coordinates to include the third coordinate \((z_{eq})\).
\[ x_{eq} = \frac{\int (F(x,y,z) * x) \, dV}{F_{eq}} \]
\[ y_{eq} = \frac{\int (F(x,y,z) * y) \, dV}{F_{eq}} \]
\[ z_{eq} = \frac{\int (F(x,y,z) * z) \, dV}{F_{eq}} \]
Example \(\)
Determine the magnitude and the point of application for the equivalent point load of the distributed force shown below.
Example \(\)
Determine the magnitude and the point of application for the equivalent point load of the distributed force shown below.
Example \(\)
Determine the magnitude and the point of application for the equivalent point load of the distributed force shown below.
Example \(\)
The wind has piled up sand into a corner on a building. The building supervisor is worried about the weight of the sand pushing against the roof of the basement below. The function describing force of the sand pushing down on the surface is given below. Find the magnitude, direction and point of application of the equivalent point load for the distributed force of the sand. Draw the equivalent point load in a diagram.

## 4.6: Chapter 4 Homework Problems

Exercise \(\)
Determine if the two systems below are statically equivalent.
No, they are not equivalent.
Exercise \(\)
Determine if the set of forces in A is statically equivalent to the set of forces and moments in B.
No, they are not equivalent.
Exercise \(\)
Resolve the force shown below into a force and a couple acting at point A. Draw this force and couple on a diagram of the L-shaped beam.
\(F_A = 150 \, N\) to the left
\(M_A = 450 \, Nm\)
Exercise \(\)
Find the equivalent force couple system acting at point A for the setup shown below. Draw this force and couple on a diagram of the L-shaped beam.
\(F_A = 155.2 \, lbs, \, 69.5\)° below the negative \(x\)-axis
\(M_A = -556.9 \, ft \, lbs\)
Exercise \(\)
A helicopter is hovering with the wind force, the force from the tail rotor, and the moment due to drag shown below. Determine the equivalent force couple system at point C. Draw the final force and moment on a new diagram of the helicopter.
\(F_{eq} = 858.01 \, N\) acting at \(16.6\)° below the negative \(x\)-axis
\(M_{eq} = -250 \, N \, m\)
Exercise \(\)
Determine the equivalent point load (magnitude and location) for the distributed force shown below, using integration.
\(F_{eq} = 105 \, N\)
\(x_{eq} = 3.29 \, m\) (measured from wall)
Exercise \(\)
Determine the equivalent point load (magnitude and location) for the distributed force shown below, using integration.
\(F_{eq} = 5400 \, lbs\)
\(x_{eq} = 8 \, ft\) (measured from wall)
Exercise \(\)
Use the method of composite parts to determine the magnitude and location of the equivalent point load for the distributed force shown below.
\(F_{eq} = 12 \, kN\)
\(x_{eq} = 2.79 \, m\) (measured from wall)
- 5: Engineering Structures

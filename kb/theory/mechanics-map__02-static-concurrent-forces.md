来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 02 2: Static Equilibrium in Concurrent Force Systems

## 2: Static Equilibrium in Concurrent Force Systems

## 2.0: Chapter 2 Video Introduction

- 2: Static Equilibrium in Concurrent Force Systems      2.1: Static Equilibrium
- 2: Static Equilibrium in Concurrent Force Systems

## 2.1: Static Equilibrium

Objects in static equilibrium are objects that are not accelerating (either linear acceleration or angular acceleration). These objects may be stationary, such as a building or a bridge, or they may have a constant velocity, such as a car or truck moving at a constant speed on a straight patch of road.
Newton's Second Law states that the force exerted on an object is equal to the mass of the object times the acceleration it experiences. Therefore, if we know that the acceleration of an object is equal to zero, then we can assume that the sum of all forces acting on the object is zero. Individual forces acting on the object, represented by force vectors, may not have zero magnitude but the sum of all the force vectors will always be equal to zero for objects in equilibrium. Engineering statics is the study of objects in static equilibrium, and the simple assumption of all forces adding up to zero is the basis for the subject area of engineering statics.
\[ \sum \vec{F} \, = \, m \vec{a} \]
\[ a = 0 \, ; \,\,\, \sum \vec{F} \, = \, 0 \]
Equilibrium follows a similar pattern for angular accelerations. The rotational equivalent of Newton's Second Law states that the moment exerted on an object is equal to the moment of inertia of that object times the angular acceleration of the object. If we know the angular acceleration of an object is equal to zero, then we know the sum of all moments acting on the object is equal to zero.
\[ \sum \vec{M} \, = \, I \vec{\alpha} \]
\[ \vec{\alpha} = 0 \, ; \,\,\, \sum \vec{M} \, = \, 0 \]

## 2.2: Point Forces as Vectors

- Force Vector Representation:
- Changing Force Vector Forms:
A point force is any force where the point of application is considered to be a single point. In reality, most forces are technically surface forces, where the force is applied over an area, but when the area is small enough (in comparison to the bodies being analyzed) it can often be approximated as a point force. Because point forces can be represented as a single vector (rather than a field of vectors for distributed forces), they are much easier to work with in engineering analysis. For this reason, point forces are used in place of distributed forces in engineering analysis whenever possible. Below are some examples of where it is appropriate to use point forces.
In addition to the magnitude, direction, and point of application of the point force, another important term to understand is the line of action of the force. The line of action of a force is the line along which the force acts. Given the direction and point of application, one can find the line of action, but this term will be important in discussing concurrent forces and in the principle of transmissibility.

## Force Vector Representation:

When vectors are drawn to form free body diagrams, the magnitude and direction are usually given in one of two formats:
- Overall magnitude and angle(s) to indicate direction (often called magnitude and direction form).
- Magnitudes in each of the coordinate directions (often called component form).
In either format we will need two values to fully define a force vector in a 2D system (either a magnitude and a single angle or a magnitude in each of the two coordinate axes), and three values to fully define a force vector in a 3D system (either a magnitude and two angles or a magnitude in each of the three coordinate axes). Below are some examples of force vectors in both representations.

## Changing Force Vector Forms:

Because the two different forms of the vector are equivalent, we can switch between representations without changing the problem. Often in engineering problems, it will initially be easier to write the force in magnitude and angle form, but later, analysis will be easier if forces are written in component form. To switch from magnitude and direction form to component form you will use right triangles and trigonometry to determine the component of the overall magnitude in each direction. This is a simple vector decomposition, and more information on this process can be seen on the vector decomposition page. To switch back from component form into magnitude and direction form you simply use the reverse of this initial process.
Example \(\)
The tension force on the box below is given in magnitude and direction form. Redraw the diagram with the tension force given in component form.
Example \(\)
The force acting on the cantilever beam shown below is given in component form. Redraw the diagram with the force given in magnitude and direction form.
Example \(\)
The force shown below is given in magnitude and direction form. Redraw the diagram with the force vector given in component form.

## 2.3: Principle of Transmissibility

The principle of transmissibility states that the point of application of a force can be moved anywhere along its line of action without changing the external reaction forces on a rigid body. Any force that has the same magnitude and direction, and which has a point of application somewhere along the same line of action will cause the same acceleration and will result in the same moment. Therefore, the points of application of forces may be moved along the line of action to simplify the analysis of rigid bodies.
When analyzing the internal forces (stress) in a rigid body, the exact point of application does matter. This difference in stresses may also result in changes in geometry which will in turn affect reaction forces. For this reason, the principle of transmissibility should only be used when examining external forces on bodies that are assumed to be rigid.

## 2.4: Concurrent Forces

A set of point forces is considered concurrent if all the lines of action of those forces all come together at a single point.
Because the forces all act through a single point, there are no moments about this point. Because no moments exist, we can treat this body as a particle. In fact, because real particles only exist in theory, most particle analysis is actually applied to extended bodies with concurrent forces acting on them.

## 2.5: Equilibrium Analysis for Concurrent Force Systems

- Finding the Equilibrium Equations:
If a body is in static equilibrium, then by definition that body is not accelerating. If we know that the body is not accelerating then we know that the sum of the forces acting on that body must be equal to zero. This is the basis for equilibrium analysis for a particle.
In order to solve for any unknowns in our sum of forces equation, we actually need to turn the one vector equation into a set of scalar equations. For two dimensional problems, we will split our one vector equation down into two scalar equations. We do this by summing up all the \(x\) components of the force vectors and setting them equal to zero in our first equation, and summing up all the \(y\) components of the force vectors and setting them equal to zero in our second equation.
\[ \sum \vec{F} \, = \, 0 \]
\[ \sum F_x \, = \, 0 \, ; \,\,\, \sum F_y \, = \, 0 \]
We do something similar in three dimensional problems except we will break all our force vectors down into \(x\), \(y\), and \(z\) components, setting the sum of \(x\) components equal to zero for our first equation, the sum of all the \(y\) components equal to zero for our second equation, and the sum of all our \(z\) components equal to zero for our third equation.
\[ \sum \vec{F} \, = \, 0 \]
\[ \sum F_x \, = \, 0 \, ; \,\,\, \sum F_y \, = \, 0 \, ; \,\,\, \sum F_z \, = \, 0 \]
Once we have written out the equilibrium equations, we can solve the equations for any unknown forces.

## Finding the Equilibrium Equations:

The first step in finding the equilibrium equations is to draw a free body diagram of the body being analyzed. This diagram should show all the known and unknown force vectors acting on the body. In the free body diagram, provide values for any of the know magnitudes or directions for the force vectors and provide variable names for any unknowns (either magnitudes or directions).
Next you will need to chose the \(x\), \(y\), and \(z\) axes. These axes do need to be perpendicular to one another, but they do not necessarily have to be horizontal or vertical. If you choose coordinate axes that line up with some of your force vectors you will simplify later analysis.
Once you have chosen axes, you need to break down all of the force vectors into components along the \(x\), \(y\) and \(z\) directions (see the vectors page in Appendix 1 if you need more guidance on this). Your first equation will be the sum of the magnitudes of the components in the \(x\) direction being equal to zero, the second equation will be the sum of the magnitudes of the components in the \(y\) direction being equal to zero, and the third (if you have a 3D problem) will be the sum of the magnitudes in the \(z\) direction being equal to zero. Collectively these are known as the equilibrium equations.
Once you have your equilibrium equations, you can solve them for unknowns using algebra. The number of unknowns that you will be able to solve for will be the number of equilibrium equations that you have. In instances where you have more unknowns than equations, the problem is known as a statically indeterminate problem and you will need additional information to solve for the given unknowns.
Example \(\)
The diagram below shows a 3-lb box (Box A) sitting on top of a 5-lb box (box B). Determine the magnitude and direction of all the forces acting on box B.
Example \(\)
A 600-lb barrel rests in a trough as shown below. The barrel is supported by two normal forces (\(F_2\) and \(F_3\)). Determine the magnitude of both of these normal forces.
Example \(\)
A 6-kg traffic light is supported by two cables as shown below. Find the tension in each of the cables supporting the traffic light.
Example \(\)
A 400-kg wrecking ball rests against a surface as shown below. Assuming the wrecking ball is currently in equilibrium, determine the tension force in the cable supporting the wrecking ball and the normal force that exists between the wrecking ball and the surface.
Example \(\)
Barrels A and B are supported in a foot truck as seen below. Assuming the barrels are in equilibrium, determine all forces acting on barrel B.
Example \(\)
Three soda cans, each weighing 0.75 lbs and having a diameter of 4 inches, are stacked in a formation as shown below. Assuming no friction forces, determine the normal forces acting on can B.
Example \(\)
The skycam shown below is supported by three cables. Assuming the skycam has a mass of 20 kg and that it is currently in a state of equilibrium, find the tension in each of the three cables supporting the skycam.
Example \(\)
A hot air balloon is tethered to the ground with three cables as shown below. If the balloon is pulling upwards with a force of 900 lbs, what is the tension in each of the three cables?

## 2.6: Chapter 2 Homework Problems

Exercise \(\)
A 30 kg barrel is sitting on a handcart as shown below. Determine the normal forces at A and B.
\(F_A = 147.15 \, N; \, F_B = 254.87 \, N\).
Exercise \(\)
A 0.25kg ball rolls into a corner as shown below. Assuming the surfaces are smooth (no friction), determine the normal forces at A and B.
\(F_A = 1.09 \, N; \, F_B = 3.01 \, N\)
Exercise \(\)
A traffic light is supported by two cables as shown below. The tension in cable one is measured to be 294.8 N. What is the tension in cable two? What is the mass of the traffic light?
\(T_2 = 276.6 \, N; \, m = 20 \, kg\)
Exercise \(\)
A 50 kg truck engine is lifted using the setup shown below. Assuming that the pulleys shown in the diagram are frictionless, what force \(P\) must be applied to the cable to hold the engine in the position shown below with \(d\) = 1 meter? (Hint: Draw a free body diagram of the pulley supporting the engine block)
\(P = 442.1 \, N\)
Exercise \(\)
Two weights are supported via cables as shown below. If body B has a weight of 60 pounds, what is the expected weight of body A based on the angles of the cables?
\(F_{gA} = 24.89 \, lbs\)
Exercise \(\)
Three equally sized cylinders, each with mass 100 kg, are stacked in a groove as shown below. Determine all forces acting on cylinder C and show them in a diagram.
\(F_{AC} = 490.5 \, N; \, F_{BC} = 693.7 \, N; \, F_{C1} = 1304.6 \, N; \, F_{C2} = 829.7 \, N; \, F_g = 981 \, N\)
Exercise \(\)
You are hanging a pterodactyl model from the ceiling of a museum with three cables as shown below. Assuming the pterodactyl model has a mass of 260 kg, what is the tension we would expect in each of the three cables?
\(T_A = 2306.94 \, N; \, T_B = 1393.86 \, N; \, T_C = 2569.19 \, N\)
Exercise \(\)
A hot air balloon is tethered as shown below. Assuming that the balloon is pulling upward with a force of 900 lbs, determine the tension in each of the cables.
\(T_A = 545.5 \, lbs; \, T_B = 430.7 \, lbs; \, T_C = 320.7 \, lbs\)
- 3: Static Equilibrium in Rigid Body Systems

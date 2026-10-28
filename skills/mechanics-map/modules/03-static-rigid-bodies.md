来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 03 3: Static Equilibrium in Rigid Body Systems

## 3: Static Equilibrium in Rigid Body Systems

## 3.0: Video Introduction to Chapter 3

- 3: Static Equilibrium in Rigid Body Systems      3.1: Moment of a Force about a Point (Scalar Calculation)
- 3: Static Equilibrium in Rigid Body Systems

## 3.1: Moment of a Force about a Point (Scalar Calculation)

- The Scalar Method in 2 Dimensions
- The Scalar Model in 3 DimensionsExample \(\)Example \(\)Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
The moment of a force is the tendency of some forces to cause rotation. Any easy way to visualize the concept is set a box on smooth surface. If you were to apply a force to the center of the box, it would simply slide across the surface without rotating. If you were instead to push on one side of the box, it will start rotating as it moves. Even though the forces have the same magnitude and the same direction, they cause different reactions. This is because the off-center force has a different point of application, and exerts a moment about the center of the box, whereas the force on the center of the box does not exert a moment about the box's center point.
Just like forces, moments have a magnitude (the degree of rotation it would cause) and a direction (the axis the body would rotate about). Determining the magnitude and direction of these moments about a given point is an important step in the analysis of rigid body systems (bodies that are both rigid and not experiencing concurrent forces). The scalar method below is the easiest way to do this in simple two-dimensional problems, while the alternative vector methods, which will be covered later, work best for more complex three-dimensional systems.

## The Scalar Method in 2 Dimensions

In discussing how to calculate the moment of a force about a point via scalar quantities, we will begin with the example of a force on a simple lever as shown below. In this simple lever there is a force on the end of the lever, distance \(d\) away from the center of rotation for the lever (point A) where the force has a magnitude \(F\).
When using scalar quantities, the magnitude of the moment will be equal to the perpendicular distance between the line of action of the force and the point we are taking the moment about. \[ M \, = \, F * d \]
To determine the sign of the moment, we determine what type of rotation the force would cause. In this case, we can see that the force would cause the lever to rotate counterclockwise about point A. Counterclockwise rotations are caused by positive moments while clockwise rotations are caused by negative moments.
Another important factor to remember is that the value \(d\) is the perpendicular distance from the force to the point we are taking the moment about. We could measure the distance from point A to the head of the force vector, or the tail of the force vector, or really any point along the line of action of force \(F\). The distance we need to use for the scalar moment calculation, however, is the shortest distance between the point and the line of action of the force. This will always be a line perpendicular to the line of action of the force, going to the point about which we are taking the moment.

## The Scalar Model in 3 Dimensions

For three-dimensional scalar calculations, we will still find the magnitude of the moment in the same way, multiplying the magnitude of the force by the perpendicular distance between the point and the line of action of the force. This perpendicular distance again is the minimum distance between the point and the line of action of the force. In some cases, finding this distance may be very difficult.
Another difficult factor in three dimensional scalar problems is finding the axis of rotation, as this is now more complex that just "clockwise or counterclockwise". The axis of rotation will be a line traveling though the point about which we are taking the moment, and perpendicular to both the force vector and the perpendicular displacement vector (the vector going from the point about which the moment was taken to the point of application of the force). While this is possible in any situation, it becomes very difficult if the force or displacement vectors do not lie in one of the three coordinate directions.
To further find the direction of the moment vector (which will act along the established line for axis of rotation), we will use the right-hand rule in a modified form. Wrap the fingers of your right hand around the axis of rotation line with your fingertips curling in the direction the body would rotate. If you do this, your thumb should point out along the line in the direction of the moment vector. This is an important last step, because we can rotate clockwise or counterclockwise in about any given axis of rotation. With the final moment vector, we known not only the axis of rotation, but which way the body would rotate about that axis.
What is the moment that Force A exerts about point A? What is the moment that Force B exerts about Point A?
What is the moment that this force exerts about point A? What is the moment this force exerts about point B?
What are the moments that each of the three tension forces exert about point A (the point where the beams come together)?

## 3.2: Varignon's Theorem

- Example \(\)
- Example \(\)
Varignon's Theorem, also often called the principle of moments, is a very useful tool in scalar moment calculations. In cases where the perpendicular distance is hard to determine, Varignon's Theorem offers an alternative to finding that distance.
In its basic form, Varignon's Theorem states that if we have two or more concurrent forces, the sum of the moments that each force creates about a single point will be equal to the moment created by the sum of those forces about the same point.
On its surface this doesn't seem that useful, but in practice we will often use this theorem in reverse by breaking down a force into components (the components being a set of concurrent forces). We can solve for the moment exerted by each component (where perpendicular distance \(d\) is easier to find) and then simply add together the moments from each component to find the moment from the original force.

## Example \(\)

Use Varignon's Theorem to find the moment that the forces in the diagram below exert about point A.

## Example \(\)

Use Varignon's Theorem to find the moment that the force in the diagram below exerts about point B.

## 3.3: Couples

- Example \(\)
- Example \(\)
A couple is a set of equal and opposite forces that exerts a net moment on an object but no net force. Because the couple exerts a net moment without exerting a net force, couples are also sometimes called pure moments.
The moment exerted by a couple also differs from the moment exerted by a single force in that it is independent of the location you are taking the moment about. In the example below we have a couple acting on a beam. Each force has a magnitude \(F\) and the distance between the two forces is \(d\).
Now we have some point A, which is distance \(x\) from the first of the two forces. If we take the moment of each force about point A, and then add these moments together for the net moment about A we are left with the following formula.
\[ M \, = \, -(F*x) + (F*(x+d)) \] If we rearrange and simplify the formula above, we can see that the variable \(x\) actually disappears from the equation, leaving the net moment equal to the magnitude of the forces (\(F\)) times the distance between the two forces (\(d\)).
\[ M \, = \, -(F*x) + (F*x) + (F*d) \]
\[ M \, = \, (F*d) \]
This means that no matter what value of \(x\) we have, the magnitude of the moment exerted by the couple will be the same. The magnitude of the moment due to the couple is independent of the location we are taking the moment about. This will work in two or three dimensions as well. The magnitude of the moment due to a couple will always be equal to the magnitude of the forces times the perpendicular distance between the two forces.

## Example \(\)

What is the moment that the couple below exerts about point A?

## Example \(\)

What is the moment that the couple below exerts about point A?

## 3.4: Moment about a Point (Vector)

- The Vector Method in 2 and 3 DimensionsExample \(\)Example \(\)
- Example \(\)
- Example \(\)
Given any point on an extended body, if there is a force acting on the body that does not travel through that point, then that force will cause a moment about that point. As discussed on the moments page, a moment is a force's tendency to cause rotation.

## The Vector Method in 2 and 3 Dimensions

An alternative to calculating the moment via scalar quantities is to use the vector method or cross product method. For simple two-dimensional problems, using scalar quantities is usually sufficient, but for more complex problems the cross product method tends to be easier. The cross product method for calculating moments says that the moment vector of a force about a point will be equal to the cross product of a position vector \(\vec{r}\), from the point to anywhere on the line of action of the force, and the force vector itself. \[ \vec{M} \, = \, \vec{r} \times \vec{F} \]
A big advantage of this method is that \(\vec{r}\) does not have to be the shortest distance between the point and the line of action; it goes from the point to any part of the line of action. For any problem, there are many possible \(\vec{r}\) vectors, but because of the way the cross product works, they should all result in the same moment vector in the end.
It is important to note here that all quantities involved are vectors: \(\vec{r}, \, \vec{F}\), and \(\vec{M}\). Before you can solve for the cross product, you will need to write out \(\vec{r}\) and \(\vec{F}\) in vector component form. You will need to write out all three components of these vectors: for two-dimensional problems their \(z\) components will simply be zero, but those values are necessary for the calculations.
The moment vector you get will line up with the axis of rotation for the moment, where you can use the right-hand rule to determine if the moment is going clockwise or counterclockwise about that axis.
Finally, it is also important to note that taking the cross product, unlike multiplication, is not communicative. This means that the order of the vectors matters, and \(\vec{r} \times \vec{F}\) will not be the same as \(\vec{F} \times \vec{r}\). It is important to always use \(\vec{r} \times \vec{F}\) when calculating moments.
What is the moment that this force exerts about point A? What is the moment this force exerts about point B?
Determine the moment that the tension in the cable exerts about the base of the pole (leave the moment in vector form). What is the magnitude of the moment the tension exerts about this point?

## 3.5: Moment of a Force About an Axis

- Calculating the Moment About an Axis via the Dot ProductExample \(\)
- Example \(\)
It is sometimes useful to be able to calculate the moment a force exerts about a certain axis that is relevant to the problem. An example would be a force on the vault door in the image below. If we took the moment about a point (such as one of the hinges on the door), we may find that the moment vector does not line up with the axis of this hinge. In that case, the component of the moment vector that lines up with the axis of the hinge will cause a rotation, while the component of the moment vector that does not line up with the axis of the hinge will cause reaction moments in the hinge. If we are only interested in the rotation of the door, we will want to find the moment that the force exerts specifically about the axis of the hinges.

## Calculating the Moment About an Axis via the Dot Product

To find the moment of a force about a specific axis, we find the moment that the force exerts about some point on that axis and then we find the component of the moment vector that lines up with the axis we are interested in.
To do this mathematically, we use the cross product to calculate the moment of the force about any point along the axis, and then we take the dot product of a unit vector \(\vec{u}\) along the axis and the moment vector we just calculated. \[ M \, = \, \vec{u} \cdot (\vec{r} \times \vec{F}) \]
The unit vector \(\vec{u}\) has a magnitude of one and will be pointing in the direction of the axis we are interested in. Your final answer from this operation will be a scalar value (having a magnitude but no direction). This is the magnitude of the moment about the given axis, with the direction being specified by the unit vector \(\vec{u}\).
A flat L-shaped plate is attached via two hinges as shown in the diagram below. If force \(F\) acts on the plate as shown in the diagram, what is the moment that force \(F\) exerts about the axis of the hinges?

## 3.6: Equilibrium Analysis for a Rigid Body

- Finding the Equilibrium EquationsExample \(\)Example \(\)Example \(\)Example \(\)Example \(\)Example \(\)Example \(\)Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
For an rigid body in static equilibrium—that is, a non-deformable body where forces are not concurrent—the sum of both the forces and the moments acting on the body must be equal to zero. The addition of moments (as opposed to particles, where we only looked at the forces) adds another set of possible equilibrium equations, allowing us to solve for more unknowns as compared to particle problems.
Moments, like forces, are vectors. This means that our vector equation needs to be broken down into scalar components before we can solve the equilibrium equations. In a two-dimensional problem, the body can only have clockwise or counterclockwise rotation (corresponding to rotations about the \(z\) axis). This means that a rigid body in a two-dimensional problem has three possible equilibrium equations; that is, the sum of force components in the \(x\) and \(y\) directions, and the moments about the \(z\) axis. The sum of each of these will be equal to zero.
For a two-dimensional problem, we break our one vector force equation into two scalar component equations. \[ \sum \vec{F} \, = \, 0 \]
\[ \sum F_x \, = \, 0\, ; \,\, \sum F_y \, = \, 0 \] The one moment vector equation becomes a single moment scalar equation. \[ \sum \vec{M} \, = \, 0 \]
\[ \sum M_z \, = \, 0 \]
If we look at a three-dimensional problem we will increase the number of possible equilibrium equations to six. There are three equilibrium equations for force, where the sum of the components in the \(x\), \(y\), and \(z\) directions must be equal to zero. The body may also have moments about each of the three axes. The second set of three equilibrium equations states that the sum of the moment components about the \(x\), \(y\), and \(z\) axes must also be equal to zero.
We break the forces into three component equations. \[ \sum \vec{F} \, = \, 0 \]
\[ \sum F_x \, = \, 0 \, ; \,\, \sum F_y \, = \, 0 \, ; \,\, \sum F_z \, = \, 0 \]
Then we also break the moments into three component equations. \[ \sum \vec{M} \, = \, 0 \]
\[ \sum M_x \, = \, 0 \, ; \,\, \sum M_y \, = \, 0 \, ; \,\, \sum M_z \, = \, 0 \]

## Finding the Equilibrium Equations

As with particles, the first step in finding the equilibrium equations is to draw a free body diagram of the body being analyzed. This diagram should show all the force vectors acting on the body. In the free body diagram, provide values for any of the known magnitudes, directions, and points of application for the force vectors and provide variable names for any unknowns (either magnitudes, directions, or distances).
Next you will need to choose the \(x\), \(y\), and \(z\) axes. These axes do need to be perpendicular to one another, but they do not necessarily have to be horizontal or vertical. If you choose coordinate axes that line up with some of your force vectors you will simplify later analysis.
Once you have chosen axes, you need to break down all of the force vectors into components along the \(x\), \(y\) and \(z\) directions (see the vectors page in Appendix 1 page for more details on this process). Your first equation will be the sum of the magnitudes of the components in the \(x\) direction being equal to zero, the second equation will be the sum of the magnitudes of the components in the \(y\) direction being equal to zero, and the third (if you have a 3D problem) will be the sum of the magnitudes in the \(z\) direction being equal to zero.
Next you will need to come up with the the moment equations. To do this you will need to choose a point to take the moments about. Any point should work, but it is usually advantageous to choose a point that will decrease the number of unknowns in the equation. Remember that any force vector that travels through a given point will exert no moment about that point. To write out the moment equations, simply sum the moments exerted by each force (adding in pure moments shown in the diagram) about the given point and the given axis, and set that sum equal to zero. All moments will be about the \(z\) axis for two-dimensional problems, though moments can be about the \(x\), \(y\) and \(z\) axes for three-dimensional problems.
Once you have your equilibrium equations, you can solve these formulas for unknowns. The number of unknowns that you will be able to solve for will again be the number of equations that you have.
The car below has a weight of 1500 lbs with the center of mass 4 ft behind the front wheels of the car. What are the normal forces on the front and the back wheels of the car?
A 5-meter-long beam has a fixed connection to a wall at point A and a force acting as shown at point B. What are the reaction forces acting on the beam at point A?
A ladder with negligible mass is supporting a 120-lb person as shown below. If the contact point at A is frictionless, and the contact point at B is a rough connection, determine the forces acting at contact points A and B.
Member ABC is 6 meters long, with point B being at its midpoint. Determine all forces acting on member ABC.
While sitting in a chair, a person exerts the forces in the diagram below. Determine all forces acting on the chair at points A and B. (Assume A is frictionless and B is a rough surface).
The trailer shown below consists of a deck with a weight of 250 lbs on an axle with wheels with a weight of 350 lbs. Assume the weight forces act in the center of each component. If we wish the tongue weight (\(F_T\)) of the unloaded trailer to be 50 lbs, what is the distance \(d\) from the front where we must place the axle?
A 12-inch-by-24-inch flat steel sign is supported by two cables, each 6 inches from the edge of the sign. The sign has a weight of 10 lbs, and the wind is causing the sign to sit at an angle of 10 degrees from vertical (the \(y\) axis). If we treat the wind as a point force acting in the negative \(z\) direction on the center of the sign, how strong must the wind force be to cause this ten-degree angle?
A sixty-kilogram acoustic panel is suspended by three cables as shown below. Assuming the panel has a uniformly distributed weight, what is the tension in each of the cables?

## 3.7: Chapter 3 Homework Problems

- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)
- Exercise \(\)

## Exercise \(\)

An 18-inch shelf is supported by a pin joint at point A, and a cable at point B. The shelf itself has a weight of 60 lbs. If we want the net moment about point A to be zero, what should the tension in the cable be?
\(T = 52.30 \, lbs\)

## Exercise \(\)

What is the moment the force shown below exerts about Point A? About Point B?
Hint: use Varginon's Theorem.
\(M_A = 10.88 \, kNm \)
\(M_B = 21.02 \, kNm\)

## Exercise \(\)

You are attempting to rotate a heavy table about the base of one leg at point O and are going to exert a 100-lb force at the opposite end. Person A recommends pulling straight up, while person B recommends pulling up at 30° from vertical. What would be the moment about point O, in inch-pounds, in either case?
\(M_{AO} = 6000 \, \text{in-lbs} \)
\(M_{BO} = 6996.15 \, \text{in-lbs}\)

## Exercise \(\)

Determine the moment vectors that each of the three tension forces in the diagram below exerts about the origin point O. Provide the answers in vector form with units.
\(M_{AO} = [0, \, -400, \, 0] \, Nm\)
\(M_{BO} = [-300, \, 0, \, 0] \, Nm\)
\( M_{CO} = [300, \, 0, \, 0] Nm\)

## Exercise \(\)

You exert a 50-lb force on the side of a fridge as shown below. Assuming the fridge is sitting on a rough surface and not moving, what is the magnitude of the moment exerted by the couple consisting of the pushing force and the friction force?
\(M = -100 \text{ft-lbs}\)

## Exercise \(\)

A space station consists of a large ring that spins in order to provide an artificial gravity for the astronauts in the station. To start the station spinning, a pair of thrusters is attached to the outside of the ring, each pointing in opposite directions as shown below.
a) If we want to exert a 10 kN-m moment with the thrusters, and the ring has a diameter of 45 meters, what thrust force should each thruster produce?
b) If we were to use the same thrusters on a 60-meter diameter ring, what moment would they exert?
a) \(F_{thruster} = 222.22 \, N\)
b) \(M_{thruster} = 13.33 \, kNm\)

## Exercise \(\)

A 60-N force is applied in the \(yz\) plane, 40° from the \(y\) direction, on an L-shaped bar as shown below.
a) What is the moment vector this force exerts about point O?
b) What is the overall magnitude of the moment about point O?
\(M_O = [-11.49, \, -11.57, \, 13.79] \, Nm\)
\(|M| = 21.36 \, Nm\)

## Exercise \(\)

What is the moment that the force shown in the diagram exerts about point O? About the axis of the cylindrical shaft (the \(y\)-axis)?
\(M_O = [16484, \, 17046, \, -20979] \, in-lbs\)
\(M_y = 17046 \, in-lbs\)

## Exercise \(\)

The diving board shown below is supported by a pin joint at A and frictionless support at B. A 150-lb diver is standing at the end of the board. Determine the reaction forces acting on the diving board at points A and B.
\(F_{AX} = 0\)
\(F_{AY} = -450 \, lbs\)
\(F_{BY} = 600 \, lbs\)

## Exercise \(\)

A simplified crane is shown lifting a 400-kg load. The crane is supported by a pin joint at A, and a cable at B. Assuming the crane arm is in equilibrium, what are the reaction forces at A and the tension at B?
\(F_{AX} = 9352.9 \, N\)
\(F_{AY} = 3924 \, N\)
\(T_{B} = 9352.9 \, N\)

## Exercise \(\)

An 8-foot ladder sits propped up against a wall at a 60-degree angle as shown below. It has a weight of 50 lbs acting at its center point and supports a 120-lb woman 6 feet from the bottom. Assume that friction acts at the bottom of the ladder, but not the top. What are the normal forces acting at the bottom and top of the ladder, and what is the friction force acting at the bottom of the ladder?
\(F_{N \, Top} = 66.4 \, lbs\)
\(F_{N \, Bottom} = 170 \, lbs\)
\(F_f = 66.4 lbs\)

## Exercise \(\)

An SUV with a weight of 4200 lbs and a center of mass located as shown below is parked pointed downhill on a 10-degree incline. The parking is engaged, locking up the back wheels but not the front wheels. What is the expected normal force at the front wheels, the expected normal force at the back wheels, and the expected friction force at the back wheels assuming the SUV does not slip?
\(F_f = 729.3 \, lbs\)
\(F_{N \, front} = 3000.6 \, lbs\)
\(F_{N \, back} = 1135.6 \, lbs\)

## Exercise \(\)

A cart with a mass of 3500 kg sits on an inclined surface as shown below. Determine the reaction forces acting on each wheel of the cart as well as the tension in the cable supporting the cart.
\(T = 21786 \, N\)
\(F_A = 7222 \, N; \, F_B = 35925 \, N\)

## Exercise \(\)

The lighting rig above a stage consists of two 100-lb, uniform beams joined together in a T as shown below (assume the weight acts in the center of each beam). The rig is supported by three cables at A, B, and C. Determine the tension in each of the three cables.
\(T_A = 50 \, lbs; \, \, T_B = 66.7 \, lbs; \, T_C = 83.3 \, lbs\)

## Exercise \(\)

A 9-meter-long pole with a mass of 100 kg is suspended horizontally, 4 meters from the ceiling with three cables as shown below. Assuming the center of mass of the pole is at the center point of the pole, what is the expected tension in each of the three cables?
\(T_A = 357.66 \, N; \, T_B = 357.66 \, N; \, T_C = 408.75 \, N\)
- 4: Statically Equivalent Systems

来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 11 11: Rigid Body Kinematics

## 11: Rigid Body Kinematics

## 11.1: Fixed-Axis Rotation in Rigid Bodies

- Angular Position, Velocity, and Acceleration:
- Velocity and Acceleration of a Point on a Rotating Body:
When moving from particle kinematics to rigid body kinematics, we add the rotation of a body into the motion analysis process. Some bodies will translate and rotate at the same time, but many engineered systems have components that simply rotate about some fixed axis. We will start our examination of rigid body kinematics by examining these fixed-axis rotation problems, where rotation is the only motion we need to worry about.

## Angular Position, Velocity, and Acceleration:

Just as with translational motion, we will have angular positions which we can take the derivative of to find angular velocities, which we can again take the derivative of to find angular accelerations. Since we can only have a single axis of rotation in two-dimensional problems (rotating about the \(z\)-axis, with counterclockwise rotations being positive, and clockwise rotations being negative) the equations will mirror the one-dimensional equations used in particle kinematics.
 \text{Angular Position:} \quad &\, \theta(t)\\ \text{Angular Velocity:} \quad &\, \omega(t) = \frac{d \theta}{dt} = \dot{\theta}\\ \text{Angular Acceleration:} \quad &\, \alpha(t) = \frac{d \omega}{dt} = \frac{d^2 \theta}{dt^2} = \ddot{\theta}
Also as with one-dimensional translational motion, we can use integration to move in the opposite direction (just remember your constants of integration).
 \text{Acceleration:} \quad &\, \alpha(t) \\ \text{Velocity:} \quad &\, \omega(t) = \int \alpha(t) \, dt \\ \text{Position:} \quad &\, \theta(t) = \int \omega(t) \, dt = \int \int \alpha(t) \, dt \, dt
If we have constant angular accelerations, we can also use the following formulas adapted from one-dimensional motion.
 \text{Acceleration:} \quad &\, \alpha(t) = \alpha \\[5pt] \text{Velocity:} \quad &\, \omega(t) = \alpha t + \omega_0 \\[5pt] \text{Position:} \quad &\, \theta(t) = \frac{1}{2} \alpha t^2 + \omega_0 t + \theta_0 \\[5pt] \text{Without time:} \quad &\, \omega^2 - \omega_0^2 = 2 \alpha (\theta - \theta_0)

## Velocity and Acceleration of a Point on a Rotating Body:

With fixed-axis rotation, there is a single point on a body that does not move; however, all other points on this body will have some velocity and some acceleration due to the rotation of the body itself.
To determine the velocities and accelerations of these points, we will adapt the equations we used for polar coordinates. As a reminder, these equations were as follows:
 \text{Velocity:} \quad &\, v = \dot{r} \hat{u}_r + r \dot{\theta} \hat{u}_\theta \\ \text{Acceleration:} \quad &\, a = (\ddot{r} - r \dot{\theta}^2) \hat{u}_r + (2 \dot{r} \dot{\theta} + r \ddot{\theta}) \hat{u}_{\theta}
To simplify the above equations, we can note that for a rigid body, the point P never gets any closer or further away from the fixed center point O. This means that the distance \(r\) never changes, and the \(\dot{r}\) and \(\ddot{r}\) terms in the above equations are zero. Putting this to work, we can simplify the above equations into the equations below.
 \text{Velocity:} \quad &\, v = r \dot{\theta} \hat{u}_{\theta} \\ \text{Acceleration:} \quad &\, a = (-r \dot{\theta}^2) \hat{u}_r + (r \ddot{\theta}) \hat{u}_{\theta}
These equations allow us to find the velocity and acceleration of any point on a body rotating about a fixed axis, given that we know the angular velocity of the body \((\dot{\theta)\), the angular acceleration of the body \((\ddot{\theta})\), and the distance from the point to the axis of rotation \((r)\).
Example \(\)
A flywheel rotates on a fixed axle in a steam engine. The flywheel is rotating at a rate of 600 rpm before a brake begins decelerating the flywheel at a constant rate of 30 rad/s2. What is the time required to bring the flywheel to a complete stop? How many rotations does the flywheel go through while decelerating?
Example \(\)
A hard drive platter 8 cm in diameter is rotating at a constant rate of 3600 rpm. What is the velocity of a point on the outer edge of the platter? What is the acceleration experienced by a point on the edge of the platter?
- 11: Rigid Body Kinematics      11.2: Belt- and Gear-Driven Systems
- 11: Rigid Body Kinematics

## 11.2: Belt- and Gear-Driven Systems

- Position, Velocity, and Acceleration in Belt-Driven Systems
- Position, Velocity, and Acceleration in Gear Systems:
Belt-and-pulley systems, along with gear-driven systems, represent the common ways that engineers transfer rotational motion and torque from one shaft to another shaft. Belts offer flexibility in that the shafts do not need to be right next to one another, and gears are more commonly used in high-load applications.

## Position, Velocity, and Acceleration in Belt-Driven Systems

The diagram below shows a simple belt-driven system. Pulley A and Pulley B each have their own radius, and are connected via a belt that we will assume is not slipping relative to the pulleys. Each pulley is undergoing fixed axis rotation and will therefore follow those kinematic rules separately; however, the motion of the belt can be used to relate the motion of the two pulleys.
As a constraint, we can assume the speed of the pulley will be uniform throughout the whole loop at any one time. If this was not true, the belt would be bunching up in some locations and stretching out in other areas. If the belt isn't slipping, the speed of the belt will be the same as the speed of the edge of each of the two pulleys. Setting these two speeds equal to one another and working backwards to relate them to angular velocities, we wind up with the middle equation below. Taking the integral or derivative allows us to also relate angular displacements or angular accelerations with similar equations.
 \text{Angular Displacements:} \quad &\, r_A (\Delta \theta_A) = r_B (\Delta \theta_B) \\[5pt] \text{Angular Velocities:} \quad &\, r_A \omega_A = r_B \omega_B \\[5pt] \text{Angular Accelerations:} \quad &\, r_A \alpha_A = r_B \alpha_B
If we have a more complex series of belts and pulleys, we will analyze the system one step at at time. This will include pulleys connected via belts as we had above, as well as pulleys connected via a shaft as shown with pulleys B and C in the diagram below.
With pulleys on the same shaft, the angular displacements, the angular velocities, and the angular accelerations will all be the same.
\[ \Delta \theta_B = \Delta \theta_C \ ; \quad \omega_B = \omega_B \ ; \quad \alpha_B = \alpha_C \]
If we know the angular displacement, angular velocity, or angular acceleration of pulley A, we could find the angular displacement, angular velocity, or angular acceleration of pulley D by moving one interaction at a time (finding the motion of pulley B, then C, then D).

## Position, Velocity, and Acceleration in Gear Systems:

The diagram below shows a simple gear system. Gear A and Gear B each have their own radius, and are interacting at their point of contact. Each gear is undergoing fixed-axis rotation and will therefore follow those kinematic rules separately; however, the motion of the teeth at the point of contact can be used to relate the motion of one gear to the next.
As a constraint, we can assume that the speed of the teeth at the point of contact will be the same. If this were not true, the teeth of one gear would be passing through the teeth of the other gear. Setting these these two speeds equal to one another and working backwards to relate the angular velocities, we find the second equation below. Taking the integral or derivative allows us to also relate the angular displacements or angular accelerations with similar equations.
 \text{Angular Displacements:} \quad &\, r_A (\Delta \theta_A) = - r_B (\Delta \theta_B) \\[5pt] \text{Angular Velocities:} \quad &\, r_A \omega_A = -r_B \omega_B \\[5pt] \text{Angular Accelerations:} \quad &\, r_A \alpha_A = - r_B \alpha_B
You will notice that the equations above match the equations we had for belt-driven systems, except for the minus sign on the right side of each equation. This is because meshed gears rotate in opposite directions (if one gear rotates clockwise, the other will rotate counterclockwise), while pulleys in belt-driven systems always rotate in the same direction.
Also similar to belt driven systems, we can have compound gear trains with three or more gears similar to the figure below. In these scenarios, we will also likely have gears that are connected via a shaft like the blue and yellow gears shown below. In such situations, the gears on the same shaft will have matching angular displacements, angular velocities, and angular accelerations. As with belt driven systems, you simply need to take the gear train one step at a time, applying the right set of equations to match each step in the interaction.
A concept that is commonly used in gear trains that is not commonly used in belt driven systems is the concept of the gear ratio. For any gear train, the gear ratio is defined as the angular speed of the input divided by the angular speed of the output. Based on the equations above, we can also prove that the ratio of angular displacements or angular accelerations will similarly be equal to the gear ratio. However, the gear ratio is always defined as a positive number, so you will still need to use intuition to determine the direction of output.
\[ \text{Gear Ratio} = \frac{\omega_{input}}{\omega_{output}} = \frac{\Delta \theta_{input}}{\Delta \theta_{output}} = \frac{\alpha_{input}}{\alpha_{output}} \]
In a simple two-gear system, the gear ratio will be equal to the radius of the output gear divided by the radius of the input gear, or the number of teeth on the output gear divided by the number of teeth on the input gear (since the number of teeth will be directly proportional to the radius). In compound gear trains this simple calculation given below will not work, but if you are given the gear ratio for a compound gear train, you can still apply the equations above.
\[ \text{Gear Ratio} = \frac{\omega_{input}}{\omega_{output}} = \frac{r_{output}}{r_{input}} = \frac{N_{output}}{N_{input}} \]
Example \(\)
If the input pulley A as shown below is rotating at a rate of 10 rad/s, what is the speed of the output pulley at D? How many rotations does D go through in the time it takes for A to make one full rotation?
Example \(\)
A car is moving at 40 ft/s on 18-inch-diameter wheels. What is the angular velocity of the wheels on the car? If the car is in third gear with a gear ratio of 4.89:1, what is the angular velocity of the engine in rotations per minute? (Hint: the engine is the input to the gear train and the wheels are the output of the gear train.)

## 11.3: Absolute Motion Analysis

- Utilizing Absolute Motion Analysis:
Absolute motion analysis is one method used to analyze bodies undergoing general planar motion. General planar motion is motion where bodies can both translate and rotate at the same time. Besides absolute motion analysis, the alternative is relative motion analysis. Either method can be used for any general planar motion problem, but one method may be significantly easier to apply for a given situation.
Absolute motion analysis will require calculus, and is generally faster for simple problems and problems where only the velocities (and not accelerations) are required. Relative motion analysis will not require calculus, but does necessitate using multiple coordinate systems; it is generally easier to use for more complex problems and problems where velocities and accelerations are being analyzed.

## Utilizing Absolute Motion Analysis:

To start our discussion on absolute motion analysis, we are going to imagine a simple robotic arm such as the one below. In this arm, we have two arm sections of fixed length with motors causing rotations at joint A and joint B.
The first step in absolute motion analysis is come up with a set of equations describing the position of some point of interest. In this case we will be looking at the position of the end effector of the arm at point C, and we will write an equation for the \(x\) position and the \(y\) position of this point with respect to the fixed origin point at A. In these equations, anything that is a constant (such as the length of the arm pieces) can be put in as a number, but anything that will change, such as angles \(\theta\) and \(\phi\), will need to remain as variables in these equations even if they are known at the moment. Using the values in the diagram, we would wind up with the following two position equations.
 x \text{-position:} \quad &\, x_C = 2 \cos (\theta) + 1.5 \cos (\phi) \\[5pt] y \text{-position:} \quad &\, y_C = 2 \sin (\theta) + 1.5 \sin (\phi)
To find the velocity of point C in the \(x\) and \(y\) directions, we simply need to take the derivatives of the position equations. The velocity equations for our robotic arm are below.
 x \text{-velocity:} \quad &\, v_{x \ C} = -2 \sin (\theta) \ \dot{\theta} - 1.5 \sin (\phi) \ \dot{\phi}\\[5pt] y \text{-velocity:} \quad &\, v_{y \ C} = 2 \cos (\theta) \ \dot{\theta} + 1.5 \cos (\phi) \ \dot{\phi}
To find the acceleration of point C in the \(x\) and \(y\) directions, we simply need to take the derivatives of the velocity equations. The acceleration equations for our robotic arm in the \(x\) and \(y\) directions are shown below.
 x \text{ acceleration:} \quad &\, a_{x \ C} = -2 \cos (\theta) \ \dot{\theta}^2 - 2 \sin (\theta) \ \ddot{\theta} - 1.5 \cos (\phi) \ \dot{\phi}^2 - 1.5 \sin (\phi) \ \ddot{\phi} \\[5pt] y \text{ acceleration:} \quad &\, a_{y \ C} = -2 \sin (\theta) \ \dot{\theta}^2 + 2 \cos (\theta) \ \ddot{\theta} - 1.5 \sin (\phi) \ \dot{\phi}^2 + 1.5 \cos (\phi) \ \ddot{\phi}
Once we have the velocity and acceleration equations, we can start solving for any unknowns. If we have known angular velocities and accelerations (\(\dot{\theta}\), \(\ddot{\theta}\), \(\dot{\phi}\), and \(\ddot{\phi}\)) we can plug those in to find the velocity and acceleration vectors for the end effector. In other instances, we may known the desired motion of the end effector (\(v_{xC}\), \(v_{yC}\), \(a_{xC}\), and \(a_{yC}\)) and will have to plug those values into the equations to solve for unknowns such as \(\dot{\theta}\) and so on.
Example \(\)
The robotic arm shown below has a fixed orange base at A and fixed-length members AB and BC. Motors at A and B allow for rotational motion at the joints. Based on the angular velocities and accelerations shown at each joint, determine the velocity and the acceleration of the end effector at C.
Example \(\)
The robotic arm from the previous problem is in the configuration shown below. Assume that \(\theta\) is currently 30 degrees and that point C currently lies along the \(x\) axis. If we want the end effector at C to travel 1 ft/s in the negative \(x\)-direction, what should the angular velocities be at joints A and B?
Example \(\)
A ladder is propped up against a wall as shown below. If the base of the ladder is sliding out at a speed of 2 m/s, what is the speed of the top of the ladder?
Example \(\)
The crank-rocker mechanism as shown below consists of a crank with a radius of 0.5 meters rotating about its fixed center at C, at a constant rate of 2 rad/s clockwise. Rocker AB is fixed at its base at A and connects to point B along the edge of the crank. The pin at point B can slide along a frictionless slot in AB. In the current state, what is the angular velocity of rocker AB?

## 11.4: Relative Motion Analysis

- Utilizing Relative Motion Analysis
- Alternate Notation for Rigid Body Relative Motion
Relative motion analysis is one method used to analyze bodies undergoing general planar motion. General planar motion is motion where bodies can both translate and rotate at the same time. Besides relative motion analysis, the alternative is absolute motion analysis. Either method can be used for any general planar motion problem, however one method may be significantly easier to apply in certain situations.
Absolute motion analysis will require calculus and is generally faster for simple problems and problems where only the velocities (and not accelerations) are required. Relative motion analysis will not require calculus, but does necessitate using multiple coordinate systems and is generally easier to use for more complex problems and problems where velocities and accelerations are being analyzed.

## Utilizing Relative Motion Analysis

To start our discussion on relative motion analysis, we are going to imagine a simple robotic arm such as the one below. In this arm, we have two arm sections of fixed length, with motors causing rotations at joint A and joint B.
The first step in relative motion analysis is to break the motion down into simple steps and assign a coordinate system (with \(r\) and \(\theta\) directions) to each step in the chain of motion. We will always start at a fixed point and move step by step from there. In the case of our robotic arm, Joint A is the only point that will not be moving so we start there; then we have two cases of rotation without extension as we move from A to B, then B to C.
Since there are two steps to the motion, there will be two coordinate systems. The first coordinate system will be attached to member AB, with the \(r\) direction going from point A to point B. The \(\theta\) direction will then be ninety degrees counterclockwise from the \(r\) direction. The second coordinate system will be attached to member BC, with the \(r\) direction going from point B to point C. Again, the \(\theta\) direction is ninety degrees counterclockwise from the \(r\) direction. At this point it is usually good to identify the angles of each of the \(r\) and \(\theta\) directions with respect to ground. Below is a picture of the robotic arm with both coordinate systems drawn in.
For relative motion analysis, we can identify the velocity or acceleration of the end point of the arm (C) with respect to the ground (A) by finding the velocity acceleration of B with respect to A and adding the velocity or acceleration of C with respect to B, just as we did with particles.
 \text{Velocity:} \quad &\, \vec{v}_{C / A} = \vec{v}_{B / A} + \vec{v}_{C / B} \\[4pt] \text{Acceleration:} \quad &\, \vec{a}_{C / A} = \vec{a}_{B / A} + \vec{a}_{B / C}
The relative motion analysis equations above are for a two-part motion (as there are two sections to the arm in our example), but we can easily expand the above equation into three, four, or even more pieces for more complex mechanisms by adding more steps to the left side of our equation.
To use the above equations, we will need to plug in the information we know. Plugging in velocities or accelerations that are given as part of the problem for any particular points is a good place to start. If the velocity of points B or C were given, for example, we would plug that in for \(\vec{v}_{B / A}\) or \(\vec{v}_{C / A}\) respectively. Do remember that point A is our fixed ground point, so \(\vec{v}_{C / A}\) is the velocity of point C relative to the ground while \(\vec{v}_{C / B}\) is the velocity of point C with respect to point B. If any point is fixed (other than our original ground point, which will always be fixed), we can also plug in zeros for both velocity and acceleration of that point. Remember that this equation is a vector equation, so these velocities have both a magnitude and a direction.
To take into account rotation or extension of any individual pieces, we will need to look back to our kinematics equations for polar coordinator systems. Below are the equations we had for velocity and acceleration.
 \text{Velocity:} \quad &\, v = \dot{r} \hat{u}_r + r \dot{\theta} \hat{u}_{\theta} \\[4pt] \text{Acceleration:} \quad &\, a = (\ddot{r} - r \dot{\theta}^2) \hat{u}_r + (2 \dot{r} \dot{\theta} + r \ddot{\theta}) \hat{u}_{\theta}
In the above equations, \(r\) represents the length of the respective arm piece (the length of member AB or BC), \(\dot{r}\) represents the rate at which that length is increasing, and \(\ddot{r}\) represents the rate at which that rate is increasing. The \(\theta\) term represents current angle of the arm piece, \(\dot{\theta}\) is the angular velocity of that arm piece, and \(\ddot{\theta}\) is the angular acceleration of that arm piece. The \(u_r\) and \(u_{\theta}\) directions are the \(r\) and \(\theta\) directions that are attached to that particular section of the arm (in our earlier drawing, \(\hat{u}_{r_1}\) and \(\hat{u}_{\theta_1}\) were attached to member AB and \(\hat{u}_{r_2}\) and \(\hat{u}_{\theta_2}\) were attached to member BC).
Though it's certainly possible to have a mechanism that is rotating and extending at the same time, we will often have either just simple rotation, or just simple extension along a fixed direction. With simple rotation, the \(\dot{r}\) and \(\ddot{r}\) terms are zero, and our equations reduce down to the following.
 \text{Velocity:} \quad &\, v = r \dot{\theta} \hat{u}_{\theta} \\[4pt] \text{Acceleration:} \quad &\, a = - r \dot{\theta}^2 \hat{u}_{r} + r \ddot{\theta} \hat{u}_{\theta}
If we have simple extension, where the length of the piece is changing but there is no rotation, the \(\dot{\theta}\) and \(\ddot{\theta}\) terms would be zero and our original equations would reduce down to the following.
 \text{Velocity:} \quad &\, v = \dot{r} \hat{u}_r \\ \text{Acceleration:} \quad &\, a = \ddot{r} \hat{u}_r
If we use the appropriate set of equations for the type of motion in each step and plug in known quantities for angular velocities, angular accelerations, and rates or extension for each piece, we can add these pieces to our relative motion analysis equation from earlier. Again, these are vectors so be sure to indicate both the magnitudes and directions when we put them into the equation.
Once we have everything in our vector equation, we will break the vector equation into \(x\) and \(y\) components in order to solve for any unknowns. Simply find the angles or each of the \(r\) and \(\theta\) directions using your diagram and then use sines and cosines to break the individual vectors down into \(x\) and \(y\) components. Once you have everything in component form, you should be able to solve for any unknowns in your equations. As a note, it is often necessary to start with the velocity equations and solve for some unknowns there before moving on to the acceleration equations.

## Alternate Notation for Rigid Body Relative Motion

In some cases, we want to analyze multiple points on the same or several rigid bodies. Another notation used for this is:
 \text{Position:} \quad &\, \vec{r}_B = \vec{r}_A + \vec{r}_{B / A} \\[5pt] \text{Velocity:} \quad &\, \vec{v}_B = \vec{v}_A + \vec{v}_{B / A} = \vec{v}_A + \vec{\omega} \times \vec{r}_{B / A} \\[5pt] \text{Acceleration:} \quad &\, \vec{a}_B = \vec{a}_A + \vec{a}_{B / A} = \vec{a}_A + \vec{\alpha} \times \vec{r}_{B / A} + \vec{\omega} \times (\vec{\omega} \times \vec{r}_{B / A}) In this notation, A and B are two points on the same rigid body. When we use only one subscript, that indicates the position/velocity/acceleration of that point with respect to the fixed coordinate system. Because the body is rigid, the two points will not change the distance between them, but the position vector between them can change orientation (which is where the relative velocity between the two points comes from). \(\vec{\omega}\) is the angular velocity of that rigid body (analogous to \(\dot{\theta}\)), and \(\vec{\alpha}\) is the angular acceleration of that rigid body (analogous to \(\ddot{\theta}\)).
For planar motion, where the angular velocity vector (out of plane) is always perpendicular to the position vector (in the plane), the acceleration can be simplified to:
\[ \text{Acceleration:} \quad \, \vec{a}_B = \vec{a}_A + \vec{\alpha} \times \vec{r}_{B / A} - \omega^2 \vec{r}_{B / A} \]
If we consider the same robotic arm, we can translate our previous notation to the new rigid body notation:
 \dot{\theta} \hat{k} &= \vec{\omega}_{AB} \\[4pt] \dot{\phi} \hat{k} &= \vec{\omega}_{BC} \\[4pt] \ddot{\theta} \hat{k} &= \vec{\alpha}_{AB} \\[4pt] \ddot{\phi} \hat{k} &= \vec{\alpha}_{BC}
All vectors will be defined with respect to the \(x\) and \(y\) coordinates in the coordinate system shown, rather than the radial and theta directions as above.
If we want to find the velocity and acceleration of the end point, C, knowing the angular velocities and accelerations, we will find the following relationships:
 \text{Velocity at point B:} \quad &\, \vec{v}_B = \vec{v}_A + \vec{\omega} \times \vec{r}_{B / A} \\[5pt] \text{Velocity at point C:} \quad &\, \vec{v}_C = \vec{v}_B + \vec{\omega} \times \vec{r}_{C / B} = \vec{v}_A + \vec{\omega} \times \vec{r}_{B / A} + \vec{\omega} \times \vec{r}_{C / B} \\[5pt] \text{Acceleration at point B:} \quad &\, \vec{a}_B = \vec{a}_A + \vec{\alpha} \times \vec{r}_{B / A} - \omega^2 \vec{r}_{B / A} \\[5pt] \text{Acceleration at point C:} \quad &\, \vec{a}_C = \vec{a}_B + \vec{\alpha} \times \vec{r}_{C / B} - \omega^2 \vec{r}_{C / B} = \vec{a}_A + \vec{\alpha} \times \vec{r}_{B / A} - \omega^2 \vec{r}_{B / A} + \vec{\alpha} \times \vec{r}_{C / B} - \omega^2 \vec{r}_{C / B}
Example \(\)
The robotic arm shown below has a fixed orange base at A and fixed length members AB and BC. Motors at A and B allow for rotational motion at the joints. Based on the angular velocities and accelerations shown at each joint, determine the velocity and the acceleration of the end effector at C.
Example \(\)
The robotic arm from the previous problem is in the configuration shown below. Assume that \(\theta\) is currently 30 degrees and that point C currently lies along the \(x\) axis. If we want the end effector at C to travel 1 ft/s in the negative \(x\)-direction, what should the angular velocities be at joints A and B?
Example \(\)
A ladder is propped up against a wall as shown below. If the base of the ladder is sliding out at a speed of 2 m/s, what is the speed of the top of the ladder?
Example \(\)
The crank-rocker mechanism as shown below consists of a crank with a radius of 0.5 meters rotating about its fixed center at C, at a constant rate of 2 rad/s clockwise. Rocker AB is fixed at its base at A and connects to point B along the edge of the crank. The pin at point B can slide along a frictionless slot in AB. In its current state, what is the angular velocity of rocker AB?

## 11.5: Rotating Frame Analysis

- Reference Frames:
- Rotating Frames:
Rotating frame analysis is a specialized part of relative motion analysis. It is typically performed in Cartesian (\(x\)-\(y\)) coordinates for rigid bodies. In the previous section, rotating frames in polar coordinates were used to solve problems with formulae similar to those in particle kinematics. We will adopt a slightly different notation that is specialized to rigid bodies. These formulae are the most general planar kinematics formulae - that is, they can always be used, and will provide the correct answer. However, they are unnecessarily complicated for many types of motion, such as pure rotation.
Rotating frame analysis is really important for cases where objects are not pinned to each other. When do you use rotating frames? When one object is sliding against another object, or two objects are not even in contact, but you want to know something about the motion relationship between them and/or are given information about the motion relationship between them.

## Reference Frames:

In most of the preceding material, you have worked with the fixed reference frame \(O_{xyz}\), and a translating (but not rotating) reference frame attached to the rigid body at a point \(A\), frame \(A_{xyz}\).
This has given us relative motion equations:
 \text{Position:} \quad &\, \vec{r}_{B / O} = \vec{r}_{A / O} + \vec{r}_{B / A} \\ \text{Velocity:} \quad &\, \vec{v}_{B / O} = \vec{v}_{A / O} + \vec{v}_{B / A} = \vec{v}_{A / O} + \vec{\omega} \times \vec{r}_{B / A} \\ \text{Acceleration:} \quad &\, \vec{a}_{B / O} = \vec{a}_{A / O} + \vec{a}_{B / A} = \vec{a}_{A / O} + \vec{\alpha} \times \vec{r}_{B / A} - \omega^2 \vec{r}_{B / A}
Note that the notation \(r_{B / O}\), where \(O\) is the fixed frame, can also be written as \(r_B\). Both indicate an absolute position (or velocity or acceleration) - that is, a value with respect to the fixed frame \(O\).

## Rotating Frames:

Now, we will consider a reference frame that is attached to a point on the rigid body and both rotating and translating with the rigid body. We will introduce some extra terms to account for the rotation of the frame.
Consider a rigid body with frame \(x'y'z'\) at point \(A\). \(x'y'z'\) moves and rotates with the body. A bug, \(B\), is crawling along the body.
For an observer sitting at \(A\), the bug appears to be crawling away in a straight line. But for an observer sitting at \(O\), the bug does not look like it is moving in a straight line, because the body it is crawling on is also moving (translating and rotating). We would like to describe the motion of the bug as seen by an observer at \(O\). To remind ourselves that we are dealing with a rotating frame attached to one body, we use capital omega \(\Omega\)) to denote the angular velocity of the object that the rotating frame is attached to, and \(\dot{\Omega}\) for the angular acceleration of the object with the rotating frame attached. Finally, we use brackets and the subscript \(rel\) to denote values of velocity or acceleration expressed with respect to the rotating frame.
Recall that vectors have both magnitude and direction. We can express a vector in components with respect to the \(\hat{i}\) and \(\hat{j}\) unit vectors:
\[ \vec{r}_{B / O} = r_{B/O, x} \hat{i} + r_{B/O, y} \hat{j} \]
Normally, when we take a time derivative of such an expression, the length of the vector (i.e. the \(r_{B/O, x}\) and \(r_{B/O, y}\) terms) change, but the unit vectors do not. In the case of the rotating frame, the unit vectors change. Now, they don't change in length - they remain unit vectors. But they are attached to a rotating body, which means they also rotate. That is, their directions change, and we have to account for that when deriving velocity and acceleration expressions.
You can see we get small vectors \(d \hat{i'}\) and \(d \hat{j'}\) that describe the change in direction of the unit vectors, and the magnitude of that change is directly related to \(\Omega\), the angular velocity of the rigid body and the rotating frame.
\[ \frac{d \hat{i'}}{dt} = \Omega \hat{k} \times \hat{i'} = \Omega \hat{j'} \]
\[ \frac{d \hat{j'}}{dt} = \Omega \hat{k} \times \hat{j'} = -\Omega \hat{i'} \]
When we differentiate the relative position of the bug, \(B\), with respect to the rotating frame, \(A\), we have:
\[\frac{d \vec{r}_{B/A}}{dt} = \left( \dot{r}_{B/A, \ x'} \ \hat{i'} + \dot{r}_{B/A, \ y'} \ \hat{j'} \right) + \vec{\Omega} \times \left( r_{B/A, \ x'} \ \hat{i'} + r_{B/A, \ y'} \hat{j'} \ \right) \]
 \text{New term:} \quad &\, \left( \dot{r}_{B/A, \ x'} \ \hat{i'} + \dot{r}_{B/A, \ y'} \ \hat{j'} \right) = \left( \vec{v}_{B/A} \right) _{rel} \\ \text{Same as before:} \quad &\, \vec{\Omega} \times \left( r_{B/A, \ x'} \ \hat{i'} + r_{B/A, \ y'} \ \hat{j'} \right) = \vec{\Omega} \times \vec{r}_{B/A}
The new term above describes the motion of the bug due to the rotation of the rigid body (and the \(x'y'z'\) frame), while the familiar term above describes the motion of the bug as seen by an observer fixed to \(x'y'z'\). Our final expression for the velocity of the bug with respect to the fixed frame is:
\[ \vec{v}_{B/O} = \vec{v}_{A/O} + \vec{\Omega} \times \vec{r}_{B/A} + ( \vec{v}_{B/A} )_{rel} \]
This final expression has the new term, \( (\vec{v}_{B/A})_{rel} \), which describes the motion of the bug as viewed from the rotating frame. You can note that if the bug is not moving, \( (\vec{v}_{B/A})_{rel} = 0\), and we get the familiar expression from the translating, non-rotating frames. Thus, this expression is the most general relative velocity expression.
We can similarly derive an acceleration equation by differentiating the above velocity equation. The final expression is:
\[ \vec{a}_{B/O} = \vec{a}_{A/O} + \dot{\vec{\Omega}} \times \vec{r}_{B/A} + \vec{\Omega} \times ( \vec{\Omega} \times \vec{r}_{B/A} ) + 2 \vec{\Omega} \times (\vec{v}_{B/A})_{rel} + (\vec{a}_{B/A})_{rel} \]
Motion of rotating frame attached to rigid body:
\( \vec{a}_{A/O} + \dot{\vec{\Omega}} \times \vec{r}_{B/A} + \vec{\Omega} \times ( \vec{\Omega} \times \vec{r}_{B/A} ) \)
Coriolis acceleration - interaction of object motion with respect to rotating frame and motion of rotating frame:
\( 2 \vec{\Omega} \times (\vec{v}_{B/A})_{rel} \)
Motion of object with respect to rotating frame:
\( ( \vec{a}_{B/A} )_{rel} \)
Note that, for planar (2D) motion:
\[ \vec{\Omega} \times ( \vec{\Omega} \times \vec{r}_{B/A} ) = - \Omega^2 \vec{r}_{B/A} \]
Again, if the bug is sitting still, both \(rel\) terms become zero (it is not moving with respect to the rigid body), and we are left with the same relative motion expression used with translating frames. So, Equation \(\) is the most general form of the relative acceleration equation and can always be used.
When tackling these problems, there are several important things to remember:
- You need to pick the correct body to attach the rotating frame to. The correct body will have another body sliding against it. If the object of interest is pinned to the body you chose, it might not be correct.
- It is often helpful to align your rotating frame such that you end up with a simplified "\(rel\)" term or terms. For example, line up the \(x'\) axis with the direction of movement of the bug, so that \( (\vec{v}_{B/A})_{rel} \) is in the \(x'\)-direction.
- The components of all terms of any one equation must be computed along the same \(\hat{i}\) and \(\hat{j}\) directions. If the frames are not aligned, you must pick ONE FRAME and express all terms along that the directions of the ONE FRAME. (You may be able to switch between frames in different equations, but make sure you are careful with notation!)
- When you are given information in a problem, pay careful attention to what frame is being referred to.
- Make sure you include all the terms in the acceleration equation! It's easy to miss one. You should have five terms.
These are some of the most complex problems in planar kinematics, so take your time!
Exercise \(\)
A camera drone, \(D\), flies over a car race in a curved trajectory (center \(O\)) with a constant ground-speed velocity of \(v_D = 9 \ m/s\). At the moment shown, car \(C\) is traveling with velocity of \(v_c = 12 \ m/s\) and an acceleration of \(a_c = 2 \ m/s^2\) as shown. Assume \(d_1 = 7.5 \ m, \ d_2\) = \ 3 m\).
- Find the velocity of the car as observed by the camera on drone D at this instant.
- Find the acceleration of the car as observed by the camera on drone D at this instant.
Example \(\)
A breathing exercise video graphic (somewhat similar to this one) shows a small circle moving in a constrained circular path (constant radius 80 cm) at a constant angular velocity of 0.4 rad/s around an expanding and contracting inner circle. The inner circle expands and contracts sinusoidally, from a minimum radius of 30 cm to a maximum radius of 60 cm. The distance from the center of the inner circle to a point on the edge of the inner circle can be described by the equation \(r = 0.45 - 0.15 \sin (\theta)\), where \(r\) is in meters and \(\theta\) is the position of the small circle (zero at the \(x\)-axis).
Find the velocity and acceleration of point B on the edge of the inner circle as viewed by an observer on the small circle at point \(A\) (see part C of the figure below). \(\theta = 45\)°, \(\alpha = 45\)°

## 11.6: Chapter 11 Homework Problems

Exercise \(\)
You are designing a bench grinder with an operating speed of 3600 rpm.
- If you want the grinder to reach its full operating speed in 4 seconds, what must the rate of angular acceleration be in radians per second squared?
- If the grinding wheel has a diameter of 8 inches, what will the speed of the surface of the wheel be?
\(\alpha = 94.25 \ \frac{rad}{s}\)
\(v = 125.67 \ ft/s\)
Exercise \(\)
A belt-driven system has an input at pulley A, which drives pulley B, which is attached with a solid shaft to pulley C, which drives pulley D. If the input is rotating at 60 rad/s counterclockwise, determine the angular velocity and direction of rotation for the output at D.
\(\omega_D = 300 \ \frac{rad}{s}\) counterclockwise
Exercise \(\)
The piston in a piston and crank mechanism has the velocity and acceleration shown below. Using absolute motion analysis, determine the current angular velocity and angular acceleration for the crank.
\(\omega = 13.33 \ \frac{rad}{s}\) clockwise
\(\alpha = 100.16 \ \frac{rad}{s^2}\) clockwise
Exercise \(\)
A trapdoor is being opened with a hydraulic cylinder extending at constant rate of 0.7 m/s. If the door is currently at a twenty-degree angle as shown below, what is the current angular velocity and angular acceleration for the door?
\(\dot{\theta} = 0.896 \ \frac{rad}{s}, \, \ddot{\theta} = -1.246 \ \frac{rad}{s^2} \)
Exercise \(\)
A robotic arm experiences the angular velocities and accelerations shown below. Based on this information, determine the velocity and the acceleration of the end of the arm in the \(x\) and \(y\) directions.
\( v_x = 9.44 \ ft/s, \, v_y = 4.39 \ ft/s \)
\( a_x = -33.78 \ ft/s^2, \, a_y = 3.39 \ ft/s^2 \)
- 12: Newton's Second Law for Rigid Bodies

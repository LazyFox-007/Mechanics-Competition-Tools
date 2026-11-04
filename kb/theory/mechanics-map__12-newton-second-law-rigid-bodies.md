来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 12 12: Newton's Second Law for Rigid Bodies

## 12: Newton's Second Law for Rigid Bodies

## 12.1: Rigid Body Translation

With rigid bodies, we have to examine moments and at least the possibility of rotation, along with the forces and accelerations we examined with particles. Some rigid bodies will translate but not rotate (translational systems), some will rotate but not translate (fixed axis rotation), and some will rotate and translate (general planar motion). Overall, we will start with an examination of translational systems, then examine fixed axis rotation, then pull everything together for general planar motion.
As the start of our analysis, we will go back to Newton's Second Law. Since this is a rigid body system, we include both the translational and rotational versions.
\[ \sum \vec{F} = m * \vec{a} \]
\[ \sum \vec{M} = I * \vec{\alpha} \]
As we did with particles, we can break the vector force equation into components, turning the one vector equation into two scalar equations (in the \(x\) and \(y\) directions respectively). As for the moment equation, a translational system by definition will have zero angular acceleration. With the angular acceleration being zero, the sum of the moments must all be equal to zero. This is similar to statics problems; however, there is one big difference we must take into account. The moments must be taken about the center of mass of the body. Setting the moments to zero about other points will lead to invalid solutions for any body experiencing an acceleration. Putting these specifics into action, we wind up with the three base equations of motion below. To solve for unknown forces or accelerations, we simply draw a free body diagram, put the knowns and unknowns into these equations, and solve for the unknowns.
\[ \sum F_x = m * a_x \]
\[ \sum F_y = m* a_y \]
\[ \sum M_G = 0 \]
Example \(\)
A refrigerator is 2.5 feet wide and 6 feet tall, and weighs 80 lbs. The center of mass is 1.25 feet from either side and 2 feet up from the base. If the refrigerator is on a conveyor belt that is accelerating the fridge at a rate of 1 ft/s2, what are the normal forces at each of the feet?
- 12: Newton's Second Law for Rigid Bodies      12.2: Fixed-Axis Rotation
- 12: Newton's Second Law for Rigid Bodies

## 12.2: Fixed-Axis Rotation

- Balanced Rotation
- Unbalanced Rotation
With rigid bodies, we have to examine moments and at least the possibility of rotation along with the forces and accelerations we examined with particles. Some rigid bodies will translate but not rotate (translational systems), some will rotate but not translate (fixed axis rotation), and some will rotate and translate (general planar motion). Here we will examine rigid body rotation about a fixed axis. As the name would suggest, fixed axis rotation is the analysis of any rigid body that rotates about some axis that does not move. Many devices rotate about their center, though the objects do not need to rotate about their center point for this analysis to work.
We will again start with Newton's Second Law. Since this is a rigid body system, we include both the translational and rotational versions.
\[ \sum \vec{F} = m * \vec{a} \]
\[ \sum \vec{M} = I * \vec{\alpha} \]
By setting up free body diagrams, determining the equations of motion using Newton's Second Law, and solving for the unknowns, we can find forces based on the accelerations or vice versa.

## Balanced Rotation

If the center of mass of the body is at the axis of rotation, which is known as balanced rotation, then acceleration at that point will be equal to zero. The pitching machine above is an example of a balanced rotation, and most fixed axis systems will be intentionally built to be balanced. With the acceleration of the center of mass being zero, the sum of the forces in both the \(x\) and \(y\) directions must be also be equal to zero.
\[ \sum F_x = 0 \]
\[ \sum F_y = 0 \]
In addition to the force equations, we will can also use the moment equations to solve for unknowns. In simple planar motion, this will be a single moment equation which we take about the axis of rotation or center of mass (remember that they are the same point in balanced rotation).
\[ \sum M_O = I_O * \alpha \]

## Unbalanced Rotation

When the center of mass is not located on the axis of rotation, the center of mass will be accelerating and therefore forces will be exerted to cause that acceleration. In perfectly anchored systems these will be forces exerted by the bearings, though these forces can often be felt as vibrations in real systems.
The kinematics equations discussed in the previous chapter can be used to determine the acceleration of a point on a rotating body, that point being the center of mass in this case. After determining those accelerations, they can be put into force equations, most likely using the \(r\) and \(\theta\) directions.
\[ \sum F_r = m a_r \]
\[ \sum F_{\theta} = m a_{\theta} \]
Note that as the body rotates, the direction of the acceleration and the direction of the forces change. Also note that the further the center of mass is from the axis of rotation, the larger the mass. The larger the angular velocity, the larger these forces will be.
To supplement the force equations, we can use a moment equation about either the axis of rotation or the center of mass, as these are no longer the same point. Whichever is chosen, just be sure to be consistent in taking the moments and the mass moment of inertia about the same point.
\[ \sum M_O = I_O * \alpha \quad\quad \text{or} \quad\quad \sum M_G = I_G * \alpha \]
More information on how to calculate the mass moment of inertia for a body can be found in Appendix 2.
Example \(\)
A hard drive platter 8 cm in diameter accelerates at a constant rate of 150 rad/s2. If the hard drive weighs a uniformly distributed 0.05 kg and we approximate the hard drive as a flat circular disc, what moment does the motor need to exert to accelerate the drive at this rate?
Example \(\)
The drum in a washing machine can be approximated as a cylinder 0.4 meters in diameter and 0.3 meters in height with a uniformly distributed mass of 35 kilograms when full. If we wish to achieve an acceleration of 15 rad/s2, what torque must the motor exert at the center of the drum?

## 12.3: Rigid-Body General Planar Motion

In general planar motion, bodies are both rotating and translating at the same time. As a result, we will need to relate the forces to the acceleration of the center of mass of the body as well as relating the moments to the angular accelerations.
To analyze a body undergoing general planar motion, we will start by drawing a free body diagram of the body in motion. Be sure to identify the center of mass, as well as identifying all known and unknown forces, and known and unknown moments acting on the body. It is also sometimes helpful to label any key dimensions as well as using dashed lines to identify any known accelerations or angular accelerations.
Next, we move on to identifying the equations of motion. At its core, this means going back to Newton's Second Law. Since this is a rigid body system, we include both the translational and rotational versions.
\[ \sum \vec{F} = m * \vec{a} \]
\[ \sum \vec{M} = I * \vec{\alpha} \]
As we did with the previous translational systems, we will break the force equation into components, turning the one vector equation into two scalar equations. Additionally, it's important to always use the center of mass for the accelerations in our force equations and take the moments and moment of inertia about the center of mass for our moment equation.
\[ \sum F_x = m * a_x \]
\[ \sum F_y = m * a_y \]
\[ \sum M_{COM} = I * \alpha \]
Plugging the known forces, moments, and accelerations into the above equations, we can solve for up to three unknowns. If more than three unknowns exist in the equations, we will sometimes have to go back to kinematics to relate quantities such as acceleration and angular acceleration.
Example \(\)
A cylinder with a radius of 0.15 m and a mass of 10 kg is placed on a ramp at a 20-degree angle. If the cylinder is released from rest and rolls without slipping, what is the initial angular acceleration of the cylinder and the time required for the cylinder to roll 5 meters?
Example \(\)
The cable spool shown below has a weight of 50 lbs and has a moment of inertia of 0.28 slug-ft2. Assume the spool rolls without slipping when we apply a 50-lb tension in the cable.
- What is the friction force between the spool and the ground?
- What is the acceleration of the center of mass of the spool?
Example \(\)
You are designing a Frisbee launcher to launch a 40-cm-diameter, 0.6 kg Frisbee that can be modeled as flat circular disc. If you want the Frisbee to have a linear acceleration of 20 m/s2 and an angular acceleration of 50 rad/s2 as shown below, what should \(F_1\) and \(F_2\) be?
Example \(\)
A pickup truck is carrying a 30-kg, 6-meter-long ladder at a 35-degree angle as shown below. The ladder is wedged against the tailgate at A and makes contact with the roof of the truck at B. The distance from A to B is 2 meters. At what rate of acceleration would we expect the ladder to start to rotate upwards?

## 12.4: Multi-Body General Planar Motion

In cases where multiple connected rigid bodies are undergoing some sort of motion, we can extend our analysis of general planar motion to this multi-body situation. In these cases, which we will call multi-body kinetics problems, we will analyze each body independently as we did for general planar motion, but we will also need to pay attention to the Newton's Third Law pairs. Each body will have forces exerted on it by the surrounding bodies, and it will exert equal and opposite forces back through those same connections.
To analyze a multi-body system, we will start by drawing a free body diagram of each body in motion. Be sure to identify the center of mass, as well as identifying all known and unknown forces, and known and unknown moments acting on the body. When drawing forces at connection points, be sure to make the forces equal and opposite on the connected body to satisfy Newton's Third Law. It is also sometimes helpful to label any key dimensions as well as using dashed lines to identify any known accelerations or angular accelerations. Often, you will need to solve a kinematics problem using absolute motion analysis or relative motion analysis in order to determine the accelerations of the centers of mass and the angular accelerations for each body. Make sure all these accelerations are with respect to ground.
Next we move onto identifying the equations of motion for each body in the system. In two dimensions, we will use the same three equations we used for general planar motion. Be sure to find the the accelerations of all the centers of masses, find all moments about the center of mass, and take the mass moments of inertia about the center of mass of each body.
\[ \sum F_x = m * a_x \]
\[ \sum F_y = m * a_y \]
\[ \sum M_G = I_G * \alpha \]
Plugging the known forces, moments, and accelerations into the above equations we can solve for up to three unknowns per body. If more than three unknowns exist in any one set of equations, you will need to start with an adjacent body. Once unknown forces are determined on one body, they can become knowns on the connected body, reducing the number of unknowns to solve for.
Example \(\)
A robotic arm has two sections (OA and AB), with section OA having a mass of 10 kg and section AB having a mass of 7 kg. Treat each section as a slender rod. If we wish to accelerate member AB from a standstill at a rate of 3 rad/s² and keep the left section stationary, what moments must we exert at joints O and A?

## 12.5: Chapter 12 Homework Problems

Exercise \(\)
The SUV shown below has an initial velocity of 90 ft/s. It slams on its brakes, coming to a stop over a distance of 300 feet. If the car has a weight of 3500 lbs and a center of mass as shown below, what are the normal forces at the front wheels? What are the normal forces at the back wheels?
\( F_{N_{rear}} = 1291.4 \ lbs\)
\( F_{N_{front}} = 2208.6 \ lbs\)
Exercise \(\)
A ring-shaped space station can be approximated as a thin ring 60 meters in diameter with a mass of 500,000 kg. The space station has a set of thrusters able to exert equal and opposite forces as shown below. If we want to cause an angular acceleration of 0.1 rad/s² in the space station, what is the force required from each thruster?
\(F_{thruster} = 750 \ kN\)
Exercise \(\)
A 50-kg barrel with a diameter of 0.75 meters is placed on a 20-degree slope. Assuming the barrel rolls without slipping, what will the acceleration of the barrel's center of mass be?
\(a_x = 2.24 \ m/s^2\)
Exercise \(\)
A 3-meter-long, 25-kg beam is supported by two cables as shown below. You can treat the beam as a slender rod. Assume that we want the left end of the beam at point A to remain at a constant height while the right end of the beam at point B accelerates upwards at a rate of 1 m/s².
- What is the rate of acceleration of the center of the beam and the rate of angular acceleration for the beam?
- What will \(T_1\) and \(T_2\) need to be to achieve these accelerations?
\( a_{C\y} = 0.5 \ m/s^2, \, \alpha = 0.333 \ \frac{rad}{s} \)
\( T_1 = 81.75 \ N, \, T_2 = 176 \ N \)
Exercise \(\)
You are modeling the robotic arm shown below. Treat each section of the arm as a slender rod. Section OA weighs 30 lbs and section AB weighs 18 lbs. If we want the relative angular accelerations and velocities shown below, what should the motor torques be at O and A? (This is a top-down view of the robot arm.)
\(M_O = - 3.9 \ ft\)-\(lbs\)
\(M_A = -19.3 \ ft\)-\(lbs\)
- 13: Work and Energy in Rigid Bodies

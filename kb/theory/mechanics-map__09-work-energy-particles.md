来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 09 9: Work and Energy in Particles

## 9: Work and Energy in Particles

## 9.0: Video Introduction to Chapter 9

- 9: Work and Energy in Particles      9.1: Conservation of Energy for Particles
- 9: Work and Energy in Particles

## 9.1: Conservation of Energy for Particles

- Work:
- Energy:
The concepts of work and energy provide the basis for solving a variety of kinetics problems. Generally, this method is called the Energy Method or the Conservation of Energy, and it can be boiled down to the idea that the work done to a body will be equal to the change in energy of that body. Dividing energy into kinetic and potential energy pieces as we often do in dynamics problems, we arrive at the following base equation for the conservation of energy.
\[ W = \Delta KE + \Delta PE \]
It is important to notice that unlike Newton's Second Law, the above equation is not a vector equation. It does not need to be broken down into components which can simplify the process. However, we only have a single equation and therefore can only solve for a single unknown, which can limit the method.

## Work:

To understand how to use the energy method we first need to understand the concepts of work and energy. Work in general is a force exerted over a distance. If we imagine a single, constant force pushing a body in a single direction over some distance, the work done by that force would be equal to the magnitude of that force times the distance the body traveled. If we have a force that is opposing the travel (such as friction), it would be negative work.
\[ W_{push} = F_{push} * d \]
\[ W_{friction} = - F_{friction} * d \]
For instances where forces and the direction of travel do not match, the component of the force in the direction of travel is the only piece of the force that will do work. Following through with this logic, forces that are perpendicular to the direction of travel for a body will exert no work on a body because there is no component of the force in the direction of travel.
\[ W_{push} = F_{push} \cos (\theta) * d \]
\[ W_{normal} = 0 \]
In the case of a force that does not remain constant, we will need to account for the changing force. To do this we will simply integrate the force function over the distance traveled by the body. Just as before, only the component of the force in the direction of travel will count towards the work done, and forces opposing travel will be negative work.
\[ W = \int\limits_{x_1}^{x_2} F(x) \, dx \]

## Energy:

When discussing energy in engineering dynamics, we will usually break energy down into kinetic energy and potential energy. Kinetic energy is the the energy mass in motion, while potential energy represents the energy that is stored up due to the position or stresses in a body.
In its equation form, the kinetic energy of a particle is represented by one half of the mass of the body times its velocity squared. If we wish to determine the change in kinetic energy, we would simply take the final kinetic energy minus the initial kinetic energy.
\[ KE = \frac{1}{2} m v^2 \]
\[ \Delta KE = \frac{1}{2} m v_f^2 - \frac{1}{2} m v_i^2 \]
As a note, a body that is rotating will also have rotational kinetic energy, but we will save that for our discussion of work and energy with rigid bodies.
Potential energy, unlike kinetic energy, is not really energy at all. Instead, it represents the work that a given force will potentially do between two instants in time. Potential energy can come in many forms, but the two we will discuss here are gravitational potential energy and elastic potential energy. These represent the work that the gravitational force and a spring force will do, respectively. We often use these potential energy terms in place of the work done by gravity or springs. When including these potential energy terms, it's important to not additionally include the work done by gravity or spring forces.
The change in gravitational potential energy for any system is represented by the product of the mass of the body, the value \(g\) (9.81 m/s2 or 32.2 ft/s2 on the earth's surface), and the vertical change in height between the start position and the end position. In equation form, this is as follows.
\[ \Delta PE_{gravity} = m * g * \Delta h \]
To find the change in elastic potential energy, we will need to know the stiffness of the spring (represented by \(k\), in units of force per distance) as well as the distance the spring has been stretched or compressed from its natural resting length (represented by \(x\), in units of distance). Once we have those values, the elastic potential energy can be calculated by multiplying one half of the stiffness by the square of the distance \(x\). To find the change in elastic potential energy, we simply take the final elastic potential energy and subtract the initial elastic potential energy.
\[ \Delta PE _{spring} = \frac{1}{2} k x_f^2 - \frac{1}{2} k x_i^2 \]
Going back to our original conservation of energy equation, we simply plug the appropriate terms on each side (work on the left and energies on the right) and balance the two sides to solve for any unknowns. Terms that do not exist or do not change, such as elastic potential energy in a problem with no springs or \(\Delta KE\) in a problem where there is no change in the speed of the body, can be set to zero.
Example \(\)
A 16-pound crate slides down a ramp as shown below. The crate is released from a height of 10 feet above the ground.
- What is the work done by gravity?
- What is the change in gravitational potential energy?
Example \(\)
A spring with an unstretched length of 40 cm and a \(k\) value of 120 N/cm is used to lift a 5-kg box from a height of 20 cm to a height of 30 cm. If the box starts at rest, what would you expect the final velocity to be?
Example \(\)
A 2,000-pound wrecking ball hangs from the end of a 40-foot cable. If the wrecking ball is released from an angle of 40 degrees from vertical, what would the expected maximum velocity at the bottom point of the travel path be?
Example \(\)
A 24,000-kilogram aircraft is launched from an aircraft carrier using a hydraulic catapult. If the force the catapult exerts over the 90-meter runway is shown in the graph below:
- What is the work done by the catapult?
- What is the speed of the plane at the end of the runway?

## 9.2: Power and Efficiency for Particles

- Power
- Efficiency
Related to the concepts of work and energy are the concepts of power and efficiency. At its core, power is the rate at which work is being done, and efficiency is the percentage of useful work or power that is transferred from the input to the output of some system.

## Power

Power at any instant is defined as the derivative of work with respect to time. If we look at the average power over a set period, we can simply measure the work done and divide that by the time. Work is defined as the force times the distance traveled, and distance over time is the velocity of a object, giving us many possible options for relating power, work, force, distance, time, and velocity.
\[ P = \frac{dW}{dt} \]
\[ P_{ave} = \frac{W}{t} = \frac{F * d}{t} = F * v \]
The common units of power are watts for the metric system, where one watt is defined as one joule per second, or one Newton-meter per second, and horsepower in the English system, where one horsepower is defined as 550 foot-pounds per second. Maximum power ratings are often a primary specification for motors and engines, as gear trains can easily change the torque provided by a motor but the overall power will not be altered by gearing.

## Efficiency

Any devices with work/power inputs and outputs will have some loss of work or power between that input and output, due to things like friction. While energy is always conserved, some energies such as heat may not be considered useful. A measure of the useful work or power that makes it from the input of a device to the output is the efficiency. Specifically, efficiency is defined as the work out of a device divided by the work put into the device. With power being the work over time, efficiency can also be described as power out divided by the power in to a device (the time term would cancel out, leaving us with our original definition).
\[ \eta = \frac{W_{out}}{W_{in}} = \frac{P_{out}}{P_{in}} \]
It is impossible to have efficiencies greater than one (or 100%) because that would be a violation of the conservation of energy; however, for most devices we wish to get the efficiencies as close to one as possible. This is not only because greater efficiencies waste less work/power, but also because any work or power that is "lost" in the device will be turned into heat that may build up.
Example \(\)
If a car delivers an average 100 horsepower to the road and weighs a total of 1.2 tons, how long will it take to go from 0 to 60 mph?
Example \(\)
Your car broke down and now needs to be repaired. How much power is required for a lift to raise your 1.2 ton car 6 feet off the ground in 15 seconds?
Example \(\)
The drag force of air on a car is equal to \[ F_d = \frac{1}{2} \rho v^2 c_d A \nonumber \] where \(\rho\) is the is the density of the air, \(v\) is the velocity, \(c_d\) is the drag coefficient, and \(A\) is the frontal area. If a Mazda RX7 has a drag coefficient of 0.29, a frontal area of 5.95 square feet, and a max power output of 146 hp, and the density of air is 0.002326 slug/ft³, what is the theoretical top speed of the Mazda assuming it only has to fight wind resistance?

## 9.3: Conservation of Energy for Systems of Particles

Just as we used the energy method for a single particle, we can also use the energy method for a system of particles. As a reminder, the conservation of energy equation states that the change in energy of a body (including kinetic and potential energies) will be equal to the work done to a body between during that time.
\[ W = \Delta KE _ \Delta PE \]
For a system of particles, the sum of the work done to all particles will be equal to the change in energy of all particles collectively, essentially combining multiple conservation of energy equations into one.
\[ \sum W = \sum \Delta KE + \sum \Delta PE \]
This would seem to make one complex equation out of multiple simple conservation of energy equations (applying the conservation of energy separately to each body), but there is an advantage in that internal forces in the system will cancel out. In the diagram below, we can see a system of two particles connected via a cable. Examining the bodies separately, we would have two tension forces and a friction force all doing work to one box or the other. In the single equation for the system of boxes, however, the work done by the two tension forces (one positive and one negative) will sum up to zero. This will be true for any forces that are exerted between the bodies in the system, and forces like these are known as internal forces. The friction force, on the other hand, is an example of an external force, in that it exists between the top box and the surface (which is not part of our system).
In the end, the sum of the work done by external forces will be equal to the change in total energy for the system of particles. Since we only have a single equation, we can only solve for a single unknown. We will often have to go back to our kinematics equations to relate the velocities and displacements of the various bodies to one another. Since these systems often consist of bodies connected to one another via cables, dependent motion analysis in particular will often come into play.
Example \(\)
Two blocks are connected by a massless rope and a frictionless pulley as shown below. If the coefficient of friction between block A and the surface is 0.4, what is the speed of the blocks after block A has moved 6 ft?
Example \(\)
The elevator shown below has a mass of 1500 kg and the counterweight has a mass of 500 kg. At some point the cable attached to the motor snaps, causing the elevator to begin falling. After falling 3 meters with no outside forces, what is the speed of the elevator? If the emergency brake is then applied at this point (3 m below the original position), exerting a constant force of 15,000 N, how much farther will the elevator fall before coming to a stop?

## 9.4: Chapter 9 Homework Problems

Exercise \(\)
A car with a mass of 1100 kg locks up its brakes when it is traveling at 50 km/hr, stopping over a distance of 18 meters. If the same car were to lock up its brakes when traveling 80 km/hr, how far would you expect the car to slide before coming to a stop? (Hint: assume the same friction force in both cases).
\(d = 46.06 \, m\)
Exercise \(\)
A 2500-lb car traveling 60 mph (88 ft/s) impacts a highway crash barrier as shown below. If the barrier were designed to exert the following force over the 40-ft distance of the barrier, how far would you expect the car to travel after impacting the barrier?
\(d = 25.03 \, ft\) (assuming no holes in the barrier)
Exercise \(\)
The Duquesne Incline transports passengers up a 30.5 degree slope. If a fully loaded car has a mass of 5500 kg, what power is required to maintain an uphill speed of 10 km/hr?
\(P = 76.13 \, kW\)
Exercise \(\)
A bungee jumper with a weight of 150 lbs uses a bungee cord with an unstretched length of 60 feet.
- Assuming no air resistance, what will the jumper’s velocity be just before the bungee cord starts to stretch?
- If the bungee jumper falls a maximum distance of 150 feet, what is the spring constant of the bungee cord?
\(v = 62.16 \, ft\)
\(k = 5.55 \, lb/ft\)
Exercise \(\)
An 1100-kg truck is being used to raise a 100-kg box using the setup shown below. When the box is at a height of 3 meters, the box has a velocity of 1 m/s.
- How far did the truck travel to lift the box this high? (Hint: this is a dependent motion problem)
- What is the velocity of the truck at this time?
- What is the work that the truck has done over this time?
\(d = 6.7 \, m\)
\(v = 2.12 \, m/s\)
\(W = 5464.92 \, J\)
- 10: Impulse and Momentum in Particles

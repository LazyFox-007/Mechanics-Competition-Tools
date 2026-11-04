来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 13 13: Work and Energy in Rigid Bodies

## 13: Work and Energy in Rigid Bodies

## 13.1: Conservation of Energy for Rigid Bodies

- Work in Rigid Body Problems:
- Energy:
The concepts of Work and Energy provide the basis for solving a variety of kinetics problems. Generally, this method is called the Energy Method or the Conservation of Energy, and it can be boiled down to the idea that the work done to a body will be equal to the change in energy of that body. Dividing energy into kinetic and potential energy pieces as we often do in dynamics problems, we arrive at the following base equation for the conservation of energy.
\[ W = \Delta KE + \Delta PE \]
It is important to notice that unlike Newton's Second Law, the above equation is not a vector equation. It does not need to be broken down into components which can simplify the process. However, we only have a single equation and therefore can only solve for a single unknown, which can limit this method.

## Work in Rigid Body Problems:

For work done to a rigid body, we must consider any force applied over a distance as we did for particles, as well as any moment exerted over some angle of rotation. If these are constant forces and constant moments, we simply multiple the force times the distance and the moment times the angle of rotation to find the overall work done in the problem. As with particles, these are the components of forces in the direction of travel, with forces opposing the motion counting as negative work. Similarly, these are moments in the direction of rotation, with moments opposing the rotation counting as negative work. Both types of work are additive, with all work being lumped together for analysis.
\[ W = F * d + M * \Delta \theta \]
In instances of non-constant forces and non-constant moments, we will need to integrate the forces and moments over the distance traveled and the angle of rotation, respectively.
\[ W = \int \limits_{x_1}^{x_2} F(x) \, dx + \int \limits_{\theta_1}^{\theta_2} M(\theta) \, d \theta \]

## Energy:

In rigid bodies, as with particles, we will break energy into kinetic energy and potential energy. Kinetic energy is the the energy mass in motion, while potential energy represents the energy that is stored up due to the position or stresses in a body.
In its equation form, the kinetic energy of a rigid body is represented by one-half of the mass of the body times its velocity squared, plus one-half of the mass moment of inertia times the angular velocity squared. If we wish to determine the change in kinetic energy, we would simply take the final kinetic energy minus the initial kinetic energy.
\[ KE = \frac{1}{2} m v^2 + \frac{1}{2} I \omega^2 \]
\[ \Delta KE = \left( \frac{1}{2} m v_f^2 - \frac{1}{2} m v_i^2 \right) + \left( \frac{1}{2} I \omega_f^2 - \frac{1}{2} I \omega_i^2 \right) \]
Potential energy, unlike kinetic energy, is not really energy at all. Instead, it represents the work that a given force will potentially do between two instants in time. Potential energy can come in many forms, but the two we will discuss here are gravitational potential energy and elastic potential energy. These represent the work that the gravitational force and a spring force will do, respectively. We often use these potential energy terms in place of the work done by gravity or springs respectively. When including these potential energy terms, it's important to not also include the work done by gravity or spring forces.
The change in gravitational potential energy for any system is represented by the mass of the body, times the value \(g\) (9.81 m/s2 or 32.2 ft/s2 on the earth's surface), times the vertical change in height between the start position and the end position. In equation form, this is as follows. \[ \Delta PE = m * g * \Delta h \]
Unlike work and kinetic energy, there is no rotational version of gravitational potential energy, so this is exactly the same as we had for particles.
To determine the change in elastic potential energy, we will have to identify any linear springs (as we had for particles), as well as any torsional springs and the spring constants for each of these springs.
To find the change in elastic potential energy, we will need to know the stiffness of any spring in the problem (represented by \(k\), in units of force per distance for linear springs or moment per angle of twist for torsional springs) as well as the distance or angle the spring has been stretched above or below its natural resting position. This difference from resting position is represented by distance \(x\) for linear springs, or angle \(\theta\) for torsional springs. Once we have those values, the elastic potential energy can be calculated by multiplying one-half of the stiffness by the distance \(x\) squared or the angle \(\theta\) squared. To find the change in elastic potential energy, we simply take the final elastic potential energy minus the initial elastic potential energy.
\[ \Delta PE_{linear \ spring} = \frac{1}{2} k \ x_f^2 - \frac{1}{2} k \ x_i^2 \]
\[ \Delta PE_{torsional \ spring} = \frac{1}{2} k \ \theta_f^2 - \frac{1}{2} k \ \theta_i^2 \]
Going back to our original conservation of energy equation, we simply plug the appropriate terms on each side (work on the left and energies on the right) and balance the two sides to solve for any unknowns. Terms that do not exist or do not change (such as elastic potential energy in a problem with no springs, or \(\Delta KE\) in a problem where there is no change in the speed of the body) can be set to zero. Again, there is only one equation, so we can only solve for a single unknown unless we supplement the conservation of energy equation with other relationship equations.
Example \(\)
The turntable on a record player consists of a disk 12 inches in diameter with a weight of 5 lbs. The motor accelerates the turntable from rest to its operating speed of 33.33 rpm in one rotation. What is the work done by the motor? What is the average torque the motor exerted?
Video \(\): Worked solution to example problem \(\), provided by Dr. Majid Chatsaz. YouTube source: https://youtu.be/UPHgU-o80Q0.
Example \(\)
A system as shown below is used to passively slow the lowering of a gate. The gate can be approximated as a flat plate on its edge with a mass of 25 kilograms and a height of 2 meters. Assume the spring is unstretched as shown in the diagram.
- What would the angular velocity of the gate be without the spring?
- If we want to reduce the angular velocity at the bottom to 25% of its original value, what should the spring constant be?
Example \(\)
A 5-kilogram spherical ball with a radius of 0.05 meters is placed on a ramp as shown below. If the ball rolls without slipping, what is the velocity of the ball at the bottom of the ramp?
Example \(\)
A 16-kilogram half-cylinder is placed on a hard, flat surface as shown below and released from rest. What will the maximum angular velocity be as it rocks back and forth?
Example \(\)
A mechanism consists of two 3-kilogram wheels connected to a 2-kilogram bar as shown below. Based on the dimensions in the diagram, what is the minimum required initial velocity for the wheels to ensure the mechanism makes it all the way through one rotation without rocking backwards?
- 13: Work and Energy in Rigid Bodies      13.2: Power and Efficiency in Rigid Bodies
- 13: Work and Energy in Rigid Bodies

## 13.2: Power and Efficiency in Rigid Bodies

- Power
- Efficiency
Related to the concepts of work and energy are the concepts of power and efficiency. At its core, power is the rate at which work is being done, and efficiency is the percentage of useful work or power that is transferred from input to output of some system.

## Power

Power at any instant is defined as the derivative of work with respect to time. \[ P = \frac{dW}{dt} \]
If we look at the average power over a set period, we can simply measure the work done and divide that by the time. Work for a rigid body is defined as the force times the distance the center of mass travels, plus the moment times angle of rotation (in radians) for our body.
\[ P_{ave} = \frac{W}{t} = \frac{F*d + M * \Delta \theta}{t} \]
Using the definition of velocity (distance over time) and the definition of angular velocity (\(\Delta \theta\) over time), we arrive at a third equation for power at a given instant.
\[ P = F * v + M * \omega \]
The common units of power are watts for the metric system, where one watt is defined as one Joule per second or one Newton-meter per second, and horsepower in the English system, where one horsepower is defined as 550 foot-pounds per second.

## Efficiency

Any devices with work/power inputs and outputs will have some loss of work or power between that input and output due to things like friction. While energy is always conserved, some energies such as heat may not be considered useful. A measure of the useful work or power that makes it from the input of a device to the output is the efficiency. Specifically, efficiency is defined as the work gotten out of a device divided by the work put into the device. With power being the work over time, efficiency can also be described as power out of a device divided by the power put into a device (the time term would cancel out, leaving us with our original definition).
\[ \eta = \frac{W_{out}}{W_{in}} = \frac{P_{out}}{P_{in}} \]
It is impossible to have efficiencies greater than one (or 100%) because that would be a violation of the conservation of energy; however, for most devices we wish to get the efficiencies as close to one as possible. This is not only because it does not waste work/power, but also because any work or power that is "lost" in the device will be turned into heat that may build up.
Example \(\)
The input to a gearbox has a measured 32 foot-pounds of torque at 700 rpm. The output has 207 foot-pounds of torque at 100 rpm.
- What is the power at the input?
- What is the power at the output?
- What is the efficiency of the gearbox?

## 13.3: Chapter 13 Homework Problems

Exercise \(\)
An impact-testing device consists of a 20-kilogram box supported by two slender 5-kilogram rods. The two rods are set up in parallel so that the box remains level as it swings. If the whole system is released from the horizontal position shown below, what is the velocity of the box after it has traveled 90°?
\(v = 3.97 \ m/s\)
Example \(\)
A 40-lb door with a width of 36 inches is attached to a spring with an unstretched length of 4 inches, designed to close the door when left open. The spring is anchored as shown below when closed (solid outline is closed, dotted outline is open 90°). If we want the door to have an angular velocity of 0.2 rad/s upon closing when released from rest at the 90° open position, what should the spring constant of the spring be? (This is the top view of the door below)
\(k = 2.68 \ lb/ft = 0.224 \ lb/in.\)
- 14: Impulse and Momentum in Rigid Bodies

来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 14 14: Impulse and Momentum in Rigid Bodies

## 14: Impulse and Momentum in Rigid Bodies

## 14.1: Impulse-Momentum Equations for a Rigid Body

- Impulse:
- Momentum:
The concepts of impulse and momentum provide a third method of solving kinetics problems in dynamics. Generally this method is called the Impulse-Momentum Method, and it can be boiled down to the idea that the impulse exerted on a body over a given time will be equal to the change in that body's momentum. In a rigid body we will be concerned with not only linear impulse and momentum, but also angular impulse and momentum. The linear and angular impulse momentum equations are below, with the new term for angular impulse \((\vec{K})\) starting out the angular impulse momentum equation.
\[ \vec{J} = m \vec{v}_f - m \vec{v}_i \]
\[ \vec{K} = I_G \vec{\omega}_f - I_G \vec{\omega}_i \]
For two-dimensional problems, we can break the linear impulse equation down into two scalar components to solve. In the case of planar problems, we simply need to break all forces and velocities into \(x\) and \(y\) components - since all rotation will be about the \(z\)-axis, the angular impulse momentum equation remains a single equation. Notice, however, that we will need to take the mass moment of inertia about the center of mass of the body into account; similarly, we will use the velocity of the center of mass when discussing the velocity in the linear impulse momentum equations.
\[ J_x = m v_{f,x} - m v_{i,x} \]
\[ J_y = m v_{f,y} - m v_{i,y} \]
\[ K_z = I_G \omega_f - I_G \omega_i \]

## Impulse:

As discussed with particles, a linear impulse in its most basic form is a force integrated over a time. For a force with a constant magnitude, we can find the magnitude of the impulse by multiplying the magnitude of the force by the time that force is exerted. If the force is not constant, we simply integrate the force function over the set time period. The direction of the impulse vector will be the direction of the force vector, and the units will be a force multiplied by a time (Newton-seconds or pound-seconds, for example).
 \text{Constant magnitude force:} \quad &\, \vec{J} = \vec{F} * t \\ \text{Non-constant magnitude force:} \quad &\, \vec{J} = \int \vec{F}(t) \ dt
An angular impulse is similar to a linear impulse, except it is the moment exerted over time instead of the force exerted over time.
 \text{Constant magnitude moment:} \quad &\, \vec{K} = \vec{M} * t \\ \text{Non-constant magnitude moment:} \quad &\, \vec{K} = \int \vec{M}(t) \ dt
This moment can come either in the form of a torque directly applied to a body, or an off-center force causing a linear and angular impulse at the same time. All moments should be taken about the center of mass of the body.

## Momentum:

As discussed with particles, the linear momentum of a body will be equal to the mass of the body times its current velocity. Since velocity is a vector, the momentum will also be a vector, having both magnitude and a direction. Unlike the impulse, which happens over some set time, the momentum is captured as a snapshot of a specific instant in time (usually right before and after some impulse is exerted). The units for linear momentum will be mass times unit distance per unit time. This is usually kilogram-meters per second in metric, or slug-feet per second in English units.
Angular momentum, on the other hand, will be equal to the body's mass moment of inertia (about its center of mass) times its current angular velocity. It's important to note that while the mass moment of inertia remains constant if the body does not change shape, a shape that does change shape will likely have changes in mass moments of inertia along with changes in angular velocity.
Practice \(\)
A miter saw has an operating speed of 1500 rpm. The blade and motor armature have a combined weight of 3 lbs and a radius of gyration of 1 inch.
- What is the time required for the bearing friction alone (torque=0.015 inch-lbs) to stop the blade?
- What is the torque a braking system would need to apply to stop the blade in just 0.25 seconds?
Not yet available.
Practice \(\)
A bowling ball is modeled as a 7-kilogram uniform sphere, 300 mm in diameter. The ball is released with an initial velocity of 6 m/s on a horizontal wooden floor (\(\mu_k\) = 0.1) with zero angular velocity.
- How long does it take before the ball begins to roll without slipping?
- What is the linear velocity of the ball at this time?
Not yet available.
- 14: Impulse and Momentum in Rigid Bodies      14.2: Rigid Body Surface Collisions
- 14: Impulse and Momentum in Rigid Bodies

## 14.2: Rigid Body Surface Collisions

In instances where a moving rigid body impacts a solid and immovable surface, the resulting impact can seem chaotic. However, we can still use the ideas of impulse and momentum to predict this impact behavior.
Just as with particles, an important first step in solving problems where a rigid body impacts a surface is to identify the normal and tangential directions. The normal direction will be perpendicular to the surface being impacted, while the tangential direction will be parallel to the surface being impacted. Also important for rigid body impact is identifying both the center of mass for the body and the point of impact between the body and the surface.
To predict the linear velocities after impact in the \(n\) and \(t\) directions, as well as the angular velocity after the impact (a total of three unknowns), we will need three equations. These equations will come in the form of the conservation of momentum in the \(t\) direction, as well as two equations based on the coefficient of restitution for the velocity in the \(n\) direction and the angular velocity after the impact.
For momentum, we will notice that the normal forces during impact will always be in the normal direction. Assuming negligible friction forces (which would be in the tangential direction), we will have no change in momentum in the tangential direction and therefore no change in velocity in the tangential direction for the center of mass of the body. This gives us the first equation we can use.
\[ v_{t,C,f} = v_{t,C,i} \]
Next, examining the coefficient of restitution will give us another equation. Specifically, the coefficient of restitution relates the velocities before an after the collision in the normal direction at the point of impact.
\[ \epsilon = - \frac{v_{n,A,f}}{v_{n,A,f}} \]
If the collision is elastic we would also conserve the kinetic energy of the body, giving us our third equation. More generally, however, the coefficient of restitution can be used to quantify the amount of energy lost on the collision, with more elastic collisions conserving a higher percentage of kinetic energy and more inelastic equations conserving less kinetic energy. The equation below can be used for any elastic or semi elastic collision with a surface. Using the third equation below, we simply set \(\epsilon\) equal to one for elastic collisions or equal to the coefficient of restitution for semi-elastic collisions.
\[ \epsilon^2 = \frac{KE_f}{KE_i} \]
Between the three equations above and whatever relevant kinematics relationships are necessary, we should be able to solve for up to three unknowns. This allows us to completely predict the velocities after an impact, assuming we know the pre-impact velocities and the coefficient of restitution for the impact itself.
Practice \(\)
An 80-centimeter-long metal bar with a mass of 1 kilogram, falling at 2 meters per second, strikes the edge of a table as shown below. Assuming a coefficient of restitution of 0.9, what is the expected velocity and angular velocity of the bar after impact?
Not yet available.

## 14.3: Chapter 14 Homework Problems

Exercise \(\)
A flywheel with a diameter of 2 ft and a weight of 60 lbs is rotating at a rate of 600 rpm. A brake applies a friction force to the outer rim of the flywheel, bringing it to a stop in 1.5 seconds. Based on this information, what was the average friction force applied by the brake over this time?
\(F_{brake} = 39.01 \ lbs\)
Exercise \(\)
A ring-shaped space station can be approximated as a thin ring 60 meters in diameter with a mass of 500,000 kg. Centrifugal acceleration of the spinning station will be used to simulate gravity.
- To simulate the acceleration of Earth (9.81 m/s²), how fast will the station need to be spinning?
- If two thrusters each capable of exerting 10 kN of force will be used to get the station up to this speed, how long will we need to run the thrusters?
\(\omega_f = 0.571 \ \frac{rad}{s}\)
\(t_{thrust} = 428.25 \ s\)
- 15: Vibrations with One Degree of Freedom

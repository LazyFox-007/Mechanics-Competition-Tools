来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 15 15: Vibrations with One Degree of Freedom

## 15: Vibrations with One Degree of Freedom

## 15.1: Undamped Free Vibrations

- Example \(\)
- Example \(\)
Vibrations occur in systems that attempt to return to their resting or equilibrium state when perturbed, or pushed away from their equilibrium state. The simplest vibrations to analyze are undamped, free vibrations with one degree of freedom.
"Undamped" means that there are no energy losses with movement (whether the losses are intentional, from adding dampers, or unintentional, through drag or friction). An undamped system will vibrate forever without any additional applied forces. A simple pendulum has very low damping, and will swing for a long time before stopping. "Damped" means that there are resistive forces and energy losses with movement that cause the system to stop moving eventually.
"Free" means that, after the initial perturbation, the only forces acting on the system are internal to the system (springs, dampers) and/or gravity. A tuning fork continues to vibrate after the one initial perturbation of being struck. In contrast, "forced" means there is an external, typically periodic, force acting on the system. A jackhammer vibrates due to having a supply of compressed air continually forcing the bit up and down, and it stops vibrating very quickly without that external periodic forcing.
"One degree of freedom" means that we will only consider systems with one mass vibrating along one direction (e.g. use variable \(x\)) or about one axis (e.g. use variable \(\theta\)). Systems having more than one mass or vibrating along or about two or more axes have more than one degree of freedom.
We can derive the equation of the system by setting up a free body diagram. Consider a mass sitting on a frictionless surface, attached to a wall via a spring.
The system above is in equilibrium. It is at rest, and will stay at rest unless some other force acts on it.
To start the system vibrating, we need to perturb it. Perturbation is moving the system away from equilibrium by a small amount.
When we perturb this system, we either stretch or compress the spring. This generates a spring force, and the spring force is always in a direction that tends to pull the system back toward equilibrium.
We can generate the equation of motion of the system, and determine the specifics of how it will vibrate, by analyzing this perturbed state. Recall that the spring force or moment is:
\[ \vec{F}_k = k \vec{x} \]
\[ \vec{M}_k = k \vec{\omega} \]
Note that the spring constants in the above equations have different units, depending on whether the spring is linear (Newton/meter) or torsional (Newton-meter/radian), and that \(\theta\) must be given in radians. The magnitude of the spring force depends on \(x\), the distance perturbed from the spring's unstretched length (not necessarily the equilibrium position of the system), and the same is true for the moment of a torsional spring. The spring force or moment is in the direction/orientation opposite that of the displacement. That is, if you pull the mass to the right, the spring force points to the left.
The process for finding the equation of motion of the system is as follows:
- Sketch the system with a small positive perturbation (\(x\) or \(\theta\)).
- Draw the free body diagram of the perturbed system. Ensure that the spring force has a direction opposing the perturbation.
- Find the one equation of motion for the system in the perturbed coordinate using Newton's Second Law. Keep the same positive direction for position, and assign positive acceleration in the same direction.
- Move all terms of the equation to one side, and check that all terms are positive. If all terms are not positive, there is an error in the direction of displacement, acceleration, and/or spring force.
For the example system above, with mass \(m\) and spring constant \(k\), we derive the following:
\[ \sum F_x = m a_x = m \ddot{x} \]
\[ -F_k = m \ddot{x} \]
\[ -kx = m \ddot{x} \]
\[ m \ddot{x} + kx = 0 \]
This gives us a differential equation that describes the motion of the system. We can rewrite it in normal form:
\[ m \ddot{x} + kx = 0 \]
\[ \Rightarrow \ddot{x} + \frac{k}{m} x = 0 \]
\[ \Rightarrow \ddot{x} + \omega_n^2 x = 0 \]
The term \(\omega_n\) is called the angular natural frequency of the system, and has units of radians/second.
\[ \omega_n^2 = \frac{k}{m} \]
\[ \omega_n = \sqrt{\frac{k}{m}} \]
Assuming that the initial perturbation of the system can be described by the position and velocity of the mass at \(t=0\), then:
\[ x(0) = x_0 \]
\[ v(0) = \dot{x}(0) = v_0. \]
The solution to the differential equation, that provides the position \(x(t)\) of the system at time \(t\), is:
\[ x(t) = C \sin \left( \omega_n t + \phi \right), \]
\[ \text{where:} \quad \omega_n = \sqrt{\frac{k}{m}}, \,\, C = \sqrt{ \left( \frac{v_0}{\omega_n} \right)^2 + x_0^2 }, \,\, \phi = \tan ^{-1} \left( \frac{x_0 \omega_n}{v_0} \right). \]
The amplitude \(C\) describes the maximum displacement during the oscillations (i.e. \(x_{max}\)), and the phase \(\phi\) describes how the sine function is shifted in time.
For a system where there is torsional vibration (that is, the oscillation involves a rotation), the equations are similarly:
\[ I \ddot{\theta} + k \theta = 0 \]
\[ \Rightarrow \ddot{\theta} + \frac{k}{I} \theta = 0 \]
\[ \Rightarrow \ddot{\theta} + \omega_n^2 \theta = 0, \]
\[ \text{where} \,\, \omega_n = \sqrt{\frac{k}{I}}. \]
Assuming that the initial perturbation of the system can be described by the position and velocity of the mass at \(t=0\),
\[x(0) = x_0 \]
\[ v(0) = \dot{x}(0) = v_0. \]
The solution to the differential equation, that provides the position \(x(t)\) of the system at time \(t\), is:
\[ x(t) = C \sin (\omega_n t + \phi) \]
\[ \text{where:} \quad \omega_n = \sqrt{\frac{k}{I}}, \,\, C = \sqrt{ \left( \frac{\omega_0}{\omega_n} \right) ^2 + \theta_0^2 }, \,\, \phi = \tan ^{-1} \left( \frac{\theta_0 \omega_n}{\omega_0} \right). \]

## Example \(\)

Find an expression for the angular natural frequency of the following system, and find the maximum amplitude of vibration of the system with mass \(m\) = 10 kg and spring constant \(k\) = 200 N/m when given an initial displacement of \(x_0\) = 0.1 m and an initial velocity of \(v_0\) = 0.3 m/s.

## Example \(\)

Determine the equation of motion of the system from Newton's Second Law. Assume mass \(m\) = 5 kg and spring constant \(k\) = 500 N/m. Find the initial displacement, \(x_0\), such that the mass oscillates over a total range of 4 meters. Assume the initial perturbation velocity, \(v_0\), is 10 m/s.
- 15: Vibrations with One Degree of Freedom      15.2: Viscous Damped Free Vibrations
- 15: Vibrations with One Degree of Freedom

## 15.2: Viscous Damped Free Vibrations

- Four Viscous Damping Cases:1. \(\zeta = 0\): Undamped2. \(\zeta > 1\): Overdamped3. \(\zeta = 1\): Critically damped4. \(\zeta < 1\): Underdamped
- 1. \(\zeta = 0\): Undamped
- 2. \(\zeta > 1\): Overdamped
- 3. \(\zeta = 1\): Critically damped
- 4. \(\zeta < 1\): Underdamped
- Comparison of Viscous Damping Cases:
Viscous damping is damping that is proportional to the velocity of the system. That is, the faster the mass is moving, the more damping force is resisting that motion. Fluids like air or water generate viscous drag forces.
We will only consider linear viscous dampers, that is where the damping force is linearly proportional to velocity. The equation for the force or moment produced by the damper, in either \(x\) or \(\theta\), is:
\[ \vec{F}_c = c \vec{\dot{x}}, \]
\[ \vec{M}_c = c \vec{\dot{\theta}}, \]
where \(c\) is the damping constant. This is a physical property of the damper based on the type of fluid, size of the piston, etc. Note that the units of \(c\) change depending on whether it is damping linear motion (N-s/m) or rotational motion (N-m s/rad).
When the system is at rest in the equilibrium position, the damper produced no force on the system (no velocity), while the spring can produce force on the system, such as in the hanging mass shown above. Recall that this is the equilibrium position, but the spring is NOT at its unstretched length, as the static mass produces an extention of the spring.
If we perturb the system (applying an initial displacement, an initial velocity, or both), the system will tend to move back to its equilibrium position. What that movement looks like will depend on the system parameters (\(m\), \(c\), and \(k\)).
To determine the equation of motion of the system, we draw a free body diagram of the system with perturbation and apply Newton's Second Law.
The process for finding the equation of motion of the system is again:
- Sketch the system with a small positive perturbation (\(x\) or \(\theta\)).
- Draw the free body diagram of the perturbed system. Ensure that the spring force and the damper force have directions opposing the perturbation.
- Find the one equation of motion for the system in the perturbed coordinate using Newton's Second Law. Keep the same positive direction for position, and assign positive acceleration in the same direction.
- Move all terms of the equation to one side, and check that all terms are positive. If all terms are not positive, there is an error in the direction of displacement, acceleration, and/or spring or damper force.
For the example system above, with mass \(m\), spring constant \(k\) and damping constant \(c\), we derive the following:
\[ \sum F_x = m a_x = m \ddot{x} \]
\[ -F_k - F_c = m \ddot{x} \]
\[ -kx - \dot{c(x)} = m \ddot{x} \]
\[ m \ddot{x} + \dot{c(x)} + kx = 0 \]
This gives us a differential equation that describes the motion of the system. We can rewrite it in normal form:
\[ m \ddot{x} + c \dot{x} + kx = 0 \]
\[ \Rightarrow \ddot{x} + \frac{c}{m} \dot{x} + \frac{k}{m} x = 0 \]
\[ \Rightarrow \ddot{x} + 2 \zeta \omega_n \dot{x} + \omega_n^2 x = 0 \]
As before, the term \(\omega_n\) is called the angular natural frequency of the system, and has units of rad/s.
\[ \omega_n ^2 = \frac{k}{m}\, ; \quad \omega_n = \sqrt{\frac{k}{m}} \]
\(\zeta\) (zeta) is called the damping ratio. It is a dimensionless term that indicates the level of damping, and therefore the type of motion of the damped system.
\[ \zeta = \frac{c}{c_c} = \frac{\text{actual damping}}{\text{critical damping}} \]
The expression for critical damping comes from the solution of the differential equation. The solution to the system differential equation is of the form
\[ x(t) = a e^{rt}, \]
where \(a\) is constant and the value(s) of \(r\) can be can be obtained by differentiating this general form of the solution and substituting into the equation of motion.
\[ m r^2 e^{rt} + c r e^{rt} + k e^{rt} = 0 \]
\[ \Rightarrow (mr^2 + cr + k) e^{rt} = 0 \]
Because the exponential term is never zero, we can divide both sides by that term and get:
\[ m r^2 + cr + k = 0. \]
Using the quadratic formula, we can find the roots of the equation:
\[ r_{1,2} = \frac{-c \pm \sqrt{c^2 - 4mk}}{2m} \]
Critical damping occurs when the term under the square root sign equals zero:
\[ c_c ^2 = 4 mk \]
\[ c_c = 2 \sqrt{mk} = 2 m \omega_n \]

## Four Viscous Damping Cases:

There are four basic cases for the damping ratio. For the solutions that follow in each case, we will assume that the initial perturbation displacement of the system is \(x_0\) and the initial perturbation velocity of the system is \(v_0\).

### 1. \(\zeta = 0\): Undamped

\[ c = 0 \]
This is the case covered in the previous section. Undamped systems oscillate about the equilibrium position continuously, unless some other force is applied.

### 2. \(\zeta > 1\): Overdamped

\[ c^2 > 4 mk \]
Roots are both real and negative, but not equal to each other. Overdamped systems move slowly toward equilibrium without oscillating.
The response for an overdamped system is:
\[ x(t) = a_1 e^{ \left( \frac{-c + \sqrt{c^2 - 4mk}}{2m} \right) t} + a_2 e^{ \left( \frac{-c - \sqrt{c^2 - 4mk}}{2m} \right) t}, \]
\[ \text{where} \,\, a_1 = \frac{-v_0 + r_2 x_0}{r_2 - r_1} \,\, \text{and} \,\, a_2 = \frac{v_0 + r_1 x_0}{r_2 - r_1}. \]

### 3. \(\zeta = 1\): Critically damped

\[ c^2 = 4 mk ( = c_c^2) \]
Roots are real and both equal to \(- \omega_n\). Critically-damped systems will allow the fastest return to equilibrium without oscillation.
The solution for a critically-damped system is:
\[ x(t) = (A + Bt) e^{-\omega_n t} , \]
\[ \text{where} \,\, A = x_0 \,\, \text{and} \,\, B = v_0 + x_0 \omega_n. \]

### 4. \(\zeta < 1\): Underdamped

\[ c^2 < 4 mk \]
The roots are complex numbers. Underdamped systems do oscillate around the equilibrium point; unlike undamped systems, the amplitude of the oscillations diminishes until the system eventually stops moving at the equilibrium position.
The solution for an underdamped system is:
\[ x(t) = [ C_1 \sin (\omega_d t) + C_2 \cos (\omega_d t) ] e^{- \omega_n \zeta t} , \]
\[ \text{where} \,\, C_1 = \frac{v_0 + \omega_n \zeta x_0}{\omega_d}, \,\, C_2 = x_0, \,\, \text{and} \,\, \zeta = \frac{c}{2 m \omega_n}. \]
\(\omega_d\) is called the damped natural frequency of the system. It is always less than \(\omega_n\):
\[ \omega_d = \omega_n \sqrt{1 - \zeta^2}. \]
The period of the underdamped response differs from the undamped response as well.
\[ \text{Undamped:} \quad \tau_n = \frac{2 \pi}{\omega_n} \]
\[ \text{Underdamped:} \quad \tau_d = \frac{2 \pi}{\omega_d} \]

## Comparison of Viscous Damping Cases:

In the figure above, we can see that the critically-damped response results in the system returning to equilibrium the fastest. Also, we can see that the underdamped system amplitude is quite attenuated compared to the undamped case.

## 15.3: Friction (Coulomb) Damped Free Vibrations

- Comparison to Viscous Underdamped System
Friction can also provide vibration damping. In this case, however, the damping is not proportional to the magnitude of velocity. It only depends on the direction of velocity.
We remember from the section on dry friction that the force of friction in sliding depends only on the coefficient of kinetic friction, \(\mu_k\), and the normal force, \(F_N\).
\[ F_f = \mu_k F_N \]
The above equation does not include velocity. We know that kinetic friction acts to oppose motion, however, so a more complete expression would be:
\[F_f = - \text{sgn} (\dot{x}) \mu_k F_N , \]
where \(sgn\) is the "sign" function, a function that captures the sign (direction) of velocity. The above equation then indicates that the direction of friction is always opposite the direction of velocity, but the magnitude of velocity does not make a difference in the magnitude of friction.
The equation of motion of the system becomes:
\[ m \ddot{x} + \mu m g \ \text{sgn} (\dot{x}) + kx = 0, \]
and the solution to this equation of motion is:
\[ x(t) = \left( x_0 - \frac{(2n-1) \mu m g}{k} \right) \cos (\omega_n t) + \frac{\mu m g}{k} (-1)^{n+1} . \]
If we plot the response, we can see that there are several differences from a system with viscous damping.
Some differences when compared to viscous damping include:
- The system oscillates at the natural frequency of the system, not a damped natural frequency.
- The bounding curves are linear, not exponential.
- The system does not return to zero. This is because the magnitude of the friction force does not diminish as the system amplitude reduces, and at some point the spring force is no longer able to overcome the static friction that the system experiences when it changes direction (\(v=0\)).

## Comparison to Viscous Underdamped System

If we consider our simple linear mass-spring system, the magnitude of \(F_f\) does not change with velocity, unlike with viscous damping. If we plotted both types of damping for the same system, we would get the following:
Note that the viscous damping has more reduction in amplitude earlier (despite relatively light damping), but continues oscillating past the point when the friction-damped system has stopped (specific relative values are dependent on the values of damping constant and coefficients of friction). Also note that since the viscous damping is relatively light, the difference in period between the two plots is quite small in this example.

## 15.4: Undamped Harmonic Forced Vibrations

- Steady-State Response:Amplitude of Forced Vibration
- Amplitude of Forced Vibration
- Rotating Unbalance:Example \(\)Example \(\)
- Example \(\)
- Example \(\)
Often, mechanical systems are not undergoing free vibration, but are subject to some applied force that causes the system to vibrate. In this section, we will consider only harmonic (that is, sine and cosine) forces, but any changing force can produce vibration.
When we consider the free body diagram of the system, we now have an additional force to add: namely, the external harmonic excitation.
The equation of motion of the system above will be:
\[ m \ddot{x} + kx = F, \]
where \(F\) is a force of the form:
\[ F = F_0 \sin (\omega_0 t). \]
This equation of motion for the system can be re-written in standard form:
\[ \ddot{x} + \frac{k}{m} x = \frac{F_0}{m} \sin (\omega_0 t). \]
The solution to this system consists of the superposition of two solutions: a particular solution, \(x_p\) (related to the forcing function), and a complementary solution, \(x_c\) (which is the solution to the system without forcing).
As we saw previously, the complementary solution is the solution to the undamped free system: \[x_c = C \sin (\omega_n t + \phi). \]
We can obtain the particular solution by assuming a solution of the form: \[x_p = D \sin (\omega_0 t), \]
where \(\omega_0\) is the frequency of the harmonic forcing function. We differentiate this form of the solution, and then sub into the above equation of motion:
\[ \ddot{x}_p = - \omega_0^2 D \sin (\omega_0 t) \]
\[ - m \omega_0^2 D \sin (\omega_0 t) + k D \sin (\omega_0 t) = F_0 \sin (\omega_0 t) \]
After solving for \(D\), we can then use it to find the particular solution, \(x_p\):
\[ D = \frac{ \dfrac{F_0}{k}}{1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2} \]
\[ x_p = \frac{ \dfrac{F_0}{k}}{1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2} \ \sin (\omega_0 t). \]
Thus, the general solution for a forced, undamped system is:
\[ x_G (t) = \frac{ \dfrac{F_0}{k}}{1- \left( \dfrac{\omega_0}{\omega_n} \right) ^2} \ \sin (\omega_0 t) + C \sin (\omega_n t + \phi) \]
The above figures show the two responses at different frequencies. Recall that the value of \(\omega_n\) comes from the physical characteristics of the system (\(m, \, k\)) and \(\omega_0\) comes from the force being applied to the system. These responses are summed, to achieve the blue response (general solution) in Figure \(\) above.

## Steady-State Response:

In reality, this superimposed response does not last long. Every real system has some damping, and the natural response of the system will be damped out. As long as the external harmonic force is applied, however, the response to it will remain. When evaluating the response of the system to a harmonic forcing function, we will typically consider the steady-state response, when the natural response has been damped out and the response to the forcing function remains.

### Amplitude of Forced Vibration

The amplitude of the steady-state forced vibration depends on the ratio of the forced frequency to the natural frequency. As \(\omega_0\) approaches \(\omega_n\) (the ratio approaches 1), the magnitude \(D\) becomes very large. We can define a magnification factor:
\[ MF = \dfrac{ \dfrac{ \dfrac{F_0}{k}}{1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2}} {\dfrac{F_0}{k}} = \dfrac{1}{1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2} \]
From the figure above, we can discuss various cases:
- \(\bf{\omega_0 = \omega_n}\): Resonance occurs. This results in very large-amplitude vibrations, and is associated with high stress and failure to the system.
- \(\bf{\omega_0 \sim 0, MF \sim 1}\): The forcing function is nearly static, leaving essentially the static deflection and limited natural vibration.
- \(\bf{\omega_0 < \omega_n}\): Magnification is positive and greater than 1, meaning the vibrations are in phase (when the force acts to the left, the system displaces to the left) and the amplitude of vibration is larger than the static deflection.
- \(\bf{\omega_0 > \omega_n}\): Magnification is negative and the absolute value is typically smaller than 1, meaning the vibration is out of phase with the motion of the forcing function (when the force acts to the left, the system displaces to the right) and the amplitude of vibration is smaller than the static deflection.
- \(\bf{\omega_0 >> \omega_n}\): The force is changing direction too fast for the block's motion to respond.

## Rotating Unbalance:

One common cause of harmonic forced vibration in mechanical systems is rotating unbalance. This occurs when the axis of rotation does not pass through the center of mass, meaning that the center of mass experiences some acceleration instead of remaining stationary. This causes a force on the axle that changes direction as the center of mass rotates. We can represent this as a small mass, \(m\), rotating about the axis of rotation at some distance, called an eccentricity, \(e\). The forced angular frequency, \(\omega_0\), in this case is the angular frequency of the rotating system.
A 10-kg fan is fixed to a lightweight beam. The static weight of the fan deflects the beam by 20 mm. If the blade is designed to spin at \(\omega\) = 15 rad/s, and the blade is mounted off-center (equivalent to a 1.5 kg mass at 50 mm from the axis of rotation), determine the steady-state amplitude of vibration.
You are designing a stylish fan that uses only one blade. Approximate that blade as a narrow plate with a density per unit length of 20 g/cm. The base weight of the rest of the device (except for the blade) is 4 kg, and the whole thing is mounted on a lightweight beam. If the spring constant of the beam is \(k\) = 1000 N/m, find the length of blade than will cause resonance if the fan is designed to spin at \(\omega\) = 15 rad/s.

## 15.5: Viscous Damped Harmonic Forced Vibrations

As described in the previous section, many vibrations are caused by an external harmonic forcing function (such as rotating unbalance). While we assumed that the natural vibrations of the system eventually damped out somehow, leaving the forced vibrations at steady-state, by explicitly including viscous damping in our model we can evaluate the system through the transient stage when the natural vibrations are present.
Consider the system above. The equation of the system becomes:
\[ m \ddot{x} + c \dot{x} + kx = F_0 \sin (\omega_0 t) \]
\[ \Rightarrow \ddot{x} + \frac{c}{m} \dot{x} + \frac{k}{m} x = \frac{F_0}{m} \ \sin (\omega_0 t). \]
Because the natural vibrations will damp out with friction (as mentioned in undamped harmonic vibrations), we will only consider the particular solution. This particular solution will have the form:
\[ x_p (t) = X' \sin (\omega_0 t - \phi '). \]
After solving, we determine that the expressions for \(X'\) and \(\phi '\) are:
\[ X' = \frac{ \dfrac{F_0}{k}}{ \sqrt{ \left[ 1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2 \right] ^2 + \left[ 2 \dfrac{c}{c_c} \dfrac{\omega_0}{\omega_n} \right] ^2 }} \]
\[ \phi ' = \tan ^{-1} \left[ \frac{ 2 \dfrac{c}{c_c} \dfrac{\omega_0}{\omega_n} }{1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2} \right]. \]
The magnification factor now becomes:
\[ MF = \frac{X'}{\dfrac{F_0}{k}} = \dfrac{1}{\sqrt{ \left[ 1 - \left( \dfrac{\omega_0}{\omega_n} \right) ^2 \right] ^2 + \left[ 2 \dfrac{c}{c_c} \dfrac{\omega_0}{\omega_n} \right] ^2 }} \]
From the figure above, we can see that the extreme amplitudes at resonance only occur when the damping ratio = 0 and the ratio of frequencies is 1. Otherwise, damping inhibits the out-of-control vibrations that would otherwise be seen at resonance.
- 16: Appendix 1 - Vector and Matrix Math

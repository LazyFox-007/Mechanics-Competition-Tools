来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 07 7: Particle Kinematics

## 7: Particle Kinematics

## 7.0: Video Introduction to Chapter 7

- 7: Particle Kinematics      7.1: One-Dimensional Continuous Motion
- 7: Particle Kinematics

## 7.1: One-Dimensional Continuous Motion

- Constant Acceleration Systems:Example \(\)Example \(\)Example \(\)Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
Imagine we have a particle that is moving along a single axis. At any given point in time, this particle will have a position, which we can quantify with a single number which we will call \(x\). This value will measure the distance from some set origin point to the position of the particle. If the particle is moving over time, we will need a function to describe the position over time \(x(t)\). This is an equation where if we plug a value for \(t\), it will give us the position at that time.
The velocity of the particle is then the rate of change of the position over time. If the particle is not moving, then position is not changing over time and the velocity is zero. If the particle is moving, we will first need to find the equation for position \(x(t)\), and then take the derivative of the position equation to find the velocity equation \(v(t)\). Velocity differs from speed in that the velocity has a direction (either positive or negative for now) while the speed is simply the magnitude of the velocity (always a positive number).
Next up is the acceleration, which is the rate of change of the velocity over time. If the velocity is not changing, the acceleration will be zero. If the velocity does change over time, then we will need to take the derivative of the velocity equation \(v(t)\) to find the acceleration equation \(a(t)\). The acceleration is then also the double derivative of the position equation over time. Like the velocity, the acceleration has both a magnitude and a direction.
To simplify the notation, we often use a dot on top of the variable to indicate a time derivative. This makes the velocity (the derivative of \(x\)) \(\dot{x}\) and the acceleration (the derivative of the derivative of \(x\)) \(\ddot{x}\). These relationships and their shorthand notations are all shown below.
 \text{Position:} \quad &\, x(t) \\ \text{Velocity:} \quad &\, v(t) = \frac{dx}{dt} = \dot{x} \\ \text{Acceleration:} \quad &\, a(t) = \frac{dv}{dt} = \frac{d^2 x}{dt^2} = \ddot{x}
If we instead start with the equation for acceleration, we can take the integral of that equation \(a(t)\) to find the equation for velocity, \(v(t)\). But unlike the derivatives, we will have an extra step in this process because whenever we integrate we wind up with a constant of integration (which we will usually call \(C\)). When we integrate the acceleration equation to find the velocity equation, this constant will be the initial velocity (the velocity at time = 0).
Next we can take the integral of the velocity equation \(v(t)\) to find the position equation \(x(t)\). With this integration we will again wind up with a constant of integration, which in this case will be the initial position (the position at time = 0). These relationships are shown below.
 \text{Acceleration:} \quad &\, a(t) \\ \text{Velocity:} \quad &\, v(t) = \int a(t) \\ \text{Position:} \quad &\, x(t) = \int v(t) = \iint a(t)

## Constant Acceleration Systems:

In cases where we have a constant acceleration (often due to a constant force), we can start with a constant value for \(a(t) = a\), and work out the integrals from there. Along the way we will add the initial velocity and the initial position as the constants of integration to wind up with the formulas below.
 \text{Acceleration:} \quad &\, a(t) = a \\ \text{Velocity:} \quad &\, v(t) = at + v_0 \\ \text{Position:} \quad &\, x(t) = \frac{1}{2} a t^2 + v_0 t + x_0
If we take the equations for the position and the velocity from above, then solve both of them for \(t\) and set those equations equal to one another, we can actually wind up with another equation that directly relates position, velocity, and acceleration without needing to know the time.
\[ v^2 - v_0^2 = 2a(x - x_0) \]
It is important to remember that these equations are only valid when the acceleration is constant. When that is not the case, you will need to use calculus to find the derivatives or integrals based on the equations for position, velocity, and acceleration that you do know.
You are in a van that steadily accelerates from 20 m/s to 35 m/s over the course of 10 seconds. What is your rate of acceleration?
You are in a van that steadily accelerates from 20 m/s to 35 m/s over the course of 10 seconds. How many meters did you travel in those ten seconds?
In a rocket sled deceleration experiment, a manned sled is decelerated from a speed of 200 mph (89.4 m/s) to a stop at a constant rate of 18 G's (176.6 m/s2). How long does it take for the sled to stop? How far does the sled travel while decelerating?
A metallic particle is accelerated in a magnetic field such that its velocity over time is defined by the function \(v(t) = 4t^2 - 12\), where time is in seconds and velocity is in meters per second. If we assume that the particle has an initial position of zero \((x_0 = 0)\), what are the equations that describe the acceleration and position over time?

## 7.2: One-Dimensional Noncontinuous Motion

- Example \(\)
- Example \(\)
- Example \(\)
In continuous motion, we used a single mathematical function each to describe the position, velocity, or acceleration over time. If we cannot describe the motion with a single mathematical function over the entire time period, that motion is considered noncontinuous motion. In cases such as this, we will use different equations for different sections of the overall time period.
For an example of noncontinuous motion, imagine a car that accelerates for a few seconds, then holds a steady speed for a few seconds, then puts on the brakes and comes to a stop over the final few seconds. There is no one mathematical function we can use to describe the motion for the full time period, but if we break the motion into three pieces, then we can come up with an equation for each section of the motion.
Analyzing the first time period will be exactly the same as analyzing a continuous function. We will initially need to identify the mathematical function to describe position, or velocity, or acceleration for that first time period. Next we take derivatives to move from position to velocity to acceleration or take integrals to move from acceleration to velocity to position. Whenever we take an integral, we need to remember to include the constant of integration which will represent the initial velocity or the initial position (in the velocity and position equations, respectively).
For the second, third, and any other following sections, we will do much the same process. We will start by identifying an equation for the position, or velocity, or acceleration for that time period. From there we again take derivatives or integrals as appropriate, but now the constants of integration will be a little more complicated. Those constants still represent initial velocities and and positions in a sense, but they will be the velocity and position when \(t=0\), not the velocity and position at the start of that section.
To find the constants of integration, we are instead going to have to use the transition point, which is the point in time where we are moving from one set of equations to the next. Even though the equations are changing, we cannot have an instantaneous jump in either the position or velocity. An instantaneous jump in either position or velocity would require infinite acceleration, which is physically impossible.
To find the velocity equations for the second time frame (or third, fourth, etc.), we start by integrating the acceleration equation for that same time period. This will lead to an equation with an unknown constant of integration. To solve for that constant, we look back to the velocity equation for the previous time frame and solve for the velocity at the very end of this prior time period. Since it can't jump instantaneously, this is also the velocity at the start of the current time period. Using this velocity, along with the time \(t\) at the transition point, we can solve for the last unknown in the current velocity equation (the constant of integration).
To find the position equation for the second time frame (or third, fourth, etc.), we start by integrating the velocity equation for the same time period (you will need to solve for the unknowns in the velocity equation first, as discussed above). After integration, we should have one new constant of integration in the position equation. Just as we did with the velocity equations, we will use the position equation from the prior time frame to solve for the position at the transition point, then use that value along with the known time \(t\) to solve for the unknown constant in the current position equation.

## Example \(\)

A car accelerates from rest at a rate of 10 m/s2 for 10 seconds. The car then immediately begins decelerating at a rate of 4 m/s2 for another 25 seconds before coming to a stop. Find the equations for the acceleration, velocity, and position functions over the full 35-second time period, and plot these functions.

## Example \(\)

A plane with an initial speed of 95 m/s touches down on a runway. For the first second the plane rolls without decelerating. For the next 5 seconds reverse thrust is applied, decelerating the plane at a rate of 4 m/s2. Finally, the brakes are applied with reverse thrust increasing the rate of deceleration to 8 m/s2. How long does it take for the plane to come to a complete stop? How far does the plane travel before coming to a complete stop?

## Example \(\)

A satellite's motion is described by the velocity function shown below over a sixty-second time period. For that same time period, determine the satellite's acceleration and position functions and draw these functions on a plot.

## 7.3: Two-Dimensional Kinematics with Rectangular Coordinates

- Example \(\)
- Example \(\)
Two-dimensional motion (also called planar motion) is any motion in which the objects being analyzed stay in a single plane. When analyzing such motion, we must first decide the type of coordinate system we wish to use. The most common options in engineering are rectangular coordinate systems, normal-tangential coordinate systems, and polar coordinate systems. Any planar motion can potentially be described with any of the three systems, though each choice has potential advantages and disadvantages.
The rectangular coordinate system (also sometimes called the Cartesian coordinate system) is the most intuitive approach to describing motion. In rectangular coordinate systems we have an \(x\)-axis and a \(y\)-axis. These axes remain fixed to some origin point in the environment and they do not change over time. Instead, the bodies we are analyzing usually move relative to these fixed axes. An example of a body with a rectangular coordinate systems is shown in the figure below.
Rectangular coordinates work best for systems where all forces maintain a constant direction. The most common example of this is projectile motion, where gravity (the only force in these systems) maintains a constant downward direction. An example of a system where the forces change direction over time would be something like a car going around a curve in the road. In this case, the friction force at the tires is going to be rotating with the car. The car problem will therefore be better suited to the use of normal-tangential or polar coordinate systems.
When describing the position of a point in rectangular coordinate systems, we are going to start by describing both \(x\) and \(y\) coordinates in a vector form. For this, the values \(x\) and \(y\) represent distances and the unit vectors \(\hat{i}\) and \(\hat{j}\) are used to indicate which distance corresponds with which direction. This may seem redundant, but remember when solving actual problems, \(x\) and \(y\) will just be numbers.
\[ \text{Position:} \quad r_{p/o} (t) = x(t) \ \hat{i} + y(t) \ \hat{j} \]
Just like with one-dimensional problems, if we take the derivative of the position equation, we will find the velocity equation. If we take the derivative of the velocity equation we will wind up with the acceleration equation. Also like one-dimensional problems, we can use integration to move in the other direction, moving from an acceleration equation to a velocity equation to a position equation.
The unit vectors add a new element in two dimensions, but since the unit vectors don't change over time (they are constants), we treat them like we would any other constant for derivatives and integrals. The resulting velocity and acceleration equations are as follows.
 \text{Velocity:} \quad &\, v(t) = \dot{x}(t) \ \hat{i} + \dot{y}(t) \ \hat{j} \\[5pt] \text{Acceleration:} \quad &\, a(t) = \ddot{x}(t) \ \hat{i} + \ddot{y}(t) \ \hat{j}
The above equations are vector equations with velocities and accelerations broken down into \(x\) and \(y\) components. Since the \(x\) and \(y\) directions are perpendicular, they are also independent (movement in the \(x\) direction doesn't impact movement in the \(y\) direction, and vice versa). This essentially means we can split our vector equation into a set of two scalar equations. To do this we just put everything in front of the \(\hat{i}\) unit vectors in the \(x\) equations and everything in front of the \(\hat{j}\) unit vectors in the \(y\) equations.
 \text{Position:} \quad &\, x(t) = \dots \quad\quad y(t) = \dots \\[5pt] \text{Velocity:} \quad &\, \dot{x}(t) = \dots \quad\quad \dot{y}(t) = \dots \\[5pt] \text{Acceleration:} \quad &\, \ddot{x}(t) = \dots \quad\quad \ddot{y}(t) = \dots
Once we have everything split into \(x\)- and \(y\)-direction equations, we can just use the same processes we used for one dimensional motion to move from \(x\) to \(\dot{x}\) to \(\ddot{x}\), and from \(y\) to \(\dot{y}\) to \(\ddot{y}\). The variable linking the two equations is time \((t)\).

## Example \(\)

A motorcycle drives off a one-meter-tall ramp at an angle of 30 degrees as shown below. Determine the equations for the acceleration, velocity, and position over time. How far does the motorcycle travel in the \(x\) direction before hitting the ground?

## Example \(\)

A basketball is thrown towards a hoop that is three feet higher in the \(y\) direction and 25 feet away in the \(x\) direction. If the ball is thrown at an initial angle of 50 degrees, what must the initial velocity be for the ball to make it into the hoop?

## 7.4: Two-Dimensional Kinematics with Normal-Tangential Coordinates

- Example \(\)
- Example \(\)
Two-dimensional motion (also called planar motion) is any motion in which the objects being analyzed stay in a single plane. When analyzing such motion, we must first decide the type of coordinate system we wish to use. The most common options in engineering are rectangular coordinate systems, normal-tangential coordinate systems, and polar coordinate systems. Any planar motion can potentially be described with any of the three systems, though each choice has potential advantages and disadvantages.
The normal-tangential coordinate system centers on the body in motion. The origin point will be the body itself, meaning that the position of the particle in the normal-tangential coordinate system is always "zero". The tangential direction (\(t\)-direction) is defined as the direction of travel at that moment in time (the direction of the current velocity vector), with the normal direction (\(n\)-direction) being 90 degrees counterclockwise from the \(t\)-direction. The diagram below shows a particle following a curved path with the current normal and tangential directions.
Normal-tangential coordinate systems work best when we are observing motion from the perspective of the body in motion, such as being a passenger in a car or plane. In such cases, we would define ourself as the origin point and "forward" would be the tangential direction. An important distinction between the rectangular coordinate system and the normal-tangential coordinate system is that the axes are not fixed in the normal-tangential coordinate system. If we go back to the car example, the "forward" or tangential direction will turn with the car, but the "east" direction or the \(x\)-direction will remain constant no matter which way the car is pointed.
The way the coordinate system is defined, the position of the particle is always set to be at the origin point. The velocity is also always set to be in the tangential direction, and thus there is no velocity in the \(n\)-direction. The variable \(v\) is the body's current speed.
 \text{Position:} \quad &\, r_{p/o}(t) = 0 \ \hat{u}_t + 0 \ \hat{u}_n \\[5pt] \text{Velocity:} \quad &\, v(t) = v \ \hat{u}_t
To find the acceleration, we need to take the derivative of the velocity function. This may seem simple, but there is a new thing to consider in that the \(u_t\) unit vector is not constant. This means a change in speed can cause an acceleration, and a change in direction (which would change the \(u_t\) direction) can also cause an acceleration. Going back to our car example, this makes some intuitive sense. We can feel accelerations, and we would be able to feel acceleration if we suddenly stepped on the gas and increased our speed, but we would also be able to feel the acceleration if we took a tight turn at a constant speed.
Going back to the derivative, we will use the product rule, taking the derivative of one piece at a time.
\[ \text{Acceleration:} \quad \, a(t) = \dot{v} \hat{u}_t + v \dot{\hat{u}}_t \]
\(\dot{v}\) is the rate of change of speed of the body, which is called the tangential acceleration. Going back to our car analogy, this is the acceleration we would experience from pressing the gas or brake pedals.
The other piece of our derivative is the speed times the derivative of a unit vector, which we will need to analyze further. When thinking about the derivative of a rotating unit vector, we think about rotating the coordinate system by a small amount \(d \theta\).
The derivative of the \(\hat{u}_t\) vector is then the change in position of the head of the vector. Using some geometry, we can see that the distance the head of the vector moves is the length of the vector (which is always 1 for a unit vector) times the angle of rotation in radians. The direction the head of the \(\hat{u}_t\) vector travels is roughly the \(\hat{u}_n\) direction. In fact, as \(d \theta\) approaches zero, it becomes exactly the \(\hat{u}_n\) direction. Putting this back into our derivative, we wind up with the following equation for acceleration.
\[ a(t) = \dot{v} \hat{u}_t + v \dot{\hat{u}}_t = \dot{v} \hat{u}_t + v \dot{\theta} \hat{u}_n \]
Before we arrive at our final set of equations, we have one last potential substitution. If a particle is moving along a curved path, the rate at which it is turning \((\dot{\theta})\) will be equal to the velocity of the particle divided by the radius of the path at that point (\(v\) divided by rho, \(\rho\)). Putting this last substitution in, we have our final set of equations with two equivalent options for calculating the accelerations.
\[ a(t) = \dot{v} \hat{u}_t + v \dot{\theta} \hat{u}_n = \dot{v} \hat{u}_t + \frac{v^2}{\rho} \hat{u}_n \]
When using these equations, it is important to remember that they are acceleration equations. If we want to know the overall acceleration we would need to add the two acceleration components as vectors. Also, if we are given an acceleration that is not in the normal or tangential direction, we will first need to break that acceleration vector down into normal and tangential components before using the above equations. Finally, if we want the velocity or acceleration in directions other than the normal and tangential directions, we will need to use a coordinate transformation.

## Example \(\)

A commercial jetliner is traveling at a constant 250 m/s when it executes an emergency 180-degree turn. If the turn takes 20 seconds, what is the acceleration experienced by the passengers? What is the radius of the curve taken by the plane?

## Example \(\)

Assuming a cloverleaf interchange has a radius of curvature of 80 meters at the tightest part of the turn, what is the fastest a car could travel around this curve without experiencing more than half a \(g\) in acceleration? Assume the car is traveling at a constant speed. If the car was instead increasing speed at a rate of 2 m/s2, what would be the new overall magnitude of the acceleration experienced by the passengers?

## 7.5: Two-Dimensional Motion with Polar Coordinates

- Example \(\)
- Example \(\)
Two-dimensional motion (also called planar motion) is any motion in which the objects being analyzed stay in a single plane. When analyzing such motion, we must first decide the type of coordinate system we wish to use. The most common options in engineering are rectangular coordinate systems, normal-tangential coordinate systems, and polar coordinate systems. Any planar motion can potentially be described with any of the three systems, though each choice has potential advantages and disadvantages.
The polar coordinate system uses a distance \((r)\) and an angle \((\theta)\) to locate a particle in space. The origin point will be a fixed point in space, but the \(r\)-axis of the coordinate system will rotate so that it is always pointed towards the body in the system. The variable \(r\) is also used to indicate the distance from the origin point to the particle. The theta-axis will then be 90 degrees counterclockwise from the \(r\)-axis with the variable \(\theta\) being used to show the angle between the \(r\)-axis and some fixed axis that does not rotate. The diagram below shows a particle with a polar coordinate system.
Polar coordinate systems work best in systems where a body is being tracked via a distance and an angle, such as a radar system tracking a plane. In cases such as this, the raw data from this in the form of an angle and a distance would be direct measures of \(\theta\) and \(r\) respectively. Polar coordinate systems will also serve as the base for extended body motion, where motors and actuators can directly control things like \(r\) and \(\theta\).
The way the coordinate system is defined, the \(r\)-axis will always point from the origin point to the body. The distance from the origin to the point is defined as \(r\) with no component of the position being in the \(\theta\) direction.
\[ \text{Position:} \quad \, r_{p/o}(t) = r \hat{u}_r + 0 \ \hat{u}_{\theta} \]
To find the velocity, we need to take the derivative of the position function over time. Since the distance \(r\) can change over time as well as the direction \(\hat{u}_r\) changing over time to track the body, we need to worry about the derivative of \(r\) as well as the derivative of the unit vector. Like we did with the normal-tangential systems, we will use the product rule and then substitute in a value for the derivative of the unit vector.
\[ \text{Velocity:} \quad \, v(t) = \dot{r} \hat{u}_r + r \dot{\hat{u}}_r = \dot{r} \hat{u}_r + r \dot{\theta} \hat{u}_{\theta} \]
To find the acceleration, we need to take the derivative of the velocity function. As all of these terms, including the unit vectors, change over time, we will need to use the product rule extensively. The \(\hat{u}_r\) term will split into two terms, and the \(\hat{u}_{\theta}\) term will split into three terms.
\[ \text{Acceleration:} \quad \, a(t) = \ddot{r} \hat{u}_r + \dot{r} \dot{\hat{u}_r} + \dot{r} \dot{\theta} \hat{u}_{\theta} + r \ddot{\theta} \hat{u}_{\theta} + r \dot{\theta} \dot{\hat{u}}_{\theta} \]
Again we will need to substitute in values for the derivatives of the unit vectors similar to before, but it is worth mentioning that the derivative of the \(\hat{u}_{\theta}\) vector as it rotates counterclockwise is in the negative \(\hat{u}_r\) direction.
After substituting in the derivatives of the unit vectors and simplifying the function, we arrive at our final equation for the acceleration.
 \text{Acceleration:} \quad \, a(t) &= \ddot{r} \hat{u}_r + \dot{r} \dot{\theta} \hat{u}_{\theta} + \dot{r} \dot{\theta} \hat{u}_{\theta} + r \ddot{\theta} \hat{u}_{\theta} - r \dot{\theta}^2 \hat{u}_r \\[5 pt] &= \left( \ddot{r} - r \dot{\theta}^2 \right) \hat{u}_r + \left( 2 \dot{r} \dot{\theta} + r \ddot{\theta} \right) \hat{u}_{\theta}
Though this final equation has a number of terms, it is still just two components in vector form. Just as with the normal-tangential coordinate system, we will need to remember that we will need to split the single vector equation into two separate scalar equations. In this case we will have the equation for the terms in the \(r\) direction and the equation for the terms in the \(\theta\) direction.

## Example \(\)

A radar tracking station gives the following raw data to a user at a given point in time. Based on this data, what is the current velocity and acceleration in the \(r\) and \(\theta\) directions? What is the current velocity and acceleration in the \(x\) and \(y\) directions?

## Example \(\)

A spotlight is tracking an actor as he moves across the stage. If the actor is moving with a constant velocity as shown below, what values do we need for the spotlight angular velocity \((\dot{\theta})\) and spotlight angular acceleration \((\ddot{\theta})\) so that the spotlight remains fixed on the actor?

## 7.6: Dependent Motion Systems

- Example \(\)
- Example \(\)
Dependent motion analysis is used when two or more particles have motions that are in some way connected to one another. The way in which the motion of these particles is connected is known as the constraint. A simple example of a constrained system is shown in the figure below. Imagine that someone's pickup truck gets stuck in the sand, and a friend uses a rope to help pull it out. This friend ties one end of the rope to the rear bumper of her car, loops the rope around a bar on the front of the pickup truck, then ties the other end to a stationary tree. In this case the two vehicles will not have the same velocity or acceleration, but their motions are related because they are tied together by the rope. In this case, the rope is acting as the constraint, allowing us to know the velocity or acceleration of one vehicle based on the velocity or acceleration of the other vehicle.
The first thing we will need to do when analyzing these systems is to come up with what is known as the constraint equation. A constraint equation will be some geometric relationship that will remain true over the course of the motion. In the above example, imagine the rope is 50 feet long. Using the tree as a stationary point, we can also say that the length of the rope is the distance from the green car to the tree, plus two times the distance from the pickup truck to the tree (since it must go out to the pickup truck and then back). If we put this into an equation (the constraint equation) we would have the following.
\[ \text{Constraint Equation: Positions} \quad \,\, \, L = 50 \, ft = 2 L_A + L_B \]
Once we have a constraint equation that works for positions, we can take the derivative of this equation to find another constraint equation that relates velocities. In this case, the length of the rope is constant, and therefore the derivative of the length will be zero. If we take the derivative of the constraint equation again, we wind up with a third constraint equation that relates accelerations.
 \text{Constraint Equation: Velocities} \quad &\,\, \dot{L} = 0 = 2 \dot{L}_A + \dot{L}_B \\[5pt] \text{Constraint Equation: Accelerations} \quad &\,\, \ddot{L} = 0 = 2 \ddot{L}_A + \ddot{L}_B
In these equations, it is important to remember that the values represent the changes in length, rather than direct measures of velocities. Though both vehicles would have positive velocities in the example above (velocities to the right), one \(\dot{L}\) value will be positive and one will be negative. This is because the truck is getting closer to the tree while the car is getting further away. A similar situation will occur for the accelerations, where both vehicles would have positive accelerations even if the \(\ddot{L}\) values are a mix of positive and negative values.

## Example \(\)

A truck becomes stuck in the sand at a local beach. To help, a friend takes a rope 50 feet in length, ties one end to her car, loops the rope around a bar at the front of the truck, and then ties the other end to a stationary tree as shown below. If the car accelerates at a rate of 0.2 ft/s², what will the velocity of the truck be by the time it gets to the tree?

## Example \(\)

A man has hooked up a pulley, a rope, and a platform as shown below to lift loads up onto a nearby rooftop. If \(x\) is currently 15 meters, \(y\) is currently 5 meters, and the man is walking away from the building at a rate of 0.5 meters per second, what is the current velocity of the platform?

## 7.7: Relative Motion Systems

- Relative Motion in One Dimension:
- Relative Motion in Two Dimension:Example \(\)Example \(\)Example \(\)
- Example \(\)
- Example \(\)
- Example \(\)
Relative motion analysis is the analysis of bodies where more than one body is in motion and we are in some way examining the motion of one moving particle relative to another moving particle. An example would be cars on a highway. If you are in one of many cars moving down one side of the highway, you and the other cars will all have velocities in a single direction. From your perspective inside the car, though, fast cars in front of you will appear to be moving away from you and slow cars in front of you will appear to be moving towards you. By knowing your speed, and by observing how fast the cars are moving away from you or towards you, you could determine or at least estimate how fast these cars are going. The process of using your speed in conjunction with the relative velocities of the other cars to find the other cars' speed is relative motion analysis.

## Relative Motion in One Dimension:

In a single dimension, we will usually have at least two moving particles as well as some fixed reference point. We usually call the fixed reference point \(O\), and then label the other points \(A\), \(B\), and so on. In the diagram, below we can see an example of this, with a fixed reference point at \(O\), a police car at \(A\), and a speeding car at \(B\).
As we can see from the diagram above, the sum of the distance from \(O\) to \(A\) \((r_{A/O})\) and the distance from \(A\) to \(B\) \((r_{B/A})\) will be equal to the distance from \(O\) to \(B\) \((r_{B/O})\). This gives us our position equation below.
\[ \text{Position:} \quad \, r_{B/O} = r_{A/O} + r_{B/A} \]
One thing we should notice about the subscripts is that if we keep to our standard naming convention (point being observed / point we are observing from) then we should be able to see which points cancel out and which remain. In this case, the \(A\)'s on the top and bottom on the right cancel out, leaving just a \(B\) on the top and an \(O\) on the bottom. This matches the subscript on the left of the equation.
Furthermore, we can take the derivative of this equation to relate velocities, or a double derivative to relate accelerations. This means that if we know any two of the terms in the equations below, we can solve for the third.
 \text{Velocity:} \quad &\, v_{B/O} = v_{A/O} + v_{B/A} \\[5pt] \text{Acceleration:} \quad &\, a_{B/O} = a_{A/O} + a_{B/A}

## Relative Motion in Two Dimension:

Just as with one dimension, we can start by examining a set of relative positions. In this case we will use the example of two planes moving through the sky. We may wish to deduce the position of plane B on a map, based on our observations from plane A. By using the information we have on our position relative to some set location, along with the relative position read in from on board instrumentation, we should be able to determine the absolute position (including an \(x\) and \(y\) coordinate) for plane B.
In two dimensions, we will use the same equations as before, except this time we will be using vectors rather than scalar values in our equations.
 \text{Position:} \quad &\, \vec{r}_{B/O} = \vec{r}_{A/O} + \vec{r}_{B/A} \\[5pt] \text{Velocity:} \quad &\, \vec{v}_{B/O} = \vec{v}_{A/O} + \vec{v}_{B/A} \\[5pt] \text{Acceleration:} \quad &\, \vec{a}_{B/O} = \vec{a}_{A/O} + \vec{a}_{B/A}
To solve these equations, we will almost always break the vector equations down into a set of component equations. This will let us solve these equations with simple algebra. Because we have more than one particle, we usually use rectangular coordinate systems for this with a universal set of \(x\) and \(y\) coordinates.
A police officer notices a car speeding by. If the police car is traveling 30 m/s and the radar gun measures the relative velocity to be 15 m/s, how fast is the speeding car actually going? If the police car immediately begins accelerating at a constant rate and catches up to the speeding car after 15 seconds, what is the rate of acceleration of the police car?
A plane has an airspeed of 250 kilometers per hour (airspeed is the velocity of the plane relative to the air) and is flying though an easterly crosswind with a speed of 20 kilometers per hour. If the plane wants to maintain a direct northerly course, what is the angle the plane must point into the wind \((\theta)\)?
You are in a boat that is traveling through the water in an area of swift currents. One instrument measures your speed with respect to the water to be 20 ft/s with your boat pointed at a 45-degree angle. GPS, however, measures your absolute speed and direction to be 25 ft/s at a 55-degree angle. Based on this information, what is the speed and direction of the water current in this area?

## 7.8: Chapter 7 Homework Problems

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

A car with an initial velocity of 30 m/s accelerates at a constant rate of 12 m/s² . Find the time required for the car to reach a speed of 60 m/s, and the distance traveled during this time.
Time = \(2.5 \, s\)
Distance = \(112.5 \, m\)

## Exercise \(\)

A car traveling at 60 miles per hour approaches a fallen log in the road 400 feet away. Assuming the driver immediately slams on the brakes, what is the required rate of deceleration needed to assure the driver does not hit the log?
Minimum acceleration: \(-9.68 \, ft/s^2\)

## Exercise \(\)

A train experiences the acceleration over time detailed below. Draw the velocity-time and position-time diagrams with all key points and equations labeled, and determine the total distance traveled by the train.
Total distance = \(4950 \, m\), plus v-t and s-t diagrams

## Exercise \(\)

As a roller coaster cart comes into the gate at the end of the ride, it goes through two sets of brakes. The cart's velocity over time is shown in the graph below. Draw the acceleration-time and position-time diagrams with all key points and equations labeled. Determine the total distance the cart travels during this seven-second period.
Total distance = \(25.5 \, ft\), plus a-t and s-t diagrams.

## Exercise \(\)

A tank fires a round at a 30-degree angle with a muzzle velocity of 600 m/s. The round is expected to hit a mountainside one kilometer away. The mountainside also has an average angle of 30 degrees. How far up the mountainside will the round be expected to travel before hitting the ground \((d)\) if we ignore air resistance?
\(d = 5.37 \, km\)

## Exercise \(\)

A plane with a current speed of 600 ft/s is increasing in speed while also making a turn. The acceleration is measured at 40 ft/s² at an angle 35° from its current heading. Based on this information, determine the rate at which the plane is increasing its speed (tangential acceleration) and the radius of the turn for the plane.
\(a_t = 32.77 \, ft/s^2\)
\(r = 15,690 \, ft\)

## Exercise \(\)

A radar station is tracking a rocket with a speed of 400 m/s and an acceleration of 3 m/s² in the direction shown below. The rocket is 3.6 km away (\(r\) = 3600 m) at an angle of 25°. What would you expect \(\dot{r}\), \(\ddot{r}\), \(\dot{\theta}\), and \(\ddot{\theta}\) to be?
\(\dot{r} = 282.8 \,\, m/s, \, \ddot{r} = 24.34 \,\, m/s^2\)
\(\dot{\theta} = 0.0786 \,\, rad/s, \, \ddot{\theta} \,\, -0.01176 \, rad/s^2\)

## Exercise \(\)

The pulley system below is being used to lift a heavy load. Assuming the end of the cable is being pulled at a velocity of 2 ft/s, what is the expected upwards velocity of the load?
\(v_L = 0.5 \, ft/s\)

## Exercise \(\)

A cable is anchored at A, goes around a pulley on a movable collar at B, and finally goes around a pulley at C as shown below. If the end of the rope is pulled with a velocity of 0.5 m/s, what is the expected velocity of the collar at this instant?
\(v_B = 0.3 \, m/s\)

## Exercise \(\)

You are driving at a velocity of 90 ft/s in the rain while you notice that the rain is hitting your car at an angle 35° from the vertical, from your perspective. Assuming the rain is actually coming straight down (when observed by a stationary person), what is the velocity of the rain with respect to the ground?
\(v_r = 128.5 \, ft/s\)
- 8: Newton's Second Law for Particles

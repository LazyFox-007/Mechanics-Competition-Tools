来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 01 1: Basics of Newtonian Mechanics

## 1: Basics of Newtonian Mechanics

- About the Book      1.0: Video Introduction to Chapter 1
- About the Book

## 1.0: Video Introduction to Chapter 1

- 1: Basics of Newtonian Mechanics      1.1: Bodies
- 1: Basics of Newtonian Mechanics

## 1.1: Bodies

- Bodies in Engineering MechanicsRigid versus Deformable BodiesParticles versus Extended Bodies
- Rigid versus Deformable Bodies
- Particles versus Extended Bodies

## Bodies in Engineering Mechanics

A body, for the purposes of engineering mechanics, is a collection of matter that is analyzed as a single object. This can be something simple like a rubber ball, or it can be something made of many parts such as a car. What can count as a body and what cannot count as a body is dependent on the circumstances of the analysis. In some circumstances in engineering mechanics, it is useful to make certain assumptions about the bodies being analyzed. We will usually need to assume the body is either rigid or deformable, and we will also need to assume that the body is either a particle or an extended body.

### Rigid versus Deformable Bodies

Rigid bodies do not deform (stretch, compress, or bend) when subjected to loads, while deformable bodies do deform. In actuality, no physical body is completely rigid, but most bodies deform so little that this deformation has a minimal impact on the analysis. For this reason, we usually assume in the statics and dynamics courses that the bodies discussed are rigid. In the strength of materials course we specifically remove this assumption and examine how bodies deform and eventually fail under loading.
There is no set boundary for determining if a body can be approximated as rigid, but there are two factors to look for that indicate that a rigid body assumption is not appropriate. First, if the body is being significantly stretched, compressed, or bent during the period of analysis, then the body should not be analyzed as a rigid body. Second, if the body has parts that are free to move relative to one another, then the body as a whole should not be analyzed as a rigid body; this is instead a machine, comprised of multiple connected bodies that will each need to be analyzed separately.

### Particles versus Extended Bodies

Particles are bodies where all the mass is concentrated at a single point in space. Particle analysis will only have to take into account translational motion and the forces acting on the body, because rotation is not considered for particles. Extended bodies, on the other hand, have mass that is distributed throughout a finite volume. Often in engineering statics, we will take a shortcut and say rigid bodies to describe extended bodies that also happen to be rigid. This is because particles, as a single point, cannot deform. Extended body analysis is more complex and also has to take into account moments and rotational motions. In actuality, no bodies are truly particles, but some bodies can be approximated as particles to simplify analysis. Bodies are often assumed to be particles if the rotational motions are negligible when compared to the translational motions, or in systems where there is no moment exerted on the body, such as a concurrent force system.

## 1.2: Forces

- Magnitude:
- Direction:
- Point of Application:
A force is any influence that causes a body to accelerate. Forces on a body can also cause stress in that body, which can result in the body deforming or breaking. Though forces can come from a variety of sources, there are three distinguishing features to every force. These features are the magnitude of the force, the direction of the force, and the point of application of the force. Forces are often represented as vectors (as in the diagram to the right) and each of these features can be determined from a vector representation of the forces on the body.

## Magnitude:

The magnitude of a force is the degree to which the force will accelerate the body it is acting on; it is represented by a scalar (a single number). The magnitude can also be thought of as the strength of the force. When forces are represented as vectors, the magnitude of the force is usually explicitly labeled. The length of the vector also often corresponds to the relative magnitude of the vector, with longer vectors indicating larger magnitudes.
The magnitude of force is measured in units of mass times length over time squared. In metric units the most common unit is the Newton (N), where one Newton is one kilogram times one meter over one second squared. This means that a force of one Newton would cause a one-kilogram object to accelerate at a rate of one meter per second squared. In English units, the most common unit is the pound (lb), where one pound is equal to one slug times a foot over a second squared. This means that a one-pound force would cause an object with a mass of one slug to accelerate at a rate of one foot per second squared.
\[ Force \, = \, \frac{(mass)(distance)}{(time)^2} \]
\[ 1 \, \text{Newton} \, (N) \, = \, \frac{(kg)(m)}{s^2} \]
\[ 1 \, \text{pound} \, (lb) \, = \, \frac{(slug)(ft)}{s^2} \]

## Direction:

In addition to having magnitudes, forces also have directions. As we said before, a force is any influence that causes a body to accelerate. Since acceleration has a specific direction, force also has a specific direction that matches this acceleration. The direction of the force is indicated in diagrams by the direction of the vector representing the force.
Direction has no units, but it is usually given by reporting angles between the vector representing the force and coordinate axes, or by reporting the X, Y, and Z components of the vector. Often times vectors that have the same direction as one of the coordinate axes will not have any angles or components listed. If this is true, it is usually safe to assume that the direction does match the direction of one of the coordinate axes.

## Point of Application:

The point, or points, at which a force is applied to a body is important for understanding how the body will react. For particles, there is only a single point for the forces to act on, but for rigid bodies there are an infinite number of possible points of application. Some points of application will lead to the body undergoing simple linear acceleration; some will exert a moment on the body which will cause the body to undergo rotational acceleration as well as linear acceleration.
Depending on the nature of the point of application of a force, there are three general types of forces. These are point forces, surface forces, and body forces. Below is a diagram of a box being pulled by a rope across a frictionless surface. The box has three forces acting on it. The first is the force from the rope. This is a force applied to a single point on the box, and is therefore modeled as point force. Point forces are represented by a single vector. Second is the normal force from the ground that is supporting the box. Because this force is applied evenly to the bottom surface of the box, it is best modeled as a surface force. Surface forces are indicated by a number of vectors drawn side by side with a profile line to indicate the magnitude of the force at any point. The last force is the gravitational force pulling the box downward. Because this force is applied evenly to the entire volume of the box, it is best modeled as a body force. Body forces are sometimes shown as a field of vectors as shown, though they are often not drawn out at all because they end up cluttering the free body diagram.
We will also sometimes talk about distributed forces. A distributed force is simply another name for either a surface or a body force.
The exact point or surface that the force is acting on can be drawn as either the head or the tail of the force vector in the free body diagram. Because of the principle of transmissibility, both options are known to represent the same physical system.

## 1.3: Moments

- The Vector Representation of a Moment:Magnitude:Direction:Axis of Rotation:
- Magnitude:
- Direction:
- Axis of Rotation:
- Calculating Moments:
A moment (also sometimes called a torque) is defined as the "tendency of a force to rotate a body". Where forces cause linear accelerations, moments cause angular accelerations. In this way moments, can be thought of as twisting forces.

## The Vector Representation of a Moment:

Moments, like forces, can be represented as vectors and have a magnitude, a direction, and a "point of application". For moments however a better name for the point of application is the axis of rotation. This will be the point or axis about which we will determine all the moments.

### Magnitude:

The magnitude of a moment is the degree to which the moment will cause angular acceleration in the body it is acting on. It is represented by a scalar (a single number). The magnitude of the moment can be thought of as the strength of the twisting force exerted on the body. When a moment is represented as a vector, the magnitude of the moment is usually explicitly labeled. though the length of the moment vector also often corresponds to the relative magnitude of the moment.
The magnitude of the moment is measured in units of force times distance. The standard metric units for the magnitude of moments are Newton-meters, and the standard English units for a moment are foot-pounds.
\[ M = F * d \]
\[ \text{Metric:} \,\, N * m \]
\[ \text{English:} \,\, lb * ft \]

### Direction:

In a two-dimensional problem, the direction can be thought of as a scalar quantity corresponding to the direction of rotation the moment would cause. A moment that would cause a counterclockwise rotation is a positive moment, and a moment that would cause a clockwise rotation is a negative moment.
In a three-dimensional problem, however, a body can rotate about an axis in any direction. If this is the case, we need a vector to represent the direction of the moment. The direction of the moment vector will line up with the axis of rotation that moment would cause, but to determine which of the two directions we can use along that axis we have available we use the right hand rule. To use the right hand rule, align your right hand as shown in Figure \(\) so that your thumb lines up with the axis of rotation for the moment and your curled fingers point in the direction of rotation for your moment. If you do this, your thumb will be pointing in the direction of the moment vector.
If we look back to two-dimensional problems, all rotations occur about an axis pointing directly into or out of the page (the \(z\)-axis). Using the right hand rule, counterclockwise rotations are represented by a vector in the positive \(z\) direction and clockwise rotations are represented by a vector in the negative \(z\) direction.

### Axis of Rotation:

In engineering statics problems we can choose any point/axis as the axis of rotation. However, the choice of this point will affect the magnitude and direction of the resulting moment, and the moment is only valid about that point.
Though we can take the moment about any point in a statics problem, if we are adding together the moments from multiple forces, all the moments must be taken about a common axis of rotation. Moments taken about different points cannot be added together to find a "net moment."
Additionally, if we move into the subject of dynamics, where bodies are moving, we will want to relate moments to angular accelerations. For this to work, either we will need to take the moments about a single point that does not move (such as the hinge on a door) or we will need to take the moments about the center of mass of the body. Summing moments about other axes of rotation will not result in valid calculations.

## Calculating Moments:

To calculate the moment that a force exerts on a body, we will have two main options: scalar methods and vector methods. Scalar methods are generally faster for two-dimensional problems where a body can only rotate clockwise or counterclockwise, while vector methods are generally faster for three-dimensional problems where the axis of rotation is more complex.

## 1.4: Free Body Diagrams

- Constructing the Free Body Diagram:
- Worked Problems:
A free body diagram is a tool used to solve engineering mechanics problems. As the name suggests, the purpose of the diagram is to "free" the body from all other objects and surfaces around it so that it can be studied in isolation. We will also draw in any forces or moments acting on the body, including those forces and moments exerted by the surrounding bodies and surfaces that we removed.
The diagram below shows a ladder supporting a person and the free body diagram of that ladder. As you can see, the ladder is separated from all other objects and all forces acting on the ladder are drawn in with the key dimensions and angles shown.

## Constructing the Free Body Diagram:

The first step in solving most mechanics problems will be to construct a free body diagram. This simplified diagram will allow us to more easily write out the equilibrium equations for statics or strengths of materials problems, or the equations of motion for dynamics problems.
To construct the diagram we will use the following process:
- First draw the body being analyzed, separated from all other surrounding bodies and surfaces. Pay close attention to the boundary, identifying what is part of the body, and what is part of the surroundings.
- Second, draw in all external forces and moments acting directly on the body. Do not include any forces or moments that do not directly act on the body being analyzed. Do not include any forces that are internal to the body being analyzed.
- Once the forces are identified and added to the free body diagram, the last step is to label any key dimensions and angles on the diagram.
Some common types of forces seen in mechanics problems are:
- Gravitational Forces: Unless otherwise noted, the mass of an object will result in a gravitational weight force applied to that body. This weight is usually given in pounds in the English system, and is modeled as 9.81 (\(g\)) times the mass of the body in kilograms for the metric system (resulting in a weight in Newtons). This force will always point down towards the center of the earth and act on the center of mass of the body.
- Normal Forces (or Reaction Forces): Every object in direct contact with the body will exert a normal force on that body which prevents the two objects from occupying the same space at the same time. Note that only objects in direct contact can exert normal forces on the body.     An object in contact with another object or surface will experience a normal force that is perpendicular (normal) to the surfaces in contact.  Joints or connections between bodies can also cause reaction forces or moments, and we will have one force or moment for each type of motion or rotation the connection prevents.
- An object in contact with another object or surface will experience a normal force that is perpendicular (normal) to the surfaces in contact.
- Joints or connections between bodies can also cause reaction forces or moments, and we will have one force or moment for each type of motion or rotation the connection prevents.
- Friction Forces: Objects in direct contact with the body can also exert friction forces, which will resist the two bodies sliding against one another, on the body. These forces will always be perpendicular to the surfaces in contact. Friction is the subject of an entire chapter in this book, but for simple scenarios we usually assume rough or smooth surfaces.     For smooth surfaces we assume that there is no friction force.  For rough surfaces we assume that the bodies will not slide relative to one another, no matter what. In this case, the friction force is always just large enough to prevent this sliding.
- For smooth surfaces we assume that there is no friction force.
- For rough surfaces we assume that the bodies will not slide relative to one another, no matter what. In this case, the friction force is always just large enough to prevent this sliding.
- Tension in Cables: Cables, wires or ropes attached to the body will exert a tension force on the body in the direction of the cable. These forces will always pull on the body, as ropes, cables and other flexible tethers cannot be used for pushing.
The above forces are the most common, but other forces such as pressure from fluids, spring forces and magnetic forces exist and may act on the body.
Once the forces are identified and added to the free body diagram, the last step is to label any key dimensions and angles on the diagram.

## Worked Problems:

Example \(\)
The drawing below shows two boxes sitting on a table. Draw a free body diagram of box A and box B.
Example \(\)
Two equally sized barrels are being transported in a handtruck as shown below. Draw a free body diagram of each of the two barrels.
Example \(\)
The car shown below is moving and then slams on the brakes locking up all four wheels. The distance between the two wheels is 8 feet and the center of mass is 3 feet behind and 2.5 feet above the point of contact between the front wheel and the ground. Draw a free body diagram of the car as it comes to a stop.
Example \(\)
A 600-pound load is supported by a 5 meter long, 100-pound cantilever beam. Assume the beam is firmly anchored to the wall. Draw a free body diagram of the beam.
Example \(\)
The main arm of a crane has a mass of 400 kg (assume the center of mass is at the midpoint of the arm), and supports a 200 kg load and a 600 kg counterweight. The arm is connected to the vertical support via a pin joint and two flexible cables. Draw a free body diagram of the arm.

## 1.5: Newton's First Law

- Net Forces:
- Rotational Motion:
Newton's first law states that: "A body at rest will remain at rest unless acted on by an unbalanced force. A body in motion continues in motion with the same speed and in the same direction unless acted upon by an unbalanced force."
This law, also sometimes called the "law of inertia", means that bodies maintain their current velocity unless a force is applied to change that velocity. If an object is at rest with zero velocity it will remain at rest until some force begins to change that velocity, and if an object is moving at a set speed and in a set direction it will remain at that same velocity until some force acts on it to change its velocity.

## Net Forces:

It is important to note that the net force is what will cause a change in velocity. The net force is the sum of all forces acting on the body. For example, we can imagine gently pushing on the rock in the figure above and observing that the rock does not move. This is because we will have a friction force equal in magnitude and opposite in direction opposing our gentle pushing force. The sum of these two forces will be equal to zero, therefore the net force is zero and the change in velocity is zero.

## Rotational Motion:

Newton's first law also applies to moments and rotational velocities. A body will maintain it's current rotational velocity until a net moment is exerted to change that rotational velocity. This can be seen in things like toy tops, flywheels, stationary bikes, and other objects that will continue spinning once started until brakes or friction stop them.

## 1.6: Newton's Second Law

- Translational Motion:
- Rotational Motion:

## Translational Motion:

Newton's second law states that: "When a net force acts on any body with mass, it produces an acceleration of that body. The net force will be equal to the mass of the body times the acceleration of the body."
\[ \vec{F} \, = \, m \vec{a}\]
You will notice that the force and the acceleration in the equation above have an arrow above them. This means that they are vector quantities, having both a magnitude and a direction. Mass, on the other hand, is a scalar quantity having only a magnitude. Based on the above equation, you can infer that the magnitude of the net force acting on the body will be equal to the mass of the body times the magnitude of the acceleration, and that the direction of the net force on the body will be equal to the direction of the acceleration of the body.

## Rotational Motion:

Newton's second law also applies to moments and rotational velocities. The revised version of the second law equation states that the net moment acting on the object will be equal to the mass moment of inertia of the body about the axis of rotation (\(I\)) times the angular acceleration of the body.
\[ \vec{M} \, = \, I * \vec{\alpha}\]
You should again notice that the moment and the angular acceleration of the body have arrows above them, indicating that they are vector quantities with both a magnitude and direction. The mass moment of inertia, on the other hand, is a scalar quantity having only a magnitude. The magnitude of the net moment will be equal to the mass moment of inertia times the magnitude of the angular acceleration, and the direction of the net moment will be equal to the direction of the angular acceleration.

## 1.7: Newton's Third Law

Newton's Third Law states "For any action, there is an equal and opposite reaction." By "action" Newton meant a force, so for every force one body exerts on another body, that second body exerts a force of equal magnitude but opposite direction back on the first body. Since all forces are exerted by bodies (either directly or indirectly), all forces come in pairs, one acting on each of the bodies interacting.
Though there may be two equal and opposite forces acting on a single body, it is important to remember that for each of the forces a Third Law pair acts on a separate body. This can sometimes be confusing when there are multiple Third Law pairs at work. Below are some examples of situations where multiple Third Law pairs occur.

## 1.8: Chapter 1 Homework Problems

Exercise \(\)
A pulley system is being used to hoist a 50 kg engine block as shown below. If distance \(d\) is currently 1 meter and we assume the pulleys are all frictionless, draw a free body diagram of the engine block with the attached pulley. Include all forces and important angles.
Exercise \(\)
The car shown below has a weight of 4500 lbs and a center of mass at point G. Assuming the car is not moving and is sitting on a level surface, draw a free body diagram of the car. Include all forces and important distances.
Exercise \(\)
A telephone pole sits on a rough surface. A cable attached to an excavator is then used to pull the pole along the surface as shown below. Assume the telephone pole has a mass of 350 kg and a length of 12 meters. Draw a free body diagram of the telephone pole. Include all forces, important distances, and important angles.
- 2: Static Equilibrium in Concurrent Force Systems

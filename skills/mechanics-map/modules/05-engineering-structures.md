来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 05 5: Engineering Structures

## 5: Engineering Structures

## 5.0: Video Introduction to Chapter 5

- 5: Engineering Structures      5.1: Structures
- 5: Engineering Structures

## 5.1: Structures

- Internal and External Forces:
- Types of Structures:Trusses:Frames and Machines:
- Trusses:
- Frames and Machines:
An engineering structure is term used to describe any set of interconnected bodies. The different bodies in the structure can move relative to one another (such as the blades in a pair of scissors) or they can be be fixed relative to one another (such as the different beams connected to form a bridge).
When analyzing engineering structures, we will sometimes analyze the structure as a whole, and we will sometimes break the structure down into individual bodies that are analyzed separately. The exact methods used depend upon what unknown forces we are looking for and what type of structure we are analyzing.

## Internal and External Forces:

When examining a single body, we would find the forces that this body exerted on surrounding bodies, and the forces that these surrounding bodies would exert on the body we are analyzing. These forces are all considered external forces because they are forces between the body and the external environment.
In an engineering structure, we still have external forces where the structure is interacting with bodies external to the structure, but we also can think about the forces that different parts of the structure exert on one another (the force between the pin and the blade in Figure \(\), for example). Since both of these bodies are part of the structure we are analyzing, these forces are considered internal forces.
If we only wish to determine the external forces acting on a structure, then we can treat the whole structure as a single body (assuming the structure is rigid as a whole). If we wish to determine the internal forces acting between components in the structure, then we will need to disassemble the structure into separate bodies in our analysis.

## Types of Structures:

Another important consideration when analyzing structures is the type of structure that is being analyzed. All structures fall into one of three categories: trusses, frames, or machines. Frames and machines are analyzed in the same way so distinction between them is less important, but the analysis methods used for trusses vary greatly from the analysis methods used for frames and machines, so determining if a structure is a truss or not is an important first step in structure analysis.

### Trusses:

A truss is a structure that consists entirely of two-force members. If any one body in the structure is not a two-force member, then the structure is either a frame or a machine. Also,in order to be a statically determinate truss (a truss where we can actually solve for all the unknowns), the truss must be independently rigid as a whole. If different parts of the truss could move relative to one another then the truss separated is not independently rigid.
A two-force member is a body where forces are applied at only two locations. If forces are applied at more than two locations, or if any moments are applied, then the body is not a two-force member (see the two-force member page for more details). Because of the unique assumptions we can make with two-force members, we can apply two unique methods to the analysis of trusses (the method of joints and the method of sections) that we cannot apply to frames and machines (where we cannot assume we have two-force members).

### Frames and Machines:

A frame or a machine is structure where at least one component of the structure is not a two-force member. This component will be a body in the structure that has forces acting at three or more points on it. The difference between a frame and a machine is that a frame is rigid as a whole, while a machine is not rigid as a whole.
Because frames and machines do not consist entirely of two-force members, we cannot make the assumptions that allow us to use the method of joints and the method of sections. For this reason, we need to use a different analysis method (simply called the analysis of frames and machines here).

## 5.2: Two-Force Members

- Why the Forces Must Be Equal, Opposite and Collinear:
- Why Two-Force Members Are Important:
A two-force member is a body that has forces (and only forces, no moments) acting on it in only two locations. In order to have a two-force member in static equilibrium, the net force at each location must be equal, opposite, and collinear. This will result in all two-force members being in either tension or compression, as shown in the diagram below.

## Why the Forces Must Be Equal, Opposite and Collinear:

Imagine a beam where forces are only exerted at each end of the beam (a two-force member). The body has some non-zero force acting at one end of the beam, which we can draw as a force vector. If this body is in equilibrium, then we know two things:
- the sum of the forces must be equal to zero, and
- the sum of the moments must be equal to zero.
In order to have the sum of the forces equal to zero, the force vector on the other side of the beam must be equal in magnitude and opposite in direction. This is the only way to ensure that the sum of the forces is equal to zero with only two forces.
In order to have the sum of the moments equal to zero, the forces must be collinear. If the forces were not collinear, then the two equal and opposite forces would form a couple. This couple would exert a moment on the beam when there are no other moments to counteract the couple. Because the moment exerted by the two forces must be equal to zero, the perpendicular distance between the forces \((d)\) must be equal to zero. The only way to achieve this is to have the forces be collinear.

## Why Two-Force Members Are Important:

By identifying two-force members, we greatly reduce the number of unknowns in our problem. In two-force members, we know that the forces must act along the line between the two connection points on the body. This means that the direction of the force vectors is known on either side of the body. Additionally, we know the forces are equal and opposite, so if we determine the magnitude and direction of the force acting on one side of the body, we automatically know the magnitude and direction of the force acting on the other side of the body.
Two-force members are also important in distinguishing between trusses, and frames and machines. When we analyze trusses using either the method of joints or the method of sections, we will assume everything is a two-force member. If this assumption is incorrect, this will cause serious problems in the analysis. By making this assumption, though, we can use some shortcuts that will make truss analysis easier and faster than the analysis of frames and machines.

## 5.3: Trusses

- Analyzing Trusses:
A truss is an engineering structure that is made entirely of two-force members. In addition, statically determinate trusses (trusses that can be analyzed completely using the equilibrium equations) must be independently rigid. This means that if the truss was separated from its connection points, no one part would be able to move independently with respect to the rest of the truss.
Trusses can be broken down further into plane trusses and space trusses. A plane truss is a truss where all members lie in a single plane. This means that plane trusses can essentially be treated as two-dimensional systems. Space trusses, on the other hand, have members that are not limited to a single plane. This means that space trusses need to be analyzed as a three-dimensional system.

## Analyzing Trusses:

When we talk about analyzing a truss, we are usually looking to identify not only the external forces acting on the truss structure, but also the forces acting on each member internally in the truss. Because each member of the truss is a two force member, we simply need to identify the magnitude of the force on each member, and determine if each member is in tension or compression.
To determine these unknowns, we have two methods available: the method of joints, and the method of sections. Both will give the same results, but each through a different process.
The method of joints focuses on the joints, or the connection points where the members come together. We assume we have a pin at each of these points that we model as a particle, we draw out the free body diagram for each pin, and then we write out the equilibrium equations for each pin. This will result in a large number of equilibrium equations that we can use to solve for a large number of unknown forces.
The method of sections involves pretending to split the truss into two or more different sections and then analyzing each section as a separate rigid body in equilibrium. In this method we determine the appropriate sections, draw free body diagrams for each section, and then write out the equilibrium equations for each section.
The method of joints is usually the easiest and fastest method for solving for all the unknown forces in a truss. The method of sections, on the other hand, is better suited to targeting and solving for the forces in just a few members without having to solve for all the unknowns. In addition, these methods can be combined if needed to best suit the goals of the problem solver.

## 5.4: Method of Joints

- Using the Method of Joints:
The method of joints is a process used to solve for the unknown forces acting on members of a truss. The method centers on the joints or connection points between the members, and it is usually the fastest and easiest way to solve for all the unknown forces in a truss structure.

## Using the Method of Joints:

The process used in the method of joints is outlined below.
In the beginning, it is usually useful to label the members and the joints in your truss. This will help you keep everything organized and consistent in later analysis. In this book, the members will be labeled with letters and the joints will be labeled with numbers.
Treating the entire truss structure as a rigid body, draw a free body diagram, write out the equilibrium equations, and solve for the external reacting forces acting on the truss structure. This analysis should not differ from the analysis of a single rigid body.
Assume there is a pin or some other small amount of material at each of the connection points between the members. Next you will draw a free body diagram for each connection point. Remember to include:
- Any external reaction or load forces that may be acting at that joint.
- A normal force for each two force member connected to that joint. Remember that for a two force member, the force will be acting along the line between the two connection points on the member. We will also need to guess if it will be a tensile or a compressive force. An incorrect guess now though will simply lead to a negative solution later on. A common strategy then is to assume all forces are tensile, then later in the solution any positive forces will be tensile forces and any negative forces will be compressive forces.
- Label each force in the diagram. Include any known magnitudes and directions and provide variable names for each unknown.
- Write out the equilibrium equations for each of the joints. You should treat the joints as particles, so there will be force equations but no moment equations. With either two (for 2D problems) or three (for 3D problems) equations for each joint; this should give you a large number of equations.     In planar trusses, the sum of the forces in the \(x\) direction will be zero and the sum of the forces in the \(y\) direction will be zero for each of the joints. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \]  In space trusses, the sum of the forces in the \(x\) direction will be zero, the sum of the forces in the \(y\) direction will be zero, and the sum of forces in the \(z\) direction will be zero for each of the joints. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \]
- In planar trusses, the sum of the forces in the \(x\) direction will be zero and the sum of the forces in the \(y\) direction will be zero for each of the joints. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \]
- In space trusses, the sum of the forces in the \(x\) direction will be zero, the sum of the forces in the \(y\) direction will be zero, and the sum of forces in the \(z\) direction will be zero for each of the joints. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \]
- Finally, solve the equilibrium equations for the unknowns. You can do this algebraically, solving for one variable at a time, or you can use matrix equations to solve for everything at once. If you assumed that all forces were tensile earlier, remember that negative answers indicate compressive forces in the members.
Example \(\)
Find the force acting in each of the members in the truss bridge shown below. Remember to specify if each member is in tension or compression.
Example \(\)
Find the force acting in each of the members of the truss shown below. Remember to specify if each member is in tension or compression.
Example \(\)
Find the force acting in each of the members of the truss shown below. Remember to specify if each member is in tension or compression.

## 5.5: Method of Sections

- Using the Method of Sections:
The method of sections is a process used to solve for the unknown forces acting on members of a truss. The method involves breaking the truss down into individual sections and analyzing each section as a separate rigid body. The method of sections is usually the fastest and easiest way to determine the unknown forces acting in a specific member of the truss.

## Using the Method of Sections:

The process used in the method of sections is outlined below.
- In the beginning, it is usually useful to label the members in your truss. This will help you keep everything organized and consistent in later analysis. In this book, the members will be labeled with letters.       Figure \(\): The first step in the method of sections is to label each member.
Figure \(\): The first step in the method of sections is to label each member.
- Treating the entire truss structure as a rigid body, draw a free body diagram, write out the equilibrium equations, and solve for the external reacting forces acting on the truss structure. This analysis should not differ from the analysis of a single rigid body.       Figure \(\): Treat the entire truss as a rigid body and solve for the reaction forces supporting the truss structure.
Figure \(\): Treat the entire truss as a rigid body and solve for the reaction forces supporting the truss structure.
- Next, you will imagine cutting your truss into two separate sections. The cut should travel through the member that you are trying to solve for the forces in, and should cut through as few members as possible. The cut does not need to be a straight line.    Figure \(\): Next you will imagine cutting the truss into two parts. If you want to find the forces in a specific member, be sure to cut through that member. It also makes things easier if you cut through as few members as possible.
- Next, you will draw a free body diagram for either one or both sections that you created. Be sure to include all the forces acting on each section.     Any external reaction or load forces that may be acting at the section.  An internal force in each member that was cut when splitting the truss into sections. Remember that for a two-force member, the force will be acting along the line between the two connection points on the member. We will also need to guess if it will be a tensile or a compressive force. An incorrect guess now, though, will simply lead to a negative solution later on. A common strategy then is to assume all forces are tensile; then later in the solution any positive forces will be tensile forces and any negative forces will be compressive forces.  Label each force in the diagram. Include any known magnitudes and directions and provide variable names for each unknown.       Figure \(\): Next, draw a free body diagram of one or both halves of the truss. Add the known forces, as well as unknown tensile forces for each member that you cut.
- Any external reaction or load forces that may be acting at the section.
- An internal force in each member that was cut when splitting the truss into sections. Remember that for a two-force member, the force will be acting along the line between the two connection points on the member. We will also need to guess if it will be a tensile or a compressive force. An incorrect guess now, though, will simply lead to a negative solution later on. A common strategy then is to assume all forces are tensile; then later in the solution any positive forces will be tensile forces and any negative forces will be compressive forces.
- Label each force in the diagram. Include any known magnitudes and directions and provide variable names for each unknown.       Figure \(\): Next, draw a free body diagram of one or both halves of the truss. Add the known forces, as well as unknown tensile forces for each member that you cut.
Figure \(\): Next, draw a free body diagram of one or both halves of the truss. Add the known forces, as well as unknown tensile forces for each member that you cut.
- Write out the equilibrium equations for each section you drew a free body diagram of. These will be extended bodies, so you will need to write out the force and the moment equations.    For 2D problems you will have three possible equations for each section: two force equations and one moment equation. \[ \sum \vec{F} = 0 \quad\quad\quad\quad \sum \vec{M} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum M_z = 0 \]  For 3D problems you will have six possible equations for each section: three force equations and three moment equations. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \] \[ \sum \vec{M} = 0 \] \[ \sum M_x = 0 \, ; \,\,\, \sum M_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- For 2D problems you will have three possible equations for each section: two force equations and one moment equation. \[ \sum \vec{F} = 0 \quad\quad\quad\quad \sum \vec{M} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- For 3D problems you will have six possible equations for each section: three force equations and three moment equations. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \] \[ \sum \vec{M} = 0 \] \[ \sum M_x = 0 \, ; \,\,\, \sum M_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- Finally, solve the equilibrium equations for the unknowns. You can do this algebraically, solving for one variable at a time, or you can use matrix equations to solve for everything at once. If you assumed that all forces were tensile earlier, remember that negative answers indicate compressive forces in the members.
Example \(\)
Find the forces acting on members BD and CE. Be sure to indicate if the forces are tensile or compressive.
Example \(\)
Find the forces acting on members AC, BC, and BD of the truss. Be sure to indicate if the forces are tensile or compressive.

## 5.6: Frames and Machines

- Analyzing Frames and Machines:
A frame or a machine is an engineering structure that that contains at least one member that is not a two-force member.
A frame is a rigid structure, while a machine is not rigid. This means that no part can move relative to the other parts in a frame, while parts can move relative to one another in a machine. Though there is a difference in vocabulary in describing frames and machines, they are grouped together here because we use the same process to analyze both of these structures.

## Analyzing Frames and Machines:

When we talk about analyzing frames or machines, we are usually looking to identify both the external forces acting on the structure and the internal forces acting between members within the structure.
The method we use to analyze frames and machines (no special name here) centers around the process of breaking the structure down into individual components and analyzing each component as a rigid body. Where the components are connected, Newton's Third Law states that each body will exert an equal and opposite force on the other body. Each component will be analyzed as an independent rigid body leading to equilibrium equations for each component, but because of Newton's Third Law, some unknowns may show up acting on two bodies.

## 5.7: Analysis of Frames and Machines

- The Process for Analyzing Frames and Machines:
The process used to analyze frames and machines involves breaking the structure down into individual components in order to solve for the forces acting on each component. Sometimes the structure as a whole can be analyzed as a rigid body, and each component can always be analyzed as a rigid body.

## The Process for Analyzing Frames and Machines:

- In the beginning it is usually useful to label the members in your structure. This will help you keep everything organized and consistent in later analysis. In this book, we will label everything by assigning letters to each of the joints.    Figure \(\): The first step in the analysis of frames and machines is to label the members.
- Next you will need to determine if we can analyze the entire structure as a rigid body. In order to do this, the structure needs to be independently rigid. This means that it would be rigid even if we separated it from its supports. If the structure is independently rigid (no machines, and only some frames, will be independently rigid), then analyze the structure as a single rigid body to determine the reaction forces acting on the structure. If the structure is not independently rigid, skip this step.       Figure \(\): If, and only if, the structure is independently rigid, you should analyze the whole structure as a single rigid body to solve for the reaction forces.
Figure \(\): If, and only if, the structure is independently rigid, you should analyze the whole structure as a single rigid body to solve for the reaction forces.
- Next you will draw a free body diagram for each of the components in the structure. You will need to include all forces acting on each member:    First, add any external reaction or load forces that may be acting on the components.  Second, identify any two-force members in the structure. At their connection points, they will cause a force with an unknown magnitude but a known direction (the forces will act along the line between the two connection points on the member).   Next, add in the reaction forces (and possibly moments) at the connection points between non-two-force members. For forces with an unknown magnitude and direction (such as in pin joints), the forces are often drawn in as having unknown \(x\) and \(y\) components (\(x\), \(y\) and \(z\) for 3D truss problems).  Remember that the forces at each of the connection points will be a Newton's Third Law pair. This means that if one member exerts some force on some other member, then the second member will exert an equal and opposite force back on the first. When we draw out our unknown forces at the connection points, we must make sure that the forces acting on each member are opposite in direction.  Figure \(\): Separate the structure into individual components and draw a free body diagram of each component. It is important to remember that the forces at each connection point are a Newton's Third Law pair.
- First, add any external reaction or load forces that may be acting on the components.
- Second, identify any two-force members in the structure. At their connection points, they will cause a force with an unknown magnitude but a known direction (the forces will act along the line between the two connection points on the member).
- Next, add in the reaction forces (and possibly moments) at the connection points between non-two-force members. For forces with an unknown magnitude and direction (such as in pin joints), the forces are often drawn in as having unknown \(x\) and \(y\) components (\(x\), \(y\) and \(z\) for 3D truss problems).
- Remember that the forces at each of the connection points will be a Newton's Third Law pair. This means that if one member exerts some force on some other member, then the second member will exert an equal and opposite force back on the first. When we draw out our unknown forces at the connection points, we must make sure that the forces acting on each member are opposite in direction.  Figure \(\): Separate the structure into individual components and draw a free body diagram of each component. It is important to remember that the forces at each connection point are a Newton's Third Law pair.
- Write out the equilibrium equations for each component you drew a free body diagram of. These will be extended bodies, so you will need to write out the force and the moment equations.    For 2D problems you will have three possible equations for each section: two force equations and one moment equation. \[ \sum \vec{F} = 0 \quad\quad\quad\quad \sum \vec{M} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum M_z = 0 \]  For 3D problems you will have six possible equations for each section: three force equations and three moment equations. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \] \[ \sum \vec{M} = 0 \] \[ \sum M_x = 0 \, ; \,\,\, \sum M_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- For 2D problems you will have three possible equations for each section: two force equations and one moment equation. \[ \sum \vec{F} = 0 \quad\quad\quad\quad \sum \vec{M} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- For 3D problems you will have six possible equations for each section: three force equations and three moment equations. \[ \sum \vec{F} = 0 \] \[ \sum F_x = 0 \, ; \,\,\, \sum F_y = 0 \, ; \,\,\, \sum F_z = 0 \] \[ \sum \vec{M} = 0 \] \[ \sum M_x = 0 \, ; \,\,\, \sum M_y = 0 \, ; \,\,\, \sum M_z = 0 \]
- Finally, solve the equilibrium equations for the unknowns. You can do this algebraically, solving for one variable at a time, or you can use matrix equations to solve for everything at once. If any force turns out to be negative, that indicates that the force actually travels in the opposite direction from what is indicated in your initial free body diagram.
Example \(\)
Find all the forces acting on each of the members in the structure below.
Example \(\)
Find all the forces acting on each of the members in the structure below.
Example \(\)
If two 150-Newton forces are exerted on the handles of the bolt cutter shown below, determine the reaction forces \((F_{R1}\) and \((F_{R2})\) exerted on the blades of the bolt cutter (this will be equal to the cutting forces exerted by the bolt cutters).
Example \(\)
A 100-lb force is exerted on one side of a TV tray as shown below. Assuming there are no friction forces at the base, determine all forces acting on each of the three parts of the TV tray.

## 5.8: Chapter 5 Homework Problems

Exercise \(\)
Use the method of joints to solve for the forces in each member of the lifting gantry truss shown below.
\(F_{AB} = 113.14\) kN T, \(F_{AC} = 80\) kN C, \(F_{BC} = 120\) kN C
\(F_{BD} = 89.44\) kN T, \(F_{CD} = 80\) kN C
Exercise \(\)
The truss shown below is supported by two cables at A and E, and supports two lighting rigs at D and F, as shown by the loads. Use the method of joints to determine the forces in each of the members.
\(F_{AB} = 60\) lbs T, \(F_{AC} = 0\), \(F_{BC} = 305.94\) lbs C
\(F_{BD} = 300\) lbs T, \(F_{CD} = 120\) lbs T, \(F_{CE} = 0\)
\(F_{CF} = 305.94\) lbs C, \(F_{DF} = 300\) lbs T, \(F_{EF} = 120\) lbs T
Exercise \(\)
The truss shown below is supported by a pin joint at A, a cable at D, and is supporting a 600 N load at point C. Use the method of joints to determine the forces in each of the members. Assume the mass of the beams are negligible.
\(F_{AB} = 1162.97\) N C, \(F_{AC} = 709.86\) N T, \(F_{BC} = 0\)
\(F_{BD} = 1162.97\) N C, \(F_{CD} = 709.86\) N T
Exercise \(\)
The space truss shown below is being used to lift a 250 lb box. The truss is anchored by a ball-and-socket joint at C (which can exert reaction forces in the \(x\), \(y\), and \(z\) directions) and supports at A and B that only exert reaction forces in the y direction. Use the method of joints to determine the forces acting all members of the truss.
\(F_{AB} = 0\), \(F_{AC} = 144.33\) lbs T, \(F_{AD} = 204.09\) lbs C
\(F_{BC} = 144.33\) lbs T, \(F_{BD} = 204.09\) lbs C, \(F_{CD} = 288.68\) lbs T
Exercise \(\)
Use the method of sections to solve for the forces acting on members CE, CF, and DF of the gantry truss shown below.
\(F_{CE} = 0\), \(F_{CF} = 306.2\) lbs C, \(F_{DF} = 300.2\) lbs T
Exercise \(\)
You are asked to compare two crane truss designs as shown below. Find the forces in members AB, BC, and CD for Design 1 and find forces AB, AD, and CD for Design 2. What member is subjected to the highest loads in either case?
Design 1: \(F_{AB} = 11,276\) lbs T, \(F_{BC} = 2902\) lbs T, \(F_{CD} = 18,967\) lbs C
Design 2: \(F_{AB} = 13,322\) lbs T, \(F_{AD} = 2902\) lbs C, \(F_{CD} = 16,914\) lbs C
The largest forces are in member CD for both designs.
Exercise \(\)
The K truss shown below supports three loads. Assume only vertical reaction forces at the supports. Use the method of sections to determine the forces in members AB and FG. (Hint: you will need to cut through more than three members, but you can use your moment equations strategically to solve for exactly what you need).
\(F_{AB} = 1066.67\) lbs C, \(F_{FG} = 1066.67\) lbs T
Exercise \(\)
The truss shown below is supported by a pin support at A and a roller support at B. Use the hybrid method of sections and joints to determine the forces in members CE, CF, and CD.
\(F_{CE} = 21\) kN T, \(F_{CF} = 8.41\) kN T, \(F_{CD} = 4.67\) kN C
Exercise \(\)
The shelf shown below is used to support a 50-lb weight. Determine the forces on members ACD and BC in the structure. Draw those forces on diagrams of each member.
\(F_{BC} = 223.6\) lbs (Compression), \(F_{A_X} = -200\) lbs, \(F_{A_Y} = -50\) lbs
Exercise \(\)
A 20 N force is applied to a can-crushing mechanism as shown below. If the distance between points C and D is 0.1 meters, what are the forces being applied to the can at points B and D? (Hint: treat the can as a two-force member)
\(F_{can} = 148.9\) N (Compression)
Exercise \(\)
The suspension system on a car is shown below. Assuming the wheel is supporting a load of 3300 N and assuming the system is in equilibrium, what is the force we would expect in the shock absorber (member AE)? You can assume all connections are pin joints.
\(F_{AE} = 4611.9\) N (Compression)
Exercise \(\)
The chair shown below is subjected to forces at A and B by a person sitting in the chair. Assuming that normal forces exist at F and G, and that friction forces only act at point G (not at F), determine all the forces acting on each of the three members in the chair. Draw these forces acting on each part of the chair on a diagram.
\(F_F = 108.3\) lbs, \(F_{G_X} = -3.95\) lbs, \(F_{G_Y} = 39.5\) lbs
\(F_{C_X} = \pm \, 16.89\) lbs, \(F_{C_Y} = \pm \, 295.4\) lbs
\(F_{D_X} = \pm \, 142.9\) lbs, \(F_{D_Y} = \pm \, 147.7\) lbs
\(F_{E_X} = \pm \, 112.9\) lbs, \(F_{E_Y} = \pm \, 256.0\) lbs
- 6: Friction and Friction Applications

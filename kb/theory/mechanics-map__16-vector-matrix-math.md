来源: Mechanics Map (Moore et al.) / LibreTexts
作者: Jacob Moore and Contributors
许可: CC BY-SA 4.0（衍生须同协议并署名）
章节: 16 16: Appendix 1 - Vector and Matrix Math

## 16: Appendix 1 - Vector and Matrix Math

## 16.1: Vectors

- Vector Representation:
- Converting Between Vector Representations in 2DGoing from a Magnitude and Direction to Component FormGoing from Component Form to Magnitude and Direction
- Going from a Magnitude and Direction to Component Form
- Going from Component Form to Magnitude and Direction
- Converting Between Vector Representations in 3DAlternative Method for Finding 3D Vector Components
- Alternative Method for Finding 3D Vector Components
Vectors are used in engineering mechanics to represent quantities that have both a magnitude and a direction. Many engineering quantities, such as forces, displacements, velocities, and accelerations, will need to be represented as vectors for analysis. Vector quantities contrast with scalar values (such as mass, area, or speed), which have a magnitude but no direction.
When dealing with vectors in equations, engineers commonly denote something as a vector by putting an arrow over the variable. Variables without an arrow over top of them represent a scalar quantity, or simply the magnitude of that vector quantity.
 \text{Vector Quantity:} \quad &\, \vec{F} \\ \text{Scalar Quantity:} \quad &\, F
In contrast with scalar quantities, we cannot add, subtract, multiply or divide them by simply adding, subtracting, multiplying or dividing the magnitudes. The directions will also play a critical role in solving equations that contain vector quantities.

## Vector Representation:

To represent a vector quantity, we will generally have two options. These two options are:
- Magnitude and Direction Form: Where the magnitude is given as a single quantity and the direction is given via an angle or combination of angles.
- Component Form: Where the magnitude and direction are given through component magnitudes in each coordinate direction.
The magnitude and direction form of vector quantities are often used at the start and end of a problem. This is because it is often easier to measure things likes forces and velocities as a magnitude and direction at the start of a problem, and it is often easier to visualize the final result as a magnitude and direction at the end. Vectors represented as a magnitude and direction need to be shown visually through the use of an arrow, where the magnitude is the length of the arrow, and the direction is shown through the arrow head and an angle or angles relative to some known axes or other direction.
The component form of a vector is often used in middle of the problem because it is far easier to do math with vector quantities in component form. Vectors can be represented in component form in one of two ways. First we can use square brackets to indicate a vector, with the \(x\), \(y\), and possibly \(z\) components separated by commas. Alternatively, we can write out a vector in component form using the magnitudes in front of unit vectors to indicate directions (generally the \(\hat{i}\), \(\hat{j}\), and \(\hat{k}\) unit vectors for the \(x\), \(y\), and \(z\) directions respectively). Neither of these component forms relies on a visual depiction of the vector as with the magnitude and direction form, though it is important to clearly identify the coordinate system in earlier diagrams.
 \text{With Brackets:} \quad &\, \vec{F} = [3,4,5] \\ \text{With Unit Vectors:} \quad &\, \vec{F} = 3 \hat{i} + 4 \hat{j} + 5 \hat{k}

## Converting Between Vector Representations in 2D

For our analysis, we will often find it advantageous to have the vectors in one form or the other, and will therefore need to convert the vector from a magnitude and direction to component form or vice versa. To do this we will use right triangles and trigonometry.

### Going from a Magnitude and Direction to Component Form

To go from a magnitude and direction to component form, we will first draw a right triangle with the hypotenuse being the original vector. The horizontal arm of the triangle will then be the \(x\)-component of the vector while the vertical arm is the \(y\) component of the vector. If we know the angle of the vector with respect to either the horizontal or the vertical, we can use the sine and cosine relationship to find the \(x\) and \(y\) components.
It is important to remember that how we measure the angle will affect the sine and cosine relationships. Multiplying the magnitude by the sine will always give us the opposite leg and multiplying the magnitude by the cosine will always give us the adjacent leg.

### Going from Component Form to Magnitude and Direction

To find the magnitude and the direction of a vector using components, we will use the same process in reverse. We will draw the components as the legs of a right triangle, where the hypotenuse of the triangle shows the magnitude and direction of the vector.
To find the magnitude of the vector we will use the Pythagorean Theorem, taking the square root of the sum of the squares of each component. To find the angle, we can easily use the inverse tangent function, relating the opposite and adjacent legs of our right triangle.
If we know the magnitude of the hypotenuse, we can also use the inverse sine and cosine functions in place of the inverse tangent function to find the angle. As with the previous conversion, it is important to clearly identify the opposite leg, the adjacent leg, and the hypotenuse in our diagrams and to think of these when applying the inverse trig functions.

## Converting Between Vector Representations in 3D

In three dimensions, we will have either three components (\(x\), \(y\), and \(z\)) for component form or a magnitude and two angles for the direction in magnitude and direction form. To convert between forms we will need to draw in two sets of right triangles. The hypotenuse of the first triangle will be the original vector and one of the legs will be one of the three components. The other leg will then be the hypotenuse of the second triangle. The legs of this second triangle will then be the remaining two components as shown in the diagram below. Use sine and cosine relationships to find the magnitude of each component along the way. This general process of two consecutive right triangles will always hold true, but depending on angles that are given or chosen which components end up being which leg can vary. Carefully plotting everything out in a diagram is important for this reason.
To go from component form back to a magnitude and direction, we will use the 3D form of the Pythagorean Theorem (the magnitude will be the square root of the sum of the three components squared) and we can again use the inverse trig functions to find the angles. We simply need to work backwards through the two right triangles in our problem, so again it is important to carefully draw out your diagrams.

### Alternative Method for Finding 3D Vector Components

Sometimes, as with the tension in a cable, the geometry of the cable is given in component form rather than as angles. In cases such as this we could use geometry to figure out the angles and then use those angles to figure out the components, but there is a mathematical shortcut that will allow us to solve for the components more quickly involving the ratio of lengths. Specifically, the ratios of the components of the cable length to the overall length of the cable will be the same as the ratio of the corresponding force components to the overall magnitude of the force.
To use this method we will first need to find the overall length of the cable (or other physical geometric feature) using the Pythagorean Theorem. Once we have that overall length, we find a ratio by taking the x component of the length divided by the overall length. To find the \(x\)-component of the force, we simply multiply the overall magnitude of the force by this ratio of lengths (\(L_x/L\)). The process for the \(y\) and \(z\) components follows a similar path, except the ratios would include the \(y\) and \(z\) component lengths instead of the \(x\) component.
Example \(\)
Determine the \(x\) and \(y\) components of the vector shown below.
Example \(\)
Determine the \(x\) and \(y\) components of the vector shown below.
Example \(\)
The velocity vector of the hockey puck shown below is given in component form. Determine the magnitude and direction of the velocity with respect to the axes given.
Example \(\)
Determine the \(x\), \(y\), and \(z\) components of the force vector shown below.
Example \(\)
A cable as shown below is used to tether the top of a pole to a point on the ground. The cable has a tension force of 3 kN that acts along the direction of the cable as shown below. What are the \(x\), \(y\), and \(z\) components of the tension force acting on the top of the pole?
- 16: Appendix 1 - Vector and Matrix Math      16.2: Vector Addition
- 16: Appendix 1 - Vector and Matrix Math

## 16.2: Vector Addition

The most common thing we will need to do with many vector quantities is to add them up. The sum of these vector quantities is the net vector quantity. For example, if we have a number of forces acting on a body, the sum of those forces is known as the net force.
The sum of any number of vectors can be determined geometrically using the following strategy. Starting with one of the vectors as the base, we redraw the second vector so that the tail of the second vector begins at the tip of the first vector. We can repeat this with a third vector, a forth vector and so on, putting the tail of each vector at the tip of the last vector until we have added taken all vectors into account. Once the vectors are all drawn tip to tail, the sum of all the vectors will be the vector connecting the tail of the first vector to the tip of the last vector.
In practice, the easiest way to determine the magnitude and direction of the sum of the vectors is to add the vectors in component form. This starts by separating each vector into \(x\), \(y\), and possibly \(z\) components. As we can see in the diagram below, the \(x\) component of the sum of all the vectors will be the sum of all the \(x\) components of the individual vectors. Similarly, the \(y\) and \(z\) components of the sum of the vectors will be the sum of all the \(y\) components and the sum of all the \(z\) components respectively.
Once we find the sum of the components in each direction, we can either leave the net vector in component form, or we can use the Pythagorean theorem and inverse tangent functions to convert the vector back into a magnitude and direction as detailed on the previous page on vectors.
Figure \(PageIndex{1}\): Vide lecture covering this section, delivered by Dr. Jacob Moore. YouTube source: https://youtu.be/0tv92MX2_ro.
Example \(\)
Determine the sum of the force vectors in the diagram below. Leave the sum in component form.
Example \(\)
Determine the sum of the force vectors in the diagram below. Give the sum in terms of a magnitude and a direction.
Example \(\)
Determine the sum of the force vectors in the diagram below. Leave the sum in component form.

## 16.3: Dot Product

The dot product (also sometimes called the scalar product) is a mathematical operation that can be performed on any two vectors with the same number of elements. The result is a scalar number equal to the magnitude of the first vector, times the magnitude of the second vector, times the cosine of the angle between the two vectors.
\[ \vec{A} \cdot \vec{B} = |A| |B| \cos (\theta) \]
In engineering mechanics, the dot product is used almost exclusively with a second vector being a unit vector. If the second vector in the dot product operation is a unit vector (thus having a magnitude of 1), the dot product will then represent the magnitude of the first vector in the direction of the unit vector. In this respect, a dot product is useful in determining the component of a given vector in any given direction, where the direction is given in terms of a unit vector.
As an alternative to the above equation for calculating the dot product, we can also calculate the dot product without knowing the angle between the vectors (\(\theta\)). For this method, we break each vector down into components and take the sum of each set of components multiplied together as shown in the equation below.
\[ \vec{A} \cdot \vec{B} = (A_x * B_x) + (A_y * B_y) + (A_z * B_z) \]
Finally, as with many vector operations, the true strength of the dot product is that computers can calculate them very quickly. Both MATLAB and the Wolfram Alpha Vector Operation Calculator are able to compute dot products for you.
Example \(\)
Find the dot product of force vector \(\vec{A}\) with the given unit vector \(\hat{B}\).
Example \(\)
Calculate the dot product of \(\vec{A}\) with \(\vec{B}\) by hand.
Example \(\)
Calculate the dot product of \(\vec{A}\) with \(\vec{B}\) using MATLAB.
Example \(\)
Calculate the dot product of \(\vec{A}\) with \(\vec{B}\) using the Wolfram Vector Operation Calculator.

## 16.4: Cross Product

- Calculating the Cross Product
The cross product is a mathematical operation that can be performed on any two three-dimensional vectors. The result of the cross product operation will be a third vector that is perpendicular to both of the original vectors and has a magnitude of the first vector times the magnitude of the second vector times the sine of the angle between the vectors.
When finding a cross product, you may notice that there are actually two directions that are perpendicular to both of your original vectors. These two directions will be in exact opposite directions. To find which of these two directions the cross product uses, we will use the right-hand rule.
To use the right-hand rule, hold out you right hand, point your index finger in the direction of the first vector, turn your middle finger in towards the direction of the second vector, and hold your thumb up. Your thumb should now point in the direction of the cross product vector.
One additional thing you can note with the right-hand rule is that switching the order of the two input vectors (switching \(\vec{A}\) and \(\vec{B}\)) would result in the cross product pointing in exactly the opposite direction. This is because the cross product operation is not commutative, meaning that order does matter. Specifically, switching the order of the inputs gives you a result that is exactly the opposite of what your original calculation.

## Calculating the Cross Product

To find the cross product by hand, the easiest method is as follows.
- Write out the letters \(x \,\, y \,\, z \,\, x \,\, y\) in a row as shown in the diagram below.
- Write out the \(x\), \(y\), and \(z\) components of the first vector underneath the corresponding letters of the row of letters from Step 1. Repeat this for the second vector, writing out the second vector's components in a row under the first vector.
- Draw in diagonals as shown in the diagram. The diagonals that travel to the right as they move down represent positive quantities, while the diagonals that travel to the left as they move down represent negative quantities.
- Using the letters the diagonals travel through in the top row as a guide for which component of the result each quantity is part of, take the sum of the positive and negative diagonal products for each of the three components in the result. This should give you the final formula shown in the diagram.
In addition to calculating the cross product by hand, we can also use computer tools such as the "cross" command in MATLAB or web-based tools such as the Wolfram Alpha Vector Operation calculator. Access to these tools allows you to very easily and quickly calculate the cross product and is a major advantage to using vectors operations to analyze problems.
Example \(\)
Calculate the cross product of force vectors \(\vec{A}\) and \(\vec{B}\) in the diagram below by hand.
Example \(\)
Calculate the cross product of the vectors \(\vec{A}\) and \(\vec{B}\) in the diagram below by hand.
Example \(\)
Calculate the cross product of the vectors \(\vec{A}\) and \(\vec{B}\) in the diagram below using MATLAB.
Figure \(\): problem diagram for Example \(\).
Example \(\)
Calculate the cross product of vectors \(\vec{A}\) and \(\vec{B}\) in the diagram below, using the Wolfram Vector Operation Calculator.

## 16.5: Solving Systems of Equations with Matrices

- Converting a System of Equations to a Matrix Equation:
- Solving the Matrix Equation:
A system of equations is any set of equations that share some variables. A linear equation is an equation that consists entirely of constants and simple variables. These variables can only be multiplied by a constant, and cannot be multiplied together, raised to an exponent, used on logs or square roots, or put through other, more complex mathematical functions. An example of a system of linear equations is provided below.
\[ F_{AX} + F_{BX} = 0 \]
\[ F_{AY} - 8 = 0 \]
\[ -16 + 4 F_{AY} + 8 F_{AX} = 0 \]
In courses such as statics and dynamics, we will often wind up with a system of linear equations and be asked to solve for the unknowns in those equations. When we have just a few equations in our system, we will generally solve the equations by hand using algebraic methods such as substitution or elimination though addition or subtraction. For larger and more complex problems, we can wind up with larger systems of equations and at some point the math may become difficult to handle by hand. For these large systems of linear equations, the easiest way to solve for the unknowns is to convert the system of equations into a single matrix equation, and then use computer tools to solve the matrix equation for unknowns. Some computer tools will let you enter the system of equations manually, but in the background the computer is probably just converting it to a matrix equation in the background. For this reason it can be useful to understand this process.
In terms of assumptions, it is important to mention that this method will only work with systems of linear equations, and to have a solvable matrix equation we will need to have the same number of equations as unknown variables. For example, above we have a system of equations with three equations and three unknown variables. If these numbers do not match we will not be able to solve the matrix equation using the method described below.

## Converting a System of Equations to a Matrix Equation:

The first step in converting a system of equations into a matrix equation is to rearrange the equations into a consistent format. Generally we will put all the variables with their coefficients on one side of the equation and the constants on the other side of the equation. Additionally, it is best to list the variables in the same order in each equation. This process of rearranging the equations will make conversion later on easier.
Next we will begin the process of writing out the three matrices that make up the matrix equation. These three matrices are the coefficient matrix (often referred to as the \(A\) matrix), the variable matrix (often referred to as the \(X\) matrix), and the constant matrix (often referred to as the \(B\) matrix).
- The coefficient matrix (or \(A\) matrix) is a \(N \times N\) matrix (where \(N\) is the number of equations / number of unknown variables) that contains all the coefficients for the variables. Each row of the matrix represents a single equation while each column represents a single variable (it is sometimes helpful to write the variable at the top of each column). For instances where a variable does not show up in an equation, we assume a coefficient of 0.
- The variable matrix (or \(X\) matrix) is a \(N \times 1\) matrix that contains all the unknown variables. It is important that the order of the variables in the coefficient matrix match the order of the variables in the variable matrix.
- Finally, on the other side of the equal sign we have the constant matrix (or \(B\) matrix). This is a \(N \times 1\) matrix containing all the constants from the right side of the equations. It is important that the order of the constants matches the order of equations in the coefficient matrix.
Once we have the three matrices set up, we are ready to solve for the unknowns in the variable matrix.

## Solving the Matrix Equation:

Starting with our \(A\), \(X\), and \(B\) matrices in the matrix equation below, we are looking to solve for for values of the unknown variables that are contained in our \(X\) matrix.
\[ [A][X] = [B] \]
For a scalar equation, we would simply do this by dividing both sides by \(A\), where the value for \(X\) would be \(B/A\). With a matrix equation, we will instead need to multiple both sides of the equation by the inverse of the \(A\) matrix. This will cancel out the \(A\) matrix on the left side, leaving only the \(X\) matrix that you are looking for. On the left we will have the inverse of the \(A\) matrix times the \(B\) matrix. The result of this operation will be a \(N \times 1\) matrix containing the solution for all the variables. The value in each row of the solution will correspond to the variable listed in the same row of the \(X\) matrix.
\[ [X] = [A]^{-1} [B] \]
It is possible to find the inverse of the \(A\) matrix by hand and then multiply this with the \(B\) matrix, but this process would take longer than just solving the equations using algebra. The true strength of the method is that computer tools such as MATLAB or Wolfram Alpha can perform the matrix inversion and multiplication for you.
Example \(\)
The equilibrium equations for the body shown below are listed on the right. Convert the system of equations into a single matrix equation and solve for the unknowns.

## 16.6: Appendix 1 Homework Problems

Exercise \(\)
Determine the \(x\) and \(y\) components of the force vector shown below.
\(F_x = 692.8 \ N\)
\(F_y = 400 N\)
Exercise \(\)
Determine the \(x\), \(y\), and \(z\) components of the vector shown below.
\(F_x = 4.17 \ kN\)
\(F_y = 2.54 \ kN\)
\(F_z = -3.50 \ kN\)
Exercise \(\)
An 80-lb tension acts along a cable stretching from point O to point A. Based on the dimensions given, break the tension force shown into \(x\), \(y\), and \(z\) components.
\(F_x = 56.47 \ lbs\)
\(F_y = -37.64 \ lbs\)
\(F_z = 42.35 \ lbs\)
Exercise \(\)
Determine the \(x\) and \(y\) components of the sum of the two vectors shown below.
\(F_{total} = [58.2, 41.7] \ lbs\)
Exercise \(\)
There are two forces acting on a barge as shown below (\(\vec{F}_1\) and \(\vec{F}_2\)). The magnitude and direction of \(\vec{F}_1\) is known, but the magnitude and direction of \(\vec{F}_2\) is not. If the sum of the two forces is 600 N along the \(x\)-axis, what must the magnitude and direction of \(\vec{F}_2\) be?
\(\vec{F}_2 = 390.3 \ N\), at 41.2° below the x-axis
- 17: Appendix 2 - Moment Integrals

from errors import *
import math

class Vector:
    def __init__(self, dimensions):
        if not isinstance(dimensions , list) :
            raise TypeError("You must list the dimensions for manipulation")
        if not 1<len(dimensions)<=3:
            raise ValueError("The vectors you define can be 2 or 3 dimensional")
        self.dimensions = dimensions

    def magnitude(self):
        """
        function to find the magnitude of the vector
        """
        if len(self.dimensions) == 2:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            length = (x**2 + y**2)**0.5

        elif len(self.dimensions) == 3:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            z = self.dimensions[2]
            length = (x**2 + y**2 + z**2)**0.5
        return length

    def information(self):
        """
        This function returns the information of the defined vector.
        """
        vektorinformation = [

        ]
        if len(self.dimensions) == 2:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            vektorinformation.append({"dimension":2 })
            length = (x**2 + y**2)**0.5
            vektorinformation.append(length)

        elif len(self.dimensions) == 3:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            z = self.dimensions[2]
            vektorinformation.append({"dimension":2})
            length = (x**2 + y**2 + z**2)**0.5
            vektorinformation.append({"length":length})    
        return vektorinformation
    
    def Inner_product(self, other):
        """
        This function finds the inner product of two defined vectors.
        """

        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a*b for a, b in zip(self.dimensions, other.dimensions))
    
    def AngleTwoVector(self, other):
        """
        It is a function that finds the angle between two vectors according to the inner product equation.
        """
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for dot product.")

        inner_product = self.Inner_product(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()

        cos_theta = max(-1, min(1, inner_product / (mag1 * mag2)))

        return math.acos(cos_theta)
    
    def Visualization(self):
        try: 
            import matplotlib.pyplot as plt
        except ModuleNotFoundError:
            raise RequiredModule(
            "matplotlib module not installed. Install it with 'pip install matplotlib'."
            )

        v = self.dimensions

        if len(v) == 2:
            origin = Vector([0, 0])
            plt.figure(figsize=(6,6))
            plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color='r', width=0.01)
            plt.xlim(-1, self.dimensions[0]+1)
            plt.ylim(-1,self.dimensions[1]+1)
            plt.grid(True)
            plt.axhline(0, color='black', linewidth=0.8)
            plt.axvline(0, color='black', linewidth=0.8)
            plt.text(v[0]/2, v[1]/2, f"{v}", fontsize=12, color='blue')

            plt.title("R^2 Visualization")
            plt.xlabel("x axis")
            plt.ylabel("y axis")
            plt.gca().set_aspect('equal', adjustable='box')
            plt.show()
        elif len(v) == 3:
            origin = Vector([0, 0, 0])
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.quiver(origin[0], origin[1], origin[2],
                    v[0], v[1], v[2],
                    color='b', arrow_length_ratio=0.1)

            ax.set_xlim([-1, self.dimensions[0]+1])
            ax.set_ylim([-1, self.dimensions[1]+1])
            ax.set_zlim([0, self.dimensions[2]+1])

            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
            ax.set_title('R^3 Visualization')

            plt.show()

    def UnitVector(self):
        """
        Returns the unit vector of the given vector.
        """
        Norm = self.magnitude()
        if Norm == 0:
            raise ValueError("Zero is undefined in division")
        return [x / Norm for x in self.dimensions]
    
    def CosTwoVector(self, other):
        """
        Finds the cosine of the angle between two vectors.
        cos(θ) = (v1 · v2) / (‖v1‖ * ‖v2‖)
        """

        InnerP = self.Inner_product(other)

        normv1 = self.magnitude()
        normv2 = other.magnitude()

        if normv1 == 0 or normv2 == 0:
            raise ValueError("Zero vector: cosine undefined.")

        return InnerP / (normv1 * normv2)
    
    def Projection(self, other):
        """
        Returns the projection of one vector onto another vector.
        proj_v2(v1) = (|v1| * cosθ) * unit(v2)
        """
        unitv2 = other.UnitVector()
        cosa = self.CosTwoVector(other)
        normv1 = self.magnitude()

        scalar = normv1 * cosa
        return [scalar * x for x in unitv2]

    def __repr__(self):
        return f"Vector({self.dimensions})"

    def __str__(self):
        if len(self.dimensions) == 2:
            dimensions = "R^2"
        elif len(self.dimensions) == 3:
            dimensions = "R^3"

        return f"<Vector {self.dimensions}, |v|={self.magnitude():.2f} , dimensions={dimensions}>"
        
    def __add__(self, other):
        """Vector addition"""
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a, b in zip(self.dimensions, other.dimensions)])

    def __sub__(self, other):
        """Vector subtraction"""
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a - b for a, b in zip(self.dimensions, other.dimensions)])

    def __mul__(self, scalar):
        """Scalar multiplication"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("You can only multiply a vector by a scalar (number).")
        return Vector([a * scalar for a in self.dimensions])

    def __matmul__(self, other):
        """Dot product with @ operator"""
        return self.Inner_product(other)

    def __eq__(self, other):
        """Check if two vectors are equal"""
        return self.dimensions == other.dimensions
    
    def __getitem__(self, index):
        return self.dimensions[index]

    def __iter__(self):
        return iter(self.dimensions)
    
class Line:
    def __init__(self, point, direction=None, slope=None, perpendicular_vector=None):
        if not (isinstance(point, list) and isinstance(direction, list)):
            raise WrongDataTypeError("Must be in the point and direction list type")
        if len(point) != len(direction):
            raise SizeLimitExceededError("Point and direction list must be the same size")
        if len(point) not in (2, 3):
            raise SizeLimitExceededError("Only dimensions 2 and 3 are supported")

        self.point = point
        #self.direction = direction

        if slope is None:
            if len(point) == 2:
                dx = direction[0]
                dy = direction[1]
                self.slope = None if dx == 0 else (dy / dx)
            else:
                self.slope = None
        else:
            if not isinstance(slope, (int, float)):
                raise WrongDataTypeError("Slope must be float")
            self.slope = float(slope)

        if perpendicular_vector is None:
            if len(direction) == 2:
                a, b = direction
                self.perpendicular_vector = [-b, a]
            else:
                self.perpendicular_vector = None
        else:
            if not isinstance(perpendicular_vector, list):
                raise WrongDataTypeError("perpendicular_vector must be list")
            self.perpendicular_vector = perpendicular_vector


    def point_at(self, t):
        if not isinstance(t, (int, float)):
            raise WrongDataTypeError("t must be float")
        return [p + t * d for p, d in zip(self.point, self.direction)]
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"r(t) {self.point} t*{self.direction}"
        
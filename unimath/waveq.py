import math
import matplotlib.pyplot as plt
from .matrix import Matrix 


def linspace(start, stop, N):
    step = (stop - start) / (N - 1)
    return [start + i * step for i in range(N)]


def psi_2d(x, y, Lx, Ly, nx, ny):
    norm = 2.0 / math.sqrt(Lx * Ly)
    return (
        norm *
        math.sin(nx * math.pi * x / Lx) *
        math.sin(ny * math.pi * y / Ly)
    )


def compute_density_2d(Lx, Ly, nx, ny, N):
    x = linspace(0, Lx, N)
    y = linspace(0, Ly, N)

    rho = [[0.0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            psi_val = psi_2d(x[i], y[j], Lx, Ly, nx, ny)
            rho[i][j] = psi_val * psi_val

    return x, y, rho


def Wave_Equation(Lx=1.0, Ly=1.0, nx=1, ny=1, N=60):
    """
    |ψ|² Visualization :
    
    """
    x, y, rho = compute_density_2d(Lx, Ly, nx, ny, N)


    #rho_T = [list(col) for col in zip(*rho)]
    rho_matrix = Matrix(rho)
    rho_T = Matrix.Transpose(rho_matrix).arrays

    plt.imshow(
        rho_T,
        origin="lower",
        extent=[0, Lx, 0, Ly],
        aspect="auto"
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"|ψ|² (nx={nx}, ny={ny})")
    plt.colorbar(label="|ψ|²")
    plt.tight_layout()
    plt.show()


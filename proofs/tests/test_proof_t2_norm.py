import math
from proofs.t2_utils import delta_J, delta_L

def test_duality():
    tau = 1e-3
    assert abs(delta_J(tau, 1) - delta_L(tau, 1)) < tau**1.5 
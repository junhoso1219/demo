from proofs.t3_utils import remainder_val

def test_remainder_scaling():
    tau = 1e-3
    val = remainder_val(tau, I_ddot=2, K=0)
    assert abs(val) < tau**1.5 
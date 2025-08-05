def remainder_val(tau: float, I_ddot: float, K: float):
    """High-order JKO remainder: -½ τ² I'' - τ³ K"""
    return -0.5 * tau**2 * I_ddot - tau**3 * K 
def delta_J(tau: float, I_mu: float):
    """ΔJ_τ = -½ τ I(μ)"""
    return -0.5 * tau * I_mu

def delta_L(tau: float, I_q: float):
    """ΔL_τ = -½ τ I(q)"""
    return -0.5 * tau * I_q 
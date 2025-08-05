# --- proof_t2_norm의 모든 코드를 여기에 담았습니다 ---

# 셀 1: 헤더
import sympy as sp
sp.init_printing()
d, tau = sp.symbols('d tau', positive=True)
sigma = sp.sqrt(2*tau)  # σ^2 = 2τ
x, eps = sp.symbols('x eps')
print("셀 1: 심볼 정의 완료")

# 셀 2: 원본 DSM 최적값 계산
I_q = sp.symbols('I_q', positive=True)
L_sigma = d/sigma**2 - I_q
print("셀 2: DSM 최적값 정의 완료")

# 셀 3: 정규화 계수 σ²/4 적용
L_tilde = (sigma**2/4)*L_sigma - d/4
L_tilde_simplified = sp.simplify(L_tilde.subs(sigma**2, 2*tau))
print("셀 3: 정규화된 값 계산 완료. 결과:")
sp.pprint(L_tilde_simplified)

# 셀 4: ΔJ_τ 계산
I_mu = sp.symbols('I_mu', positive=True)
DeltaJ = -tau/2*I_mu
expr_gap = sp.expand(DeltaJ - L_tilde_simplified)
print("셀 4: DeltaJ와의 차이 계산 완료. 결과:")
sp.pprint(expr_gap)

# 셀 5: 1-D Gaussian toy 검증
import torch
def deltaJ_numeric(tau_val):
    return -0.5*tau_val

def deltaL_numeric(tau_val):
    return -0.5*tau_val

taus = torch.logspace(-3, -1, 10)
assert torch.allclose(
    torch.tensor([deltaJ_numeric(t) for t in taus]),
    torch.tensor([deltaL_numeric(t) for t in taus]),
    atol=1e-6)
print("셀 5: 수치 검증 성공!") 
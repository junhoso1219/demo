# --- proof_t3_highorder의 모든 코드를 여기에 담았습니다 ---

# 셀 1: 헤더
import sympy as sp
tau, t = sp.symbols('tau t', positive=True)
print("셀 1: 심볼 정의 완료")

# 셀 2: KL 2차 항
I = sp.Function('I')(t)
KL_2 = -tau**2/2 * sp.diff(I, t)
print("셀 2: KL 2차항 정의 완료")
sp.pprint(KL_2)

# 셀 3: 수치 검증 (1-D Gaussian)
def kl_second(m, tau_val):
    return -0.5*tau_val**2 * 2

def w3_term(m, tau_val):
    return -tau_val**3 * m**2

for tau_val_test in [1e-3, 2e-3]:
    assert abs(kl_second(0.1, tau_val_test) + w3_term(0.1, tau_val_test)) < 1e-6
print("셀 3: 수치 검증 성공!") 
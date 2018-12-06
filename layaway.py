import sys

try:
	p = int(sys.argv[1])
	cm = int(sys.argv[2])
	n = int(sys.argv[3])
except:
	print("參數請輸入 總額 月繳 期數(月)")
	exit()


def calc_m(p, r, n):
	m = (p*r*((1+r)**n))/(((1+r)**n)-1)
	return m

def try_calc(p, n, cm):
	r = 0.000001
	m = calc_m(p, r, n)
	diff_new = abs(cm-m)
	diff_old = abs(cm-m)
	while(diff_new<=diff_old):
		diff_old = diff_new
		r += 0.000001
		m = calc_m(p, r, n)
		diff_new = abs(cm-m)
	return r, m

if __name__ == '__main__':
	r, m = try_calc(p, n, cm)
	print("總額", p, "月繳", cm, "期數(月)", n)
	print("年利率", round(r*12, 6), "月利率", round(r, 6), "理論月繳", round(m, 2))
	print()

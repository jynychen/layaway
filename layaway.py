import sys

try:
	p = int(sys.argv[1])
except:
	print("參數請輸入貸款金額")
	exit()

n_list = [3, 6, 12, 24]
cr_list = [0.97, 0.94, 0.92, 0.88]

def calc_cm(p, cr, n):
	cmr = round(round(p/cr)/n)
	cm = (p/cr)/n
	return cmr, cm

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

def calc_rk(p, n , cr):
	return (1/cr-1)*2/(n+1)

for i, n in enumerate(n_list):
	cr = cr_list[i]
	cmr, cm = calc_cm(p, cr, n)
	r, m = try_calc(p, n, cm)
	rk = calc_rk(p, n, cr)
	print("期數", n, "設定", cr, "本利比", round(1/cr-1, 4), "期均本利比",  round((1/cr-1)/n, 4), "月還款", cmr, round(cm, 2))
	print("等額本金月利率", round(rk, 6), "等額本息月利率", round(r, 6), "等額本息月還款", round(m, 2))
	print()

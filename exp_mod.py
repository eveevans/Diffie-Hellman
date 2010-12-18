#x^y mod n
def exp_mod(x,y,n):
	s=1l
	t=x
	u=y
	while u:
		if u&1:
			s=(s*t)%n
		u>>=1;
		t=(t*t)%n
	return s


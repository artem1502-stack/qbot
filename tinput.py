NAME="qioqiijeqifqieikcsmkkovqwef_bot"
TOKEN="1664123952:AAEM-8BZAhGcKWu5kTGvB-gvzovde5yIFrE"
def tinput(d="data.txt"):
	P=[]
	R=[]
	with open(d,'r') as f:
		for line in f:
			a=line.split('#')
			P.append(a[0])
			R.append(a[1])
	print(f"P: {P}")
	print(f"R: {R}")
	return P,R
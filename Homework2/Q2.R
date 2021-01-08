BS<-function(s, k, t, sigma, r) {
	x = sigma * sqrt(t)
	y = log(s / k) + (r + (sigma^2) / 2) * t
	d1 = y / x
	d2 = d1 - x
	c = s * pnorm(d1) - k * exp(-(r * t)) * pnorm(d2)

	return(c)
}

print(BS(100, 100, 0.5, 0.1, 0.04))
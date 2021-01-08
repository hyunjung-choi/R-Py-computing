simulation <- function(s, k, t, sigma, r, dt, n){
	m = t / dt
	S <- matrix(0, nrow = n, ncol = m)
	V <- c()

	for (i in 1:nrow(S)){
		for (j in 1:ncol(S)){
			if(j == 1){
				S[i, j] <- s
			}
			else {
				S[i, j] <- S[i, j - 1] * exp((r - 0.5 * (sigma^2)) * dt + sigma * sqrt(dt) * rnorm(1, 0, 1))
			}

			if(j == ncol(S)){
				val = max(c((S[i, j] - k), 0))
				V <- append(V, val)
			}
		}
	}

	C = exp(-(r * t)) / n * sum(V)
	cat("C = ", C, "\n")

	return(S)
}

S = simulation(100, 100, 0.5, 0.1, 0.04, 0.001, 10000)

for (i in 1:5){
	x <- 1:ncol(S)
	y <- S[i, ]
	df = data.frame(x, y)
	basicPlot <- ggplot(data = df, aes(x = x, y = y)) + geom_line(size=1) + labs(x = "기간(t)", y = "주가 경로(S)") 
	plot <- basicPlot+ ggtitle(paste(toString(i), "번째 주가경로 그래프")) + 
	theme(plot.title = element_text(face = "bold", hjust = 0.5, size = 15, color = "darkblue"))
	print(plot)
}


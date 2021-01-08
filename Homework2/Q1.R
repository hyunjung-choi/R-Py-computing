library('ggplot2')

q1<-function() {
	s<-c(0:200)
	k = 100
	y = c()

	for (i in s){
		x <- c(i-k,0)
		y <- append(max(x), y)
	}

	df = data.frame(s, y)
	qplot(s,y, data=df, geom=c("point"))
	basicPlot <- ggplot(data=df, aes(x=s, y=y)) + geom_point(size=1) + 
	labs(x = "기준자산 가격(s)", y = "수입(y)") + 
	ggtitle("콜옵션 소유자의 수입(y)과 기준자산 가격(s)의 그래프") + 
	theme(plot.title = element_text(face = "bold", hjust = 0.5, size = 15, color = "darkblue"))
}

q1()
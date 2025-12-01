data <- read.csv("../data/processed/sales_clean.csv")

summary(data)

plot(data$quantity, 
     data$total_price, 
     main="Quantity vs Total Price",
     xlab="Quantity",
     ylab="Total Price")
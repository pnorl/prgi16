tal = 5;
lista = [1 2 3 4 5];
f = @(x) x.^2;
x = 1:0.1:6;
y = f(x);

plot(x,y)
xlabel('xv�rde')
ylabel('yv�rde')
grid on;
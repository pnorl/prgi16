clear;
clc;
disp('För en funktion på formen ax+bx^2+c ange a,b och c.')
a = input('a: ');
b = input('b: ');
c = input('c: ');

f = @(x) a*x + b*x.^2 + c;

x = 0:0.1:10;
y = f(x);

plot(x, y);

xlabel('x-axel');
ylabel('y-axel');
grid on;
title('Funktionen')

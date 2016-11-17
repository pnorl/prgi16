clear;
clc;
tal = input('Ange ett tal: ');
tal2 = tal*2;
disp(['Ditt tal gånger två är: ', num2str(tal2)]);

for i = 1:5
    disp(num2str(i))
end
feltolerans = 1e6;

fel = 1;
a = 0;
while (fel > feltolerans)
    disp(num2str(a*2))
    a = a+1;
end



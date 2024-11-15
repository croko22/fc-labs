x = linspace(0,50,50); t = linspace(0,250,100); [X,T]= meshgrid(x,t);

[X,T]= meshgrid(0:1:50,0:2.5:250);

u=0;
for n=1:20
    u = u + exp(-(2.*n-1).^2.*pi.^2.*T./2500).*sin((2.*n-1).*pi.*X./50)./(2.*n-1);
end

surf(T,X,u)
xlabel('Tiempo')
ylabel('Posicion')
zlabel('Temperatura')
title('Solucion de la Ecuacion de Calor')
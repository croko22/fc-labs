x = linspace(0, 50, 50);
t = linspace(0, 250, 100);
[X, T] = meshgrid(x, t);

[X, T] = meshgrid(0:1:50, 0:2.5:250);

u = 0;
for n = 1:20
    u = u + sin((2 * n - 1) * pi * X / 50) .* cos((2 * n - 1) * pi * T / 50) / (2 * n - 1);
end

surf(T, X, u)
xlabel('Tiempo')
ylabel('Posición')
zlabel('Amplitud')
title('Solución de la Ecuación de Onda')
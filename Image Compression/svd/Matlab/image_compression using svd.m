a = imread('dada_high4.jpg');
R = a(:, :, 1);
G = a(:, :, 2);
B = a(:, :, 3);

gray = 0.2989*R + 0.5870*G + 0.114*B;
figure, subplot(4, 4, 1)
imagesc(gray);
[u,s,v] = svd(gray, 'econ');
i = 2;
q = 1:10
for r = q*10
  subplot(4, 4, i), i = i + 1;
  imagesc(u(:, 1:r)*s(1:r, 1:r)*v(:, 1:r)');
  end
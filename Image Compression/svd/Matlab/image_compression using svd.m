a = imread('dada_high4.jpg');

%Break the image into its 3 different channels
R = a(:, :, 1);
G = a(:, :, 2);
B = a(:, :, 3);

% Take the weighted average of the different channels to convert the rgb image to grayscale
gray = 0.2989*R + 0.5870G + 0.114*B;

%Visualising the Grayscale image
figure, subplot(4, 4, 1)
imagesc(gray);

%Calculate the economy svd
[u,s,v] = svd(gray, 'econ');


% calculating and plotting of the images with different truncation of the decomposition
i = 2;
q = 1:10
for r = q*10
  subplot(4, 4, i), i = i + 1;
  imagesc(u(:, 1:r)*s(1:r, 1:r)*v(:, 1:r)');
  end
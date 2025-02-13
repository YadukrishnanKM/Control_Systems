pkg load control
clear all
close all
clc

num = [1 2]
den = [1 2 3]

# Create the transfer function
sys = tf(num, den)

# Plot the nyquist plot
pol = pole(sys)
zer = zero(sys)

pol_real = real(pol)
pol_img  = imag(pol)

zer_real = real(zer)
zer_img  = imag(zer)


plot(pol_real, pol_img , 'x', zer_real, zer_img, 'o')
xlim([-4, 2])
ylim([-2, 2])
line ([0,0],[-2, 2], "linewidth", 2, "color", 'k')
line ([-4,2],[0, 0], "linewidth", 2, "color", 'k')
grid on
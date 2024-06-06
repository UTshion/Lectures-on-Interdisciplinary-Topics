# van der Pol の微分方程式

**van der Pol の微分方程式**  
$$\frac{d^2x}{dt^2} - \mu(1-x^2)\frac{dx}{dt} + x = 0 $$

のベクトル場と解軌道を、x-y平面上にプロットするプログラムです。  


![animation](https://github.com/UTshion/Lectures-on-Interdisciplinary-Topics/blob/main/van_der_Pol/van_der_pol_animation.gif)

# OVモデルの拡張  
**OVモデル（Optimal Velocity Model）の微分方程式**  
$$　X_n'' = a \left( V (X_{n+1} - X_n) - X_n' \right) $$


**路面状態（damping）のパラメータを新たに追加した拡張モデル**

$$　X_n'' = a \left( V (X_{n+1} - X_n) - X_n' \right) - damping \times X_n' $$


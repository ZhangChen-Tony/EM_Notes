# 2. Electric polarization

> Matter is not free space, it contains atoms
>
> The first two pictures are from Griffith Book

## 2.1 Bound charges

Electric field can induce a dipole moment in a neutral atom

<img src="./images/2_Electric_Field_In_Matter/v2-4af8f8b877ec6ec19ad2aa7d7c8b6397.png" alt="Image" style="zoom:33%;" />

And the electric moment is defined as $\mathbf p = \alpha \mathbf E$ where $\alpha$ is the **polarizability** of the atom. A list of polarizability can be seen from the handout.

If, for example, the outside E ~ $10^6$ V/m, then the displacement would be about $10^{-15}$ m, which is much less the size of an atom.

Also, there are polar molecules which already have a dipole moment, but they are randomized because of the present of inner energy $K_B T$

<img src="./images/2_Electric_Field_In_Matter/v2-b3f7c7ce3043aaeead6c6e814ae380d4.png" alt="Image" style="zoom: 50%;" />

However, an E field can line them up

For a bok of aligned dipoles (per unit volume), define the polarization $\mathbf P$ as the dipole moment per unit volume as $\mathbf P = n\mathbf p$

If they are not aligned, then the polarization is zero.

> Question: what is the electric potential produced by a box of dipoles?

<img src="./images/2_Electric_Field_In_Matter/v2-0aebbe347369877395d1f736af205cc8.png" alt="Image" style="zoom:25%;" />

$$
\begin{align*}V(\mathbf R) &=\frac{1}{4\pi\epsilon_0}\int \frac{\mathbf P(\mathbf r)\cdot\mathbf R}{|R|^3}d^3\mathbf \tau'\\ &=\frac{1}{4\pi \epsilon_0}\int\mathbf{P(r)}\cdot\mathbf\nabla \frac{1}{R}d\tau'\\\nabla \frac{1}{R} &= -\frac{\mathbf R}{R^3}\\
\nabla\frac{1}{|r-r'|} &= -\frac{r-r'}{|r-r'|^3}\\
\nabla'\frac{1}{|r-r'|} &= \frac{r-r‘}{|r-r'|^3}\\
\end{align*}
$$

Note that $\mathbf\nabla\cdot (f\mathbf F)=f\mathbf\nabla\cdot\mathbf F+\mathbf F\cdot\mathbf\nabla f$

$$
\Rightarrow V(\mathbf r) = \frac{1}{4\pi\epsilon_0}\int \mathbf\nabla'\frac{\mathbf P(\mathbf r')}{|\mathbf R|}d\mathbf \tau' - \frac{1}{4\pi\epsilon_0}\int\frac{1}{R}\nabla\cdot\mathbf P(\mathbf r')d\mathbf \tau'
$$

$$
=\frac{1}{4\pi\epsilon_0}\int_{s'}\frac{\sigma_bdS'}{R}+\frac{1}{4\pi\epsilon_0}\int_{\tau'}\frac{\rho_bd\tau'}{R}
$$

where $\sigma_b = \mathbf P\cdot\mathbf n$ is the surface bounded charge density and $\rho_b = -\nabla\cdot\mathbf P$ is the volume bound charge density (the minus sign is because $\mathbf P$ is defined as the dipole moment per unit volume).

The derivation can be seen from Griffiths' book page 176.

Remember to drop primes!

In bulk, Gauss's Law is $\nabla\cdot\mathbf E = \frac{\rho}{\epsilon_0}$, but $\rho = \rho_{free} + \rho_{bound}$ remember that $\rho_{bound} = -\nabla\cdot\mathbf P$ and hence $\nabla\cdot\mathbf E = \frac{\rho_{free}}{\epsilon_0} - \frac{\nabla\cdot\mathbf P}{\epsilon_0}$

We define electric displacement

$$
\mathbf D = \epsilon_0\mathbf E + \mathbf P
$$

$$
\Rightarrow \mathbf\nabla\cdot\mathbf D = \rho_{free}
$$

That is much easier, since it only depends on free charges.

The integral form is

$$
\oint \mathbf D\cdot d\mathbf a = Q_{free}
$$

## Linear dielectrics

For a linear dielectric, $\mathbf P = \epsilon_0\chi_e\mathbf E$ where $\chi_e$ is the electric susceptibility, which is dimensionless.

$$
\Rightarrow \mathbf D =\epsilon_0\mathbf E + P = \epsilon_0(1+\chi_e)\mathbf E
$$

$(1+\chi_e)$ is the relative permitivity $\epsilon_r$ and it is dimensionless.

*Example:*

Field from a point charge in a linear dielectric:

$$
\int_s\mathbf D\cdot d\mathbf s = Q_{free}
$$

$$
\Rightarrow \mathbf D = \frac{Q_f}{4\pi r^2}\mathbf{\hat{r}}
$$

$$
\Rightarrow \mathbf E = \frac{Q_f}{4\pi\epsilon_0 r^2}\mathbf{\hat{r}}
$$

> Recap of lecture 5:
> Polarization: $\overrightarrow{P}=n\overrightarrow{p}$
> Bound charges: $\rho_b=-\nabla\cdot\overrightarrow{P}$, $\sigma_b=\overrightarrow{P}\cdot\hat{n}$
> Electric displacement: $\overrightarrow{D}=\epsilon_0\overrightarrow{E}+\overrightarrow{P}=\epsilon_0\epsilon_r\overrightarrow{E}$
> Maxwell: $\nabla\cdot\overrightarrow{D}=\rho_f$
> Linear dielectric: $\overrightarrow{P}=\epsilon_0\chi_e\overrightarrow{E}$
> Where $\chi_e$ is the electric susceptibility = $\epsilon_r-1$

*Question* Has D solved everything?
-- No. The div equation is easier, but...

> Reminder: $\overrightarrow{\nabla}\cdot\overrightarrow{E}=\frac{\rho_{tot}}{\epsilon_0}$
> $\overrightarrow{\nabla}\cdot\overrightarrow{D}=\rho_f$
> And the equation for $\overrightarrow{D}$ is $\epsilon_0\overrightarrow{E}+\overrightarrow{P}=\epsilon_0\epsilon_r\overrightarrow{E}$

$$
\overrightarrow\nabla\times\overrightarrow{E}=0
$$

$$
\overrightarrow\nabla\times\overrightarrow{D}=\epsilon\overrightarrow\nabla\times\overrightarrow E+\overrightarrow\nabla\times\overrightarrow P\ne 0
$$

## Boundrary conditions

$E_{//}$ is continuous

$$
\overrightarrow\nabla\times\overrightarrow E=0
$$

$$
\oint\overrightarrow E\cdot d\overrightarrow l=0
$$

But $D_{//}$ is not continuous (if $\nabla\times\overrightarrow P\ne0$ at interface)

*$D_\perp$* is continuous

$$
\nabla\cdot\overrightarrow D=\rho_f
$$

$$
\oint\overrightarrow D\cdot d\overrightarrow a=Q_f
$$

but $E_\perp$ may not be continuous if we have bound charges at the interface

*Example*

![Image](./images/2_Electric_Field_In_Matter/v2-e013e9f7011c9cea9e3df1e9ddef4a85.png)

$$
\Rightarrow E_0//x
$$

$$
E_1=E_3=E_0
$$

$D_\perp$ is continuous

$$
\Rightarrow D_1=D_3=\epsilon_0E_0=D_2
$$

$D_2=\epsilon_0\epsilon_rE_2$

$$
\Rightarrow E_2=\frac{E_0}{\epsilon_r}
$$

So there is a smaller E field in the dielectric

$$
P_2=\epsilon_0(\epsilon_r-1)E_2\\
 = \frac{\epsilon_0}{\epsilon_r}(\epsilon_r-1)E_0
$$

$$(P_1=P_3=0)$$

Since $P_2$ is constant, $\nabla\times\overrightarrow P=0\Rightarrow \rho_b=0$

$$z = o,  \sigma_b = \mathbf P\cdot\mathbf n  = \frac{\epsilon_0}{\epsilon_r}(\epsilon_r-1)E_0$$
$$z = d, \sigma_b = \mathbf P\cdot\mathbf n = \frac{\epsilon_0}{\epsilon_r}(\epsilon_r-1)E_0$$

### Example: 

There is dielectric sphere, with radius a and relative permittiaty \epsilon_r. The sphere is in a uniform electric field $\mathbf{E_0}$. Find V.
> We got to use Laplace's equation 

General solution to Laplace's equation in spherical coordinates (with azimuthal symmetry) is 

$$V(r,\theta) = \sum^{\infty}_{l = 0}\left(A_lr^l+\frac{B_l}r^{l+1}\right)P_l(\cos\theta)$$

where $P_l$ is the Legendre polynomial.

Solve separatively for r > a and r < a

As $r\rightarrow\infty$, $V\rightarrow -E_0r\cos \theta$
As $r\rightarrow 0$, $V$ should be finite (not blow up)
$$\Rightarrow B_l = 0$$ for r<a

case r<a:
$$V = V_{in}\sum^{\infty}_{l = 0}A_lr^lP_l(\cos\theta)$$

And for r>a:
$$V = V_{out}=-E_0r\cos\theta+\sum^{\infty}_{l = 0}\frac{B_l}{r^{l+1}}P_l(\cos\theta)$$

As for r = a, $E_{//}, D_{\perp}, V$ are continuous

$$\sum_{l=0}^{\infty}A_lr^lP_l(\cos \theta) = -E_0 a \cos\theta+\sum_{l=0}^\infty\frac{B_l}{a^{l+1}}P_l(\cos\theta)$$

$$\Rightarrow A_l = \left\{ 
\begin{matrix}\frac{B_l}{a^{l+1}}&&l\ne 1\\
-E_0+\frac{B_1}{a^2} && l=1
\end{matrix}\right.$$

$E_0 = -\frac{1}{r}\frac{\partial V}{\partial \theta}$ is continuous

$\rightarrow$ generates same expressions



That is not terribly useful, so we will try another one

$D_{\perp} = -\epsilon_0\epsilon_r\frac{\partial V}{\partial r}$ is continuous

$$\Rightarrow -\epsilon_0\epsilon_r\frac{\partial V}{\partial r}|_{r=a} = -\epsilon_0\frac{\partial V_{out}}{\partial r}|_{r=a}$$

$$\epsilon_r\sum_{l=0}^\infty lA_la^{l-1}P_l(\cos\theta) = -E_0\cos\theta+\sum_{l=0}^\infty -(l+1)\frac{B_l}{a^{l+2}}P_l(\cos\theta)$$

$$A_l = \left\{\begin{matrix}-\frac{1}{\epsilon_r}\frac{l+1}{l}\frac{B_l}{a^{2l+1}} && l\ne 1 \\
\frac{1}{\epsilon_r}(-E_0-\frac{2B_l}{a^3})&&l=1\end{matrix}\right.$$

Hence, we got two expressions for A in terms of l. They cant both be right unless $A_l=B_l=0$ for $l\ne 1$ 

On the other hand, we have 

$$A_1 = \underbrace{-E_0+\frac{B_1}{a^3}}_①=\underbrace{\frac{1}{\epsilon_r}\left(-E_0-\frac{2B_0}{a^3}\right)}_②$$

$\epsilon_r(①-②) = 0$

Hence

$$(1-\epsilon_r)E_0+(\epsilon_r+2)\frac{B_1}{a^3}=0$$

$$\Rightarrow B_1 = a^3E_0\left(\frac{\epsilon_r-1}{\epsilon_r+2}\right)$$

$$\rightarrow A_1 = -\frac{3E_0}{\epsilon_r+2}$$

Now, put everything together

$$V = \left\{\begin{matrix}
\underbrace{\frac{3}{\epsilon_r+2}E_0r\cos\theta}_{\text{uniform field}} && r<a\\
\underbrace{-E_0r\cos\theta}_{\text{uniform field}}+\underbrace{\left(\frac{E_r-1}{E_r+2}\frac{E_0a^3\cos\theta}{r^2}\right)}_{\text{dipole field}}&&r>a\end{matrix}\right.$$

Interestingly, we all have uniform fields applied inside and outside. And if in vacuum, we will have uniform field outside (dipole field vanishes)



#### P inside sphere:

$$P = \epsilon_0(\epsilon_r-1)E_{in}$$

where $E_in$ is $\frac{3E_0}{\epsilon_r+2}$

#### Dipole moment of sphere

$$p= \frac{4}{3}\pi a^3P=\frac{4\pi a^3\epsilon_0(\epsilon_r-1)E_0}{\epsilon_r+2}$$

#### Polarizability 

$$\begin{align*}\alpha &= \frac{P}{E_0}\\
&=4\pi a^3\epsilon_0\frac{\epsilon_r-1}{\epsilon_r+2}\end{align*}$$

#### Bound charge on the surface

$$\begin{align*}\sigma_b&=\mathbf P\cdot\hat{\mathbf n}\\&=P\cos\theta\\*
&=\frac{3\epsilon_0(\epsilon_r-1)}{\epsilon_r+2}E_0\cos\theta\end{align*}$$
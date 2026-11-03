# Material reservado — Semana 07: planos e intersección

Este material se retira de la clase única de la semana 06 y se conserva para preparar la semana 07, dedicada a intersección de subespacios. Los bloques son fragmentos LaTeX para incorporar a los futuros apuntes, no un documento independiente para compilar. Al incorporarlos, adaptar el prefijo de las etiquetas a la semana 07.

## Ejemplo del plano y figura
```latex
\subsection{Un plano de desplazamientos en el espacio}

\begin{ejem}[Moverse sin salir de un plano]\label{sem06cl01:plano}
    Consideremos una plataforma cuyos desplazamientos deben satisfacer
    \[
        P=\{(x,y,z)\in\R^3:x+y-z=0\}.
    \]
    Geométricamente, $P$ es el plano $z=x+y$, que pasa por el origen.
    Los movimientos $a=(1,0,1)$ y $b=(0,1,1)$ pertenecen a él; también
    su suma $a+b=(1,1,2)$ y sus múltiplos reales.

    Al despejar $z$, todo vector de $P$ se escribe como $(s,t,s+t)$.
    Comprobemos las tres condiciones del criterio:
    \begin{enumerate}
        \item $(0,0,0)\in P$, pues $0+0-0=0$.
        \item Si $u=(s,t,s+t)$ y $v=(r,q,r+q)$ pertenecen a $P$, entonces
              \[
                  u+v=(s+r,t+q,(s+r)+(t+q))\in P.
              \]
        \item Si $u=(s,t,s+t)\in P$ y $\alpha\in\R$, entonces
              \[
                  \alpha u=(\alpha s,\alpha t,\alpha s+\alpha t)\in P.
              \]
    \end{enumerate}
    Por tanto, $P$ es un subespacio de $\R^3$. Combinar desplazamientos
    permitidos o cambiar su escala no hace que la plataforma salga del plano.
\end{ejem}

\begin{center}
    \begin{tikzpicture}[x={(1cm,-0.25cm)},y={(-0.65cm,-0.4cm)},
        z={(0cm,1cm)},scale=0.95]
        \filldraw[fill=colordef!10,draw=colordef!50]
            (-0.4,-0.4,-0.8)--(1.7,-0.4,1.3)--(1.7,1.7,3.4)
            --(-0.4,1.7,1.3)--cycle;
        \draw[->] (0,0,0)--(2.4,0,0) node[right] {$x$};
        \draw[->] (0,0,0)--(0,2.3,0) node[left] {$y$};
        \draw[->] (0,0,0)--(0,0,3.7) node[above] {$z$};
        \fill[colordef!20] (0,0,0)--(1,0,1)--(1,1,2)--(0,1,1)--cycle;
        \draw[->,thick,colordef] (0,0,0)--(1,0,1) node[right] {$a$};
        \draw[->,thick,colordef] (0,0,0)--(0,1,1) node[left] {$b$};
        \draw[dashed] (1,0,1)--(1,1,2)--(0,1,1);
        \draw[->,very thick] (0,0,0)--(1,1,2) node[above right] {$a+b$};
        \node[below] at (0,0,0) {$0$};
        \node[right] at (1.7,1.7,3.4) {$P:z=x+y$};
    \end{tikzpicture}

    {\small Se dibuja una porción del plano; el plano completo se extiende sin límite.}
\end{center}

La cerradura bajo la suma significa que el paralelogramo construido con
dos vectores del plano tiene su diagonal también en él. La cerradura bajo
escalares significa que, junto con cada vector, el plano contiene la recta
completa determinada por él y el origen.
```

## Ejercicio de intersección
```latex
\begin{ejer}[La recta donde se encuentran dos planos]
    Considere $P_1=\{(x,y,z)\in\R^3:x-y=0\}$ y
    $P_2=\{(x,y,z)\in\R^3:y-z=0\}$.
    \begin{enumerate}
        \item Escriba como sistema las dos condiciones que debe cumplir
              un vector de $P_1\cap P_2$ y deduzca que
              $P_1\cap P_2=\{t(1,1,1):t\in\R\}$.
        \item Verifique que esta recta es un subespacio de $\R^3$.
              Interprete por qué sumar o escalar vectores que satisfacen
              ambas restricciones mantiene las dos restricciones.
    \end{enumerate}
\end{ejer}
```

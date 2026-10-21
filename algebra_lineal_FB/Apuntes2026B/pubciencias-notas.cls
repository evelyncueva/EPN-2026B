%%
%% This is file `pubciencias-notas.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% pubciencias-notas.dtx  (with options: `pubciencias-notas')
%% 
%% This is a generated file.
%% LaTeX class for typesetting notes
%% 
%% Copyright (C) 2018 by Andres Merino <mat.andresmerino@gmail.com>
%% 
%% Para un mejor uso y entendimiento de la actual clase,
%% consultar la documentación.
%% 
\NeedsTeXFormat{LaTeX2e}[2009/09/24]
\ProvidesClass{pubciencias-notas}[2018/09/05 v1.0]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Inicialización
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Primero definimos una serie de comandos auxiliares para las opciones
\newcommand\@idioma{spanish,es-noitemize}
\newcommand\@tipo{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Opciones
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Opciones de tamaño de letra.
\DeclareOption{10pt}{\PassOptionsToClass{10pt}{article}}
\DeclareOption{11pt}{\PassOptionsToClass{11pt}{article}}
\DeclareOption{12pt}{\PassOptionsToClass{12pt}{article}}
%%  Opciones predeterminadas de tamaño de página |compacto| y |amplio|.
\DeclareOption{amplio}{
    \PassOptionsToPackage{paperwidth=195mm,paperheight=265mm,twoside,
    inner=2.2cm,outer=2.2cm,top=2.25cm,bottom=2.25cm}{geometry}}
\DeclareOption{compacto}{
    \PassOptionsToPackage{paperwidth=160mm,paperheight=240mm,twoside,
    inner=1.7cm,outer=1.7cm,top=2.25cm,bottom=2.25cm}{geometry}}
\DeclareOption{a4}{
    \PassOptionsToPackage{paperwidth=210mm,paperheight=297mm,twoside,
    inner=2.2cm,outer=2.2cm,top=2.25cm,bottom=2.25cm}{geometry}}
\DeclareOption{a5}{
    \PassOptionsToPackage{paperwidth=148mm,paperheight=210mm,twoside,
    inner=1.7cm,outer=1.7cm,top=2.25cm,bottom=2.25cm}{geometry}}
%%  Opción de formato |guia| o |resumen|.
\DeclareOption{guia}{\renewcommand\@tipo{guia}}
\DeclareOption{resumen}{\renewcommand\@tipo{resumen}}
%%  Opciones predeterminadas son |compacto|, |guia| y |10pt|.
\ExecuteOptions{compacto,guia,10pt}
\ProcessOptions\relax
\LoadClass{article}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Paquetes
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Son necesarios los siguientes paquetes para dar formato al documento.
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[\@idioma]{babel}
\RequirePackage{ifthen}
\RequirePackage{calc}
\RequirePackage{etex}
\RequirePackage{xcolor}
\RequirePackage{amsmath,amsthm}
\RequirePackage[framemethod=TikZ]{mdframed}
\RequirePackage{mathpazo}
\RequirePackage{graphicx}
\RequirePackage{titlesec}
\RequirePackage{setspace}
\RequirePackage{fancyhdr}
\RequirePackage{titletoc}
\RequirePackage{xparse}
\RequirePackage[many]{tcolorbox}
\RequirePackage[font={small},labelfont={bf,small},
   justification=centerlast]{caption}
\RequirePackage{geometry}
\RequirePackage[colorlinks,linkcolor=black,urlcolor=black,
   citecolor=black,bookmarks=true]{hyperref}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Variables internas
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  La siguiente es la lista de las variables internas utilizadas para el formato.
\newcommand\@universidad{Escuela Politécnica Nacional}
\newcommand\@longtitulo{0.75\linewidth}
\newcommand\@interlineado{1.2}
\newcommand\@espteo{-0.75ex}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Colores predeterminados
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Los siguientes son los colores predefinidos de la clase.
\definecolor{colordef}{RGB}{5,1,100}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Espaciado
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Para mejorar la medida entre las ecuaciones.
\AtBeginDocument{
   \addtolength{\abovedisplayskip}{-0.5mm}
   \addtolength{\belowdisplayskip}{-0.5mm}
    }
%%  Interlineado
\newcommand{\interlineado}[1]{\renewcommand\@interlineado{#1}}
%%  Espacio para recuadro de teoremas
\newcommand{\espteo}[1]{\renewcommand\@espteo{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Definición de comandos de datos
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Universidad
\newcommand{\universidad}[1]%
    {\renewcommand\@universidad{#1}}
%%  Autor: autor corto, autor normal
\newcommand{\autor}[2][]{\ifthenelse{\equal{#1}{}}
   {\newcommand\@autorcorto{#2}\newcommand\@autor{#2}}
   {\newcommand\@autorcorto{#1}\newcommand\@autor{#2}}}
%%  Materia
\newcommand{\materia}[1]%
    {\newcommand\@materia{#1}}
%%  Examen
\newcommand{\nota}[1]%
    {\newcommand\@nota{#1}}
%%  Tema
\newcommand{\tema}[1]%
    {\newcommand\@tema{ #1}}
%%  Fecha
\newcommand{\fecha}[1]%
    {\newcommand\@fecha{#1}}
%%  Logo uno
\newcommand{\logouno}[2][0.1\linewidth]%
    {\newcommand\@logouno{#2}
    \newcommand\@longlogouno{#1}}
%%  Logo dos
\newcommand{\logodos}[2][0.1\linewidth]%
    {\newcommand\@logodos{#2}
    \newcommand\@longlogodos{#1}}
%%  Longitud del título
\newcommand{\longtitulo}[1]%
    {\renewcommand\@longtitulo{#1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Encabezado
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Comando para generar el título
\newcommand\@titulo{
    \large\textbf{\textsc{\@universidad\\
    \ifthenelse{\isundefined{\@hoja}}{}{\@hoja\\}
    \normalsize
    \@materia\ \ $\bullet$\ \
    \@nota}}\\
    \ifthenelse{\isundefined{\@tema}}{}{\normalsize\textsc{\@tema}\\}
    }
\newcommand\@inlogouno{
    \parbox{\@longlogouno}
    {\centering
    \ifthenelse{\isundefined{\@logouno}}{\hspace{0pt}}
        {\includegraphics[width=0.95\linewidth]{\@logouno}}}
    }
\newcommand\@inlogodos{
    \parbox{\@longlogodos}
    {\centering
    \ifthenelse{\isundefined{\@logodos}}{\hspace{0pt}}
        {\includegraphics[width=0.95\linewidth]{\@logodos}}}
    }
%%  Comando para generar el encabezado
\newcommand{\encabezado}{
    \vspace*{-10mm}
    \begingroup\color{colordef}
    \thispagestyle{plain}
    \hrule
    \vspace{-2mm}
    \begin{center}
    \ifthenelse{\isundefined{\@logodos}}
        {\ifthenelse{\isundefined{\@logouno}}
            {\@titulo}
            {
                \@inlogouno
                \parbox{\@longtitulo}{\centering \@titulo}
            }
        }
        {
            \@inlogouno
            \parbox{\@longtitulo}{\centering \@titulo}
            \@inlogodos
        }
    \end{center}
    \vspace{0mm}
    \noindent
    \@fecha\hspace{\fill}
    \@autor\\[-3mm]
    \noindent
    \hrule
    \endgroup
    \vspace{5mm}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Estilo página
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Interlineado
\renewcommand{\baselinestretch}{\@interlineado}
%%  Encabezado y pie de página
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\fancyhead[LE,RO]{\bfseries\@autorcorto}
\fancyhead[LO,RE]{\bfseries\@nota}
\renewcommand{\headrulewidth}{.2pt}
\renewcommand{\footrulewidth}{0pt}
\addtolength{\headheight}{.1pt}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Estilo títulos
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Estilo de sección
\titleformat{\section}[display]
    {\vspace*{-1mm}\bfseries\scshape\centering}
    {}{1ex}
    {\color{colordef}\large\titlerule\vspace{.05ex} \thesection.\ }
    [\color{colordef}\vspace{.2ex}\titlerule]
%%  Estilo subsecciones
\titleformat{\subsection}
    {\color{colordef}\normalsize\bfseries}
    {\thesubsection}{1em}{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Estilo teoremas
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Estilo de teorema
\newtheoremstyle{estiloteorema}%
    {9pt}{9pt}{}{0pt}{\bfseries\scshape}{.}{ }{}
%%  Recuadro sin título aparte
\mdfdefinestyle{recuadrost}{
    hidealllines=true,leftline=true,
    linewidth=1pt, innertopmargin=-.1\baselineskip,
    backgroundcolor=\mdf@@color!05,
    linecolor=\mdf@@color}
%%  Recuadro con título aparte a la izquierda
\mdfdefinestyle{recuadrocti}{
    settings={\refstepcounter{\mdf@@contador}},
    hidealllines=true,leftline=true,
    linewidth=1pt, innertopmargin=1.1\baselineskip,
    backgroundcolor=\mdf@@color!05,
    linecolor=\mdf@@color,
    singleextra={% en un solo recuadro
        %Creación del nombre para medirlo
        \node[xshift=13pt,yshift=\@espteo,thick,anchor=west](frame) at (P-|O)%
            {
                \strut{\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        %Sombra del recuadro
        \path[fill=\mdf@@color!60!black]
            ([yshift=-1.6ex,xshift=-0.2mm]frame.north west) arc[start angle=0,end angle=180,radius=0.8ex]
            ([yshift=-1.6ex,xshift=0.2mm]frame.north east) arc[start angle=180,end angle=0,radius=0.8ex];
        %Recuadro
        \path[fill=\mdf@@color!20]
            ([xshift=-2mm,yshift=-0.8ex]frame.north west) -- ([xshift=2mm,yshift=-0.8ex]frame.north east)% Linea superior
            [rounded corners=1mm] -- ([xshift=1mm,yshift=-1.5mm]frame.north east) --
            ([yshift=0.8ex]frame.south east) -- ([yshift=0.8ex]frame.south west)% Linea inferior
            -- ([xshift=-1mm,yshift=-1.5mm]frame.north west) [sharp corners]-- cycle;
        % Escritura del nombre
        \node[xshift=13pt,yshift=\@espteo,thick,anchor=west] at (P-|O)%
            {
                \strut{%\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        },
    firstextra={% si el recuadro se parte
        %Creación del nombre para medirlo
        \node[xshift=13pt,yshift=\@espteo,thick,anchor=west](frame) at (P-|O)%
            {
                \strut{\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        %Sombra del recuadro
        \path[fill=\mdf@@color!60!black]
            ([yshift=-1.6ex,xshift=-0.2mm]frame.north west) arc[start angle=0,end angle=180,radius=0.8ex]
            ([yshift=-1.6ex,xshift=0.2mm]frame.north east) arc[start angle=180,end angle=0,radius=0.8ex];
        %Recuadro
        \path[fill=\mdf@@color!20]
            ([xshift=-2mm,yshift=-0.8ex]frame.north west) -- ([xshift=2mm,yshift=-0.8ex]frame.north east)% Linea superior
            [rounded corners=1mm] -- ([xshift=1mm,yshift=-1.5mm]frame.north east) --
            ([yshift=0.8ex]frame.south east) -- ([yshift=0.8ex]frame.south west)% Linea inferior
            -- ([xshift=-1mm,yshift=-1.5mm]frame.north west) [sharp corners]-- cycle;
        % Escritura del nombre
        \node[xshift=13pt,yshift=\@espteo,thick,anchor=west] at (P-|O)%
            {
                \strut{%\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        }
    }
%%  Recuadro con título aparte a la derecha
\mdfdefinestyle{recuadroctd}{
    settings={\refstepcounter{\mdf@@contador}},
    hidealllines=true,leftline=true,
    linewidth=1pt, innertopmargin=1.0\baselineskip,
    backgroundcolor=\mdf@@color!05,
    linecolor=\mdf@@color,
    singleextra={% en un solo recuadro
        \node[xshift=-13pt,yshift=\@espteo,thick,anchor=east](frame) at (P)%
            {
                \strut{\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        %Sombra del recuadro
        \path[fill=\mdf@@color!60!black]
            ([yshift=-1.6ex,xshift=-0.2mm]frame.north west) arc[start angle=0,end angle=180,radius=0.8ex]
            ([yshift=-1.6ex,xshift=0.2mm]frame.north east) arc[start angle=180,end angle=0,radius=0.8ex];
        %Recuadro
        \path[fill=\mdf@@color!20]
            ([xshift=-2mm,yshift=-0.8ex]frame.north west) -- ([xshift=2mm,yshift=-0.8ex]frame.north east)% Linea superior
            [rounded corners=1mm] -- ([xshift=1mm,yshift=-1.5mm]frame.north east) --
            ([yshift=0.8ex]frame.south east) -- ([yshift=0.8ex]frame.south west)% Linea inferior
            -- ([xshift=-1mm,yshift=-1.5mm]frame.north west) [sharp corners]-- cycle;
        % Escritura del nombre
        \node[xshift=-13pt,yshift=\@espteo,thick,anchor=east] at (P)%
            {
                \strut{%\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        },
    firstextra={% si el recuadro se parte
        \node[xshift=-13pt,yshift=\@espteo,thick,anchor=east](frame) at (P)%
            {
                \strut{\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        %Sombra del recuadro
        \path[fill=\mdf@@color!60!black]
            ([yshift=-1.6ex,xshift=-0.2mm]frame.north west) arc[start angle=0,end angle=180,radius=0.8ex]
            ([yshift=-1.6ex,xshift=0.2mm]frame.north east) arc[start angle=180,end angle=0,radius=0.8ex];
        %Recuadro
        \path[fill=\mdf@@color!20]
            ([xshift=-2mm,yshift=-0.8ex]frame.north west) -- ([xshift=2mm,yshift=-0.8ex]frame.north east)% Linea superior
            [rounded corners=1mm] -- ([xshift=1mm,yshift=-1.5mm]frame.north east) --
            ([yshift=0.8ex]frame.south east) -- ([yshift=0.8ex]frame.south west)% Linea inferior
            -- ([xshift=-1mm,yshift=-1.5mm]frame.north west) [sharp corners]-- cycle;
        % Escritura del nombre
        \node[xshift=-13pt,yshift=\@espteo,thick,anchor=east] at (P)%
            {
                \strut{%\color{\mdf@@color!05}
                    \bfseries\textsc{\mdf@@tipo~\arabic{\mdf@@contador}}%
                    \ifdefempty{\mdf@@nombre}{}{:~~\mdf@@nombre}}
            };
        }
    }
%%  Keys para mdframe: |tipo|, |nombre|, |color| y |contador|.
\def\mdf@@nombre{}\define@key{mdf}{nombre}{\def\mdf@@nombre{#1}}
\def\mdf@@tipo{}\define@key{mdf}{tipo}{\def\mdf@@tipo{#1}}
\def\mdf@@color{colordef}\define@key{mdf}{color}{\def\mdf@@color{#1}}
\def\mdf@@contador{}\define@key{mdf}{contador}{\def\mdf@@contador{#1}}
%%  Ambiente auxiliar |recuadrocti| y |recuadroctd|.
\newmdenv[style=recuadrocti]{recuadrocti}
\newmdenv[style=recuadroctd]{recuadroctd}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Definición de ambientes de teoremas
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Ambientes sin recuadro: |ejem| y |obs|
\theoremstyle{estiloteorema}
\newtheorem{ejem}{Ejemplo}
\newtheorem{ejer}{Ejercicio}
\newtheorem{obs}{Observaci\'on}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Teoremas en el formato resumen
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifthenelse{\equal{\@tipo}{resumen}}
{
%%  Ambientes sin recuadro: |prop|, |cor|, |lem|
\theoremstyle{estiloteorema}
    \newtheorem{prop}{Proposici\'on}
    \newtheorem{cor}[prop]{Corolario}
    \newtheorem{lem}[prop]{Lema}

%%  Ambientes con recuadro sin titulo aparte |teo|, |defi|, |axioma| y |ejer|.
\theoremstyle{estiloteorema}
    \newmdtheoremenv[style=recuadrost,color=colordef]{teo}[prop]
        {Teorema}
    \newmdtheoremenv[style=recuadrost,color=colordef]{defi}
        {Definici\'on}
    \newmdtheoremenv[style=recuadrost,color=colordef]{axioma}
        {Axioma}
%    \newmdtheoremenv[style=recuadrost,color=colordef]{ejer}
%        {Ejercicio}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% --- Teoremas en el formato guia
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Ambientes con recuadro: |prop|, |cor|, |lem|, |ejer|.
{
\theoremstyle{estiloteorema}
    \newmdtheoremenv[style=recuadrost,color=colordef]{prop}
        {Proposici\'on}
    \newmdtheoremenv[style=recuadrost,color=colordef]{cor}[prop]
        {Corolario}
    \newmdtheoremenv[style=recuadrost,color=colordef]{lem}[prop]
        {Lema}
%    \newmdtheoremenv[style=recuadrost,color=colordef]{ejer}
%        {Ejercicio}
%%  Ambientes con título aparte: |teo|.
\newenvironment{teo}[1][]
    {\begin{recuadrocti}[nombre=#1,tipo=Teorema,contador=prop,
        color=colordef]}
    {\end{recuadrocti}}
%%  Ambientes con título aparte: |defi|.
\newcounter{defi}
\renewcommand{\thedefi}{\arabic{defi}}
\newenvironment{defi}[1][]
    {\begin{recuadrocti}[nombre=#1,tipo=Definición,contador=defi,
        color=colordef]}
    {\end{recuadrocti}}



%%  Ambientes con título aparte: |axioma|.
\newcounter{axioma}
\renewcommand{\theaxioma}{\arabic{axioma}}
\newenvironment{axioma}[1][]
    {\begin{recuadrocti}[nombre=#1,tipo=Axioma,contador=axioma,
        color=colordef]}
    {\end{recuadrocti}}
}
%%  Ambiente advertencia
\newtcolorbox{advertencia}{enhanced,breakable,
  before skip=2mm,after skip=3mm,
  boxrule=0.4pt,left=5mm,right=2mm,top=1mm,bottom=1mm,
  colback=yellow!50,
  colframe=yellow!20!black,
  sharp corners,rounded corners=southeast,arc is angular,arc=3mm,
  underlay={%
%    \path[fill=tcbcol@back!80!black] ([yshift=3mm]interior.south east)--++(-0.4,-0.1)--++(0.1,-0.2);
%    \path[draw=tcbcol@frame,shorten <=-0.05mm,shorten >=-0.05mm] ([yshift=3mm]interior.south east)--++(-0.4,-0.1)--++(0.1,-0.2);
    \path[fill=yellow!50!black,draw=none] (interior.south west) rectangle node[white]{} ([xshift=4mm]interior.north west);
    },
  drop fuzzy shadow}
%%  Y ¡se acabó!
\endinput
%%
%% End of file `pubciencias-notas.cls'.
Summary:	A collection of BSD (Berkeley Standard Distribution) games
Summary(de):	Diverse BSD-Games  
Summary(es):	Paquete con varios juegos BSD
Summary(fr):	Paquetage de jeux BSD divers
Summary(tr):	Metin ekranda oyunlar paketi
Summary(pl):	Zestaw gier BSD (Berkeley Standard Distribution)
Summary(pt):	Pacote com vários jogos BSD
Name:		bsd-games
Version:	2.12
Release:	2
License:	distributable
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://metalab.unc.edu/pub/Linux/games/%{name}-%{version}.tar.gz
Patch0:		%{name}-hole.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-ospeed.patch
Patch3:		%{name}-config.patch
Patch4:		%{name}-from.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	words
Requires:	textutils 
Requires:	words
Requires:	/usr/bin/frm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bsd-games includes adventure, arithmetic, atc, backgammon, battlestar,
bcd, caesar, canfield, cfscores, countmail, cribbage, dm, factor,
fish, gomoku, hunt, mille, monop, morse, number, phantasia, pig, pom,
ppt, primes, quiz, rain, random, robots, rot13, sail, snake, snscore,
teachgammon, tetris-bsd, trek, wargames, worm, worms and wump.

%description -l de
Dies ist eine Sammlung von Games. Zu den bekanntesten gehören
Backgammon, Cribbage, Monop, Primes, Trek und Battlestar.

%description -l es
Esto es un conjunto de juegos. Los destaques incluyen gammon, barajas,
ahorcado, monopolio y guerra en las estrellas.

%description -l fr
Lot de jeux. Contient backgammon, cribbage, le pendu, monop, primes,
trek et battlestar.

%description -l pl
W sk³ad gier BSD wchodz±: adventure, arithmetic, atc, backgammon,
battlestar, bcd, caesar, canfield, cfscores, countmail, cribbage, dm,
factor, fish, gomoku, hunt, mille, monop, morse, number, phantasia,
pig, pom, ppt, primes, quiz, rain, random, robots, rot13, sail, snake,
snscore, teachgammon, tetris-bsd, trek, wargames, worm, worms i wump.

%description -l pt
Isto é um conjunto de jogos. Os destaques incluem gamão, jogo de
cartas, forca, monopólio e guerra nas estrelas.

%description -l tr
Tavla, cribbage, adam asmaca, monop, primes, trek ve battlestar gibi
oyunlar içeren bir paket.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} LDFLAGS="%{rpmldflags}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
chmod +x install-man install-score

%{__make} INSTALL_PREFIX="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT{%{_bindir}/factor,%{_mandir}/man6/factor.6*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/*
%{_datadir}/misc/acronyms
/var/games/atc_score
/var/games/battlestar.log
/var/games/cfscores
/var/games/criblog
/var/games/robots_roll
%attr(640,root,root) /var/games/phantasia/characs
/var/games/phantasia/gold
/var/games/phantasia/lastdead
/var/games/phantasia/mess
/var/games/phantasia/monsters
/var/games/phantasia/motd
/var/games/phantasia/scoreboard
/var/games/phantasia/void
%attr(750,root,root) /var/games/sail/
/var/games/saillog
/var/games/snake.log
/var/games/snakerawscores
/var/games/tetris-bsd.scores
%{_mandir}/man*/*
